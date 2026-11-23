/-
Builder (Z4) | B1: finite-level generalization of FiniteGroupControl.

Setting. A finite index type ι of "levels", values c : ι → ℝ, a distinguished
maximizer i0, a spacing d > 0 with c j ≤ c i0 - d for every j ≠ i0, and
"characters" χ : ι → ℝ with |χ j| ≤ 1 and χ i0 = 1.
  lam0 b = ∑ j, exp (b * c j)          (top character coefficient)
  lam1 b = ∑ j, exp (b * c j) * χ j    (next character coefficient)
Main bound (levels_gap_le): for b ≥ 0 with 2 * K * exp (-b d) ≤ 1, K = card ι,
  0 < lam1 b ≤ lam0 b  and  -log (lam1 b / lam0 b) ≤ 4 * K * exp (-b d),
hence b * (-log ratio) ≤ 4 K · b exp(-b d), and along b = (N+1)^2 the physical
gap tends to 0 (levels_physical_gap_tendsto_zero).
Z_n: ι = Fin n, c j = cos(2πj/n), χ j = cos(2πj/n) (real part of the charge-1
character; for n ≥ 3 the pair ±j gives the same real sum), d = 1 - cos(2π/n).
That identification, and the identification of the transfer eigenvalues with
the character coefficients, are NOT formalized here.
χ is taken real-valued: this covers the real part, which is what the sum
equals whenever the weight is invariant under j ↦ -j (as for exp(b cos θ)).
-/
import Mathlib

open Filter Topology Finset

namespace Z4YM

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

noncomputable def lam0 (c : ι → ℝ) (b : ℝ) : ℝ := ∑ j, Real.exp (b * c j)
noncomputable def lam1 (c χ : ι → ℝ) (b : ℝ) : ℝ := ∑ j, Real.exp (b * c j) * χ j

theorem levels_gap_le (c χ : ι → ℝ) (i0 : ι) {d b : ℝ}
    (hgap : ∀ j, j ≠ i0 → c j ≤ c i0 - d)
    (hχ : ∀ j, |χ j| ≤ 1) (hχ0 : χ i0 = 1) (hb : 0 ≤ b)
    (hsmall : 2 * (Fintype.card ι : ℝ) * Real.exp (-b * d) ≤ 1) :
    0 < lam1 c χ b ∧ lam1 c χ b ≤ lam0 c b ∧
      -Real.log (lam1 c χ b / lam0 c b) ≤ 4 * (Fintype.card ι : ℝ) * Real.exp (-b * d) := by
  set K : ℝ := (Fintype.card ι : ℝ)
  set q : ℝ := Real.exp (-b * d)
  set e0 : ℝ := Real.exp (b * c i0)
  set S := (univ : Finset ι).erase i0
  set E : ℝ := ∑ j ∈ S, Real.exp (b * c j)
  set R : ℝ := ∑ j ∈ S, Real.exp (b * c j) * χ j
  have he0 : 0 < e0 := Real.exp_pos _
  have hq : 0 < q := Real.exp_pos _
  have h0 : lam0 c b = e0 + E := by
    unfold lam0; rw [← Finset.add_sum_erase _ _ (mem_univ i0)]
  have h1 : lam1 c χ b = e0 + R := by
    unfold lam1; rw [← Finset.add_sum_erase _ _ (mem_univ i0), hχ0, mul_one]
  -- each other level is suppressed by q
  have hterm : ∀ j ∈ S, Real.exp (b * c j) ≤ e0 * q := by
    intro j hj
    have hj' : j ≠ i0 := Finset.ne_of_mem_erase hj
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have := mul_le_mul_of_nonneg_left (hgap j hj') hb
    linarith
  have hE0 : 0 ≤ E := Finset.sum_nonneg fun j _ => (Real.exp_pos _).le
  have hEle : E ≤ K * (e0 * q) := by
    calc E ≤ ∑ _j ∈ S, e0 * q := Finset.sum_le_sum hterm
      _ = (S.card : ℝ) * (e0 * q) := by rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ K * (e0 * q) := by
          apply mul_le_mul_of_nonneg_right _ (by positivity)
          have : S.card ≤ Fintype.card ι := by
            simpa [S] using Finset.card_erase_le (s := (univ : Finset ι)) (a := i0)
          simp only [K]; exact_mod_cast this
  have hRabs : |R| ≤ E := by
    calc |R| ≤ ∑ j ∈ S, |Real.exp (b * c j) * χ j| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ j ∈ S, Real.exp (b * c j) := by
          apply Finset.sum_le_sum; intro j _
          rw [abs_mul, abs_of_pos (Real.exp_pos _)]
          exact mul_le_of_le_one_right (Real.exp_pos _).le (hχ j)
  have hR1 := neg_abs_le R
  have hR2 := le_abs_self R
  have hEhalf : 2 * E ≤ e0 := by
    have : 2 * K * q * e0 ≤ e0 := by nlinarith
    nlinarith
  have hl1pos : 0 < e0 + R := by linarith
  have hl0pos : 0 < e0 + E := by linarith
  refine ⟨by rw [h1]; exact hl1pos, by rw [h0, h1]; linarith, ?_⟩
  rw [h0, h1, ← Real.log_inv, inv_div]
  have hpos : 0 < (e0 + E) / (e0 + R) := div_pos hl0pos hl1pos
  calc Real.log ((e0 + E) / (e0 + R)) ≤ (e0 + E) / (e0 + R) - 1 :=
        Real.log_le_sub_one_of_pos hpos
    _ = (E - R) / (e0 + R) := by field_simp
    _ ≤ 4 * E / e0 := by
        rw [div_le_div_iff₀ hl1pos he0]; nlinarith
    _ ≤ 4 * K * q := by
        rw [div_le_iff₀ he0]; nlinarith

/-- Physical-gap form: b · (−log ratio) ≤ 4 K · b · exp(−b d). -/
theorem levels_physical_gap_le (c χ : ι → ℝ) (i0 : ι) {d b : ℝ}
    (hgap : ∀ j, j ≠ i0 → c j ≤ c i0 - d)
    (hχ : ∀ j, |χ j| ≤ 1) (hχ0 : χ i0 = 1) (hb : 0 ≤ b)
    (hsmall : 2 * (Fintype.card ι : ℝ) * Real.exp (-b * d) ≤ 1) :
    b * (-Real.log (lam1 c χ b / lam0 c b)) ≤
      4 * (Fintype.card ι : ℝ) * (b * Real.exp (-b * d)) := by
  have h := (levels_gap_le c χ i0 hgap hχ hχ0 hb hsmall).2.2
  calc b * (-Real.log (lam1 c χ b / lam0 c b))
      ≤ b * (4 * (Fintype.card ι : ℝ) * Real.exp (-b * d)) :=
        mul_le_mul_of_nonneg_left h hb
    _ = _ := by ring

/-- b · exp(−b d) → 0 as b → ∞, for d > 0. -/
theorem mul_exp_neg_tendsto_zero {d : ℝ} (hd : 0 < d) :
    Tendsto (fun b : ℝ => b * Real.exp (-b * d)) atTop (𝓝 0) := by
  have h1 := (Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero 1).comp
    (tendsto_id.atTop_mul_const hd)
  have h2 := h1.const_mul (1 / d)
  rw [mul_zero] at h2
  refine h2.congr fun b => ?_
  simp only [Function.comp, id, pow_one]
  field_simp
  ring_nf

/-- Along the trajectory b = (N+1)², the physical gap tends to zero. -/
theorem levels_physical_gap_tendsto_zero (c χ : ι → ℝ) (i0 : ι) {d : ℝ} (hd : 0 < d)
    (hgap : ∀ j, j ≠ i0 → c j ≤ c i0 - d)
    (hχ : ∀ j, |χ j| ≤ 1) (hχ0 : χ i0 = 1) :
    Tendsto (fun N : ℕ => ((N : ℝ) + 1) ^ 2 *
        (-Real.log (lam1 c χ (((N : ℝ) + 1) ^ 2) / lam0 c (((N : ℝ) + 1) ^ 2))))
      atTop (𝓝 0) := by
  set K : ℝ := (Fintype.card ι : ℝ)
  have hb : Tendsto (fun N : ℕ => ((N : ℝ) + 1) ^ 2) atTop atTop := by
    have : Tendsto (fun N : ℕ => (N : ℝ) + 1) atTop atTop :=
      tendsto_atTop_add_const_right _ 1 tendsto_natCast_atTop_atTop
    exact (tendsto_pow_atTop (two_ne_zero)).comp this
  have hupper : Tendsto (fun N : ℕ => 4 * K * (((N : ℝ) + 1) ^ 2 *
      Real.exp (-(((N : ℝ) + 1) ^ 2) * d))) atTop (𝓝 0) := by
    have := ((mul_exp_neg_tendsto_zero hd).comp hb).const_mul (4 * K)
    rw [mul_zero] at this; exact this
  -- eventually the smallness hypothesis holds
  have hq : Tendsto (fun N : ℕ => 2 * K * Real.exp (-(((N : ℝ) + 1) ^ 2) * d)) atTop (𝓝 0) := by
    have hexp : Tendsto (fun b : ℝ => Real.exp (-b * d)) atTop (𝓝 0) := by
      have : Tendsto (fun b : ℝ => -b * d) atTop atBot := by
        have h := tendsto_neg_atTop_atBot.comp (tendsto_id.atTop_mul_const hd)
        refine h.congr fun b => ?_
        simp [Function.comp, neg_mul]
      exact Real.tendsto_exp_atBot.comp this
    have := (hexp.comp hb).const_mul (2 * K)
    rw [mul_zero] at this; exact this
  have hev : ∀ᶠ N : ℕ in atTop, 2 * K * Real.exp (-(((N : ℝ) + 1) ^ 2) * d) ≤ 1 :=
    (hq.eventually (ge_mem_nhds (by norm_num : (0:ℝ) < 1)))
  refine squeeze_zero' ?_ ?_ hupper
  · filter_upwards [hev] with N hN
    have hbN : (0 : ℝ) ≤ ((N : ℝ) + 1) ^ 2 := by positivity
    obtain ⟨hp, hle, -⟩ := levels_gap_le c χ i0 hgap hχ hχ0 hbN hN
    have hl0 : 0 < lam0 c (((N : ℝ) + 1) ^ 2) := lt_of_lt_of_le hp hle
    have hr : lam1 c χ (((N : ℝ) + 1) ^ 2) / lam0 c (((N : ℝ) + 1) ^ 2) ≤ 1 :=
      (div_le_one hl0).mpr hle
    have : Real.log (lam1 c χ (((N : ℝ) + 1) ^ 2) / lam0 c (((N : ℝ) + 1) ^ 2)) ≤ 0 :=
      Real.log_nonpos (div_pos hp hl0).le hr
    exact mul_nonneg hbN (by linarith)
  · filter_upwards [hev] with N hN
    exact levels_physical_gap_le c χ i0 hgap hχ hχ0 (by positivity) hN

end Z4YM

#print axioms Z4YM.levels_gap_le
#print axioms Z4YM.levels_physical_gap_le
#print axioms Z4YM.levels_physical_gap_tendsto_zero
