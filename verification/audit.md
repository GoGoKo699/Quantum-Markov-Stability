# Boundary-case and causal-structure audit

This note records independent checks of the places where a line-circuit argument can fail: nonunitary gate reordering, arbitrary cuts, small buffers, edge blocks, and two-sided conditioning. It is a mathematical audit of the stated proof, supplemented by the finite checks in [verify.py](verify.py). It is not a formal proof-assistant certificate or an external expert review.

The model, assumptions, and constants are defined in [model.md](../science/model.md). The contraction and its sequential iteration are inherited information-theoretic tools. The circuit consequence relies on showing that their hypotheses follow from this preparation model.

## 1. Nonunitary regrouping must preserve the wire DAG

Moving every geometrically interior gate before every boundary gate is generally invalid. A gate can act inside one spatial block after receiving information through an earlier boundary-crossing gate. Neither trace preservation nor faithfulness permits reversing that dependency.

The safe construction uses the complete structural backward cone of a gate, including all input wires of every ancestor. A first-layer group consists of gates whose entire cone lies in one input block. If $`h`$ is an ancestor of such a gate $`g`$, then $`C(h)\subseteq C(g)`$, so $`h`$ belongs to the same group. The selected groups are therefore ancestor closed.

Any topological ordering of the wire DAG gives the same channel: whenever two ordered gates share a physical site, the earlier one is a predecessor of the later one along that wire. Only gates with disjoint supports can be interchanged in a legal topological reorder, and their extended CPTP maps commute. No inverse channel, recovery map, or channel-specific erasure of a dependency is used.

The remaining geometric step uses the bound $`|x-y|\le Dr`$ for every output support site $`x`$ of a gate and every initial site $`y`$ in its structural cone. A remaining cone crosses one coarse-block boundary, and the entire gate support lies within $`Dr`$ sites of that boundary on either side. With $`K=4Dr+1`$, distinct boundary strips are disjoint. These facts apply equally to noncontiguous actual supports with overlapping interval hulls.

The fixed negative controls in the verifier reject physical-support-only regrouping both at the dependency level and by a nonzero change in a small nonunitary channel's Choi state.

## 2. Small buffers need a cut bound

An arbitrary physical buffer may contain no complete emitted cell. In that case one cannot invoke a full-cell contraction step, and absorbing both endpoint fragments without checking their geometry can incorrectly place the same cell on both sides.

A direct cut mutual-information bound handles this case. Consider one gate crossing a cut. Let $`a`$ and $`b`$ be its support to the left and right, and let $`L`$ and $`R`$ be the untouched exteriors. The output support is denoted $`a'b'`$; its dimensions equal those of $`ab`$ in the stated circuit model. Trace preservation leaves the $`LR`$ marginal unchanged. By the chain rule and the dimension bound on conditional mutual information,

```math
\begin{aligned}
I(La':b'R)_{\mathrm{out}}
&\le I(L:R)_{\mathrm{out}}
   +2\log\dim a'+2\log\dim b'\\
&=I(L:R)_{\mathrm{in}}
   +2\log\dim a+2\log\dim b\\
&\le I(La:bR)_{\mathrm{in}}
   +2|S_g|\log d.
\end{aligned}
```

Thus the gate increases cut mutual information by at most $`2|S_g|\log d`$. Gates wholly on one side cannot increase it.

For a gate of hull range at most $`r`$ to cross the cut between $`c`$ and $`c+1`$, every site in its support lies in

```math
\{c-r+2,\ldots,c+r-1\},
```

which has $`2(r-1)`$ sites. Actual supports within a layer are disjoint. Hence the sum of their crossing support sizes is at most $`2(r-1)`$, even if their hulls overlap. Starting from a product state and summing over $`D`$ layers gives

```math
I(\text{left}:\text{right})
\le4D(r-1)\log d
\le4Dr\log d.
```

For any consecutive interior intervals $`A:B:C`$,

```math
I(A:C\mid B)
\le I(A:BC)
\le I(\text{full left prefix}:\text{full right suffix}),
```

where the cut is the physical boundary immediately to the right of $`A`$. This proves the needed $`4Dr\log d`$ estimate for empty buffers, tiny buffers, and interior intervals without assuming that $`ABC`$ exhausts the chain.

## 3. Absorbing incomplete endpoint cells

If the buffer contains at least one complete emitted cell, decompose it as $`B_\ell B_0 B_r`$, where $`B_0`$ is a union of complete consecutive cells and $`B_\ell,B_r`$ are the endpoint fragments. Chain rule and nonnegativity give

```math
I(A:C\mid B_\ell B_0 B_r)
\le I(AB_\ell:CB_r\mid B_0).
```

For example, expanding the right side first on $`AB_\ell`$ and then on $`CB_r`$ leaves the left side plus two nonnegative CMIs. After this absorption, the endpoint regions may be enlarged further on their unconditioned sides to a full emitted prefix and a generated future suffix. Conditional data processing permits those enlargements because the retained conditioning region is unchanged.

The endpoint fragments have total length less than $`2K`$, so the number $`k`$ of complete cells obeys

```math
k\ge \max\{0,\lfloor |B|/K\rfloor-2\}.
```

The aligned sequential contraction starts from an incoming memory of at most $`w=Dr`$ sites. It gives $`2w\log d\,q^k`$ for the enlarged state. The common prefactor $`4w\log d`$ also covers the no-complete-cell case from the previous section. The constants need not be optimized to obtain a uniform exponential bound.

## 4. Edge blocks and finite-chain padding

An incomplete terminal block is not entitled to a $`K`$-site cell count without a boundary argument. Independent padding supplies one. Add at least $`K`$ maximally mixed $`d`$-dimensional sites at each end and choose the right padding to make the total length divisible by $`K`$. No original gate acts on them.

The padded output factors as independent left padding, the original output, and independent right padding. Every original reduced state is unchanged. The convention $`\delta\le1/d`$ preserves the input floor, and identity gates satisfy the declared $`\alpha\le1`$ floor. All original sites then lie between the exceptional initial emitted interval and final memory of the sequential representation; their buffers encounter the regular $`K`$-site emitted cells.

This construction is valid even for a one-site chain or a chain shorter than one coarse block. The finite structural checks additionally include short unpadded terminal blocks, but the proof uses padding to keep the cell accounting uniform.

## 5. Two-sided line geometry

For the ordered regions

```math
C_L\;B_L\;A\;B_R\;C_R,
```

the needed inequality is

```math
\begin{aligned}
I(A:C_LC_R\mid B_LB_R)
\le{}&I(C_L:AB_RC_R\mid B_L)\\
&+I(C_LB_LA:C_R\mid B_R).
\end{aligned}
```

To verify it, expand the left side as

```math
I(A:C_L\mid B_LB_R)
+I(A:C_R\mid B_LB_RC_L).
```

The first term is bounded by the first CMI on the right by expanding the latter with $`B_R`$ first, then $`A`$, then $`C_R`$. The second term is bounded by the second CMI on the right by expanding its left endpoint with $`C_LB_L`$ first and then $`A`$. Every discarded term is nonnegative.

The two right-hand CMIs are one-sided line geometries with buffers $`B_L`$ and $`B_R`$, respectively. Applying the proved one-sided bound to each yields the sum of exponentials. A buffer may be empty. An absent outer region contributes zero and need not be assigned a nonzero bound.

This is a line argument. It does not turn a ring into an open chain or account for an additional route around periodic boundaries.

## 6. Infinite lines and uniformity

For a fixed finite output region, a fixed-depth finite-range circuit depends on only finitely many input sites and gates. Enlarge the finite restriction to include its complete backward cone. Gates outside that cone cannot change the reduced state, by trace preservation. The finite-chain estimate then applies with constants independent of the enlarged restriction.

For a fixed finite buffer and increasingly large endpoint regions, CMI is monotone under inclusion of either unconditioned endpoint. Its bounded monotone limit defines the semi-infinite endpoint version. This avoids assigning potentially infinite entropies to half-chain density matrices and subtracting them formally.

The input floor, gate faithfulness floor, depth, range, and site-dimension bound must remain uniform. A separate positive lower bound for each finite system without a common floor does not yield a common Markov-length estimate.

## 7. What the audit does not establish

The local contraction is a consequence of established internal-channel Doeblin contraction, and its sequential iteration is standard. Neither is certified as a new information-theoretic inequality here.

The conservative value $`p_0=\delta^K\alpha^{KD}`$ may be extremely small. The conclusion is qualitative finiteness of a uniform spatial Markov length under fixed assumptions; it does not provide a sharp physical decay length or a practical numerical certificate at large depth.

The audit supplies no extension to correlated initial states, global shared gate coins, postselected channels, periodic rings, higher dimensions, or an extensive continuous-time evolution obtained by sending circuit depth to infinity. It is limited to the model as stated.
