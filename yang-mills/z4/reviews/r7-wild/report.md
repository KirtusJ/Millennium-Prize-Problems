# r7-wild report (wildcard worker for Director Z4, seed word "refinement")

**What I chose and why.** I chose Z4's trajectory audit. Z4's README (l.164-167) and the Z4 row of OVERALL_DISPOSITION.md say that A4's plaquette window leaves every fixed physical window as b → 0 only when β = o(b^(−1/2)), and call "β²b bounded below" the *exact* condition. That condition holds only for A4's particular choice L = A/16. A4's own inputs (K_e + g·u ≤ B) bound the variance of the plaquette by K_F = min(4, 8B/g). With that bound, A4's own extraction inequality gives a lower endpoint L' = A/(4K_F) ≥ κ/154 for every magnetic coupling. So the guaranteed band leaves every fixed physical window whenever βb → 0, which covers more trajectories than β²b → 0. **What I looked at and discarded:** I checked C4's `momentum/adjoint-refinement.md` line by line by hand (sphere identities, M1 lower bound, window algebra, constants 1024, 12288, 1728) and found no fault, so there is nothing to report there. I did not redo B4's gap constants because Z4 has already cross-read them.

## Verdict table (counts: met, failed, measured only)

| Item | Verdict | Evidence |
|---|---|---|
| Z4 README l.164-167 / DISPOSITION: "exact condition β²b bounded below" for the window to stay in a fixed physical window | **DEFECT (misleading wording)** | It is exact only for A4's choice L=A/16. With L'=A/(4K_F), the band escapes on β=b^(−0.75): L' goes from 0.048 to 15.6 while L_A4 goes from 9.1e-3 to 9.4e-8 (b from 1e-2 to 1e-12). On β=1/b, L' stays in [0.0154, 0.0156] (results/run1.json, P5, P6) |
| New: fundamental plaquette, ν_F([A/(4K_F), 4D/A]) ≥ A²/(8D), with L'/κ ≥ 9/(32·43) = 1/152.9 uniformly in g | **STANDS** (text proof below; numerics 6, 0, 0) | P1 4002/4002, P2 sup K_F(1+B) = 41.599 at g = 18.88, P3, P4 0 violations in 10⁵ random measures |
| sup_{g>0} K_F(g)(1+B(g)) ≤ 43 | **STANDS** (Lean, by the sub-agent; I reran it) | child/KBound.lean `KB_bound`: exit 0, axioms [propext, Classical.choice, Quot.sound], no sorry (my check K2); grid sup 41.61 (K3) |
| Z4 Lean `L_bounded_forces`, `L_tendsto_top` | STANDS (as statements about A4's L) | Not recompiled. The statements concern L = A/16 and remain true; only the prose generalises them too far |
| C4 adjoint-refinement constants and window algebra | STANDS (hand check) | a_A, 1024, 12288, 1728, a²/(2D) re-derived; the same algebra checked numerically as P4 (D4/C4 form) |
| B4, G4, Z5 lanes | NOT CHECKED | outside the chosen item |

**Statement and proof (favourable item).** We use A4's hamiltonian-variance conventions. F = 2x_p, u = E(1−x_p), and B = min(g, 17√g/8 + 3/16).

1. Since 0 ≤ 1−x ≤ 2, Var F = 4 Var x ≤ 4E(1−x)² ≤ 8u. A4's l.39 gives g·u ≤ B, so M0 = ν_F(ℝ) = Var F ≤ K_F := min(4, 8B/g).
2. Integrate A4's pointwise inequality E ≤ L + E²/U + U·1_[L,U] (excited-band l.51-55). This gives A ≤ L·K_F + D/U + U·ν([L,U]).
3. Take L = A/(4K_F) and U = 4D/A. Then ν([L,U]) ≥ A²/(8D). Also L < U, because A² ≤ M1² ≤ M0·M2 ≤ K_F·D.
4. L/κ = 9/(32·K_F(1+B)) ≥ 9/(32·43).
5. On tree level (κ_A = 2/(βb)) this gives L ≥ 9/(688·βb) → ∞ iff βb → 0.

U and w are A4's own. **Caveat:** when β → ∞ the weight w → 0, so on those trajectories the window says nothing in any fixed window whichever L is used. The improvement concerns where the guaranteed band sits, not how much weight it carries. At fixed β both L and L' diverge like 1/b. On the logarithmic trajectory both diverge. The gap between the two conditions is the range b^(−1/2) ≲ β ≪ b^(−1).

**Combined reading (the cross-lane point).** Every positive-energy band guaranteed in the repository has a lower endpoint at a fixed fraction of the electric scale κ = 2/(βb), uniformly in g:
- D4's adjoint band: κ/576;
- C4's smeared adjoint band: δκ/12288;
- the improved A4 fundamental band: κ/153.

The method locates weight only at the electric cutoff scale, on every trajectory. This is a sharper form of "the band moves to ultraviolet energies" than any lane states for the fundamental plaquette.

**What would have to be proved, and by whom.**
- A4: adopt L' in excited-band/README.md (one line: replace mass ≤ 4 by K_F).
- Z4: replace "exact condition β²b bounded below" by "for A4's choice L = A/16". Optionally restate the audit with L' and the condition βb bounded below, and in Lean prove `L'_bounded_forces : L' ≤ C → βb ≥ c`. The delegated lemma below is the only non-algebraic input.

## Hypotheses used, and where they are stated
- K_e + g·u ≤ B(g): A4 `observable-normalization/hamiltonian-variance/README.md` l.39.
- First-moment lower bound M1 ≥ A = 9κ/(8(1+B)): A4 `.../excited-band/README.md` l.10, l.24-33.
- Second-moment upper bound M2 ≤ D = κ²(6+8√B)²: same note, l.10, l.35-45.
- Extraction inequality: same note, l.49-55.
- Tree-level matching κ_A = 2/(βb), g = β²/2: Z4 README l.145, B4 hamiltonian-time.
- Box side ≥ 3, unique positive vacuum: A4 parent note l.11.

## Failed predicates
None. Mine: 6 met, 0 failed (P6/P7 are one check), measured only: 2 (the sup and its argmax, and the hypothesis count A² ≤ 16·K_F·D on 4002/4002 grid points). Sub-agent: 2 met, 0 failed. All predicates met, so there are no failures to attribute either to my expectations or to a defect of the target.

## What I did not check
- A4's proofs of K_e + gu ≤ B, of A, and of D (taken as hypotheses).
- A4's third-moment D_* variant (it would improve U and w; L' is unaffected).
- Whether tree-level matching is the true trajectory.
- Z4's Lean files (not recompiled).
- C4's integration-by-parts frame-change claim beyond a hand reading.
- The "radius-two Schur" constant 63.
- Whether the momentum version of L' (smeared fundamental) holds: it needs a smeared variance bound and is not claimed.

## Delegated question and outcome
**Question delegated:** prove in Lean 4/Mathlib that for every real g > 0, min 4 (8B/g)·(1+B) ≤ 43, where B = min g (17√g/8 + 3/16). The sub-agent also had to run a grid check. Its control question was -ln tanh 1, and it answered 0.272341 (correct). It used its own register in child/pcp, whose verify passed.

**What came back:** `KB_bound` passed on the first draft, with no failed drafts. Its grid max was 41.6097 at g = 18.81.

**What I did with it:** I read the theorem statement against my definitions and they match (K_F = 4 at g = 0 is outside its scope; that case is trivial at 4·1). I reran the Lean file in my register (K2, exit 0, same output hash, axioms as above, 0 occurrences of "sorry") and reran the grid (K3, same output hash). Counts for the sub-agent: 2 met, 0 failed, 0 measured only.

## Rerun
```
cd C:/Users/donke/z4-workers/r7-wild
export PYTHONUTF8=1
mv results results_old   # the program refuses to overwrite results/run1.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name window_audit_rerun --expect-exit 0 -- python window_audit.py
cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-wild/child/KBound.lean
cd C:/Users/donke/z4-workers/r7-wild && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Register checks: K1 window_audit, K2 kbound_lean_rerun, K3 kgrid_rerun. Last line of `pcp_os.py verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

One model family throughout. This is not independent review.
