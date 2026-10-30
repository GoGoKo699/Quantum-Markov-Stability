# A 30-milestone map of Quantum Markov Stability

The central question is how a finite-depth circuit of local quantum channels can preserve a finite spatial Markov length when it starts from uniformly full-rank product states. The argument joins two kinds of structure: conditional-information contraction for one independent resource, and an exact causal regrouping that exposes such resources throughout a physical circuit.

This common map has **12 background/preliminaries milestones, M01–M12, and 18 narrative/innovation milestones, M13–M30**. The background moves from individual states and channels to the information and locality framework. The narrative follows the longer project-specific route from one resource and one boundary step to a uniform theorem for complete chains, its examples, and its scope. This allocation gives the physical circuit construction and its local-to-global argument the greater share of the map. Detailed calculations remain in the linked scientific pages.

The IDs identify stable understanding targets. Dependencies refer only to earlier milestones. Each phase ends by integrating its constituent ideas into a complete account.

## One educational anchor

The sole educational anchor is **Mark M. Wilde, _Quantum Information Theory_, second edition, Cambridge University Press, 2017**. The edition is identified in the publisher's [front matter](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf), and the section labels and published pagination below are verified against its [table of contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf).

The main foundations used here are:

- §§4.1 and 4.3: noisy states and composite noisy systems, beginning on pages 102 and 117.
- §§4.4–4.7: quantum evolutions, channel interpretations, preparations and measurements as channels, and channel examples, beginning on pages 129, 141, 143, and 154.
- §§5.1–5.2: purification and isometric evolution, beginning on pages 165 and 168.
- §§11.1, 11.4, and 11.6–11.9: entropy, conditional entropy, mutual information, CMI, relative entropy, and entropy inequalities, beginning on pages 301, 311, 315, 318, 321, and 327.
- §§3.6 and 6.2: entanglement and unit protocols, beginning on pages 81 and 188, for the entanglement-swapping example.

Wilde supplies these foundations. The resource inequality, causal regrouping, uniform spectral estimates, and spatial theorem are supplied in the project's scientific account. Research-level conditional Doeblin and sequential-channel ingredients retain their separate primary-source attribution in [contraction](../science/contraction.md) and the [literature comparison](../references/comparison.md).

Wilde's entropic notation uses bits. The project uses natural logarithms and nats:

```math
S_{\mathrm{nats}}=(\ln2)H_{\mathrm{bits}}.
```

The same factor converts mutual information, CMI, and relative entropy. Multiplicative contraction factors are unchanged by this conversion.

## Phase I — Background/preliminaries

<a id="m01"></a>

### M01 — States, spectra, and positive lower bounds

**Phase:** Background/preliminaries.

**Central question:** What does a positive eigenvalue floor say about a quantum state?

**Understanding target:** Interpret a density operator, its spectrum, and the inequality $`\omega\ge\delta I`$. Distinguish a full-rank state from a pure state and distinguish individual full rank from a lower bound uniform across a family.

**Dependencies and story role:** No earlier milestones. This establishes the local state property that supplies the proof's positive resource component.

**Conceptual connection:** A spectral statement about one site becomes a quantitative assumption that can survive local channel operations.

**Source pointers:** Wilde §4.1. Project: [input and faithfulness assumptions](../science/model.md#2-input-and-faithfulness-assumptions).

<a id="m02"></a>

### M02 — Composite systems and independent resources

**Phase:** Background/preliminaries.

**Central question:** What is gained by knowing that a composite input is a product state?

**Understanding target:** Relate tensor products, partial traces, reduced states, and independence. Explain why separate channels on independent blocks produce independent output resources, and why having specified marginals alone does not imply independence.

**Dependencies and story role:** M01. This turns the single-site description into the preparation structure used across the chain.

**Conceptual connection:** The fresh-resource assumption in a conditional-information argument comes from an actual factorization of the physical preparation.

**Source pointers:** Wilde §§3.5 and 4.3. Project: [input model](../science/model.md#2-input-and-faithfulness-assumptions) and [independent block resources](../science/circuit-regrouping.md#5-independent-resources-and-a-uniform-spectral-floor).

<a id="m03"></a>

### M03 — CPTP maps and local environments

**Phase:** Background/preliminaries.

**Central question:** What mathematical description includes coherent evolution, noise, and discarded local environments?

**Understanding target:** Explain complete positivity, trace preservation, and the Kraus representation as a description of an unconditional physical operation. Include averaging over measurement outcomes or retaining a complete classical record, without postselection, and the use of independent local environments.

**Dependencies and story role:** M01–M02. This establishes the allowed operations before imposing their additional spectral condition.

**Conceptual connection:** The trace-preserving property makes discarded systems and unchanged outside marginals behave correctly in the later entropy arguments.

**Source pointers:** Wilde §§4.4–4.6 and 5.2. Project: [sites, gates, and depth](../science/model.md#1-sites-gates-and-depth) and [independence of the model](../science/examples-and-limits.md#why-the-models-independence-matters).

<a id="m04"></a>

### M04 — Faithfulness as a property of a channel

**Phase:** Background/preliminaries.

**Central question:** How can a channel preserve full rank without being reversible or close to the identity?

**Understanding target:** Derive the implication $`X\ge\lambda I\Rightarrow\Phi(X)\ge\lambda\Phi(I)`$ and interpret $`\Phi(I)\ge\alpha I`$. Distinguish preservation of positive definiteness from invertibility, unitality, and weak noise.

**Dependencies and story role:** M01 and M03. This adds the gate assumption that will propagate a state eigenvalue floor through a finite block.

**Conceptual connection:** An order-preserving local operation carries a quantitative preparation condition forward even when it dissipates information.

**Source pointers:** Wilde §§4.4 and 4.7. Project: [uniform faithfulness](../science/model.md#2-input-and-faithfulness-assumptions) and [a nonunital example](../science/examples-and-limits.md#a-strong-nonunital-example).

<a id="m05"></a>

### M05 — Purification and the state–channel correspondence

**Phase:** Background/preliminaries.

**Central question:** How can a bipartite resource state be represented using a channel acting on a purification?

**Understanding target:** Explain purification, the Choi representation, and complete positivity in terms of a positive Choi operator. Distinguish full rank of a physical gate's image of the identity from full rank of a channel's Choi operator.

**Dependencies and story role:** M02–M04. This provides the local representation needed to identify the correct internal contraction channel later.

**Conceptual connection:** A state inequality can become a completely positive order inequality for an internal channel, while the external physical gate obeys different conditions.

**Source pointers:** Wilde §§4.4 and 5.1–5.2. Project: [internal resource channel](../science/contraction.md#4-reduction-to-an-internal-doeblin-channel).

<a id="m06"></a>

### M06 — Entropy and conditional entropy

**Phase:** Background/preliminaries.

**Central question:** How do entropy and conditional entropy quantify uncertainty in a composite quantum state?

**Understanding target:** Interpret $`S(A)`$ and $`S(A\mid B)=S(AB)-S(B)`$, including the possibility of negative quantum conditional entropy. Relate local Hilbert-space dimension to the bounds used on conditional information, and translate bits to nats.

**Dependencies and story role:** M01–M02. This introduces the scalar information quantities that will measure the circuit's spatial structure.

**Conceptual connection:** Finite memory dimension eventually controls a prefactor even when the reference region contains arbitrarily many sites.

**Source pointers:** Wilde §§11.1–11.2, 11.4, and 11.9. Project: [entropy convention](../science/model.md#3-conditional-mutual-information) and [complete-cell bound](../science/spatial-decay.md#2-buffers-made-of-complete-emitted-cells).

<a id="m07"></a>

### M07 — Mutual information and data processing

**Phase:** Background/preliminaries.

**Central question:** Which correlations can local processing remove, and which can it create?

**Understanding target:** Explain quantum mutual information and its relation to relative entropy. Use data processing when channels act separately on the two endpoint systems, while recognizing that a gate crossing a physical cut acts jointly across that division.

**Dependencies and story role:** M03 and M06. This connects quantum operations with bounds on bipartite correlations.

**Conceptual connection:** The same distinction separates harmless local processing from the crossing gates responsible for the cut mutual-information prefactor.

**Source pointers:** Wilde §§11.6, 11.8–11.9. Project: [cut mutual-information bound](../science/spatial-decay.md#1-a-cut-mutual-information-bound).

<a id="m08"></a>

### M08 — Conditional mutual information and shielding

**Phase:** Background/preliminaries.

**Central question:** What can remain correlated between two regions after the information in a separating region is taken into account?

**Understanding target:** Explain $`I(A:C\mid B)`$ through its entropy definition and chain rule. Relate its nonnegativity to strong subadditivity, and distinguish it from the unconditioned mutual information $`I(A:C)`$.

**Dependencies and story role:** M06–M07. This introduces the information quantity whose spatial decay defines the project's stability question.

**Conceptual connection:** A buffer can carry information relevant to distant correlations even when ordinary endpoint mutual information vanishes.

**Source pointers:** Wilde §§11.6–11.7 and 11.9. Project: [CMI definition](../science/model.md#3-conditional-mutual-information) and [conditional correlations in a chain](../science/examples-and-limits.md#an-exactly-solvable-chain-with-conditional-correlations).

<a id="m09"></a>

### M09 — Valid operations on conditional information

**Phase:** Background/preliminaries.

**Central question:** Why must the conditioning register be treated differently from the two endpoint registers?

**Understanding target:** Distinguish endpoint data processing, chain-rule enlargements, and concavity of conditional entropy. Explain why neither arbitrary processing of the conditioning register nor arbitrary convex mixing gives a general CMI monotonicity rule.

**Dependencies and story role:** M03 and M06–M08. This supplies the logical safeguards needed when averaging resource branches and moving buffer fragments.

**Conceptual connection:** Correct register bookkeeping turns familiar entropy inequalities into valid bounds and prevents an unjustified hidden-reset argument.

**Source pointers:** Wilde §§11.7 and 11.9. Project: [resource contraction proof](../science/contraction.md#2-resource-contraction-lemma) and [arbitrary physical cuts](../science/spatial-decay.md#3-arbitrary-positions-of-the-cuts).

<a id="m10"></a>

### M10 — The geometry of a local channel circuit

**Phase:** Background/preliminaries.

**Central question:** What does bounded depth and bounded range mean for the causal structure of an open chain?

**Understanding target:** Explain actual gate supports, disjoint layers, geometric range, and backward wire cones. Recognize that ordinary tensor-product locality and independent gate implementations are substantive assumptions.

**Dependencies and story role:** M02–M04. This places the local state and channel objects into the physical architecture of the theorem.

**Conceptual connection:** Circuit geometry determines which operations can be rearranged and how many sites can form a boundary memory.

**Source pointers:** Wilde §§4.3–4.5 for composition and local operations; the spatial circuit structure is supplied by the project. Project: [circuit model](../science/model.md#1-sites-gates-and-depth) and [geometric backward cones](../science/circuit-regrouping.md#2-the-geometric-backward-cone-of-a-gate).

<a id="m11"></a>

### M11 — Sequential emission and a retained memory

**Phase:** Background/preliminaries.

**Central question:** How can a channel emit an output while retaining a smaller system that carries future dependence?

**Understanding target:** Track a reference, accumulated output, incoming memory, fresh ancillary resource, and outgoing memory in one sequential step. Explain why information transferred to an emitted conditioning register differs from information remaining in the memory.

**Dependencies and story role:** M02–M03, M05, and M08–M09. This assembles the information-theoretic framework to which the physical circuit will be converted.

**Conceptual connection:** A full output channel may transmit input information perfectly even though the conditional dependence carried by its retained memory contracts.

**Source pointers:** Wilde §§4.5, 5.2, and 11.7. Project: [register roles](../science/contraction.md#1-registers-and-resource-condition) and [the channel whose contraction is required](../science/contraction.md#5-which-channel-must-satisfy-the-contraction-hypothesis).

<a id="m12"></a>

### M12 — The full spatial stability question

**Phase:** Background/preliminaries.

**Central question:** Which combination of preparation, locality, and information assumptions is needed for a finite Markov length?

**Understanding target:** State the problem using uniformly full-rank product inputs, uniformly faithful finite-depth local circuits, and exponential CMI decay across a buffer. Explain why a finite causal cone for ordinary observables does not by itself establish that conditional-information conclusion.

**Dependencies and story role:** M01–M11. This is the background synthesis: the individual objects and inequalities now form the complete setting of the theorem.

**Conceptual connection:** The next phase must connect a local spectral resource to a uniform spatial information bound, rather than infer one from ordinary correlation decay.

**Source pointers:** Wilde §§4.3–4.5 and 11.6–11.9. Project: [main theorem and assumptions](../science/model.md), [the proof's actual ingredients](../science/spatial-decay.md#6-what-the-argument-does-and-does-not-use), and [the full-rank stability question](../references/comparison.md#relation-to-the-full-rank-stability-question).

## Phase II — Narrative/innovation

<a id="m13"></a>

### M13 — A positive product component in one resource

**Phase:** Narrative/innovation.

**Central question:** What quantitative structure does a full-rank block state provide across a chosen split?

**Understanding target:** Explain the inequality $`\sigma_{LMR}\ge p\,\sigma_{LM}\otimes\sigma_R`$ and why a positive smallest eigenvalue supplies an admissible $`p`$. Distinguish this product-component weight from the amount of ordinary correlation or entanglement in the resource.

**Dependencies and story role:** M01–M02, M04, and M12. The narrative begins with the local resource property that makes contraction possible.

**Conceptual connection:** Positivity converts a spectral floor into a decomposition containing a branch whose retained memory is independent.

**Source pointers:** Wilde §§4.1 and 4.3. Project: [obtaining the resource condition](../science/contraction.md#3-obtaining-the-resource-condition).

<a id="m14"></a>

### M14 — Why the branch average is legitimate

**Phase:** Narrative/innovation.

**Central question:** What makes CMI behave convexly for this particular resource decomposition?

**Understanding target:** Show that the product branch and residual branch have the same emitted $`ABYM`$ marginal. Explain how this fixes one conditional-entropy term while concavity bounds the other, without assuming general convexity of CMI.

**Dependencies and story role:** M06, M09, M11, and M13. This establishes the load-bearing logical step in the one-resource argument.

**Conceptual connection:** Equality of a physically visible marginal makes averaging over an unobserved branch compatible with the desired conditional-information bound.

**Source pointers:** Wilde §§11.4, 11.7, and 11.9. Project: [conditional-entropy proof](../science/contraction.md#2-resource-contraction-lemma).

<a id="m15"></a>

### M15 — Contraction across one boundary

**Phase:** Narrative/innovation.

**Central question:** Why does the outgoing memory retain at most a factor $`1-p`$ of the incoming conditional information?

**Understanding target:** Combine the vanishing CMI of the product branch with the chain-rule/data-processing bound on the residual branch. Explain the resulting inequality $`I(A:R\mid BYM)\le(1-p)I(A:X\mid B)`$ for arbitrary reference systems and arbitrary CPTP boundary maps.

**Dependencies and story role:** M07–M09 and M13–M14. This completes the local mechanism before embedding it in a physical chain.

**Conceptual connection:** An independent resource supplies strict contraction even when the physical map on the incoming memory and the new left register is strong or nonunital.

**Source pointers:** Wilde §§11.7–11.9. Project: [resource contraction lemma](../science/contraction.md#2-resource-contraction-lemma).

<a id="m16"></a>

### M16 — The internal channel and inherited contraction tools

**Phase:** Narrative/innovation.

**Central question:** Which channel carries the replacement component used by existing conditional Doeblin results?

**Understanding target:** Translate the resource inequality into a completely positive replacement component of $`\mathcal T_{V\to R}`$, constructed from a purification of $`\sigma_{LM}`$. Explain why the entire emitted-output channel can have contraction coefficient one and why the established inequality is applied internally instead.

**Dependencies and story role:** M05, M11, and M13–M15. This identifies both the correct mathematical channel and the provenance of the local tool.

**Conceptual connection:** The state–channel correspondence reconciles the resource proof with existing Doeblin theory without imposing an unnecessary full-output mixing assumption.

**Source pointers:** Wilde §§4.4, 5.1–5.2, and 11.7–11.9. Project: [internal-channel reduction](../science/contraction.md#4-reduction-to-an-internal-doeblin-channel), [CKB23](../references/sources.md#ckb23), and [HGNW26](../references/sources.md#hgnw26).

<a id="m17"></a>

### M17 — Backward cones and ancestor-closed gate sets

**Phase:** Narrative/innovation.

**Central question:** How can gates be selected for an earlier coarse layer without changing a nonunitary circuit?

**Understanding target:** Explain the geometric cone bound and the inclusion of every ancestor's cone in a descendant's cone. Use that structure to identify gate sets that are closed under predecessors, and distinguish wire dependence from a smaller functional dependence caused by erasure.

**Dependencies and story role:** M03, M10, and M12. The argument now turns from one resource to the physical construction that will produce independent resources.

**Conceptual connection:** An order property of the circuit's causal graph permits exact reordering without an inverse channel.

**Source pointers:** Wilde §§4.4–4.5 for channel composition. Project: [backward cones](../science/circuit-regrouping.md#2-the-geometric-backward-cone-of-a-gate) and [the first coarse layer](../science/circuit-regrouping.md#3-assigning-gates-to-the-first-coarse-layer).

<a id="m18"></a>

### M18 — Exact regrouping into two coarse layers

**Phase:** Narrative/innovation.

**Central question:** Why do all gates left after the first coarse layer belong to disjoint boundary strips?

**Understanding target:** Relate $`w=Dr`$ and $`K=4Dr+1`$ to the unique boundary crossed by a remaining gate's cone. Explain the exact composition of independent block maps followed by independent boundary maps, including noncontiguous actual supports.

**Dependencies and story role:** M10 and M17. This turns local causal constraints into a complete geometric representation of the circuit.

**Conceptual connection:** Spatial separation of boundary strips makes a many-layer physical circuit compatible with independent-resource information arguments.

**Source pointers:** Wilde §§4.4–4.5 for the underlying map composition; the regrouping is supplied locally. Project: [boundary-strip assignment and exact channel identity](../science/circuit-regrouping.md#4-assigning-all-remaining-gates-to-boundary-strips).

<a id="m19"></a>

### M19 — Finite edges and independent padding

**Phase:** Narrative/innovation.

**Central question:** How can one uniform block argument include chains shorter than its chosen block size?

**Understanding target:** Explain why independent, untouched maximally mixed padding leaves every original reduced state unchanged and respects the same spectral assumptions. Relate that operation to regular emitted cells and to a theorem valid at finite-chain endpoints.

**Dependencies and story role:** M02, M04, and M18. This establishes that the coarse geometry does not silently restrict the finite systems covered by the result.

**Conceptual connection:** A mathematical extension by independent systems handles geometric edges without introducing extra correlations or changing the physical output of interest.

**Source pointers:** Wilde §§4.3 and 11.2. Project: [padding finite chains](../science/circuit-regrouping.md#1-padding-finite-chains) and [arbitrary-cut edge treatment](../science/spatial-decay.md#3-arbitrary-positions-of-the-cuts).

<a id="m20"></a>

### M20 — Uniform resource floors from local assumptions

**Phase:** Narrative/innovation.

**Central question:** Why does the first coarse layer produce a usable product-component weight independent of total chain length?

**Understanding target:** Combine the input floor $`\delta^K`$, the gate-by-gate faithfulness factor, and the count of at most $`KD`$ gates per block to obtain $`p_0=\delta^K\alpha^{KD}`$. Explain why the proof uses a fixed-size block bound instead of a many-body smallest eigenvalue.

**Dependencies and story role:** M01–M04, M13, and M18–M19. This joins the physical circuit construction to the local contraction mechanism.

**Conceptual connection:** Uniform local spectral assumptions provide the same positive contraction resource at every spatial step.

**Source pointers:** Wilde §§4.1 and 4.4. Project: [independent resources and the uniform spectral floor](../science/circuit-regrouping.md#5-independent-resources-and-a-uniform-spectral-floor).

<a id="m21"></a>

### M21 — Reading the circuit as a spatial memory chain

**Phase:** Narrative/innovation.

**Central question:** How does the two-layer representation become a sequence of complete physical cells and a bounded memory?

**Understanding target:** Track $`J_i=R_{i-1}L_iM_i`$ as a contiguous $`K`$-site emitted cell and $`R_i`$ as a memory of at most $`w`$ sites. Explain why this left-to-right description reproduces the state without increasing the physical circuit's time depth.

**Dependencies and story role:** M11, M18–M20. This provides the bridge from the geometric construction to spatial iteration.

**Conceptual connection:** A long sequential description can be a way of reading spatial correlations rather than a claim of a long dynamical evolution.

**Source pointers:** Wilde §§4.3–4.5 and 5.2. Project: [block parts, emitted cells, and memory](../science/circuit-regrouping.md#6-block-parts-emitted-cells-and-retained-memory).

<a id="m22"></a>

### M22 — A finite bound before any exponential decay

**Phase:** Narrative/innovation.

**Central question:** What controls the amount of information across a physical cut when the buffer is very short?

**Understanding target:** Explain why a crossing gate increases cut mutual information by at most its local dimension cost, while gates confined to one side obey data processing. Use disjoint crossing supports to obtain the safe bound $`4Dr\log d`$.

**Dependencies and story role:** M06–M10 and M18. This supplies the global prefactor and covers buffers for which there is no complete cell to contract through.

**Conceptual connection:** A local information budget at each crossing gate controls a whole-chain quantity without invoking full rank or faithfulness.

**Source pointers:** Wilde §§11.4, 11.6–11.7, and 11.9. Project: [cut mutual-information bound](../science/spatial-decay.md#1-a-cut-mutual-information-bound).

<a id="m23"></a>

### M23 — Propagating contraction through a complete buffer

**Phase:** Narrative/innovation.

**Central question:** How do independent local contraction factors accumulate across many cells?

**Understanding target:** Explain the recurrence with the previously emitted cells in the conditioning register, the factor $`q^k`$ with $`q=1-p_0`$, and the memory-dimension prefactor $`2w\log d`$. Include the final data-processing step that generates the entire right-hand region.

**Dependencies and story role:** M09, M15–M16, and M20–M21. This is the first complete spatial exponential bound for aligned cuts.

**Conceptual connection:** A bounded memory and a uniform contraction at each independent resource convert a local inequality into a system-size-independent decay law.

**Source pointers:** Wilde §§11.6–11.9. Project: [complete-cell buffers](../science/spatial-decay.md#2-buffers-made-of-complete-emitted-cells) and the inherited sequential-channel account in [HGNW26](../references/sources.md#hgnw26).

<a id="m24"></a>

### M24 — Arbitrary cuts and the exact finite-chain statement

**Phase:** Narrative/innovation.

**Central question:** How does the aligned-cell bound remain valid for a physically chosen buffer with arbitrary endpoints?

**Understanding target:** Explain the chain-rule inequality that moves partial end cells into enlarged endpoint regions, the complete-cell count, and the separate treatment when no full cell exists. Recover the exponent $`\max\{0,\lfloor |B|/K\rfloor-2\}`$ without assuming monotonicity under changing a conditioning system.

**Dependencies and story role:** M09, M19, and M21–M23. This removes the artificial alignment restriction and completes the one-sided finite-chain proof.

**Conceptual connection:** Exact entropy bookkeeping connects a regular mathematical block decomposition to arbitrary experimental or physical region boundaries.

**Source pointers:** Wilde §§11.7 and 11.9. Project: [arbitrary positions of the cuts](../science/spatial-decay.md#3-arbitrary-positions-of-the-cuts).

<a id="m25"></a>

### M25 — Two-sided shields and infinite lines

**Phase:** Narrative/innovation.

**Central question:** How does the finite one-sided result cover the usual surrounding buffer geometry and thermodynamic limits?

**Understanding target:** Reduce a two-sided shield to a sum of two one-sided CMIs using the chain rule. Explain why finite backward cones reproduce finite-region states on an infinite line and why uniform bounds permit monotone limits of endpoint regions.

**Dependencies and story role:** M08–M10, M17, and M24. This establishes the full spatial geometry and size range of the theorem.

**Conceptual connection:** Uniform local estimates support global limits without subtracting infinite entropies or identifying the two ends of an open chain.

**Source pointers:** Wilde §§4.3, 11.7, and 11.9 for the finite-system foundations. Project: [two-sided shielding](../science/spatial-decay.md#4-two-sided-shielding-on-a-line) and [infinite-line limits](../science/spatial-decay.md#5-infinite-and-half-infinite-lines).

<a id="m26"></a>

### M26 — Reading the quantitative Markov-length bound

**Phase:** Narrative/innovation.

**Central question:** What does the final bound assert uniformly, and how should its length scale be interpreted?

**Understanding target:** Connect the finite-buffer inequality to $`\xi_*=K/[-\log(1-p_0)]`$ and identify the dependence on $`D,r,d,\delta,\alpha`$. Distinguish a sufficient upper bound on Markov length from an exact length, a sharp threshold, or a lower bound.

**Dependencies and story role:** M12, M20, and M22–M25. This integrates the quantitative content of the theorem after its geometric cases are established.

**Conceptual connection:** The proof's local parameters become one common spatial decay estimate for a family of many-body preparations.

**Source pointers:** Wilde §§11.7–11.9 for the information quantities. Project: [quantitative theorem and exponential form](../science/model.md#4-quantitative-theorem).

<a id="m27"></a>

### M27 — Physical preparation families within the theorem

**Phase:** Narrative/innovation.

**Central question:** Which familiar physical preparations satisfy the theorem with uniform constants?

**Understanding target:** Apply the assumptions to maximally mixed and noninteracting thermal inputs, unitary gates, amplitude damping bounded away from complete reset, arbitrary sufficiently diamond-close channels, and finite-time bounded local Lindblad gates. Identify the local spectral floor supplied in each case.

**Dependencies and story role:** M03–M05, M20, and M26. This connects the abstract uniform theorem to concrete coherent and dissipative circuit families.

**Conceptual connection:** Stability is controlled by preparation and faithfulness floors, rather than by unitality or a blanket requirement that every gate be weak.

**Source pointers:** Wilde §§4.4–4.7 for state and channel foundations; the local Lindblad estimate is supplied by the project. Project: [examples and their explicit bounds](../science/examples-and-limits.md).

<a id="m28"></a>

### M28 — An exactly solvable chain of conditional correlations

**Phase:** Narrative/innovation.

**Central question:** Can distant endpoints have zero mutual information but retain a nonzero conditional correlation through the intervening record?

**Understanding target:** Explain the noisy Bell-link construction, retained Bell outcomes, and endpoint visibility $`v^\ell`$. Relate the exact CMI $`2\log2-S(\sigma_{v^\ell})`$ to the resource bound and identify what changes at the excluded value $`v=1`$.

**Dependencies and story role:** M02–M03, M06–M08, M13–M15, and M26–M27. This supplies a complete physical illustration of the theorem's information quantity and spectral boundary.

**Conceptual connection:** A classical record can reveal endpoint dependence that averaging hides, while full-rank links still suppress that conditional dependence with length.

**Source pointers:** Wilde §§3.6, 6.2, 11.1, and 11.6–11.7. Project: [exactly solvable chain](../science/examples-and-limits.md#an-exactly-solvable-chain-with-conditional-correlations) and [finite spatial checks](../verification/README.md#spatial-cmi-and-cut-geometry).

<a id="m29"></a>

### M29 — The boundaries of the stability statement

**Phase:** Narrative/innovation.

**Central question:** Which stronger conclusions would require additional science?

**Understanding target:** Distinguish a full-rank preparation theorem from a criterion on arbitrary output marginals, a fixed-depth circuit from an extensive continuous-time limit, and an unconditional CPTP process from postselection or an unmodeled shared environment. Explain why rank loss can invalidate the guarantee without being sufficient for a divergence.

**Dependencies and story role:** M04, M10, M12, and M25–M28. This integrates the theorem's load-bearing assumptions with its physical interpretation.

**Conceptual connection:** The same structure that makes the proof work identifies which changes to the physical problem the result does not yet control.

**Source pointers:** Wilde §§4.3–4.6 and 11.7 for the channel and information foundations. Project: [model limits](../science/model.md#6-limits-of-the-conclusion), [divergence and uniformity](../science/examples-and-limits.md#what-a-divergent-markov-length-would-require), and [the full-rank stability comparison](../references/comparison.md#relation-to-the-full-rank-stability-question).

<a id="m30"></a>

### M30 — Synthesis: a preparation-level obstruction to Markov criticality

**Phase:** Narrative/innovation.

**Central question:** What is the complete scientific reason a uniformly faithful finite-depth preparation has finite Markov length?

**Understanding target:** Give a connected account from causal regrouping to independent full-rank resources, internal conditional contraction, spatial iteration, and the uniform theorem. Separate textbook foundations, inherited Doeblin and sequential-channel results, and the circuit consequence established here. Explain how the exact example and finite checks support understanding while the analytical proof supplies the general conclusion.

**Dependencies and story role:** M12, M16, M18, M20, and M23–M29. This is the narrative synthesis and the global understanding target of the map.

**Conceptual connection:** A microscopic spectral preparation condition constrains macroscopic conditional-information structure, with a precise distinction between a necessary rank-boundary condition and a sufficient mechanism for criticality.

**Source pointers:** Wilde §§4.4–4.5 and 11.6–11.9. Project: [connected scientific account](../science/README.md), [exact theorem](../science/model.md#4-quantitative-theorem), [inherited and project-specific ingredients](../references/comparison.md#what-is-inherited-and-what-must-be-established-here), and [limits of finite verification](../verification/README.md#limits-of-this-evidence).
