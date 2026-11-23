# Verification of the temporal-line calculation

Three PCP OS guests generated the [Lean source](TemporalLines.lean) from [the templates and integer controls](worker.c). The parent verified the minimizing ramp for 127 lengths. Its child counted all 32,768 positive three-dimensional frequencies up to index 32 and checked the shell-count bound. The grandchild checked the signed difference between a two-atom law and its reversed product for 4,096 pairs of unnormalized laws. Each worker recorded 47 kernel events and terminated successfully. A second three-generation deployment reproduced the emitted bytes. The host launched the requested child after each measured guest returned. [Replay procedure](../../execution.md)

| Artifact | SHA-256 |
|---|---|
| PCP OS kernel | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent | `90cd9d83fe43639c7d36635cf51658f836fceb916f9ccdf19ab61d2783afb3c8` |
| Child | `da489b3dec2b9df2d93fcee776d921387b6d1eacdbc58a800a4b2d4f6c862fed` |
| Grandchild | `8907ebbdf8c085a3f6a7ba6c0e0a389e7750e1218841e5ba7aaaf2de339cdace` |
| Generated Lean | `02dce8759126dda2fcd2ba318e63c1d182770a778a584e9bbe972169a1c1a59a` |

All six supporting declarations compiled on Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`, with axiom union `{propext, Classical.choice, Quot.sound}`. Doubling the residual ramp energy, exchanging the wrong density factors, and halving the mixed term in the action-error bound each made the corresponding proof fail. The covariance identification, moment argument and measure comparison are mathematical proofs in the accompanying notes.

From this directory with GCC, QEMU, NumPy and SciPy installed, run

```sh
python ../../replay-guests.py /path/to/kernel.elf32 --proof TemporalLines.lean
OPENBLAS_NUM_THREADS=1 python -I check_lines.py
OPENBLAS_NUM_THREADS=1 python -I check_one_box.py
```

From the pinned Mathlib checkout, run `lake env lean /path/to/TemporalLines.lean`.

[The matrix check](check_lines.py) solves the full four-dimensional incidence system on one elementary source at each bottom vertex. Independently it applies the three-dimensional spatial Laplacian to the resulting inverse submatrix and whitens it in the spatial sine basis.

| Side | Four-dimensional free links per color | Spatial modes | Maximum entrywise error in $A\,\mathrm{Cov}(b)-L I$ |
|---:|---:|---:|---:|
| 2 | 7 | 1 | 0 |
| 3 | 80 | 8 | $4.88\cdot10^{-15}$ |
| 4 | 351 | 27 | $1.24\cdot10^{-14}$ |
| 5 | 1,024 | 64 | $4.53\cdot10^{-14}$ |
| 6 | 2,375 | 125 | $1.03\cdot10^{-13}$ |
| 7 | 4,752 | 216 | $1.44\cdot10^{-13}$ |

The same program checks common-root conjugation and the Taylor bound on 120 noncommuting input pairs at four couplings. On 200 pairs of discrete densities, it verifies the exchange inequality when their supports differ.

[The independent one-box integration check](check_one_box.py) uses the exact compact ordered Wilson action and exponential-chart Haar factors to reweight Gaussian proposals. Each entry uses two separately seeded sets of 8,192 samples to estimate the squared conditional mean of the temporal holonomy. At $L=2$ the Gaussian prediction for the normalized variance is $3/6=0.5$.

| Shell held fixed in scaled coordinates | $\beta=64$ | $\beta=256$ | $\beta=4096$ |
|---|---:|---:|---:|
| Identity | 0.497365 | 0.498638 | 0.499035 |
| Nonzero shell | 0.501170 | 0.499914 | 0.499240 |

The smallest effective sample size across these runs was 7,803 of 8,192. These are fixed-shell numerical controls of normalization and signs. They do not sample the infinite-volume thermal shell used in the growing-box theorem.
