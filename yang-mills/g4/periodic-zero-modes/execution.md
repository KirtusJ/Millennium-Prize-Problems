# Checks on the fixed-volume Wilson calculation

Director G4 deposited the compact integral, its determinant and the fixed-box consequence on November 23, 2026. The analytic argument uses tree gauge, dominated convergence and a local sublevel expansion. Lean checks seven algebraic lemmas used along the way. The compact integration, analytic expansion and distributional limit have paper proofs. [Compact integral](proof.md) · [Determinant](determinant.md) · [Plaquette step](step.md)

## Lean and PCP

Lean 4.19.0, with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b`, checked the word-length inequality, the flux-sheet identity, the transverse Gram polynomial and its determinant, the scalar tree-factor simplification, the per-face normalization and the sign of the step. The compiler reported only `propext`, `Classical.choice` and `Quot.sound`. All five adverse variants failed elaboration. The first development build lacked the import for real numbers. The second build passed with linter warnings. The final positive transcript has seven axiom reports and no warnings. [Lean source](PeriodicZeroModes.lean) · [Adverse variants](mutations.json)

The eight PCP model commissions cover the pivot, the tree fillings, extraction of the mean action, the Gaussian coefficient, the graph determinant, the fixed-box step, and two final readings. The final integral reader received the exact compact proof and determinant text. The final observable reader received the exact statement and step argument, assuming the leading partition estimate supplied by the first reader. Their conditions include probability Haar, fixed $L$, and distinct parallel links at $L=2$. A separate PCP model wrote the transverse Gram lemma, and its supervisor commissioned a challenge to those exact bytes. Each hosted supervisor observed process termination before reading the child result. The model workers used the same provider family and had only their supplied text. [PCP and compiler records](evidence.zip)

The evidence contains 21 hosted PCP registers, including the compiler supervisor and child. The 58-file method fingerprint is `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`. A separate measured native kernel ran six method controls and three source emitters. The emitters reproduced prepared portions of the completed Lean file. Concatenating their serial frames gives SHA-256 `3c2c4d14360def3936df8d7c1c2010b1f692ff79983f76c2efa1a57f78904d40`. Lean ran in the hosted compiler process. [Evidence verifier](verify.py)

## Independent computational checks

- Direct word and cochain calculations over $L=1,2,3,4$ checked 1,074 zero-displacement based words, 2,124 background face words and 12,744 integer curl values. A separate calculation checked 729 rational unit-quaternion pairs. [Exact controls](check.py)
- For $L=2$, integer elimination gave $\tau_L=1\,391\,569\,403\,904$ and $\det(D_1^TD_1)=30\,983\,446\,494\,107\,742\,247\,059\,456$. At $L=3$, independent eliminations gave $\tau_L=285429$ and determinant $40240$ modulo $1000003$. The $L=1$ empty determinant was one. [Determinant controls](check.py)
- Composite Simpson quadrature on the transverse cube gave the one-site coefficient $0.0126651478$, compared with $1/(8\pi^2)$. [Cube quadrature](check.py)
- A separate 65,536-node Halton quadrature used the original compact six-commutator Wilson energy and Haar weight, restricted to $1/4\le -4\log r/\log\beta\le3/4$. The coefficient below is per unit length of that interval. The energy mean and Laplace transform condition on the interval. These deterministic diagnostics have no certified numerical error bound. [Compact quadrature](quadrature.py)

| Bare $\beta$ | Partition coefficient | Mean $\beta S$ | Mean $\exp(-\beta S)$ |
| --- | ---: | ---: | ---: |
| $10^8$ | 0.012903 | 2.9976 | 0.12532 |
| $10^{32}$ | 0.012662 | 2.9982 | 0.12529 |
| Analytic limit | $1/(8\pi^2)$ | $3$ | $1/8$ |

## Reproduction

From this directory, run `python -B verify.py` with Python 3.10 or newer. The verifier reruns both computational checks, binds the final reviewers’ inputs to the four research documents, checks the seven Lean reports and five compiler failures against the supplied sources, and reconstructs the Lean source from native output. To deep-replay each stored register, supply `--runtime PATH_TO_PCP_OS_PYTHON --method PATH_TO_PCP_METHOD`. To rerun Lean, invoke `lake env lean PATH_TO/PeriodicZeroModes.lean` in the pinned Mathlib checkout. [Verifier](verify.py) · [Complete evidence](evidence.zip)
