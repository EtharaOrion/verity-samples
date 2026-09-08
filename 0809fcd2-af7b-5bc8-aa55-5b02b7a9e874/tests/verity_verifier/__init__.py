"""The Verity verifier.

One shared package across the corpus. It reads the run specification, grades the submitted bytes and the
recorded evaluation logs, and writes the reward contract. It holds no check that the run specification
does not declare, because a check that exists only in code cannot be reviewed at the sign-off gate.

Dependency-free on purpose, so it runs inside the verifier image and inside a bare authoring checkout
without the bundle pinning a parser it would then have to trust.
"""

__all__ = ["spec", "parse", "rules", "redline", "runchecks", "reward", "main"]
