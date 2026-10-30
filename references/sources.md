# Primary sources and verification record

Checked on 30 October 2026. Section, theorem, and equation numbers below refer to the specified versions. “Reviewed” identifies the portions used in [comparison.md](comparison.md); it does not claim a complete independent audit of each paper.

## CKB23

Chi-Fang (Anthony) Chen, Kohtaro Kato, and Fernando G. S. L. Brandão, **“Matrix Product Density Operators: when do they have a local parent Hamiltonian?”** arXiv:2010.14682v3, 13 May 2023.

- [Versioned abstract](https://arxiv.org/abs/2010.14682v3)
- [Versioned PDF](https://arxiv.org/pdf/2010.14682v3)
- [Versioned HTML](https://arxiv.org/html/2010.14682v3)
- Reviewed PDF locations: Section III.B, Proposition III.2, Eqs. (38)–(42), printed p. 15; proof in Section V.B.3, printed p. 30; adjacent discussion in Section III.C.
- **Format distinction:** the HTML labels the same proposition's location Section III.2, Eqs. (53)–(57), and its proof Section V.2.3. PDF numbering is the default for CKB23 in this repository.
- Used for: CP replacement decomposition, conditional-memory contraction, and exponential CMI in a sequential MPDO construction.

## HGNW26

Christoph Hirche, Ian George, Theshani Nuradha, and Mark M. Wilde, **“Conditional contraction coefficients and their applications to quantum networks.”** arXiv:2608.27171v1, 27 August 2026.

- [Versioned abstract](https://arxiv.org/abs/2608.27171v1)
- [Versioned full text](https://arxiv.org/html/2608.27171v1)
- Reviewed: Section 2.4, Propositions 1–2, Eqs. (2.36)–(2.37); Section 3.1, Corollary 1, Eq. (3.24) and its proof; Section 7.2, Propositions 21–24, Eqs. (7.47)–(7.58).
- Normalization: Proposition 23 uses the **unnormalized** Choi operator. Its bound is $`\alpha_+(N)\ge |B|\lambda_{\min}(\Gamma^N)`$ for $`N:A\to B`$. The resource-marginal normalization in the circuit proof also constructs an unnormalized Choi operator; it should not be confused with division by the input dimension to obtain a Choi state.

## SMK24

Pavel Svetlichnyy, Shivan Mittal, and T. A. B. Kennedy, **“Matrix product states and the decay of quantum conditional mutual information.”** arXiv:2211.06794v2, 6 March 2024; *Journal of Mathematical Physics* **65**, 022201 (2024).

- [Versioned abstract](https://arxiv.org/abs/2211.06794v2)
- [Versioned full text](https://arxiv.org/html/2211.06794v2)
- [Published article](https://doi.org/10.1063/5.0152063)
- Reviewed: introduction's distinction between MPS and general MPDOs; Section II, Eqs. (1)–(5); Section III, Theorem III.1 and its explanatory remarks.
- Model: infinite uniform MPS specified by an isometry and a stationary virtual state. The theorem bounds CMI by an exponential times a polynomial in the buffer length.

## YLLLZ26

Jinmin Yi, Kangle Li, Chuan Liu, Zixuan Li, and Liujun Zou, **“Universal Decay of Mutual Information and Conditional Mutual Information in Gapped Pure- and Mixed-State Quantum Matter.”** arXiv:2510.22867v3, 19 March 2026; *Physical Review Letters* **136**, 116604 (2026).

- [Versioned abstract](https://arxiv.org/abs/2510.22867v3)
- [Versioned full text](https://arxiv.org/html/2510.22867v3)
- [Published article](https://doi.org/10.1103/mqp8-y1m7)
- Reviewed: Theorem 2; Definition 1, Eqs. (14)–(16), and its following discussion; Supplementary Theorem VII.1.
- Used for: stability of correlation decay under the paper's explicit local-reversibility condition. Forward and reverse finite-depth channels, including subset-of-gates requirements, are part of that condition.

## ZG25

Yifan F. Zhang and Sarang Gopalakrishnan, **“Stability of mixed-state phases under weak decoherence.”** arXiv:2511.01976v1, submitted 3 November 2025.

- [Versioned abstract](https://arxiv.org/abs/2511.01976v1)
- [Versioned PDF](https://arxiv.org/pdf/2511.01976v1)
- Reviewed: Sections I.A and II.B; Definitions 3–4; Theorem 5; Appendix B, Theorem 38, including Eqs. (B6)–(B7).
- Used for: the quantum weak-noise result's commuting-Pauli input and stabilizer-mixing hypotheses. The submission date above is distinguished from the date printed inside the PDF.

## ZG25HT

Yifan Zhang and Sarang Gopalakrishnan, **“Conditional Mutual Information and Information-Theoretic Phases of Decohered Gibbs States.”** arXiv:2502.13210v1, 18 February 2025.

- [Versioned abstract](https://arxiv.org/abs/2502.13210v1)
- [Versioned full text](https://arxiv.org/html/2502.13210v1)
- Reviewed: Definition 1 and Theorem 1 in the main text; Appendix A, Theorem A.1, Eq. (13), and its stated hypotheses.
- Used for: high-temperature commuting-Gibbs results under single-site unital, commutation-preserving channels.
- Publication metadata: the authors' related published article is titled **“Approximate Markovianity in high-temperature hidden Markov networks,”** *Physical Review B* **113**, 115101 (2026), [publisher page](https://journals.aps.org/prb/abstract/10.1103/gbzk-v4bh). Technical pointers here refer to the explicitly inspected arXiv version, not to presumed identical numbering in the publication.

## T26

Xuan Du Trinh, Nicholas Pardave, Angie Huang, Xiangyi Meng, and Nengkun Yu, **“Full-Rank Noise Forbids Long-Range Entanglement Swapping.”** arXiv:2609.11021v1, 10 September 2026.

- [Primary abstract](https://arxiv.org/abs/2609.11021)
- [Versioned record](https://arxiv.org/abs/2609.11021v1)
- Reviewed: **abstract only**. The complete text was unavailable in this review.
- Verified scope from that abstract: full-rank entangled two-qubit links, adaptive postselected swapping, a finite entanglement distance, and a connection to MPDO/localizable-entanglement constructions.
- Outstanding: complete-paper comparison, including exact theorem hypotheses, the MPDO extension, and proof-level overlap. No claim about those uninspected details is made.

## NL26

David C. Newsom and Michael Levin, **“An Instability of the Quantum Markov Length.”** arXiv:2610.12929v3, 29 October 2026.

- [Versioned abstract](https://arxiv.org/abs/2610.12929v3)
- [Versioned full text](https://arxiv.org/html/2610.12929v3)
- Reviewed: introduction and Markov-length convention; the pure-product Gaussian construction; discussion of finite-temperature perturbations; the closing discussion immediately before “Note added”; footnote 4 concerning one-sided and two-sided geometries.
- Used for: the explicit question about full-rank initial states and the limitation of the present answer to uniformly faithful one-dimensional product inputs.

## GKS76

Vittorio Gorini, Andrzej Kossakowski, and E. C. G. Sudarshan, **“Completely positive dynamical semigroups of N-level systems.”** *Journal of Mathematical Physics* **17**, 821–825 (1976).

- [Publisher DOI](https://doi.org/10.1063/1.522979)
- Reviewed: publisher bibliographic record and abstract, which identifies the finite-dimensional completely positive semigroup generator characterization.
- Used for: the standard generator form in the local Lindblad-gate example in [examples-and-limits.md](../science/examples-and-limits.md). The quantitative faithfulness estimate displayed there is derived in the repository; it is not presented as a quoted theorem from this paper.
