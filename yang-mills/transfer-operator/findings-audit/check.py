"""Reconcile frozen configuration identities and replay the matched measurement under three sample selections."""
from math import hypot
from pathlib import Path
import sys

import numpy as np

YM = Path(__file__).resolve().parents[2]
FROZEN = YM / "z4/reviews/ext-match/predeclared"
sys.path.insert(0, str(FROZEN))
sys.path.insert(0, str(YM / "observable-normalization/thermal-transitions"))
import ext_analyse as z4
from matched_rows import circular_means, seed_rows


def records(path):
    lines = path.read_text().splitlines()
    header = [s for s in lines if s.startswith("#")]
    rows = [s for s in lines if s.strip() and not s.startswith("#")]
    unique = {}
    duplicates = []
    for row in rows:
        fields = row.split()
        cfg = int(fields[0])
        if cfg in unique:
            # The last field is elapsed wall time. Compare every physics token.
            if fields[:-1] != unique[cfg].split()[:-1]:
                raise ValueError(f"Conflicting observations for {path.name}, ID {cfg}")
            duplicates.append(cfg)
        else:
            if cfg != len(unique):
                raise ValueError(f"Gap or reorder in {path.name} at ID {cfg}")
            unique[cfg] = row
    return header, rows, unique, duplicates


def fine_variants():
    variants = {name: {} for name in ("historical-rows", "frozen-unique", "declared-ids")}
    expected = {623: 3000, 824: 1500, 1205: 270, 1206: 300, 1207: 300}
    counts = {}
    for path in sorted(FROZEN.glob("meas_*.txt")):
        header, rows, unique, duplicates = records(path)
        seed = int(path.stem.split("_s")[-1])
        print(path.name, "rows", len(rows), "IDs", len(unique), "repeats", duplicates)
        counts[seed] = len(rows)
        assert duplicates == ([40, 41, 42] if seed in (1206, 1207) else [])
        if seed in (623, 824):
            continue
        clean = list(unique.values())
        recovered = clean
        if duplicates:
            orig_header, longer, all_unique, repeats = records(FROZEN.parent / path.name)
            assert header == orig_header and rows == longer[:len(rows)]
            assert repeats == duplicates and len(longer) == 332
            assert list(range(len(unique), 300)) == [297, 298, 299]
            recovered = [all_unique[i] for i in range(300)]
        selections = {"historical-rows": rows, "frozen-unique": clean, "declared-ids": recovered}
        for name, data in selections.items():
            variants[name][path.name] = [int(row.split()[0]) for row in data[z4.A.NSKIP:]]
    assert counts == expected
    return variants


def diagnostics(fine, anchors):
    mean, error = fine[:2]
    results = {**anchors, 12: fine}
    eligible = positive = 0
    for side, (m, e, *_) in results.items():
        sl = slice(1, side // 2 + 2)
        eligible += np.count_nonzero(m[sl] >= -2*e[sl])
        positive += np.count_nonzero(m[sl] > 2*e[sl])

    def line_z(index, scale):
        vals = [results[n][0][index] * s for n, s in zip((6, 8, 12), scale)]
        errs = [results[n][1][index] * s for n, s in zip((6, 8, 12), scale)]
        # Flow times in lattice units from the three frozen measurement headers.
        x6, x8, x12 = (1 / (8*s) for s in (0.5, 0.888889, 2.0))
        w = (x8 - x12) / (x6 - x12)
        return (vals[1] - w*vals[0] - (1-w)*vals[2]) / hypot(errs[1], w*errs[0], (1-w)*errs[2])

    print("E1 eligible / positive", eligible, positive, "Q0, R0 line pulls",
          f"{line_z(0, (1, 4*.888889**2, 16)):.3f}", f"{line_z(1, (1, 1, 1)):.3f}")
    print("Q0 and R0..R6 (one estimated SE)",
          " ".join(f"{v:.8f}({s:.8f})" for v, s in zip(
              np.r_[16*mean[0], mean[1:8]], np.r_[16*error[0], error[1:8]])))
    for fine_t, other_side, other_t in [(2, 6, 1), (3, 8, 2), (4, 6, 2), (6, 8, 4)]:
        other, other_err = anchors[other_side][:2]
        x, y = mean[1+fine_t], other[1+other_t]
        print("ratio", fine_t, other_side, other_t, f"{x/y:.4f}",
              f"{hypot(error[1+fine_t]/y, x*other_err[1+other_t]/y**2):.4f}")


def all_rows(chains, block):
    stats = []
    for chain in chains:
        products = [(chain * np.roll(chain, t, axis=1)).mean(1) for t in range(12)]
        stats.append(np.column_stack([chain.mean(1), *products]))
    center, draws = circular_means(stats, block)

    def normalized(values):
        mean = values[..., :1]
        return np.concatenate([mean, values[..., 1:] / mean**2 - 1], axis=-1)

    return normalized(center), normalized(draws).std(axis=0, ddof=1)


def main():
    anchors = {}
    for side in (6, 8):
        path, = FROZEN.glob(f"meas_L{side}_*.txt")
        anchors[side] = z4.ens(z4.A.load(path)[2], side)
    for sample, files in fine_variants().items():
        chains = list(seed_rows(12, sample))
        assert [len(c) for c in chains] == [len(ids) for ids in files.values()]
        keys = [(file, cfg) for file, ids in files.items() for cfg in ids]
        result = z4.ens(np.concatenate(chains), 12)
        _, _, count, block, tau = result
        keep = count*block
        fits = [z4.ens(chain, 12) for chain in chains]
        pulls = [abs(a[0][0]-b[0][0])/hypot(a[1][0], b[1][0])
                 for j, a in enumerate(fits) for b in fits[j+1:]]
        print("\n", sample, "input", len(keys), "distinct", len(set(keys)),
              "block/count/used/unique used", block, count, keep, len(set(keys[:keep])),
              "tau", round(tau, 3), "largest seed-mean pull", round(max(pulls), 3))
        if sample == "historical-rows":
            assert (block, count, keep, len(set(keys[:keep]))) == (17, 49, 833, 827)
        diagnostics(result, anchors)
        for size in (17, 25, 50):
            pieces = [c[:len(c)//size*size] for c in chains]
            estimates = z4.A.jack(z4.est_factory(12), np.concatenate(pieces), size)
            print("seed-respecting", size, "per-seed retained", [len(p) for p in pieces])
            diagnostics(estimates, anchors)
        for size in (25, 50):
            print("all rows, within-seed circular blocks", size)
            diagnostics(all_rows(chains, size), anchors)


if __name__ == "__main__":
    main()
