"""The static rule checks, compiled from the upstream disallowed-submission rules.

Each check is a pure function of the submitted bytes and names the syntactic pattern it rejects. None of
them tries to decide the spirit of the rules, because a check that does is not deterministic. The gap
between a named pattern and the upstream prose is a standing property of the design, recorded in
requirements/oracle-verification.md section 10, and not a defect these checks can close.

Every check reports the pattern it matched and the source location, so a failure is reviewable rather
than a bare boolean.
"""

import ast
import os
import re

PERMITTED_FUNCTIONS = frozenset(
    {
        "get_batch_size",
        "get_eval_batch_size",
        "init_optimizer_state",
        "update_params",
        "prepare_for_eval",
        "data_selection",
    }
)

KERNEL_MODULES = frozenset(
    {
        "torch.utils.cpp_extension",
        "triton",
        "numba",
        "cupy",
        "ctypes",
        "cffi",
        "pycuda",
        "torch.utils.benchmark",
    }
)

KERNEL_CALLS = frozenset(
    {
        "torch.compile",
        "torch.jit.script",
        "torch.jit.trace",
        "torch.utils.cpp_extension.load",
        "torch.utils.cpp_extension.load_inline",
        "triton.jit",
        "numba.cuda.jit",
        "numba.jit",
    }
)

BACKGROUND_MODULES = frozenset({"threading", "multiprocessing", "concurrent.futures", "subprocess", "asyncio"})

BACKGROUND_CALLS = frozenset(
    {
        "torch.cuda.Stream",
        "torch.cuda.stream",
        "os.fork",
        "os.system",
        "os.popen",
    }
)

ENV_MUTATION_CALLS = frozenset({"os.putenv", "os.unsetenv", "os.environ.update", "os.environ.setdefault", "os.environ.pop"})

CREDENTIAL_PATTERNS = (
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github-token", re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}")),
    ("slack-token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("private-key-block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("bearer-literal", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]{20,}")),
    # A leading \b does not fire on the most common shape a leaked key takes, because an identifier such
    # as _WANDB_API_KEY has a word character before the fragment and therefore no boundary there. The
    # boundary is expressed as start-of-string or a non-alphanumeric character instead, which admits the
    # underscore. The value is required to look like a secret rather than merely to be a string, so a
    # legitimate assignment such as token = "cls" does not trip a red line.
    ("wandb-key", re.compile(r"(?i)(?:^|[^a-z0-9])wandb[_-]?api[_-]?key\s*[:=]\s*[\"'][^\"']{20,}[\"']")),
    (
        "generic-secret-assign",
        re.compile(
            r"(?i)(?:^|[^a-z0-9])(?:api[_-]?key|apikey|secret[_-]?key|password|passwd|"
            r"access[_-]?token|auth[_-]?token|client[_-]?secret)\s*[:=]\s*[\"'][A-Za-z0-9_\-./+=]{20,}[\"']"
        ),
    ),
)


# The two halves of an assembled credential, matched separately from the literal patterns above. The name
# side lists what a credential is called and the value side what one looks like, and both must hold: a name
# alone is a variable and a value alone is a string.
CREDENTIAL_NAME_RE = re.compile(
    r"(?i)(api[_-]?key|apikey|secret|password|passwd|access[_-]?token|auth[_-]?token|"
    r"client[_-]?secret|bearer|credential|wandb.*key|.*_token)"
)
CREDENTIAL_VALUE_RE = re.compile(r"[A-Za-z0-9_\-./+=]{20,}")


class Result(object):
    __slots__ = ("check_id", "passed", "reason", "locations")

    def __init__(self, check_id, passed, reason="", locations=None):
        self.check_id = check_id
        self.passed = passed
        self.reason = reason
        self.locations = locations or []

    def as_dict(self):
        return {
            "id": self.check_id,
            "passed": bool(self.passed),
            "reason": self.reason,
            "locations": list(self.locations),
        }


def _dotted(node):
    """Render an attribute or name chain as a dotted string, or None."""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return ".".join(reversed(parts))
    return None


def _loc(node):
    return "line %d col %d" % (getattr(node, "lineno", 0), getattr(node, "col_offset", 0))


WORKLOAD_NAME_PARAMETERS = frozenset({"workload_name", "base_workload_name"})

# The workload reaches four of the five submission functions as an object rather than as a name, and only
# get_batch_size takes a string. Seeding taint from the string parameters alone therefore left
# update_params, init_optimizer_state, data_selection, and prepare_for_eval with no taint at all, which is
# how comparing workload.__class__.__name__ walked past this check on every bundle in the batch.
WORKLOAD_OBJECT_PARAMETERS = frozenset({"workload"})

# What it means to extract identity from that object. The distinction that matters is between asking the
# workload to compute something, which is the whole point of the API, and asking it what it is. model_fn
# and loss_fn are the former and are untouched here; the attributes below are the latter. Tainting the
# object wholesale would make every value it computed tainted, and a submission branching on its own loss
# would fail a check about workload identity, which is a worse defect than the one being repaired.
IDENTITY_ATTRIBUTES = frozenset(
    {"__class__", "__name__", "__qualname__", "__module__", "__doc__", "name", "workload_name"}
)
IDENTITY_CALLS = frozenset({"type", "repr", "str", "id", "dir", "vars", "isinstance"})

# The model reaches the submission as a parameter container. A count or an aggregate over it is a
# fingerprint; reading an element's gradient is not. A bare container name is deliberately not a shape
# expression, because `if p.grad is not None` over a loop variable is ordinary training code.
PARAMETER_CONTAINER_PARAMETERS = frozenset(
    {"model_params", "current_param_container", "param_container", "model_state", "params",
     "current_params_types"}
)
CONTAINER_ATTRIBUTES = frozenset(
    {"parameters", "named_parameters", "state_dict", "buffers", "named_buffers", "modules", "children"}
)
# A count call collapses a container to a scalar, and that scalar is the fingerprint. Materialising a
# container -- list(), tuple(), sorted() -- does not: it yields another container, so `params =
# list(model.parameters())` is the ordinary way to hold the parameters, not a measurement of them. Keeping
# the two sets apart matters because a materialise call was the root of every propagation cascade measured
# over the run corpus, and nothing is lost: a count over a materialised container still mentions the
# container, so len(list(params)) is still a count over a container.
COUNT_CALLS = frozenset({"len", "sum", "hash", "max", "min"})
MATERIALISE_CALLS = frozenset({"sorted", "tuple", "list", "set", "frozenset"})

IMPORT_INDIRECTION_CALLS = frozenset({"__import__", "importlib.import_module", "import_module"})


def _scope_parameters(scope, names):
    found = set()
    if isinstance(scope, (ast.FunctionDef, ast.AsyncFunctionDef)):
        arguments = scope.args
        for argument in list(arguments.args) + list(arguments.kwonlyargs) + list(arguments.posonlyargs):
            if argument.arg in names:
                found.add(argument.arg)
    return found


def _bears_identity(node, identity_names):
    """True when the expression evaluates to the workload OBJECT, not to some value read off it.

    This distinction is the whole of the repair below. `workload` is the object; `workload.name` is
    its identity; but `workload.validation_target_value` is a published number every workload has, and
    an expression that reads it no longer carries identity at all -- the float that comes back cannot
    say which workload produced it.

    So an attribute read is identity-bearing only when the attribute is itself an identity attribute.
    Everything else collapses the object to a value and stops the walk. `getattr(obj, "const")` is
    treated as the attribute access it is, because it is the same operation spelled differently.
    """
    if not identity_names:
        return False
    if isinstance(node, ast.Name):
        return node.id in identity_names
    if isinstance(node, ast.Attribute):
        if node.attr in IDENTITY_ATTRIBUTES:
            return _bears_identity(node.value, identity_names)
        return False
    if isinstance(node, ast.Call):
        name = _dotted(node.func)
        if name == "getattr" and node.args:
            attribute = node.args[1] if len(node.args) > 1 else None
            if isinstance(attribute, ast.Constant) and isinstance(attribute.value, str):
                if attribute.value not in IDENTITY_ATTRIBUTES:
                    return False
            return _bears_identity(node.args[0], identity_names)
        if name in IDENTITY_CALLS:
            return any(_bears_identity(argument, identity_names) for argument in node.args)
        return False
    if isinstance(node, (ast.Subscript, ast.Starred)):
        return _bears_identity(node.value, identity_names)
    if isinstance(node, ast.BoolOp):
        return any(_bears_identity(value, identity_names) for value in node.values)
    if isinstance(node, ast.IfExp):
        return _bears_identity(node.body, identity_names) or _bears_identity(node.orelse, identity_names)
    return False


def _identity_expr(node, identity_names):
    """True when the expression asks a workload-bearing value what it is.

    Three routes, and each was reachable before this existed: an identity attribute anywhere in the
    expression, a call that renders or types the object, and an isinstance test, which identifies by class
    without naming one.

    Each route now requires the interrogated expression to still BEAR identity, per `_bears_identity`.
    Before that requirement the rule matched on mention alone, and mention is not identification: it
    zeroed an attempt whose sole flagged line was
    `isinstance(getattr(workload, 'validation_target_value', None), float)`, a type test on a
    published number that names no workload and branches on none. That attempt had earned a closure of
    0.9295 with every perturbation reached, and lost all of it to this function.
    """
    if not identity_names:
        return False
    for child in ast.walk(node):
        if isinstance(child, ast.Attribute) and child.attr in IDENTITY_ATTRIBUTES:
            if _bears_identity(child.value, identity_names):
                return True
        if isinstance(child, ast.Call):
            name = _dotted(child.func)
            if name in IDENTITY_CALLS and any(_bears_identity(argument, identity_names) for argument in child.args):
                return True
    return False


def _slot_key(node):
    """The (base, key) a subscript or attribute expression addresses, or None.

    Only a constant subscript key and an attribute name qualify, and only over a bare name. That is
    deliberately narrow: it is the form a submission uses to stash a value in the optimizer state and read
    it back, and nothing wider can be matched without an alias analysis.
    """
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
        index = node.slice
        if isinstance(index, ast.Index):  # Python 3.8
            index = index.value
        if isinstance(index, ast.Constant) and isinstance(index.value, (str, int)) and not isinstance(index.value, bool):
            return (node.value.id, index.value)
        return None
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
        return (node.value.id, node.attr)
    return None


def _bind_target(target, names, slots):
    """Record what one assignment target binds, and return whether anything was newly recorded.

    A bare name, and a name inside a tuple, list, or starred target, binds that name. A subscript or an
    attribute target does NOT bind its base name: `optimizer_state['params'] = params` writes one slot of a
    dictionary, it does not make the dictionary into the thing that was written. Treating it as a binding
    of the base name is what turned the optimizer state -- and through it every value read back out of it,
    including step counters and None sentinels -- into a parameter container and a shape expression, which
    is the propagation cascade this narrows. The slot itself is recorded instead, so stashing a fingerprint
    in the state and reading it back is still tracked, and tracked precisely.
    """
    changed = False
    if isinstance(target, ast.Name):
        if target.id not in names:
            names.add(target.id)
            changed = True
        return changed
    if isinstance(target, ast.Starred):
        return _bind_target(target.value, names, slots)
    if isinstance(target, (ast.Tuple, ast.List)):
        for element in target.elts:
            changed = _bind_target(element, names, slots) or changed
        return changed
    key = _slot_key(target)
    if key is not None and key not in slots:
        slots.add(key)
        changed = True
    return changed


def _mentions_tainted(node, names, slots):
    """True when the expression reads a tainted name or a tainted slot of one."""
    for child in ast.walk(node):
        if isinstance(child, ast.Name) and child.id in names:
            return True
        if isinstance(child, (ast.Subscript, ast.Attribute)) and _slot_key(child) in slots:
            return True
    return False


# The workload object is the one thing in the API that computes from the model. model_fn returns logits and
# loss_fn returns a loss: both are values the model produced, not the model itself, and their shapes are
# the shape of the batch. Letting container taint flow out of such a call made the per-example correctness
# vector of an evaluation probe into a parameter container, and its length into a parameter count.
COMPUTE_CALL_OBJECTS = frozenset({"workload"})

# The harness hands the submission the model's own shape tree as a public property of the
# workload (algoperf/spec.py:215 param_shapes, :225 model_params_types). Reading it is the
# shortest fingerprint route in the API and mentions no parameter container at all.
WORKLOAD_SHAPE_ATTRIBUTES = frozenset({"param_shapes", "model_params_types"})


def _is_compute_call(node):
    """True when the expression is a call asking the workload object to compute something."""
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
        return False
    return isinstance(node.func.value, ast.Name) and node.func.value.id in COMPUTE_CALL_OBJECTS


def _container_taint(scope):
    """Names and slots inside one scope whose value derives from a parameter container."""
    tainted = _scope_parameters(scope, PARAMETER_CONTAINER_PARAMETERS)
    slots = set()
    changed = True
    while changed:
        changed = False
        for node in ast.walk(scope):
            targets = []
            if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                if node.value is None or _is_compute_call(node.value):
                    continue
                if not _mentions_tainted(node.value, tainted, slots):
                    continue
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            elif isinstance(node, (ast.For, ast.comprehension)):
                source = node.iter
                if not _mentions_tainted(source, tainted, slots):
                    continue
                targets = [node.target]
            else:
                continue
            for target in targets:
                changed = _bind_target(target, tainted, slots) or changed
    return tainted, slots


def _fold_strings(node, bindings):
    """Resolve an expression to the set of string values it can take.

    Folds literal concatenation and single-assignment local bindings, so a registry key spelled
    "mn" + "ist" or bound to a local name is the same object to this check as the bare literal. Without
    folding, a check that rejects a literal comparison rejects only the least imaginative way to write it.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return {node.value}
    if isinstance(node, ast.Name):
        return set(bindings.get(node.id, ()))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _fold_strings(node.left, bindings)
        right = _fold_strings(node.right, bindings)
        if left and right:
            return {a + b for a in left for b in right}
        return set()
    if isinstance(node, ast.JoinedStr):
        parts = [_fold_strings(v, bindings) for v in node.values]
        if all(parts):
            out = {""}
            for candidate in parts:
                out = {prefix + suffix for prefix in out for suffix in candidate}
            return out
        return set()
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        found = set()
        for element in node.elts:
            found |= _fold_strings(element, bindings)
        return found
    return set()


def _string_bindings(scope):
    """Names bound to string constants inside one function scope."""
    bindings = {}
    for node in ast.walk(scope):
        if isinstance(node, ast.Assign):
            values = _fold_strings(node.value, bindings)
            if not values:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name):
                    bindings.setdefault(target.id, set()).update(values)
    return bindings


def _workload_taint(scope):
    """Names inside one scope whose value derives from the workload-name parameter.

    The upstream rule is that a submission may not identify the workload, directly or through a learned
    detector. Deciding that in general is undecidable, so this tracks the one syntactic thing that is
    decidable: whether a value flowed from the parameter that carries the workload identity.
    """
    identity_names = _scope_parameters(scope, WORKLOAD_OBJECT_PARAMETERS)
    tainted = _scope_parameters(scope, WORKLOAD_NAME_PARAMETERS)

    changed = True
    while changed:
        changed = False
        for node in ast.walk(scope):
            if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                continue
            value = node.value
            if value is None:
                continue
            # Two seeds, not one. A value flows from an already-tainted name, or it is freshly extracted
            # from the workload object. The second seed is what makes a local binding useless as a
            # laundering step: naming the class before comparing it taints the name.
            flows = _mentions(value, tainted)
            extracts = _identity_expr(value, identity_names)
            if not (flows or extracts):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                for element in ast.walk(target):
                    if isinstance(element, ast.Name) and element.id not in tainted:
                        tainted.add(element.id)
                        changed = True
    return tainted, identity_names


def _mentions(node, names):
    return any(isinstance(child, ast.Name) and child.id in names for child in ast.walk(node))


def _is_constant_expr(node):
    """True for literals and for containers built only from literals."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return all(_is_constant_expr(e) for e in node.elts)
    if isinstance(node, ast.Dict):
        return all(_is_constant_expr(k) for k in node.keys if k is not None) and all(
            _is_constant_expr(v) for v in node.values
        )
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        return _is_constant_expr(node.operand)
    if isinstance(node, ast.BinOp):
        return _is_constant_expr(node.left) and _is_constant_expr(node.right)
    return False


def load_registry_keys(workloads_py_path):
    """Read the registry keys from the pinned tree rather than from an authored list."""
    with open(workloads_py_path, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    keys = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "WORKLOADS" and isinstance(node.value, ast.Dict):
                for key in node.value.keys:
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        keys.add(key.value)
            if isinstance(target, ast.Name) and target.id == "BASE_WORKLOADS" and isinstance(node.value, ast.List):
                for element in node.value.elts:
                    if isinstance(element, ast.Constant) and isinstance(element.value, str):
                        keys.add(element.value)
    if not keys:
        raise ValueError("no registry keys resolved from %s" % workloads_py_path)
    return keys


def parse_submission(source_path):
    with open(source_path, "r", encoding="utf-8") as handle:
        source = handle.read()
    return source, ast.parse(source, filename=source_path)


def c_api_surface(tree):
    """Reject any module-level statement beyond imports, constants, and permitted function definitions."""
    offending = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            continue  # module docstring
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in PERMITTED_FUNCTIONS or node.name.startswith("_"):
                continue
            offending.append("public helper function %r at %s" % (node.name, _loc(node)))
            continue
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            if value is None or _is_constant_expr(value):
                continue
            offending.append("module-level assignment with a non-constant value at %s" % _loc(node))
            continue
        offending.append("module-level %s at %s" % (type(node).__name__, _loc(node)))
    if offending:
        return Result("C-API-SURFACE", False, "module-level statements outside imports, constants, and permitted definitions", offending)
    return Result("C-API-SURFACE", True, "module level carries only imports, constants, and permitted definitions")


def c_no_workload_dispatch(tree, registry_keys):
    """Reject selecting behaviour by workload identity.

    Two patterns, because either alone is trivially evaded. The first is a registry key reaching a
    comparison, a mapping key, or a subscript, with string constants folded so concatenation and local
    bindings do not launder the literal. The second is any value that flowed from the workload-name
    parameter reaching a branch condition or a hashing call, which catches prefix tests, hashes, and
    membership tests that never mention a registry key at all.
    """
    # `registry_keys` is intersected with folded string sets below, so it has to be a set. Callers have
    # passed a list, and `set & list` raises TypeError inside the check -- a crash, not a verdict, and
    # one that reaches the driver as an infrastructure failure rather than a conformance result.
    registry_keys = frozenset(registry_keys or ())

    offending = []
    scopes = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    scopes.append(tree)

    for scope in scopes:
        bindings = _string_bindings(scope)
        tainted, identity_names = _workload_taint(scope)

        for node in ast.walk(scope):
            if isinstance(node, ast.Compare):
                found = _fold_strings(node.left, bindings)
                for comparator in node.comparators:
                    found |= _fold_strings(comparator, bindings)
                hit = found & registry_keys
                if hit:
                    offending.append("comparison against registry key %s at %s" % (sorted(hit), _loc(node)))
                elif _identity_expr(node, identity_names):
                    offending.append("comparison over the workload's own identity at %s" % _loc(node))
                elif tainted and _mentions(node, tainted):
                    offending.append("comparison over a value derived from the workload identity at %s" % _loc(node))
            elif isinstance(node, ast.Dict):
                found = set()
                for key in node.keys:
                    if key is not None:
                        found |= _fold_strings(key, bindings)
                hit = found & registry_keys
                if hit:
                    offending.append("mapping literal keyed by registry key %s at %s" % (sorted(hit), _loc(node)))
            elif isinstance(node, ast.Subscript):
                hit = _fold_strings(node.slice, bindings) & registry_keys
                if hit:
                    offending.append("subscript by registry key %s at %s" % (sorted(hit), _loc(node)))
                elif _identity_expr(node.slice, identity_names):
                    offending.append("subscript by the workload's own identity at %s" % _loc(node))
                elif tainted and _mentions(node.slice, tainted):
                    offending.append("subscript by a value derived from the workload identity at %s" % _loc(node))
            elif isinstance(node, ast.Call):
                name = _dotted(node.func)
                if isinstance(node.func, ast.Attribute) and node.func.attr in ("startswith", "endswith", "find", "index", "count", "__contains__"):
                    if tainted and _mentions(node.func.value, tainted):
                        offending.append("string probe %r over the workload name at %s" % (node.func.attr, _loc(node)))
                if name in ("hash", "len") and any(
                    (tainted and _mentions(argument, tainted)) or _identity_expr(argument, identity_names)
                    for argument in node.args
                ):
                    offending.append("call to %s over a value derived from the workload identity at %s" % (name, _loc(node)))
                elif name in IDENTITY_CALLS and any(
                    _bears_identity(argument, identity_names) for argument in node.args
                ):
                    # `_bears_identity` rather than `_mentions`, for the reason `_identity_expr`
                    # records: mentioning the workload is not interrogating it. This branch is the one
                    # that fired on `isinstance(getattr(workload, 'validation_target_value', None),
                    # float)` and zeroed an attempt that had earned 0.9295.
                    offending.append("call to %s over the workload object at %s" % (name, _loc(node)))
            elif isinstance(node, (ast.If, ast.IfExp, ast.While)):
                if _identity_expr(node.test, identity_names):
                    offending.append("branch on the workload's own identity at %s" % _loc(node))
                elif tainted and _mentions(node.test, tainted):
                    offending.append("branch on a value derived from the workload identity at %s" % _loc(node))

    if offending:
        return Result("C-NO-WORKLOAD-DISPATCH", False, "the submission selects behaviour by workload identity", sorted(set(offending)))
    return Result(
        "C-NO-WORKLOAD-DISPATCH",
        True,
        "no registry key reaches a comparison, mapping, or subscript after constant folding, and no value derived from the workload name reaches a branch or a hash",
    )


SHAPE_MARKERS = frozenset({"shape", "size", "numel", "nelement", "stride", "ndim", "keys", "state_dict", "__len__"})


# The rank of a tensor -- how many axes it has -- is not an extent. Every model has rank-1 biases and
# norms and rank-2-or-more weights, so an ordering test on rank separates a weight from a bias and
# separates nothing else; it is the "generic property such as layer type" the instruction permits, and it
# is how every AdamW submission builds its no-decay group. An equality test on rank is different: rank 4 is
# convolutional and rank 3 is attention, so naming an exact rank names an architecture. The exemption below
# is therefore on the operator, not on the marker, and it applies to the three spellings of rank alike so
# that p.ndim > 1 and len(p.shape) > 1 cannot disagree.
ORDERING_OPS = (ast.Lt, ast.LtE, ast.Gt, ast.GtE)


def _is_rank_expr(node):
    """True when the expression yields a tensor's rank and nothing finer."""
    if isinstance(node, ast.Attribute) and node.attr == "ndim":
        return True
    if isinstance(node, ast.Call):
        function = node.func
        if isinstance(function, ast.Attribute) and function.attr == "dim" and not node.args:
            return True
        if _dotted(function) == "len" and len(node.args) == 1:
            argument = node.args[0]
            if isinstance(argument, ast.Attribute) and argument.attr == "shape":
                return True
            if isinstance(argument, ast.Call) and isinstance(argument.func, ast.Attribute):
                if argument.func.attr == "size" and not argument.args:
                    return True
    return False


def _is_shape_expr(node, containers, container_slots, shape_names, shape_slots):
    """True when the expression yields a fingerprint of the model rather than a value from it.

    Four routes. A shape-marker attribute anywhere in the expression. A count over a parameter container,
    which is what makes len(model_params) a fingerprint even though no attribute in it names a shape. A
    mention of a name already bound to a shape expression, which is the propagation that stops a local
    binding from laundering a fingerprint through a bare Name into the comparison. And a read of a slot a
    shape expression was written into, which is the same laundering through a dictionary.

    A bare container name is deliberately not a fingerprint, and neither is a materialised copy of one.
    Reading an element's gradient inside a loop over the parameters is ordinary training code, and so is
    holding the parameters in a list; a check that rejected either would reject every submission rather
    than the fingerprinting ones.
    """
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            marker_func = child.func
            if isinstance(marker_func, ast.Attribute) and marker_func.attr in SHAPE_MARKERS:
                if any(_mentions_tainted(a, containers, container_slots) for a in child.args):
                    return True
            if _dotted(marker_func) == "getattr" and len(child.args) == 2:
                key = child.args[1]
                if isinstance(key, ast.Constant) and key.value in SHAPE_MARKERS:
                    if _mentions_tainted(child.args[0], containers, container_slots):
                        return True
        if isinstance(child, ast.Attribute) and child.attr in WORKLOAD_SHAPE_ATTRIBUTES:
            if isinstance(child.value, ast.Name) and child.value.id in COMPUTE_CALL_OBJECTS:
                return True
        if isinstance(child, ast.Attribute) and child.attr in SHAPE_MARKERS:
            # Rooted at the model, not at any tensor. The check is scoped to "a parameter shape, a
            # parameter count, or a model-state key set"; the lead dimension of an input batch is none of
            # those, and the submission is handed the batch size by its own get_batch_size, so reading it
            # back off the batch tells it nothing it did not already choose. Ungated, this route reported
            # every replay buffer and every chunked evaluation loop in the corpus as a fingerprint.
            if _mentions_tainted(child.value, containers, container_slots):
                return True
        if isinstance(child, ast.Name) and child.id in shape_names:
            return True
        if isinstance(child, (ast.Subscript, ast.Attribute)) and _slot_key(child) in shape_slots:
            return True
        if isinstance(child, ast.Call):
            name = _dotted(child.func)
            if name in COUNT_CALLS:
                # Only the container test is needed here. ast.walk above already visits every descendant of
                # this call, so a shape marker or a bound shape name inside the argument is reported by the
                # routes above; repeating those two tests without the container gate was what reported
                # max(1, value.numel() // batch_size) over an input batch as a parameter count.
                for argument in child.args:
                    if _mentions_tainted(argument, containers, container_slots):
                        return True
    return False


def _shape_bindings(scope, containers, container_slots):
    """Names and slots inside one scope bound to a shape expression, to a fixpoint."""
    shape_names = set()
    shape_slots = set()
    changed = True
    while changed:
        changed = False
        for node in ast.walk(scope):
            if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                continue
            if node.value is None:
                continue
            if not _is_shape_expr(node.value, containers, container_slots, shape_names, shape_slots):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                changed = _bind_target(target, shape_names, shape_slots) or changed
    return shape_names, shape_slots


def _is_fingerprint_literal(node):
    """True for a literal that could carry model information.

    None, True, False, and Ellipsis are excluded. A shape is an integer or a tuple of integers and a state
    key set is a collection of strings; none of them is ever a singleton, so a comparison against one
    cannot be reading a shape. `if params is None` asks whether a value has been initialised, which every
    submission that caches anything in its optimizer state has to ask.
    """
    if isinstance(node, ast.Constant):
        if node.value is None or isinstance(node.value, bool) or node.value is Ellipsis:
            return False
        return node.value not in (0, 1)
    return _is_constant_expr(node)


def c_no_shape_fingerprint(tree):
    """Reject a comparison of a parameter shape, count, or state key set against a literal."""
    offending = []
    scopes = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    scopes.append(tree)

    for scope in scopes:
        containers, container_slots = _container_taint(scope)
        shape_names, shape_slots = _shape_bindings(scope, containers, container_slots)
        for node in ast.walk(scope):
            if not isinstance(node, ast.Compare):
                continue
            if all(isinstance(op, (ast.Is, ast.IsNot)) for op in node.ops):
                # Identity can only distinguish singletons, and no shape is a singleton.
                continue
            if not any(isinstance(op, (ast.Eq, ast.NotEq, ast.In, ast.NotIn)) for op in node.ops):
                continue  # an ordering test is a magnitude, not a name
            sides = [node.left] + list(node.comparators)
            shape_sides = [side for side in sides if _is_shape_expr(side, containers, container_slots, shape_names, shape_slots)]
            has_literal = any(_is_fingerprint_literal(side) for side in sides)
            if shape_sides and has_literal:
                if all(_is_rank_expr(side) for side in shape_sides) and all(
                    isinstance(op, ORDERING_OPS) for op in node.ops
                ):
                    continue  # a rank split is layer type, not identity
                offending.append("shape or parameter-count expression compared against a literal at %s" % _loc(node))
    if offending:
        return Result("C-NO-SHAPE-FINGERPRINT", False, "the submission fingerprints the model by shape", sorted(set(offending)))
    return Result(
        "C-NO-SHAPE-FINGERPRINT",
        True,
        "no parameter shape, parameter count, or model-state key set is compared against a non-singleton "
        "literal, after container-taint, shape-binding, and slot propagation; a rank ordering is treated as "
        "layer type rather than as identity",
    )


def c_search_space_invariant(submission_dir, registry_keys, search_space_required):
    """Reject a search space naming a registry key, or more than one search-space file."""
    candidates = []
    for entry in sorted(os.listdir(submission_dir)):
        if entry.endswith(".json") and "search_space" in entry:
            candidates.append(entry)
    if not search_space_required:
        if candidates:
            return Result(
                "C-SEARCH-SPACE-INVARIANT",
                False,
                "the self-tuning ruleset exposes no hyperparameters, so a search-space file must not be present",
                candidates,
            )
        return Result("C-SEARCH-SPACE-INVARIANT", True, "no search-space file is present, as the self-tuning ruleset requires")
    if len(candidates) != 1:
        return Result(
            "C-SEARCH-SPACE-INVARIANT",
            False,
            "the external ruleset requires exactly one search-space file",
            candidates,
        )
    with open(os.path.join(submission_dir, candidates[0]), "r", encoding="utf-8") as handle:
        text = handle.read()
    hit = sorted(key for key in registry_keys if key in text)
    if hit:
        return Result("C-SEARCH-SPACE-INVARIANT", False, "the search space names registry keys", hit)
    return Result("C-SEARCH-SPACE-INVARIANT", True, "exactly one search-space file, naming no registry key")


def c_no_env_mutation(tree):
    """Reject an assignment into the process environment from the submission module."""
    offending = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if not isinstance(target, ast.Subscript):
                    continue
                base = _dotted(target.value)
                if base in ("os.environ", "environ"):
                    offending.append("assignment into %s at %s" % (base, _loc(node)))
                    continue
                # getattr(os, "environ")["X"] = "y" and __import__("os").environ["X"] = "y" reach the
                # same object by routes that carry no os.environ attribute chain to match on.
                if isinstance(target.value, ast.Call):
                    inner = _dotted(target.value.func)
                    literals = set()
                    for argument in target.value.args:
                        literals |= _fold_strings(argument, {})
                    if inner == "getattr" and "environ" in literals:
                        offending.append("assignment into an environment mapping reached by getattr at %s" % _loc(node))
                elif isinstance(target.value, ast.Attribute) and target.value.attr == "environ":
                    offending.append("assignment into an environment mapping reached by a dynamic import at %s" % _loc(node))
        if isinstance(node, ast.Call):
            name = _dotted(node.func)
            if name in ENV_MUTATION_CALLS:
                offending.append("call to %s at %s" % (name, _loc(node)))
    if offending:
        return Result("C-NO-ENV-MUTATION", False, "the submission mutates the process environment", sorted(set(offending)))
    return Result("C-NO-ENV-MUTATION", True, "the submission makes no assignment into the process environment")


def _imported_modules(tree):
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                modules.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                modules.add(node.module)
                for alias in node.names:
                    modules.add("%s.%s" % (node.module, alias.name))
    return modules


def _matches(modules, forbidden):
    hit = set()
    for module in modules:
        for candidate in forbidden:
            if module == candidate or module.startswith(candidate + "."):
                hit.add(module)
    return hit


def c_no_kernel(tree):
    """Reject an import of, or call into, a runtime compilation surface."""
    offending = []
    hit = _matches(_imported_modules(tree), KERNEL_MODULES)
    for module in sorted(hit):
        offending.append("import of runtime compilation surface %r" % module)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _dotted(node.func)
            if name in KERNEL_CALLS:
                offending.append("call to %s at %s" % (name, _loc(node)))
            # A dynamic import reaches the same surface without an import statement to match on. The
            # attribute form has no resolvable dotted name, as in __import__("importlib").import_module(x),
            # so the callee attribute is matched directly rather than through a dotted chain.
            indirect = name in IMPORT_INDIRECTION_CALLS or (
                isinstance(node.func, ast.Attribute) and node.func.attr in ("import_module", "__import__")
            )
            if indirect:
                literals = set()
                for argument in node.args:
                    literals |= _fold_strings(argument, {})
                hit = _matches(literals, KERNEL_MODULES)
                if hit:
                    offending.append("dynamic import of runtime compilation surface %s at %s" % (sorted(hit), _loc(node)))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                name = _dotted(decorator) or _dotted(getattr(decorator, "func", None))
                if name in KERNEL_CALLS:
                    offending.append("kernel JIT decorator %s at %s" % (name, _loc(node)))
    if offending:
        return Result("C-NO-KERNEL", False, "the submission reaches a runtime compilation surface", offending)
    return Result("C-NO-KERNEL", True, "no runtime compilation surface is imported or called")


def c_no_background_work(tree):
    """Reject a thread, process, or device stream created by the submission."""
    offending = []
    hit = _matches(_imported_modules(tree), BACKGROUND_MODULES)
    for module in sorted(hit):
        offending.append("import of concurrency surface %r" % module)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _dotted(node.func)
            if name in BACKGROUND_CALLS:
                offending.append("call to %s at %s" % (name, _loc(node)))
    if offending:
        return Result("C-NO-BACKGROUND-WORK", False, "the submission creates work outside the timed update call", offending)
    return Result("C-NO-BACKGROUND-WORK", True, "no thread, process, or device stream is created by the submission")


def _folded_strings(tree):
    """Every module-level string a reader can determine statically, including concatenated fragments.

    A literal matcher reads bytes as they lie, so a credential written as "0123..." + "89ab..." is invisible
    to it while being exactly as much of a credential once the module loads. The Phase 3 probe
    P-CREDENTIAL-SPLIT evaded C-NO-CREDENTIAL on every bundle in this batch for that reason, and an
    undefeated checker hack is BLOCK:INVALID_TASK until it is rehardened, so this folds what it can before
    matching.

    Folding is deliberately shallow: literal concatenation, module-level name resolution one level deep, and
    nothing else. It is not an evaluator and must never become one, because a checker that executes
    submitted expressions to decide whether to reject them has handed the submission the decision. What it
    buys is that the shortest form of the evasion no longer works, and the residue is recorded rather than
    claimed away.
    """
    constants = {}
    sequences = {}
    folded = []
    pairs = []

    def fold(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return constants.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left, right = fold(node.left), fold(node.right)
            if left is not None and right is not None:
                return left + right
        if isinstance(node, ast.JoinedStr):
            parts = []
            for value in node.values:
                if isinstance(value, ast.Constant) and isinstance(value.value, str):
                    parts.append(value.value)
                elif isinstance(value, ast.FormattedValue):
                    inner = fold(value.value)
                    if inner is None:
                        return None
                    parts.append(inner)
                else:
                    return None
            return "".join(parts)
        if isinstance(node, ast.Call):
            # "".join(...) is the third form of the same move, over a literal sequence or over a name bound
            # to one. Resolving only the literal form left the bound form evading, which the probe set
            # caught as P-OTHER-credential-join.
            joiner = fold(node.func.value) if isinstance(node.func, ast.Attribute) else None
            if joiner is not None and getattr(node.func, "attr", None) == "join" and node.args:
                pieces = elements(node.args[0])
                if pieces is not None:
                    return joiner.join(pieces)
        return None

    def elements(node):
        """The string members of a literal sequence, or of a name bound to one."""
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            pieces = [fold(element) for element in node.elts]
            return pieces if all(piece is not None for piece in pieces) else None
        if isinstance(node, ast.Name):
            return sequences.get(node.id)
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            members = elements(node.value)
            if members is not None:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        sequences[target.id] = members
            value = fold(node.value)
            if value is None:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name):
                    constants[target.id] = value
                    pairs.append((target.id, value))
            folded.append(value)
    return folded, pairs


def c_no_credential(submission_dir, tree=None):
    """Reject any credential pattern in the submitted tree, literal or assembled."""
    offending = []
    for base, _dirs, files in os.walk(submission_dir):
        for name in sorted(files):
            path = os.path.join(base, name)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as handle:
                    text = handle.read()
            except OSError:
                continue
            for label, pattern in CREDENTIAL_PATTERNS:
                match = pattern.search(text)
                if match:
                    rel = os.path.relpath(path, submission_dir)
                    offending.append("%s pattern in %s at offset %d" % (label, rel, match.start()))

    if tree is not None:
        folded, pairs = _folded_strings(tree)

        # Two questions, because a credential has two halves and the fold splits them apart. A folded value
        # can carry its own shape, as an AWS key or a private-key header does, and those patterns match the
        # value alone. A generic secret does not: its patterns match "name = value" as written, and folding
        # discards the assignment syntax they key on. So the pair is matched directly, the identifier
        # against the names a credential takes and the value against the shape a secret takes. Without this
        # second question the fold changes nothing, which is what the first repair of this check got wrong.
        for value in folded:
            for label, pattern in CREDENTIAL_PATTERNS:
                if pattern.search(value):
                    offending.append("%s pattern in a statically assembled string" % label)
                    break
        for name, value in pairs:
            if CREDENTIAL_NAME_RE.search(name) and CREDENTIAL_VALUE_RE.fullmatch(value):
                offending.append("credential-shaped value assembled into %s" % name)

    if offending:
        return Result("C-NO-CREDENTIAL", False, "a credential pattern appears in the submitted tree", sorted(set(offending)))
    return Result("C-NO-CREDENTIAL", True, "no credential pattern appears in the submitted tree, literal or statically assembled")


def c_deps_unchanged(submission_dir, allow_requirements_txt, pinned_packages):
    """Reject an added dependency that re-pins a package the harness already pins."""
    path = os.path.join(submission_dir, "requirements.txt")
    if not os.path.exists(path):
        return Result("C-DEPS-UNCHANGED", True, "the submission adds no dependency")
    if not allow_requirements_txt:
        return Result("C-DEPS-UNCHANGED", False, "the task forbids an added dependency and requirements.txt is present", ["requirements.txt"])
    offending = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            entry = line.split("#", 1)[0].strip()
            if not entry:
                continue
            name = re.split(r"[<>=!~\[ ]", entry, 1)[0].strip().lower().replace("_", "-")
            if name in pinned_packages:
                offending.append("%s re-pins a package the harness already pins" % entry)
    if offending:
        return Result("C-DEPS-UNCHANGED", False, "an added dependency re-pins a harness-pinned package", offending)
    return Result("C-DEPS-UNCHANGED", True, "no added dependency re-pins a harness-pinned package")


def submission_modules(submission_dir, submission_file):
    paths = [os.path.join(submission_dir, submission_file)]
    for name in sorted(os.listdir(submission_dir)):
        if name.endswith(".py") and name != submission_file:
            paths.append(os.path.join(submission_dir, name))
    return paths


def merge_across_modules(results):
    check_id = results[0].check_id
    failed = [r for r in results if not r.passed]
    if not failed:
        return Result(check_id, True)
    locations = []
    for result in failed:
        locations.extend(result.locations)
    return Result(check_id, False, "; ".join(r.reason for r in failed if r.reason), locations)


def run_all(submission_dir, submission_file, registry_keys, search_space_required, allow_requirements_txt, pinned_packages):
    """Every static check over the submitted bytes, in declaration order."""
    source_path = os.path.join(submission_dir, submission_file)
    _source, tree = parse_submission(source_path)

    # submission_dir is on PYTHONPATH, so a sibling module is importable and sitecustomize.py runs before
    # the submission imports at all. Merged results reuse each check's own id, adding no vocabulary entry.
    trees = [parse_submission(path)[1] for path in submission_modules(submission_dir, submission_file)]

    return [
        c_api_surface(tree),
        merge_across_modules([c_no_workload_dispatch(t, registry_keys) for t in trees]),
        merge_across_modules([c_no_shape_fingerprint(t) for t in trees]),
        c_search_space_invariant(submission_dir, registry_keys, search_space_required),
        merge_across_modules([c_no_env_mutation(t) for t in trees]),
        merge_across_modules([c_no_kernel(t) for t in trees]),
        merge_across_modules([c_no_background_work(t) for t in trees]),
        c_no_credential(submission_dir, tree),
        c_deps_unchanged(submission_dir, allow_requirements_txt, pinned_packages),
    ]
