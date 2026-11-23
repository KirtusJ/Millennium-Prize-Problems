# Report — worker r2-char (formalizer), Director Z4

Control: `control.txt` = `0.272341` (−ln tanh 1). The child answered the same control the same way.

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| F1 `conv_char`: T_w ψ = c_ψ • ψ | STANDS | `CharTransfer.lean`, `lake env lean` exit 0 (register K2), axioms propext/Classical.choice/Quot.sound |
| F2 `iterate_char`: T_w^[N] ψ = c_ψ^N • ψ | STANDS | same file, same run |
| F3 `iterate_eq_kern`: T_w^[n+1] f = conv (kern w n) f | STANDS (narrow form, see "not checked") | same file, same run |
| F4 `coeff_real_even`: c_ψ = ↑(∑ w y · Re ψ y) for real even w, unitary ψ | STANDS | same file, same run |
| Link to LevelsControl `lam0`/`lam1` (`coeff_eq_lam1`, `coeff_one_eq_lam0`, `iterate_eq_lam1_pow`) | STANDS | same file. The definitions are copied word for word. The input file is unmodified and not imported. |
| Numerics on Z₂×Z₄ (H, P1–P4) | STANDS | Child's `char_check.py` reread and rerun by me in `rerun/` (K3, exit 0). The result file is byte-identical to `child/results_1.txt`. |
| README §2 "diagonal in characters": that the characters are a complete eigenbasis (exhaust the spectrum) | NOT CHECKED in Lean | F1/F2 give eigenvectors only. Completeness is checked numerically for Z₂×Z₄ only (P3). |
| README §2: the lattice transfer operator on the cylinder equals T_w^N | NOT CHECKED in Lean | F3 covers convolution power = chain kernel. The reduction from the lattice, which needs gauge fixing and integrating out the links, is not formalized. |

Counts: STANDS 6, DEFECT 0, NOT CHECKED 2. Predicates: met 5 (H, P1–P4), failed 0, measured only 0. The Lean first draft failed (see below).

### Exact Lean statements proved (`CharTransfer.lean`, namespace `Z4Char`, `variable {G : Type*} [Group G] [Fintype G]`)

```lean
def conv (w f : G → ℂ) : G → ℂ := fun x => ∑ y, w y * f (x * y⁻¹)
def coeff (w ψ : G → ℂ) : ℂ := ∑ y, w y * ψ y⁻¹
def kern (w : G → ℂ) : ℕ → G → ℂ
  | 0 => w
  | n + 1 => fun x => ∑ g, kern w n g * w (g⁻¹ * x)

theorem conv_char (w ψ : G → ℂ) (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) :
    conv w ψ = coeff w ψ • ψ
theorem iterate_char (w ψ : G → ℂ) (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (N : ℕ) :
    (conv w)^[N] ψ = coeff w ψ ^ N • ψ
theorem iterate_eq_kern (w f : G → ℂ) (n : ℕ) :
    (conv w)^[n + 1] f = conv (kern w n) f
theorem coeff_real_even (w : G → ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)
    (heven : ∀ y, w y⁻¹ = w y) :
    coeff (fun y => (w y : ℂ)) ψ = ((∑ y, w y * (ψ y).re : ℝ) : ℂ)
theorem coeff_eq_lam1 (c : G → ℝ) (b : ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)
    (heven : ∀ y, c y⁻¹ = c y) :
    coeff (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)) ψ = ((lam1 c (fun y => (ψ y).re) b : ℝ) : ℂ)
theorem coeff_one_eq_lam0 (c : G → ℝ) (b : ℝ) :
    coeff (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)) (fun _ => 1) = ((lam0 c b : ℝ) : ℂ)
theorem iterate_eq_lam1_pow (c : G → ℝ) (b : ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)
    (heven : ∀ y, c y⁻¹ = c y) (N : ℕ) :
    (conv (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)))^[N] ψ =
      (((lam1 c (fun y => (ψ y).re) b : ℝ) : ℂ)) ^ N • ψ
```

`kern w (N−1) x = ∑_{g₁..g_{N−1}} w g₁ · w(g₁⁻¹g₂) ⋯ w(g_{N−1}⁻¹x)`, which is the chain kernel for N plaquettes.

`#print axioms` output (final run, exit 0, no `sorry` in the file):
```
'Z4Char.conv_char' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.iterate_char' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.iterate_eq_kern' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.coeff_real_even' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.coeff_eq_lam1' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.coeff_one_eq_lam0' depends on axioms: [propext, Classical.choice, Quot.sound]
'Z4Char.iterate_eq_lam1_pow' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Hypotheses used, and where they are stated

- F1, F2, F3 use `[Group G] [Fintype G]` (the `variable` line) and, in F1/F2, multiplicativity `hψ`. **I dropped commutativity and `DecidableEq`: the proofs do not use them.** F1/F2 therefore hold for one-dimensional characters of any finite group. F3 holds for any finite group with this left-chain convention.
- F4 uses `hψ`, `hu : ‖ψ y‖ = 1` and `heven : w y⁻¹ = w y`. In the `coeff_eq_lam1` signature, `heven` is stated on c, which makes exp(b·c) even. `coeff_one_eq_lam0` needs no evenness.
- Normalization: plain sums with counting measure, not Haar averages. lam0/lam1 in LevelsControl are also plain sums, so the two agree. Normalized coefficients differ by the factor 1/|G|, and eigenvalue ratios are unchanged.
- Z_n reading, in a comment only and not instantiated in Lean: G = Multiplicative (ZMod n), c j = cos(2πj/n), ψ₁ j = exp(2πij/n). Re ψ₁ is the χ of LevelsControl, and ψ = 1 gives lam0.
- Numerics (child script docstring): G = Z₂×Z₄. w is uniform(0.5, 1.5), evened over the pairs {g, −g}, seed 20261122. Tolerances come from eps = 2.2e-16 times the operation count, scaled by S1 = Σw: UNIT 1e-12, SMALL 1e-12·S1, BIG 1e-10·S1³, EIG 1e-9·S1³. They are loose, with about 10⁵ headroom over the measured errors (1e-13 to 1e-15).

## Failed predicates / failed runs

- Lean first draft (`CharTransfer_draft1_failed.lean`, register K1, exit 1 as expected on rerun). All errors were mine, not defects of the target:
  - three definitions not marked `noncomputable`;
  - the `Equiv.sum_comp` reindex rewrote the wrong side in F3 and F4;
  - a `rw ← hA` in F4 went in the wrong direction.

  `conv_char`, `iterate_char` and `coeff_one_eq_lam0` already passed in that draft.
- No numerical predicate failed.

## What I did not check

1. **Completeness.** That the |G| characters of a finite abelian G form a basis, which is what "diagonal" means, is not proved in Lean. It is seen numerically for Z₂×Z₄: the 8 eigenvalues of T³ match the c_ψ³ multiset.
2. **Lattice → T_w^N.** The gap between the Wilson transfer operator on the N-plaquette cylinder and T_w^N is not formalized. That step needs:
   - the state space as gauge-invariant functions of the spatial links;
   - reduction, by gauge fixing, to class functions of the holonomy, which for abelian G are functions on G;
   - integrating out the time-like links of one time step, which gives the product of plaquette weights whose group arguments chain as in `kern`.

   F3 proves only the final algebraic step: iterating convolution equals the chain kernel.
3. **Non-abelian groups (SU(2) etc.).** Not attempted. The open parts are:
   - characters of dimension d_r > 1 are not multiplicative, so F1 does not apply;
   - the eigenvalue on χ_r of convolution by a class function w is c_r/d_r per plaquette, with c_r = ∫ w χ̄_r, so the N-plaquette eigenvalue is (c_r/d_r)^N, up to the README's normalization of c_r;
   - this needs Schur orthogonality and Peter–Weyl or Haar integration, which is absent here.

   The README's "c_r(β)^N" is therefore correct only with c_r normalized by d_r. For SU(2) that convention has to be stated. I did not check which convention `two_dim_control.py` uses.
4. Infinite/compact abelian G (U(1)): not covered, since sums are over a Fintype.
5. No mutation test of the Lean file.

## Delegated question (rule 7) and outcome

Delegated: on G = Z₂×Z₄ with a random positive even weight (seed 20261122), build T_w, form T³, and check:
- H: 8 characters, multiplicative and distinct;
- P1: T³ψ = c³ψ;
- P2: c is real and equals Σ w Re ψ;
- P3: eig(T³) = {c_ψ³};
- P4: T³ equals the explicit chain kernel.

Control: −ln tanh 1, known answer 0.272341. The child answered correctly.

Returned: all five predicates PASS, with worst errors H 4.5e-15, P1 1.35e-13, P2 8.3e-16, P3 1.71e-13, P4 1.42e-14. Its own register verified PASS.

My check of that claim:
- I reread `child/char_check.py`. Predicates and tolerances are in the docstring, the seed is fixed, and the result file is opened with mode "x" (never overwritten).
- I reran it in `rerun/` through my register (K3), with exit 0 and output byte-identical to the child's.
- I replayed the child register, `verify` PASS.

Remark: P3 compares sorted multisets with a loose tolerance. P1 is the sharp test.

## Commands to rerun (Git Bash, PYTHONUTF8=1, from C:/Users/donke/z4-workers/r2-char)

```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
L="cd C:/Users/donke/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean"
python $P check --ws pcp --name lean_draft1_failed --expect-exit 1 -- bash -c "$L C:/Users/donke/z4-workers/r2-char/CharTransfer_draft1_failed.lean"
python $P check --ws pcp --name lean_CharTransfer --expect-exit 0 -- bash -c "$L C:/Users/donke/z4-workers/r2-char/CharTransfer.lean"
python $P check --ws pcp --name rerun_char_check --expect-exit 0 -- bash -c "cd C:/Users/donke/z4-workers/r2-char/rerun && python -I char_check.py"   # writes results_N.txt, next free N
python $P verify --ws pcp
(cd child && python $P verify --ws pcp)
```

`pcp_os.py verify --ws pcp`, last line (own register, 4 events; child register also PASS):
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Director, worker and sub-agent are one model family. This agreement is not independent review.
