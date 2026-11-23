# Challenger report r9-mag: C4 magnetic-smearing and A4 electric-endpoint

Control: control.txt = 0.272341 (-ln tanh 1).
Sources: input/c4/*.md, input/a4/*.md, input/bench/*.md, input/README_round7.md only. Linked files that were not provided (moments.md, reflection.md, dipole.md, the Lean sources, check_ward.py, check_scales.py) were not seen.

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| C1 Main theorems: statement, hypotheses, regime | STANDS (as restated below) | Joint limit. The time period goes to infinity first at fixed (L, β). Then r, L, β go to infinity together with L ≫ r³√ℓ and β ≫ r¹⁶ℓ, or L ≫ r²√ℓ and β ≫ r¹²ℓ for the symmetric/m=2 case. The limit is a Gaussian (free) field, so this is a free control-class limit. |
| C2 Free by construction? | STANDS (free; C4 says so) | Trajectories need β ≥ r¹²⁺. Example β = r¹⁷ gives g² = 4b¹⁷, and β/β_AF = 1.2e17 already at r = 10. An asymptotic-freedom β fails the conditions: β/(r¹²ℓ) = 3.7e-25 at r = 100 (T2). C4 README par. 3: "These trajectories produce a free field … logarithmic … lies outside". |
| C2' Gaplessness stated | STANDS | README and spectrum.md: spectral mass below ε ~ ε⁸ (or ε¹², ε¹⁶), and r·Δ_lattice → 0. The result is a gap upper bound tending to zero, not a gap. |
| C3 Known free values | STANDS | Per colour, C4's kernel (p₁²+p₂²)e^{-t\|p\|}/(2\|p\|) is the Maxwell ⟨B₃B₃⟩. It equals Z4's (t²+x₃²−x₁²−x₂²)/(π²(r²+t²)³), with rel. err. 1.1e-6 at 5 points, and gives C₀ ~ J²/(π²t⁴) (P2). The t⁻⁸ law, the 3J⁴ε⁸/(2π⁴8!) mass, the angular constants, the 3C²/2 covariance and the B(t) formula all reproduce (P3–P7). The printed 0.02029847 / 0.00180930 / 0.0891348 reproduce to 1.5e-6 (P6). The lattice covariance converges to the continuum one, with error 4.7e-3, 1.2e-3, 2.9e-4 at r = 4, 8, 16 (P8). |
| C4 Normalization / gauge invariance | STANDS with caveat | F_p = √β·Im U_p, field r⁻²ΣFδ, and X_r = √β·Σ r⁻¹ψ(x/r)·Im(P U P⁻¹). Linear rooted X_r is not gauge invariant: it rotates under the root frame. The norms \|X_r\|² and exp(−σ\|X_r\|²) are invariant (checked by reading). These are path-dependent, single-slice observables whose definitions carry explicit factors of β. |
| C5a A4 derivation and arithmetic of κ/18 | STANDS | 2u−u²≤(11/2)S ⇒ M₁≥(2κ/9)M₀; max of (2−u)(289/256+27u/16) is 3.00513 ≤ 99/32. Band bound holds on 20000 random measures with 0 failures (child, §5). κ/18 does not depend on g. |
| C5b A4 'stronger uniform choice' | DEFECT (wording) | For g<17/64 the old edge A/16 is higher (0.0703κ vs 0.0556κ as g→0); the correct statement is max(A/16, κ/18). |
| C6a Commit title vs theorems | DEFECT (wording) | "positive physical-time magnetic spectrum" reads as a positive spectral edge. The theorems prove the opposite: weight down to E = 0 and a transfer gap → 0 in physical units. The title also does not say the spectrum is that of a free field. |
| C6b README paragraph 1 | DEFECT (wording) | It says "a magnetic field smeared over a fixed physical region has a nonzero connected reading … on explicit weak-coupling trajectories". It omits three things: the reading is non-zero only after rescaling by √β (linear) or β (quadratic); the field is rooted (gauge-fixed); and the limit is free. Those qualifiers come only in paragraph 3. Unrescaled, the connected covariance vanishes like 1/β² ≈ 1e-34 at r = 10 (README_round7: (3/2)K²/β²). |
| Rate statement min(β^{1/13},L^{1/3})Δ_lattice → 0 | STANDS as bookkeeping | Algebra checked on 9841 qualifying random pairs, 0 violations (T4). The underlying analytic estimates were NOT CHECKED. |
| Ward/Wilson-moment analytic chain | NOT CHECKED | Rests on sup_p E exp[β(1−x_p)/8] ≤ C uniformly in L, cited from moments.md, which was not provided. |

Counts (met, failed, measured only):
- check_c4 run 2: 8 met, 0 failed, 1 measured (M1).
- check_c4 run 1: same numbers, but 6 predicates were mislabeled "MEASURED" by my own bug (see §3).
- check_traj: 3 met, 1 failed (T3), 1 measured.
- Verdicts: see the final line.

## 2. Hypotheses each statement uses (where stated)
- **Field limit (README; field.md):**
  - SU(2) isotropic Wilson action; time period → ∞ first (ward.md §1).
  - r → ∞, L/(r³√ℓ) → ∞, β/(r¹⁶ℓ) → ∞ (README, smoothing.md table).
  - Large-β uniform exponential plaquette moment bound (ward.md, cited from moments.md).
  - Site reflection positivity for odd spatial sides (ordinary-profile.md, cited from reflection.md).
  - Smooth compactly supported tests, H^{-a}_loc with a > 2.
  - Ordered coordinate rooting paths (field.md, ward.md).
- **Linear smeared vectors and Q_r (ordinary-profile.md):** the same first-order conditions; ψ ∈ C_c^∞ real; J = ∫ψ ≠ 0 for the ε⁸ law.
- **Symmetric shorter box:** ψ even in x₁, centre sampling; L/(r²√ℓ) → ∞, β/(r¹²ℓ) → ∞ (ordinary-profile.md, last section but one).
- **Differenced profiles m = 1, 2 (spectrum.md, smoothing.md):** rows of the smoothing table.
- **Spectral measure / gap upper bound (spectrum.md):** the above, plus convergence of moments of e^{-E} under the normalized transfer matrix; finite box.
- **A4 (README):**
  - Finite periodic SU(2) Hamiltonian boxes, side ≥ 3.
  - K + gu ≤ B = min(g, 17√g/8 + 3/16), from the earlier ground-state note (not provided).
  - The energy-form identity M₁ = 4κS (excited-band README).
  - The second-moment bound D_* (third-moment note, not provided).

## 3. Failed predicates
- **check_traj T3 (failed).** The Ward error bound with C4's stated choice of A, along β = r¹⁷, L = r⁴, decreases (1.55 → 0.31 over r = 10…10⁶) but is not below 0.1 at r = 10⁶.
  - Cause: my own expectation. C4 claims only → 0, and that holds.
  - Measured consequence: the convergence rate is about r^{-1/8} up to logarithms, so the quantitative bound is O(1) at any realistic r.
- **check_c4 run 1 (defect of my program, not of C4).** P1, P3, P4, P5, P7 and P8 were labelled MEASURED because `numpy.bool_ is True` is False. The numbers were within tolerance. The script was fixed with a bool cast and rerun as results_check_c4_1_n.txt; the run-1 file is kept.

## 4. Not checked
- The Wilson moment bound, site reflection positivity, and the lattice projection normalization (moments.md, reflection.md, dipole.md not provided).
- C4's Lean source (21 theorems), check_ward.py, check_scales.py and the quoted Haar-quadrature values (-0.1960184343 etc.); none were provided.
- Details of the Ward identity (1), the Bianchi estimate (2) and H^{-a} tightness: read, not re-derived line by line.
- Weak convergence of the transfer spectral measures (spectrum.md "Transfer measurements"): read only.
- Z4's κ/153 derivation: not in my inputs, so the comparison κ/153 → κ/18 can only be made through A4's own description (K_F and A/(4K_F)).
- The "t⁻⁵ law" named in the task: C4 prints no t⁻⁵ quantity, so there was nothing to compare.
- C4's profile was not specified exactly. My guessed profile (normalized standard bump, fourfold convolution, tensor product) gives C₀(0,1,2) = 0.019735, 0.004557, 0.001374 against the printed 0.019730, 0.004552, 0.001369. That is within 3e-4 relative: measured only, consistent.

## 5. Delegated question and outcome
Delegated question (to child/, A4 files only): verify (a) 2u-u^2 <= (11/2)S => M1 >= (2kappa/9)M0, and (b) nu([kappa/18,4D/A]) >= A^2/(8D) on random positive measures satisfying the moment hypotheses; identify which inequality improved and whether kappa/18 is g-uniform. Control: 99/32 - max(2-u)(289/256+27u/16) = 0.088539 (child/control.txt; I confirmed by hand: max at u=575/864).
Outcome:
- All arithmetic in (a) STANDS: exact fractions, 20000 random rational instances. I re-derived it independently by hand, and I reran child/scripts/exact_a.py through my own register: exit 0.
- (b) STANDS: 20000 qualifying random measures out of 24811, 0 failures. The bound is not tight; the infimum ratio is about 9/2. 4D/A > kappa/18 holds automatically, since D >= (2kappa/9)A.
- The improvement is in the mass/first-moment relation. The old route bounded L*M0 with a mass bound (M0 <= 4, or K_F = min(4, 8B/g)). The new route bounds it by M1/4, using the variance-keeping relation M0 <= (9/(2kappa))M1. The extraction term D/U = A/4 and the first-moment bound A are unchanged.
- kappa/18 contains no g, so it is uniform in the magnetic coupling. The weight A^2/(8D*) still depends on g.
- DEFECT (wording, A4 README par. 1 "stronger uniform choice"): for g < 17/64, A/16 = 9kappa/(128(1+g)) > kappa/18, i.e. 0.0703kappa vs 0.0556kappa as g -> 0. I checked the threshold myself: 162/128 - 1 = 17/64. The new edge is stronger only for g >= 17/64. A4 keeps the A/16 band valid, so max(A/16, kappa/18) is the correct statement.
- Child's own failed predicate: its optimizer accepted a negative weight; that was its tool's fault, fixed in band_b3.
- Not rerun by me: band_b3.py (~2 min). Not checked: D_*, K+gu <= B, M1 = 4kappa S (inputs from notes not provided); Z4's kappa/153 text (not in inputs).
- Child PCP verify: PASS.

## 6. Rerun commands
```sh
cd C:/Users/donke/z4-workers/r9-mag
export PYTHONUTF8=1
python -c "import math;print('%.6f'%-math.log(math.tanh(1)))"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name check_c4_v2 --expect-exit 0 -- python check_c4.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name check_traj --expect-exit 0 -- python check_traj.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
(Result files are never overwritten; a rerun writes *_n.txt. check_traj exits 1 because of T3, so the PCP check records exit 1 against an expected 0.)

Verdict counts: 7 STANDS, 3 DEFECT (all wording: C4 commit title, C4 README par. 1, A4 "stronger uniform"), 1 NOT CHECKED.
PCP verify (parent), last line: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
