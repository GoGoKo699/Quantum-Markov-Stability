#!/usr/bin/env python3
"""Finite numerical and combinatorial checks for the Markov-stability theorem.

These checks do not prove the theorem. All random draws use a fixed, reported
seed. Entropies use natural logarithms. No network or external data is used.
"""

from __future__ import annotations

import argparse
import bisect
from dataclasses import dataclass
import json
from pathlib import Path
import platform
import time

import numpy as np


TOL = 5e-9


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def hermitian(a):
    return (a + a.conj().T) / 2


def random_state(rng, dim, floor=0.02):
    z = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    rho = z @ z.conj().T
    rho /= np.trace(rho)
    return (1 - floor) * rho + floor * np.eye(dim) / dim


def random_unitary(rng, dim):
    z = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, _ = np.linalg.qr(z)
    return q


def random_channel(rng, din, dout, env=3):
    require(dout * env >= din, "Isometry output too small")
    z = rng.normal(size=(dout * env, din)) + 1j * rng.normal(size=(dout * env, din))
    v, _ = np.linalg.qr(z, mode="reduced")
    return [v[j * dout : (j + 1) * dout] for j in range(env)]


def check_channel(kraus):
    din = kraus[0].shape[1]
    err = np.linalg.norm(sum(k.conj().T @ k for k in kraus) - np.eye(din))
    require(err < TOL, f"Channel is not trace preserving: {err}")
    return float(err)


def partial_trace(rho, dims, keep):
    keep = set(keep)
    current = list(dims)
    t = rho.reshape(tuple(current + current))
    for i in reversed(range(len(dims))):
        if i not in keep:
            t = np.trace(t, axis1=i, axis2=i + len(current))
            current.pop(i)
    size = int(np.prod(current, dtype=int)) if current else 1
    return t.reshape(size, size)


def permute_state(rho, dims, order):
    n = len(dims)
    out_dims = [dims[i] for i in order]
    t = rho.reshape(tuple(dims + dims)).transpose(tuple(order + [i + n for i in order]))
    return t.reshape(rho.shape), out_dims


def entropy(rho):
    vals = np.linalg.eigvalsh(hermitian(rho))
    require(vals.min() > -TOL, f"Nonpositive density matrix: {vals.min()}")
    require(abs(vals.sum() - 1) < TOL, f"Density-matrix trace error: {vals.sum() - 1}")
    vals = vals[vals > 1e-14]
    return float(-np.dot(vals, np.log(vals)))


class Entropies:
    def __init__(self, rho, dims):
        self.rho = rho
        self.dims = list(dims)
        self.cache = {(): 0.0}

    def s(self, sites):
        key = tuple(sorted(set(sites)))
        if key not in self.cache:
            self.cache[key] = entropy(partial_trace(self.rho, self.dims, key))
        return self.cache[key]

    def cmi(self, a, c, b=()):
        a, b, c = set(a), set(b), set(c)
        require(not (a & b or a & c or b & c), "CMI systems overlap")
        return self.s(a | b) + self.s(b | c) - self.s(b) - self.s(a | b | c)


def apply_front(rho, dims, targets, kraus):
    """Apply a local channel, returning its single output subsystem first."""
    targets = list(targets)
    rest = [i for i in range(len(dims)) if i not in targets]
    moved, _ = permute_state(rho, list(dims), targets + rest)
    din = int(np.prod([dims[i] for i in targets]))
    dr = int(np.prod([dims[i] for i in rest]))
    dout = kraus[0].shape[0]
    require(kraus[0].shape[1] == din, "Local channel input dimension mismatch")
    t = moved.reshape(din, dr, din, dr)
    out = sum(np.einsum("ai,irjs,bj->arbs", k, t, k.conj(), optimize=True) for k in kraus)
    return out.reshape(dout * dr, dout * dr), [dout] + [dims[i] for i in rest]


def apply_local(rho, dims, targets, kraus):
    """Dimension-preserving local map with original subsystem order restored."""
    targets = list(targets)
    rest = [i for i in range(len(dims)) if i not in targets]
    out, _ = apply_front(rho, dims, targets, kraus)
    order = targets + rest
    split_dims = [dims[i] for i in order]
    inverse = list(np.argsort(order))
    restored, _ = permute_state(out, split_dims, inverse)
    return restored


def parity_channel():
    kraus = []
    for x in range(2):
        for l in range(2):
            k = np.zeros((2, 4), complex)
            k[x ^ l, 2 * x + l] = 1
            kraus.append(k)
    return kraus


def replacement_channel(rho, din):
    vals, vecs = np.linalg.eigh(hermitian(rho))
    ks = []
    for j, val in enumerate(vals):
        if val > 1e-14:
            for i in range(din):
                k = np.zeros((len(rho), din), complex)
                k[:, i] = np.sqrt(val) * vecs[:, j]
                ks.append(k)
    return ks


def inverse_sqrt(a):
    vals, vecs = np.linalg.eigh(hermitian(a))
    require(vals.min() > 0, "Inverse square root requires positive definiteness")
    return (vecs / np.sqrt(vals)) @ vecs.conj().T


def contraction_checks(rng, count=72):
    worst_gap = -float("inf")
    max_output = 0.0
    max_tp = 0.0
    max_reconstruction = 0.0
    min_p = 1.0
    zero_input_cases = 0
    nonzero_output_cases = 0
    for i in range(count):
        # A, B and X are all retained qubits. In particular B is not omitted.
        omega = random_state(rng, 8, floor=0.03)
        if i % 9 == 0:
            # Classical parity: I(A:X)=0 but I(A:X|B)=log(2).
            omega = np.zeros((8, 8), complex)
            for a in range(2):
                for x in range(2):
                    j = 4 * a + 2 * (a ^ x) + x
                    omega[j, j] = 0.25
        elif i % 9 == 1:
            # Exact conditional independence; X states need not commute.
            omega = np.zeros((8, 8), complex)
            for b in range(2):
                tau = random_state(rng, 2)
                omega[6 * b : 6 * b + 2, 6 * b : 6 * b + 2] = tau / 2
            zero_input_cases += 1

        dm = 2 if i % 3 == 0 else 1
        dims_sigma = [2, dm, 2]
        if i % 7 == 0:
            sigma = np.kron(random_state(rng, 2 * dm), random_state(rng, 2))
        else:
            sigma = random_state(rng, 4 * dm, floor=[0.002, 0.08, 0.4][i % 3])
        left = partial_trace(sigma, dims_sigma, [0, 1])
        right = partial_trace(sigma, dims_sigma, [2])
        product = np.kron(left, right)
        b_inv = inverse_sqrt(product)
        p = float(np.linalg.eigvalsh(hermitian(b_inv @ sigma @ b_inv)).min())
        p = min(1.0, p)
        require(p > 0, "Faithful resource has nonpositive minorization coefficient")
        min_p = min(min_p, p)

        kind = i % 5
        if kind == 0:
            ks = [np.eye(4)]
        elif kind == 1:
            ks = [random_unitary(rng, 4)]
        elif kind == 2:
            ks = random_channel(rng, 4, 4, env=3)
        elif kind == 3:
            ks = replacement_channel(random_state(rng, 3), 4)
        else:
            ks = parity_channel()
        max_tp = max(max_tp, check_channel(ks))
        # Input order A B X L M R; output order Y A B M R.
        output, dims = apply_front(np.kron(omega, sigma), [2, 2, 2, 2, dm, 2], [2, 3], ks)
        before = Entropies(omega, [2, 2, 2]).cmi([0], [2], [1])
        after = Entropies(output, dims).cmi([1], [4], [0, 2, 3])
        gap = after - (1 - p) * before
        require(before >= -TOL and after >= -TOL, "Negative CMI beyond numerical tolerance")
        require(gap <= TOL, f"Contraction inequality failed in case {i}: gap={gap}")
        worst_gap = max(worst_gap, gap)
        max_output = max(max_output, after)
        nonzero_output_cases += int(after > 1e-7)

        # Independently reconstruct sigma using the internal Choi channel.
        inv = np.kron(inverse_sqrt(left), np.eye(2))
        choi = hermitian(inv @ sigma @ inv)
        require(np.linalg.norm(partial_trace(choi, [2 * dm, 2], [0]) - np.eye(2 * dm)) < TOL,
                "Internal Choi channel is not trace preserving")
        require(np.linalg.eigvalsh(hermitian(choi - p * np.kron(np.eye(2 * dm), right))).min() > -TOL,
                "Internal Doeblin minorization failed")
        vals, vecs = np.linalg.eigh(choi)
        tks = [np.sqrt(v) * vecs[:, j].reshape(2 * dm, 2).T for j, v in enumerate(vals) if v > 1e-14]
        root_vals, root_vecs = np.linalg.eigh(left)
        root = (root_vecs * np.sqrt(root_vals)) @ root_vecs.conj().T
        purification = root.reshape(-1)
        purified = np.outer(purification, purification.conj())
        rebuilt, rdims = apply_front(purified, [2 * dm, 2 * dm], [1], tks)
        rebuilt, _ = permute_state(rebuilt, rdims, [1, 0])
        reconstruction = float(np.linalg.norm(rebuilt - sigma))
        max_reconstruction = max(max_reconstruction, reconstruction)
        require(reconstruction < TOL, "Internal-leg resource reconstruction failed")

    # Negative control: arbitrary CMI convexity would give the wrong answer.
    omega_ax = np.diag([0.5, 0.0, 0.0, 0.5]).astype(complex)
    branches = []
    for f in range(2):
        sigma = np.zeros((4, 4), complex)
        sigma[3 * f, 3 * f] = 1
        out, ds = apply_front(np.kron(omega_ax, sigma), [2, 2, 2, 2], [1, 2], parity_channel())
        branches.append(out)
        require(abs(Entropies(out, ds).cmi([1], [2], [0])) < TOL, "Product branch control failed")
    mixture_cmi = Entropies((branches[0] + branches[1]) / 2, ds).cmi([1], [2], [0])
    require(abs(mixture_cmi - np.log(2)) < TOL, "CMI nonconvexity negative control failed")
    return dict(cases=count, zero_input_cmi_cases=zero_input_cases,
                nonzero_output_cmi_cases=nonzero_output_cases,
                minimum_resource_p=min_p, maximum_output_cmi=max_output,
                maximum_bound_excess=worst_gap, maximum_trace_preservation_error=max_tp,
                maximum_internal_leg_reconstruction_error=max_reconstruction,
                unequal_marginal_negative_control_cmi=mixture_cmi)


@dataclass(frozen=True)
class Gate:
    layer: int
    support: tuple[int, ...]


def analyze_dag(gates, n, cuts, strip_width=None):
    last = [None] * n
    input_cones = [{i} for i in range(n)]
    preds, cones, labels = [], [], []
    occupied = {}
    for j, g in enumerate(gates):
        used = occupied.setdefault(g.layer, set())
        require(not used.intersection(g.support), "Gates overlap within a layer")
        used.update(g.support)
        pred = {last[x] for x in g.support if last[x] is not None}
        cone = set().union(*(input_cones[x] for x in g.support))
        blocks = {bisect.bisect_right(cuts, x) for x in cone}
        if len(blocks) == 1:
            label = (0, next(iter(blocks)))
        else:
            require(len(blocks) == 2 and max(blocks) == min(blocks) + 1,
                    "A remaining gate meets more than one block boundary")
            boundary_index = min(blocks)
            label = (1, boundary_index)
            if strip_width is not None:
                boundary = cuts[boundary_index]
                require(all(boundary - strip_width <= x < boundary + strip_width for x in g.support),
                        "Remaining gate is outside its boundary strip")
        preds.append(pred)
        cones.append(cone)
        labels.append(label)
        for x in g.support:
            last[x] = j
            input_cones[x] = cone.copy()
    for j, label in enumerate(labels):
        if label[0] == 0:
            require(all(labels[p] == label for p in preds[j]), "First-layer set is not ancestor closed")
    second_support = {}
    for g, label in zip(gates, labels):
        if label[0] == 1:
            second_support.setdefault(label[1], set()).update(g.support)
    occupied = set()
    for support in second_support.values():
        require(not occupied.intersection(support), "Coarse boundary channels overlap")
        occupied.update(support)
    order = sorted(range(len(gates)), key=lambda j: (*labels[j], gates[j].layer, j))
    positions = {j: i for i, j in enumerate(order)}
    require(all(positions[p] < positions[j] for j, ps in enumerate(preds) for p in ps),
            "Regrouping reversed a causal dependency")
    return order, labels, preds, cones


def random_layer(rng, n, r, layer):
    free = set(range(n))
    out = []
    while free:
        start = min(free)
        possible = [x for x in range(start, min(n, start + r)) if x in free]
        support = [start] + [x for x in possible[1:] if rng.random() < 0.65]
        for x in support:
            free.remove(x)
        if rng.random() < 0.82:
            out.append(Gate(layer, tuple(support)))
    return out


def structural_checks(rng, count=320):
    total_gates = total_second = noninterval = max_cone = 0
    edge_sizes = set()
    for i in range(count):
        depth = 1 + i % 8
        r = 1 + (i // 8) % 5
        k = 4 * depth * r + 1
        end_size = 1 + int(rng.integers(k))
        n = 2 * k + end_size
        cuts = [k, 2 * k]
        edge_sizes.add(end_size)
        gates = [g for layer in range(depth) for g in random_layer(rng, n, r, layer)]
        _, labels, _, cones = analyze_dag(gates, n, cuts, depth * r)
        total_gates += len(gates)
        total_second += sum(label[0] == 1 for label in labels)
        noninterval += sum(len(g.support) != max(g.support) - min(g.support) + 1 for g in gates)
        max_cone = max(max_cone, max((max(c) - min(c) + 1 for c in cones), default=0))
        # Independently check the strip-count argument used by the small-buffer bound.
        for cut in cuts:
            for layer in range(depth):
                crossing = [g for g in gates if g.layer == layer and min(g.support) < cut <= max(g.support)]
                require(sum(len(g.support) for g in crossing) <= 2 * (r - 1),
                        "Cut-crossing support count exceeds the layer bound")
    # A later gate wholly inside a block can nevertheless have a crossing cone.
    fixture = [Gate(0, (2, 3)), Gate(1, (3, 4)), Gate(2, (4, 5))]
    _, labels, preds, _ = analyze_dag(fixture, 6, [3], strip_width=6)
    require(labels == [(1, 0)] * 3, "Backward-cone adversarial fixture was misclassified")
    naive = sorted(range(3), key=lambda j: (len({x // 3 for x in fixture[j].support}) != 1, j))
    pos = {j: i for i, j in enumerate(naive)}
    require(any(pos[p] > pos[j] for j, ps in enumerate(preds) for p in ps),
            "Naive geometric grouping negative control did not fail")
    return dict(cases=count, gates=total_gates, second_coarse_layer_gates=total_second,
                noncontiguous_support_gates=noninterval, distinct_short_end_block_sizes=len(edge_sizes),
                largest_input_cone_span=max_cone, naive_geometric_grouping_rejected=True)


def lift_qubit_operator(local, n, targets):
    """Slow independent basis-index implementation for small reference cases."""
    targets = list(targets)
    k = len(targets)
    full = np.zeros((2**n, 2**n), complex)
    for col in range(2**n):
        old = [(col >> (n - 1 - j)) & 1 for j in range(n)]
        local_col = sum(old[t] << (k - 1 - j) for j, t in enumerate(targets))
        for local_row in range(2**k):
            new = old.copy()
            for j, t in enumerate(targets):
                new[t] = (local_row >> (k - 1 - j)) & 1
            row = sum(bit << (n - 1 - j) for j, bit in enumerate(new))
            full[row, col] = local[local_row, local_col]
    return full


def faithful_damping_gate(rng, sites):
    gamma = float(rng.uniform(0.12, 0.65))
    identity = np.eye(2 ** (sites - 1))
    a0 = np.kron(np.diag([1.0, np.sqrt(1 - gamma)]), identity)
    a1 = np.kron(np.array([[0.0, np.sqrt(gamma)], [0.0, 0.0]]), identity)
    u = random_unitary(rng, 2**sites)
    return [a0 @ u, a1 @ u]


def circuit_equality_checks(rng):
    # Single-boundary small circuits allow exact dense checks; the universal
    # K=4Dr+1 layout is tested at larger sizes by structural_checks above.
    fixtures = [
        (4, [Gate(0, (1, 2)), Gate(0, (0,)), Gate(0, (3,)),
             Gate(1, (0, 1)), Gate(1, (2, 3)), Gate(2, (1, 2))]),
        (6, [Gate(0, (2, 3)), Gate(0, (0, 1)), Gate(0, (4, 5)),
             Gate(1, (1, 2)), Gate(1, (4, 5)),
             Gate(2, (0, 1)), Gate(2, (3, 4)), Gate(2, (5,))]),
    ]
    max_difference = 0.0
    negative_control_difference = 0.0
    for n, gates in fixtures:
        order, _, _, _ = analyze_dag(gates, n, [n // 2], strip_width=n)
        channels = [faithful_damping_gate(rng, len(g.support)) for g in gates]
        for ks in channels:
            check_channel(ks)
            require(np.linalg.eigvalsh(sum(k @ k.conj().T for k in ks)).min() > 0,
                    "Finite-circuit gate is not faithful")
        if n == 4:
            # Choi-state comparison checks the entire channel, including a reference.
            v = np.eye(2**n).reshape(-1) / np.sqrt(2**n)
            rho = np.outer(v, v.conj())
            actual_n = 2 * n
        else:
            rho = random_state(rng, 2**n)
            actual_n = n
        original = rho.copy()
        for g, ks in zip(gates, channels):
            lifted = [lift_qubit_operator(k, actual_n, g.support) for k in ks]
            original = sum(k @ original @ k.conj().T for k in lifted)
        regrouped = rho.copy()
        for j in order:
            regrouped = apply_local(regrouped, [2] * actual_n, gates[j].support, channels[j])
        difference = float(np.linalg.norm(original - regrouped))
        require(difference < TOL, f"Nonunitary regrouping changed the channel/state: {difference}")
        max_difference = max(max_difference, difference)
        if n == 4:
            naive_order = sorted(range(len(gates)),
                                 key=lambda j: (len({x // (n // 2) for x in gates[j].support}) != 1, j))
            wrong = rho.copy()
            for j in naive_order:
                wrong = apply_local(wrong, [2] * actual_n, gates[j].support, channels[j])
            negative_control_difference = float(np.linalg.norm(original - wrong))
            require(negative_control_difference > 1e-4, "Naive grouping did not change the test channel")
    return dict(cases=len(fixtures), whole_channel_choi_cases=1,
                maximum_frobenius_difference=max_difference,
                naive_geometric_grouping_choi_difference=negative_control_difference)


def bell_state():
    v = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
    return np.outer(v, v.conj())


def bell_measurement():
    basis = [np.array(v, complex) / np.sqrt(2) for v in
             ([1, 0, 0, 1], [1, 0, 0, -1], [0, 1, 1, 0], [0, 1, -1, 0])]
    return [np.outer(np.eye(4)[j], v.conj()) for j, v in enumerate(basis)]


def spatial_checks():
    max_formula_error = 0.0
    max_endpoint_mi = 0.0
    examples = []
    geometry_checks = 0
    max_geometry_excess = -float("inf")
    for visibility in (0.2, 0.65, 0.9):
        for links in (2, 3, 4):
            pair = visibility * bell_state() + (1 - visibility) * np.eye(4) / 4
            rho = np.array([[1.0]], complex)
            for _ in range(links):
                rho = np.kron(rho, pair)
            n = 2 * links
            for j in range(links - 1):
                rho = apply_local(rho, [2] * n, [2 * j + 1, 2 * j + 2], bell_measurement())
            ent = Entropies(rho, [2] * n)
            actual = ent.cmi([0], [n - 1], range(1, n - 1))
            v = visibility**links
            expected = 2 * np.log(2) - entropy(v * bell_state() + (1 - v) * np.eye(4) / 4)
            error = abs(actual - expected)
            require(error < TOL, "Noisy Bell-chain CMI disagrees with its analytic value")
            require(actual <= 2 * np.log(2) * visibility ** (links - 1) + TOL,
                    "Aligned resource-chain contraction failed")
            endpoint_mi = abs(ent.cmi([0], [n - 1]))
            require(endpoint_mi < TOL, "Distant Bell-chain endpoints have unexpected unconditional MI")
            max_endpoint_mi = max(max_endpoint_mi, endpoint_mi)
            max_formula_error = max(max_formula_error, error)
            examples.append(dict(visibility=visibility, links=links, cmi=actual, analytic_cmi=expected))
            if links == 3 and visibility == 0.65:
                # All ordered interval triples, including empty/tiny buffers.
                for start in range(n - 1):
                    for a in range(start + 1, n):
                        for b in range(a, n):
                            for end in range(b + 1, n + 1):
                                lhs = ent.cmi(range(start, a), range(b, end), range(a, b))
                                cut_mi = ent.cmi(range(a), range(a, n))
                                excess = lhs - cut_mi
                                require(excess < TOL, "Ordered interval absorption into a physical cut failed")
                                max_geometry_excess = max(max_geometry_excess, excess)
                                geometry_checks += 1
                # Two-sided line geometry; both buffers may be empty.
                for l in range(1, n - 1):
                    for a in range(l, n - 1):
                        for b in range(a + 1, n):
                            for r in range(b, n):
                                cl, bl, aa, br, cr = (list(range(l)), list(range(l, a)), list(range(a, b)),
                                                     list(range(b, r)), list(range(r, n)))
                                lhs = ent.cmi(aa, cl + cr, bl + br)
                                rhs = ent.cmi(cl, aa + br + cr, bl) + ent.cmi(cl + bl + aa, cr, br)
                                excess = lhs - rhs
                                require(excess < TOL, "Two-sided line inequality failed")
                                max_geometry_excess = max(max_geometry_excess, excess)
                                geometry_checks += 1
                # Partial-cell absorption, retaining a nonempty middle buffer.
                for a in range(1, n - 2):
                    for b in range(a + 1, n):
                        for lo in range(a, b):
                            for hi in range(lo + 1, b + 1):
                                lhs = ent.cmi(range(a), range(b, n), range(a, b))
                                rhs = ent.cmi(range(lo), range(hi, n), range(lo, hi))
                                excess = lhs - rhs
                                require(excess < TOL, "Partial-cell enlargement inequality failed")
                                max_geometry_excess = max(max_geometry_excess, excess)
                                geometry_checks += 1
    return dict(bell_chain_cases=len(examples), examples=examples,
                maximum_analytic_cmi_error=max_formula_error,
                maximum_distant_endpoint_mutual_information=max_endpoint_mi,
                geometry_inequalities=geometry_checks,
                maximum_geometry_bound_excess=max_geometry_excess)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261030)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    rng = np.random.default_rng(args.seed)
    result = dict(seed=args.seed, python=platform.python_version(), numpy=np.__version__,
                  entropy_units="nats", absolute_tolerance=TOL)
    result["contraction"] = contraction_checks(rng)
    result["structural_regrouping"] = structural_checks(rng)
    result["nonunitary_circuit_equality"] = circuit_equality_checks(rng)
    result["spatial_cmi"] = spatial_checks()
    result["status"] = "all finite checks passed"
    result["elapsed_seconds"] = round(time.monotonic() - started, 3)
    result["limitation"] = "Finite numerical and combinatorial checks do not prove the universal theorem."
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
