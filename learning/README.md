# Learning Quantum Markov Stability

The project connects a microscopic preparation condition to a spatial information bound: uniformly full-rank product inputs and uniformly faithful local circuits of bounded depth and range produce exponential conditional mutual-information decay on a one-dimensional line. The learning route explains why ordinary endpoint correlations do not answer this question, how a fresh resource contracts retained conditional information, and how the physical circuit exposes a sequence of those resources.

## Start with the map and the worked bridge

The [30-milestone map](MILESTONES.md) records the project's understanding targets, dependencies, conceptual connections, and source pointers. It has two phases:

- **[M01–M12: background and preliminaries](MILESTONES.md#m01).** States, channels, entropy, conditional information, locality, and the full stability question.
- **[M13–M30: narrative and innovation](MILESTONES.md#m13).** Resource contraction, exact nonunitary circuit regrouping, uniform spatial decay, physical examples, and the theorem's boundaries.

The [Wilde bridge](WILDE_BRIDGE.md) is a connected explanation through these targets. It includes a complete parity example, a four-qubit noisy Bell-swapping calculation, and a five-gate causal regrouping. These examples expose the mechanism while the canonical scientific pages retain the full proofs.

## One selected educational source

The educational anchor is **Mark M. Wilde, _Quantum Information Theory_, second edition, Cambridge University Press, 2017** ([publisher DOI](https://doi.org/10.1017/9781316809976)). Its relevant sections cover density operators and composite systems, CPTP maps and Choi representations, purification, and quantum entropy and conditional information.

The [bridge's source table](WILDE_BRIDGE.md#the-selected-source-and-a-focused-reading-route) gives verified 2017 section and page pointers. It also distinguishes the accessible 2021 author manuscript's pagination. The bridge translates Wilde's bits into the project's nats and keeps physical gates, boundary operations, and internal resource channels distinct.

Research papers cited for conditional Doeblin contraction, sequential chains, and related results are primary proof dependencies and attribution sources. Their roles are documented in [resource contraction](../science/contraction.md) and [the literature comparison](../references/comparison.md).

## Follow the question to its authoritative account

| Question | Milestones | Scientific account |
|---|---|---|
| What is assumed and what is proved? | [M12](MILESTONES.md#m12), [M26](MILESTONES.md#m26) | [Model and theorem](../science/model.md) |
| Why does one resource contract conditional information? | [M13–M16](MILESTONES.md#m13) | [Resource contraction](../science/contraction.md) |
| How can nonunitary gates be regrouped exactly? | [M17–M21](MILESTONES.md#m17) | [Causal regrouping](../science/circuit-regrouping.md) |
| How does a local coefficient control arbitrary spatial cuts? | [M22–M26](MILESTONES.md#m22) | [Spatial decay](../science/spatial-decay.md) |
| Which preparations illustrate the theorem and its limits? | [M27–M29](MILESTONES.md#m27) | [Examples and boundaries](../science/examples-and-limits.md) |
| What is inherited, and what do the finite calculations check? | [M30](MILESTONES.md#m30) | [Related work](../references/comparison.md), [verification](../verification/README.md) |

For a direct specialist route, the [science overview](../science/README.md) connects the exact assumptions, proof components, and conclusions. The [verification guide](../verification/README.md) provides commands and explains how finite checks relate to the general analytical result.
