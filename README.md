<p align="center"><img src="images/hero.svg" alt="Verity" width="720"></p>

# Verity: samples

<p align="center"><b>The samples lane: 30 of 30 Harbor task bundles.</b></p>

<p align="center"><a href="#summary"><img src="https://img.shields.io/badge/bundles-30_of_30-845EF7" alt="bundles: 30 of 30"></a> <a href="#evidence-status"><img src="https://img.shields.io/badge/sealed-0-845EF7" alt="sealed: 0"></a> <a href="#difficulty-tiers"><img src="https://img.shields.io/badge/difficulty-measured-845EF7" alt="difficulty: measured"></a></p>

<p align="center"><sub><a href="#abstract">Abstract</a> | <a href="#summary">Summary</a> | <a href="#difficulty-tiers">Difficulty tiers</a> | <a href="#evidence-status">Evidence status</a> | <a href="#coverage">Coverage</a> | <a href="#dataset-structure">Dataset structure</a> | <a href="#verification-and-quality-assurance">Verification and quality assurance</a> | <a href="#reproduction">Reproduction</a> | <a href="#cite">Cite</a> | <a href="#license">License</a> | <a href="#contact">Contact</a></sub></p>

## Abstract

The curated lane of this corpus: at most 30 Harbor task bundles, every anchor seated first and every other bundle in seal order. Bundles past that ceiling live in `delivery/`.

Each bundle is one Harbor task in a directory named by its content-derived uuid5, so the name doubles as an integrity check. This page is rendered from the resident bundles on every reconcile; a value a bundle does not carry reads `absent`, and the page never fills one in.

## Summary

| Property | Value |
| --- | --- |
| Bundles | 30 of 30 |
| Sealed | 0 of 30 |
| Registrations | unregistered (30) |
| Audit verdicts | none (30) |
| Harbor schema | absent (30) |

## Difficulty tiers

Difficulty is measured by the signed pilot alone and never declared in a bundle, so this page states no tier a bundle claims.

## Evidence status

The verdict is the audit outcome recorded at the sealed digest, and `none` means no verdict has landed for that digest yet. Only an authoring run removes a bundle from this lane, so removal waits for the next one.

| uuid | Verdict | Sealed digest | Stream |
| --- | --- | --- | --- |
| 03597ef0-b47c-53ec-98a1-e0b21ba25359 | none | absent | none |
| 0809fcd2-af7b-5bc8-aa55-5b02b7a9e874 | none | absent | none |
| 198555d0-7868-5d6b-a141-99bb917af89a | none | absent | none |
| 278c3877-da79-57e3-ad0a-ed3786751493 | none | absent | none |
| 298dfc1a-00b9-5fad-8496-4558fc23dbd9 | none | absent | none |
| 43edd11e-f330-5557-adec-eccc7afa03fc | none | absent | none |
| 5a6c8a34-c444-5b19-93da-05abad76075b | none | absent | none |
| 5bafb40e-bccc-5ea2-89c7-34f7c81849d9 | none | absent | none |
| 86f297e7-8883-56d8-8fd0-7fafcdcd5a63 | none | absent | none |
| 9585bb37-07a0-53a4-802c-8ab3754ff608 | none | absent | none |
| 983a1cd1-be81-568f-8f37-4ca98d3b791f | none | absent | none |
| 9e40e442-b491-5d73-b2d3-b848290d01bc | none | absent | none |
| 9fdd9718-bd4b-5f8f-831b-ff501a01c000 | none | absent | none |
| a15faad2-0017-5818-b05c-3340c53dfae9 | none | absent | none |
| ab7b355e-1aee-5681-a777-c6bf7954ed28 | none | absent | none |
| b2e18fe9-c91e-5bd2-8f1d-67900d582bc0 | none | absent | none |
| b515061d-e187-5f6c-b28b-3c8aac0507bc | none | absent | none |
| b5bceb71-0380-5dcc-8665-8e50ab2849b2 | none | absent | none |
| b785b44e-dcb4-526d-b286-3d0bee22c28f | none | absent | none |
| b80d5e2b-6d36-5c08-98ca-0e365204eadc | none | absent | none |
| bc86a5d0-7dbd-5196-8b4b-70f616684513 | none | absent | none |
| c2a86c28-7a6d-5455-b462-ae744aec1aec | none | absent | none |
| c44186bc-8349-59e9-8706-41098106b5f5 | none | absent | none |
| cb70623c-50fe-507a-8732-605fd8d6d0eb | none | absent | none |
| d308e307-1075-5b79-954b-ee7870dea5a0 | none | absent | none |
| d6361f41-c550-5c44-998d-67f92cf0bba3 | none | absent | none |
| dc900317-ebb1-54d7-848f-15493ad88d19 | none | absent | none |
| f1314171-6866-5dd3-9917-83576740520f | none | absent | none |
| fbff0f7c-ab3f-5b1d-a179-23edf74fe573 | none | absent | none |
| fc4fdf5c-418b-5f13-ae89-bb0a4713b323 | none | absent | none |

## Coverage

| Keyword | Bundles |
| --- | --- |
| algoperf | 30 |
| bounded-continuous | 30 |
| conformance | 30 |
| optimization | 30 |
| training-algorithms | 30 |

## Dataset structure

| Bundle | Task | Keywords | Registration | Sealed at | Tier |
| --- | --- | --- | --- | --- | --- |
| [`03597ef0-b47c-53ec-98a1-e0b21ba25359`](03597ef0-b47c-53ec-98a1-e0b21ba25359/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`0809fcd2-af7b-5bc8-aa55-5b02b7a9e874`](0809fcd2-af7b-5bc8-aa55-5b02b7a9e874/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`198555d0-7868-5d6b-a141-99bb917af89a`](198555d0-7868-5d6b-a141-99bb917af89a/) | `ethara/verity-mnist_fine_grained-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`278c3877-da79-57e3-ad0a-ed3786751493`](278c3877-da79-57e3-ad0a-ed3786751493/) | `ethara/verity-mnist_fine_grained-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`298dfc1a-00b9-5fad-8496-4558fc23dbd9`](298dfc1a-00b9-5fad-8496-4558fc23dbd9/) | `ethara/verity-mnist_fine_grained-selftuning-ar3` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`43edd11e-f330-5557-adec-eccc7afa03fc`](43edd11e-f330-5557-adec-eccc7afa03fc/) | `ethara/verity-cifar-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`5a6c8a34-c444-5b19-93da-05abad76075b`](5a6c8a34-c444-5b19-93da-05abad76075b/) | `ethara/verity-mnist_fine_grained-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`5bafb40e-bccc-5ea2-89c7-34f7c81849d9`](5bafb40e-bccc-5ea2-89c7-34f7c81849d9/) | `ethara/verity-cifar-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`86f297e7-8883-56d8-8fd0-7fafcdcd5a63`](86f297e7-8883-56d8-8fd0-7fafcdcd5a63/) | `ethara/verity-cifar-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`9585bb37-07a0-53a4-802c-8ab3754ff608`](9585bb37-07a0-53a4-802c-8ab3754ff608/) | `ethara/verity-mnist_fine_grained-selftuning-ar3` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`983a1cd1-be81-568f-8f37-4ca98d3b791f`](983a1cd1-be81-568f-8f37-4ca98d3b791f/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`9e40e442-b491-5d73-b2d3-b848290d01bc`](9e40e442-b491-5d73-b2d3-b848290d01bc/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`9fdd9718-bd4b-5f8f-831b-ff501a01c000`](9fdd9718-bd4b-5f8f-831b-ff501a01c000/) | `ethara/verity-mnist_fine_grained-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`a15faad2-0017-5818-b05c-3340c53dfae9`](a15faad2-0017-5818-b05c-3340c53dfae9/) | `ethara/verity-mnist_fine_grained-selftuning-ar3` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`ab7b355e-1aee-5681-a777-c6bf7954ed28`](ab7b355e-1aee-5681-a777-c6bf7954ed28/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`b2e18fe9-c91e-5bd2-8f1d-67900d582bc0`](b2e18fe9-c91e-5bd2-8f1d-67900d582bc0/) | `ethara/verity-cifar-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`b515061d-e187-5f6c-b28b-3c8aac0507bc`](b515061d-e187-5f6c-b28b-3c8aac0507bc/) | `ethara/verity-mnist_fine_grained-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`b5bceb71-0380-5dcc-8665-8e50ab2849b2`](b5bceb71-0380-5dcc-8665-8e50ab2849b2/) | `ethara/verity-mnist_fine_grained-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`b785b44e-dcb4-526d-b286-3d0bee22c28f`](b785b44e-dcb4-526d-b286-3d0bee22c28f/) | `ethara/verity-mnist_fine_grained-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`b80d5e2b-6d36-5c08-98ca-0e365204eadc`](b80d5e2b-6d36-5c08-98ca-0e365204eadc/) | `ethara/verity-mnist_fine_grained-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`bc86a5d0-7dbd-5196-8b4b-70f616684513`](bc86a5d0-7dbd-5196-8b4b-70f616684513/) | `ethara/verity-mnist_fine_grained-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`c2a86c28-7a6d-5455-b462-ae744aec1aec`](c2a86c28-7a6d-5455-b462-ae744aec1aec/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`c44186bc-8349-59e9-8706-41098106b5f5`](c44186bc-8349-59e9-8706-41098106b5f5/) | `ethara/verity-cifar-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`cb70623c-50fe-507a-8732-605fd8d6d0eb`](cb70623c-50fe-507a-8732-605fd8d6d0eb/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`d308e307-1075-5b79-954b-ee7870dea5a0`](d308e307-1075-5b79-954b-ee7870dea5a0/) | `ethara/verity-cifar-selftuning-ar3` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`d6361f41-c550-5c44-998d-67f92cf0bba3`](d6361f41-c550-5c44-998d-67f92cf0bba3/) | `ethara/verity-mnist_fine_grained-selftuning-ar6` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`dc900317-ebb1-54d7-848f-15493ad88d19`](dc900317-ebb1-54d7-848f-15493ad88d19/) | `ethara/verity-cifar-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`f1314171-6866-5dd3-9917-83576740520f`](f1314171-6866-5dd3-9917-83576740520f/) | `ethara/verity-mnist_fine_grained-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`fbff0f7c-ab3f-5b1d-a179-23edf74fe573`](fbff0f7c-ab3f-5b1d-a179-23edf74fe573/) | `ethara/verity-mnist_fine_grained-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`fc4fdf5c-418b-5f13-ae89-bb0a4713b323`](fc4fdf5c-418b-5f13-ae89-bb0a4713b323/) | `ethara/verity-cifar-selftuning-ar7` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    bundle["&lt;uuid&gt;/"]
    bundle --> n0["task.toml<br/>runner manifest"]
    bundle --> n1["instruction.md<br/>objective the agent reads"]
    bundle --> n2["environment/<br/>agent sandbox image"]
    bundle --> n3["tests/<br/>verifier, hidden from the agent"]
    bundle --> n4["solution/<br/>private oracle"]
```

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    staging["staging/"]
    staging --> samples["samples/<br/>30 of 30"]
    samples --> delivery["delivery/<br/>0 of 10000"]
    delivery --> stock["stock/<br/>0 of 10000"]
```

## Verification and quality assurance

Each bundle's signed provenance carrier holds its screening roots, screening instant, and absolute expiry. Placement moves that carrier into the private derivation set, which this page never reads, so reconcile lists no root it cannot verify here.

## Reproduction

Each bundle directory is a complete Harbor task: `task.toml` is the runner manifest, `instruction.md` the objective, `environment/` the sandbox image, and `tests/` the verifier. Point a Harbor runner at one bundle directory to reproduce it; `solution/` stays private.

## Cite

```bibtex
@software{verity,
  title  = {Verity: Adversarial Training-Algorithm Tasks on the AlgoPerf Harness},
  author = {{Ethara.AI}},
  year   = {2026},
  note   = {No measured difficulty results are published at this revision}
}
```

The upstream benchmark must be cited separately and is not superseded by this work. Verity runs a reduced path on different hardware against thresholds that are frequently authored, so no Verity number is an AlgoPerf result.

## License

MIT. See `LICENSE`.

The vendored upstream harness is Apache-2.0 and its licence and notice travel with it. MLCommons AlgoPerf is named in every delivered artifact, and the Verity name never substitutes for naming it.

## Contact

Organization: [Ethara.AI](https://github.com/Ethara-Ai)

Security and benchmark-integrity disclosure: see `SECURITY.md`. Do not open a public issue for a contamination finding or a leaked task byte.

Contribution route: see `CONTRIBUTING.md`.
