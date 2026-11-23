Closed: (A) corner absorption in Lemma tu:L-S4: PROVED, with a new explicit condition (M_A) on M and an explicit error margin m(eta)/2. (B) Lemma tu:L-balls, valley-ball points with a_1 just outside [a_-, pi-a_-]: PROVED, by restructuring the case split; no new estimate is needed. (C) M^2 numbers: recomputed and corrected in the text. Not closed: none of the three assigned gaps.

# GAPS.md — u1-gapB (T174)

Patched file: `note/tun_lower_patched.tex`. `tun_upper.tex` is unchanged, since none of my gaps lies there. It compiles with `build/wrap_patched.tex` (upper + patched lower): pdflatex exit 0, 0 undefined references, and the same 28 overfull boxes as the original.

## (A) Corner absorption, Lemma tu:L-S4 (S4-alg) — PROVED

**Old statement.** The lemma assumed Δ1+Δ3 ≤ η/4 and Δ2 ≤ 1, and the c₁ condition e^{-M²} ≤ G_min(e^{η/2}−1)e^{−C}/4. It concluded that the right side of the ring identity is ≥ 0, but the absorption bullets said only "≫", "≈0" and "V large".

**New statement (label kept).** Let
- m0 = (1−e^{−3η/4})/2, m1 = (1−e^{−1/16})/2, m = min(m0, m1);
- M_A²(η) = 2√(2+r0²) + max{coth η·log(1/m1), ¾η coth η + log(1/m0)}.

Assume:
- **(M_A)** M² ≥ M_A²;
- δ := Δ1⁺ + max(Δ2⁺, Δ3⁺) ≤ m/2;
- y_β := exp(−√β(Θ(r0)−Θ(ℓ))) ≤ m/2.

Then (Tφ_L)(x) ≥ λφ_L(x) for every λ ∈ (0,1] and every x ∈ supp φ_L with a1 ∈ [a_−, π/2]. The ring identity is no longer needed. The cut-off inequality (label tu:L-cutoff) is kept.

**The proof in one paragraph.** Put x_c = c1/G and y_c = c2/E. The exact relation G = e^{−kV/2} with k = √(1+S²)/S gives (A2/A1)x_c = P·x_c^γ, where P = e^{e(S)−M²/k} and γ = 1−1/k. The needed inequality becomes e^δ F ≤ 1, where F = a(1−x_c)(1−y_c) + P x_c^γ + b y_c, a = λ/A1° ≤ e^{−3η/4}, and b = e^{−Θ'(a2)²/2}. F is affine in y_c, so two slices suffice:
- y_c = 0: weighted AM–GM gives F ≤ 1−m0 under the second branch of (M_A).
- y_c = 1, which is reachable only where a2 ≥ ℓ, so b ≤ e^{−1/16}: F ≤ P + b ≤ 1−m1 under the first branch.
- On the strip a2 < ℓ we have y_c ≤ y_β.
- Then e^{m/2}(1−m/2) ≤ 1 absorbs the errors.

**Answers to the brief's questions.**
- The margin is positive for every η in (0, 0.4], and it is proportional to η as η→0. The quantified error margin is m/2 ≈ 3η/16. A margin of order η cannot be avoided: at x_c = y_c = 0, a2 = 0 the exact limit slack is 1−e^{−η}. The writer's 0.0100 at η = 0.01 is exactly this.
- M² of order 1/η is also necessary in the corner. The smallest M² that works on the grid is η·M² = 3.74 / 2.96 / 2.77 / 2.75 at η = 0.4 / 0.1 / 0.01 / 0.001 (measured only).

**Downstream changes.** I rewrote:
- the assembly bullet for M, to M² ≥ M_A² and M² ≥ 1.5ρ_B² + log 2;
- the β₀ list;
- the Remark on M;
- the status lines of Prop tu:L-sub, Cor tu:L-H4cor and Thm tu:L-main.

The old c₁ choice implies (M_A). The proof is given in the lemma's remark, and the numerical slack is ≥ 5.98 on 4005 points. So the assembly's earlier M may be kept. Nothing else uses the ring identity or e^{η/2}−1; I checked with grep.

## (B) Lemma tu:L-balls — PROVED

The old proof split by the value of a1 at the ball centre, and the points with a1 just outside [a_−, π−a_−] in a valley ball fell between the cases. The fix is to split by ball type:

1. **Step-1 and step-3 balls.** Every point z has a_i(z) < a_− + ρ_B/√β and V(z) ≤ 2M''², with M'' = 1+2ρ_B+ρ_B² = 2.25. Theorem H4 then applies pointwise and gives −log g(z) ≤ (3·8.35+9.09)a_−√β + R'_β ≤ 35a_−√β + R'_β, with R'_β written out.
2. **Valley balls.** For every point z, with any a1:
   - q ≤ ρ_B²/β and βαq/2 ≤ 1.4804ρ_B² ≤ 1.5ρ_B² (for β ≥ 4);
   - G − c1 ≥ e^{−1.5ρ_B²}/2;
   - E − c2 ≥ 1/2, using four explicit β conditions.

   Also φ = μe^{−√β min(Ψ(a1),Ψ(π−a1))}(G−c1)₊(E−c2)₊ holds at every point of X, not only on Ω. Since Prop tu:L-sub gives g ≥ φ on all of X, we get g(z) ≥ (μ/4)e^{−1.5ρ_B²}e^{−√βΨ(π/2)}.

## (C) M² — corrected

The note's c₁ formula at equality gives M² = 18.05, 30.38, 54.36, 101.6, 475.7 at η = 0.4, 0.2, 0.1, 0.05, 0.01, so η·M² = 7.22 falling to 4.656 = √2(e(√2)+1) as η→0.
- The writer's 18.0 is right.
- The child's 7.2 → 4.7 is right.
- The working file's 14.8 and "3.4/η" are wrong for that formula.

The new (M_A) gives M_A² = 12.06, 20.55, 37.91, 72.82, 352.5 at the same η, with η·M_A² → log(1/m1) = 3.497. The text is corrected in the Remark on M and in the S4-alg remark.
