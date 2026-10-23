<p align="center"><img src="images/hero.svg" alt="Verity" width="720"></p>

# Verity: samples

<p align="center"><b>The samples lane: 2 of 30 Harbor task bundles.</b></p>

<p align="center"><a href="#summary"><img src="https://img.shields.io/badge/bundles-2_of_30-845EF7" alt="bundles: 2 of 30"></a> <a href="#evidence-status"><img src="https://img.shields.io/badge/sealed-0-845EF7" alt="sealed: 0"></a> <a href="#difficulty-tiers"><img src="https://img.shields.io/badge/difficulty-measured-845EF7" alt="difficulty: measured"></a></p>

<p align="center"><sub><a href="#abstract">Abstract</a> | <a href="#summary">Summary</a> | <a href="#difficulty-tiers">Difficulty tiers</a> | <a href="#evidence-status">Evidence status</a> | <a href="#coverage">Coverage</a> | <a href="#dataset-structure">Dataset structure</a> | <a href="#verification-and-quality-assurance">Verification and quality assurance</a> | <a href="#reproduction">Reproduction</a> | <a href="#cite">Cite</a> | <a href="#license">License</a> | <a href="#contact">Contact</a></sub></p>

## Abstract

The curated lane of this corpus: at most 30 Harbor task bundles, every anchor seated first and every other bundle in seal order. Bundles past that ceiling live in `delivery/`.

Each bundle is one Harbor task in a directory named by its content-derived uuid5, so the name doubles as an integrity check. This page is rendered from the resident bundles on every reconcile; a value a bundle does not carry reads `absent`, and the page never fills one in.

## Summary

| Property | Value |
| --- | --- |
| Bundles | 2 of 30 |
| Sealed | 0 of 2 |
| Registrations | unregistered (2) |
| Audit verdicts | none (2) |
| Harbor schema | 1.4 (2) |

## Difficulty tiers

Difficulty is measured by the signed pilot alone and never declared in a bundle, so this page states no tier a bundle claims.

## Evidence status

The verdict is the audit outcome recorded at the sealed digest, and `none` means no verdict has landed for that digest yet. Only an authoring run removes a bundle from this lane, so removal waits for the next one.

| uuid | Verdict | Sealed digest | Stream |
| --- | --- | --- | --- |
| 4ec54b6c-bc0f-5825-b02c-c4ab16aa1cc8 | none | absent | none |
| c0bc30af-f325-59fc-a921-e8d496177092 | none | absent | none |

## Coverage

| Keyword | Bundles |
| --- | --- |
| algoperf | 2 |
| bounded-continuous | 2 |
| conformance | 2 |
| optimization | 2 |
| training-algorithms | 2 |

## Dataset structure

| Bundle | Task | Keywords | Registration | Sealed at | Tier |
| --- | --- | --- | --- | --- | --- |
| [`4ec54b6c-bc0f-5825-b02c-c4ab16aa1cc8`](4ec54b6c-bc0f-5825-b02c-c4ab16aa1cc8/) | `ethara/verity-mnist_fine_grained-selftuning-ar9` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |
| [`c0bc30af-f325-59fc-a921-e8d496177092`](c0bc30af-f325-59fc-a921-e8d496177092/) | `ethara/verity-cifar-selftuning-ar1` | algoperf, bounded-continuous, conformance, optimization, training-algorithms | unregistered | unsealed | - |

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    bundle["&lt;uuid&gt;/"]
    bundle --> n0["task.toml<br/>runner manifest"]
    bundle --> n1["instruction.md<br/>objective the agent reads"]
    bundle --> n2["environment/<br/>agent sandbox image"]
    bundle --> n3["tests/<br/>verifier, hidden from the agent"]
    bundle --> n4["solution/<br/>private oracle"]
    bundle --> n5["README.md"]
    bundle --> n6["inspector.html"]
    bundle --> n7["plots/"]
    bundle --> n8["trajectories/"]
```

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#131a33","primaryTextColor":"#e8ecff","primaryBorderColor":"#845EF7","lineColor":"#22d3ee","fontFamily":"monospace"}}}%%
flowchart LR
    staging["staging/"]
    staging --> samples["samples/<br/>2 of 30"]
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
