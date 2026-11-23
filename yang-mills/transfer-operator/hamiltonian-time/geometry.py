"""Check periodic edge multiplicities, gauge cycles and the local supports of the Hamiltonian."""
from collections import Counter, defaultdict, deque
from itertools import combinations, product
import json
import math


def advance(x, axis, size):
    return tuple((v+1) % size if k == axis else v for k, v in enumerate(x))


def girth(adjacency, edges):
    best = len(edges) + 1
    for origin, axis in edges:
        end = edges[origin, axis]
        blocked = (origin, axis)
        queue = deque([(origin, 0)])
        seen = {origin}
        while queue:
            vertex, dist = queue.popleft()
            if dist + 2 >= best:
                continue
            for nxt, edge in adjacency[vertex]:
                if edge == blocked or nxt in seen:
                    continue
                if nxt == end:
                    best = dist + 2
                    break
                queue.append((nxt, dist + 1))
                seen.add(nxt)
    return best


def check(size):
    sites = list(product(range(size), repeat=3))
    adjacency = defaultdict(list)
    edges, covers, anchors = {}, Counter(), {}
    for x in sites:
        targets = {x}
        for axis in range(3):
            y = advance(x, axis, size)
            edges[x, axis] = y
            adjacency[x].append((y, (x, axis)))
            adjacency[y].append((x, (x, axis)))
        for i, j in combinations(range(3), 2):
            face = [(x, i), (advance(x, i, size), j), (advance(x, j, size), i), (x, j)]
            if len(set(face)) != 4:
                raise ValueError("a plaquette repeats an unoriented link")
            targets.update(y for y, _ in face)
        anchors[x] = targets
        covers.update(targets)
    if set(covers.values()) != {4} or any(len(s) != 4 for s in anchors.values()):
        raise ValueError("overlapping electric blocks do not cover each site exactly four times")
    turns = girth(adjacency, edges)
    if turns != min(size, 4):
        raise ValueError(f"unexpected shortest circuit at side {size}: {turns}")
    # Excite a neighboring site in just one outgoing spin-1/2 link. The term
    # that acts solely at the anchor sees zero. The redistributed term sees one.
    first = sites[0]
    spectator = next(y for y in anchors[first] if y != first)
    costs = [int(spectator == first), sum(int(y == spectator) for y in anchors[first])]
    if costs != [0, 1]:
        raise ValueError("spectator control did not distinguish the two block forms")
    return {"sites": len(sites), "edges": len(edges), "girth": turns, "site_coverage": covers[first],
            "spectator_costs": costs}


def haar_modes():
    """Midpoint quadrature of normalized characters, independent of a Bessel implementation."""
    angles = [math.pi*(i+0.5)/4096 for i in range(4096)]
    results = []
    prior = {}
    for coupling in (64, 256, 1024):
        weights = [math.exp(coupling*(math.cos(x)-1))*math.sin(x)**2 for x in angles]
        norm = math.fsum(weights)
        energies = []
        for n in (1, 2, 4):
            eigenvalue = math.fsum(w*math.sin((n+1)*x)/((n+1)*math.sin(x))
                                   for x, w in zip(angles, weights)) / norm
            energy = -coupling*math.log(eigenvalue)
            error = abs(energy-n*(n+2)/2)
            if error >= prior.get(n, float("inf")) or (coupling == 1024 and error >= 0.007):
                raise ValueError("fixed-order Casimir control failed")
            if n == 1 and not (0 < coupling*(1-eigenvalue) <= 1.5):
                raise ValueError("polar trial Gamma bound failed")
            prior[n] = error
            energies.append(round(energy, 9))
        results.append([coupling, *energies])
    return results


def generate(out):
    controls = {str(size): check(size) for size in (2, 3, 4, 5, 6)}
    (out / "geometry.json").write_text(json.dumps(
        {"tori": controls, "coupling_and_energies_n_1_2_4": haar_modes()}, indent=2) + "\n")
    count = controls["2"]["site_coverage"]
    names = ("p", "q", "r")[:count-1]
    summands = " + ".join(["A i", *(f"A ({name} i)" for name in names)])
    proof = ("/-- Sum over the four translations of the anchored sites. Each shift is a permutation. -/\n"
             f"theorem rangeSum {{ι : Type*}} [Fintype ι] (A : ι → ℝ) ({' '.join(names)} : Equiv.Perm ι) :\n"
             f"    ∑ i, ({summands}) = {count} * ∑ i, A i := by\n"
             "  simp only [Finset.sum_add_distrib, Equiv.sum_comp]\n  ring\n")
    (out / "range").write_text(proof)
