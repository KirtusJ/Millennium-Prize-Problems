import Mathlib
open Real

/-- 1 - cos x ≥ (2/π²) x² on [-π, π], via 1 - cos x = 2 sin²(x/2) and Jordan. -/
theorem one_sub_cos_ge (x : ℝ) (h1 : -π ≤ x) (h2 : x ≤ π) :
    2 / π ^ 2 * x ^ 2 ≤ 1 - cos x := by
  have hpi := Real.pi_pos
  have hc : 1 - cos x = 2 * sin (|x| / 2) ^ 2 := by
    have : cos x = cos (2 * (|x| / 2)) := by
      rw [show 2 * (|x| / 2) = |x| by ring]; exact (Real.cos_abs x).symm
    rw [this, Real.cos_two_mul, Real.cos_sq']; ring
  have ha : 0 ≤ |x| / 2 := by positivity
  have hb : |x| / 2 ≤ π / 2 := by
    have : |x| ≤ π := abs_le.mpr ⟨h1, h2⟩
    linarith
  have hj := Real.mul_le_sin ha hb
  have h0 : 0 ≤ 2 / π * (|x| / 2) := by positivity
  have hsq : (2 / π * (|x| / 2)) ^ 2 ≤ sin (|x| / 2) ^ 2 := pow_le_pow_left₀ h0 hj 2
  have hA : (2 / π * (|x| / 2)) ^ 2 = |x| ^ 2 / π ^ 2 := by field_simp; rw [mul_pow, sq_abs]; ring
  rw [hc]
  calc 2 / π ^ 2 * x ^ 2 = 2 * (|x| ^ 2 / π ^ 2) := by rw [sq_abs]; ring
    _ = 2 * (2 / π * (|x| / 2)) ^ 2 := by rw [hA]
    _ ≤ 2 * sin (|x| / 2) ^ 2 := by linarith

/-- (a-b)_+^2 / 2 ≥ a^2/4 - b^2/2 for a ≥ 0, b ≥ 0. -/
theorem half_pos_part_sq (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    a ^ 2 / 4 - b ^ 2 / 2 ≤ (max (a - b) 0) ^ 2 / 2 := by
  rcases le_total b a with h | h
  · rw [max_eq_left (by linarith)]; nlinarith [sq_nonneg (a - 2 * b)]
  · rw [max_eq_right (by linarith)]; nlinarith

/-- |u+v|² ≥ ½|u|² - |v|² in any real inner product space. -/
theorem norm_add_sq_ge {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E] (u v : E) :
    ‖u‖ ^ 2 / 2 - ‖v‖ ^ 2 ≤ ‖u + v‖ ^ 2 := by
  have h := norm_add_sq_real u v
  have h2 := norm_add_sq_real u (2 • v)
  have h3 : ‖u + (2:ℝ) • v‖ ^ 2 ≥ 0 := sq_nonneg _
  rw [norm_add_sq_real, inner_smul_right, norm_smul] at h3
  simp at h3
  nlinarith [h, h3]

/-- e^s - 1 - s ≤ (s^2/2) e^s for s ≥ 0. -/
theorem exp_rem (s : ℝ) (hs : 0 ≤ s) : exp s - 1 - s ≤ s ^ 2 / 2 * exp s := by
  -- g(s) = (s^2/2) e^s - e^s + 1 + s, g(0)=0, g' = (s^2/2+s-1)e^s + 1 ≥ 0 ? use bound e^{-s} ≥ 1 - s + ... instead
  have h := Real.add_one_le_exp (-s)
  have he : 0 < exp s := exp_pos s
  have hm : exp (-s) * exp s = 1 := by rw [← Real.exp_add]; simp
  -- need: 1 + s ≥ e^s (1 - s^2/2)  i.e. (1+s) e^{-s} ≥ 1 - s^2/2
  have key : 1 - s ^ 2 / 2 ≤ (1 + s) * exp (-s) := by
    -- f(s) = (1+s)e^{-s} - 1 + s^2/2, f(0)=0, f'(s) = -s e^{-s} + s = s(1-e^{-s}) ≥ 0
    have hmono : MonotoneOn (fun t => (1 + t) * exp (-t) - 1 + t ^ 2 / 2) (Set.Ici 0) := by
      apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
      · fun_prop
      · fun_prop
      · intro t ht
        simp only [Set.nonempty_Iio, interior_Ici', Set.mem_Ioi] at ht
        have hd : deriv (fun t => (1 + t) * exp (-t) - 1 + t ^ 2 / 2) t = t * (1 - exp (-t)) := by
          have : HasDerivAt (fun t => (1 + t) * exp (-t) - 1 + t ^ 2 / 2)
              ((1:ℝ) * exp (-t) + (1 + t) * (exp (-t) * (-1)) + (2 * t) / 2) t := by
            have h1 : HasDerivAt (fun t : ℝ => 1 + t) 1 t := by simpa using (hasDerivAt_id t).const_add 1
            have h2 : HasDerivAt (fun t : ℝ => exp (-t)) (exp (-t) * (-1)) t := by
              simpa using (hasDerivAt_neg t).exp
            have h3 : HasDerivAt (fun t : ℝ => t ^ 2 / 2) (2 * t / 2) t := by
              simpa using (hasDerivAt_pow 2 t).div_const 2
            exact ((h1.mul h2).sub_const 1).add h3
          rw [this.deriv]; ring
        rw [hd]
        have : exp (-t) ≤ 1 := by rw [Real.exp_le_one_iff]; linarith
        nlinarith
    have := hmono (Set.mem_Ici.mpr le_rfl) (Set.mem_Ici.mpr hs) hs
    simp at this
    linarith
  have : (1 - s ^ 2 / 2) * exp s ≤ (1 + s) := by
    calc (1 - s ^ 2 / 2) * exp s ≤ (1 + s) * exp (-s) * exp s := by
          exact mul_le_mul_of_nonneg_right key he.le
      _ = 1 + s := by rw [mul_assoc, hm, mul_one]
  nlinarith

#print axioms one_sub_cos_ge
#print axioms half_pos_part_sq
#print axioms norm_add_sq_ge
#print axioms exp_rem
