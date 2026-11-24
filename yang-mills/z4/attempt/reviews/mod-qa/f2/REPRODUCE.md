# Reproducing the frozen test Z:ratio-opt of f2-cross2 from the deposit

QA rerun, 24 November 2026. No Monte Carlo was regenerated: the inputs are the per-chain files in the
deposited archive and the two deposited analysis programs.

## Inputs (deposit, repository `Millennium-Prize-Problems` at commit `c7c2a16`)

| File | SHA-256 |
|---|---|
| `yang-mills/z4/attempt/reviews/f2-cross2/results.tgz` | `914fc35fa496bb433362b1378b972032c40ed1e67c4732c45e823d7d811b5795` |
| `yang-mills/z4/attempt/reviews/f2-cross2/src/analysis2.py` | `b9657114d1925c226f144f65dc2efd28a78cebcfad3a4cf707a7f925c12987a5` |
| `yang-mills/z4/attempt/reviews/f2-cross2/src/cross_eval2.py` | `adc88ee326b5d81e2ac29a002f8093124fddb28b96a15df25173fe67553c0fda` |

The archive holds 82 entries: seven result texts, and 16 per-chain files for each of `c2` (N=5, T=10),
`f2` (N=10, T=20), `c4` (N=5, T=20), `f4b` (N=10, T=40), plus two chains of the abandoned `f4` (unused).
The per-chain files are accumulated moment sums (`S1`, `S00`, `SL` per class), not configurations.

## Commands

```
D=/home/user/Millennium-Prize-Problems/yang-mills/z4/attempt/reviews/f2-cross2
Q=/home/user/z4-workers/mod-qa
sha256sum $D/results.tgz
mkdir -p $Q/f2 && tar xzf $D/results.tgz -C $Q/f2            # gives $Q/f2/results/
python3 -I $Q/scripts/reproduce_f2.py $D/src $Q/f2/results/ $Q/f2/rerun1 > $Q/f2/rerun1.stdout 2>&1 ; echo $?
python3 -I $Q/scripts/reproduce_f2.py $D/src $Q/f2/results/ $Q/f2/rerun2 > $Q/f2/rerun2.stdout 2>&1 ; echo $?
cmp $Q/f2/rerun1.stdout $Q/f2/rerun2.stdout ; for f in $Q/f2/rerun1/*; do cmp $f $Q/f2/rerun2/$(basename $f); done
cp $Q/f2/rerun1/frozen_vector_Z_ratio_opt.json $Q/f2/
```

The output directory (third argument) must not exist; result files are opened create-new. Each run takes
about 11 s. Environment of this rerun: Python 3.13.18, numpy 2.5.3 (OpenBLAS 0.3.34), x86_64 Linux.

`scripts/reproduce_f2.py` (SHA-256 `3a818c79400982d858a8b124042f22cef606be56eab23f83e2e4f0e4e3493b63`)
executes the text of the two deposited programs with two substitutions made in memory, because both hard-code
the worker's directory:

1. in `analysis2.py`, `ROOT = "/home/user/z4-workers/f2-cross2/results/"` becomes the unpacked directory;
2. in `cross_eval2.py`, `import sys; sys.path.insert(0, "/home/user/z4-workers/f2-cross2/src")` becomes
   `import sys` (the module `analysis2` is supplied from the deposited text).

It wraps `analysis2.ratio_min` only to record the vectors it returns. Nothing else is changed. The deposited
programs cannot be run from the deposit as they stand: this is a finding of the QA pass (F-6 in the worker's
handback).

## Predicates (written in the driver before the first run) and outcome

| | Predicate | Outcome |
|---|---|---|
| Q1 | regenerated `cross-eval-2l-frozen-on-4l.txt` byte-identical to the deposited one | MET (`47022242e3e3bf60721e5646ecc6431fdcb198e5107222a1172b64be5afee37f`) |
| Q2 | regenerated `analysis-2l.txt`, `analysis-4l.txt` byte-identical to the deposited ones | MET (`bb18d907...d76f`, `6eabb965...51ce`) |
| Q3 | vector read back from the JSON gives bit-identical values, printing as `0.94092(0.00490)` and `0.93574(0.00271)` | MET |
| Q4 | eight leading standardised coefficients recomputed from the JSON equal the deposited printed line | MET |

Exit code 0 on both runs; the two runs are byte-identical in every output (stdout, three texts, JSON,
`qa_summary.json`). Failed predicates: none.

## The numbers

| Quantity | Paper (Section 8.3) | Reproduced |
|---|---|---|
| R_5 held-out at 2l | 0.990(3) | 0.99027(0.00297) |
| R_10 held-out at 2l | 0.932(4) | 0.93177(0.00396) |
| R_10/R_5 held-out at 2l | 0.941(5) | 0.94092(0.00490) |
| R_10/R_5 on the 4l ensembles (all 16 + 16 chains) | 0.936(3) | 0.93574(0.00271) |
| ratio + 2 SE, larger of the two | 0.951 | 0.95071 (2l); 0.94117 (4l) |

They reproduce exactly, to every printed digit, and the regenerated result files are byte-identical.

## The vector

`frozen_vector_Z_ratio_opt.json` (SHA-256 `b542495cb7dc4c6a70c29b7ab41b257f12b867040da752fdc333264c7576bac2`):

- `names`: the 54 functions in the order of `analysis2.NAMES` (`w0..w2`, `p0..p2`, `rect*`, `chair*`, `hh*`,
  `ww*`, `w*^2`, `p*^2`, `w*p*`, `p0p1..`, `ind*b*`);
- `coefficients`: the frozen vector `a` in the raw basis, as returned by `ratio_min` (also as hexadecimal
  floats in `coefficients_hex`); all 54 are non-zero;
- `standardised.values`: `a_i * sqrt((Vf_ii + Vc_ii)/2)` on the TRAIN chains, divided by the largest modulus;
  the first eight in modulus are `w1p1 -1.00, w1 +0.76, w2p2 +0.27, hh12 +0.23, hh10 +0.21, w2 -0.20,
  ww12 -0.15, p1 +0.15`, as deposited;
- `by_name`: the same, keyed by function name.

Notes for a user of the vector.

- The test is in class `Z` (zero spatial momentum). It is the second class in the program's loop, so the
  random generator (seed 239) has already supplied the 12 random starts of class `L` when class `Z` is
  optimised. Running class `Z` alone with a fresh generator would not give this vector.
- The reduced span of class `Z` has dimension 48 of 54 on the training chains. The 54 coefficients are
  therefore one representative: adding a null direction of the training covariances changes `a` but not the
  test on those chains.
- `R` is invariant under scaling of `a`.
- What this establishes: the deposited numbers follow deterministically from the deposited per-chain sums and
  programs. It does not check the sampler, the per-chain sums, the thermalisation, or the choice of span.
