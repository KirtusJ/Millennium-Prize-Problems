import Mathlib

open MeasureTheory Real

theorem M6_child (ν : Measure ℝ) [IsFiniteMeasure ν] (hsupp : ν (Set.Iio 0) = 0)
    (s t : ℝ) (hs : 0 ≤ s) (ht : 0 ≤ t) :
    (∫ E, exp (-((s + t) / 2) * E) ∂ν) ^ 2 ≤ (∫ E, exp (-s * E) ∂ν) * (∫ E, exp (-t * E) ∂ν) := by
  have hae : ∀ᵐ E ∂ν, 0 ≤ E := by
    rw [ae_iff]
    have : {a : ℝ | ¬ 0 ≤ a} = Set.Iio 0 := by ext a; simp
    rw [this]; exact hsupp
  have memlp : ∀ c : ℝ, 0 ≤ c → MemLp (fun E => exp (-c * E)) (ENNReal.ofReal 2) ν := by
    intro c hc
    refine MemLp.of_bound (Continuous.aestronglyMeasurable (by fun_prop)) 1 ?_
    filter_upwards [hae] with E hE
    rw [Real.norm_eq_abs, abs_of_pos (exp_pos _)]
    apply exp_le_one_iff.mpr
    nlinarith
  set f : ℝ → ℝ := fun E => exp (-(s / 2) * E) with hf
  set g : ℝ → ℝ := fun E => exp (-(t / 2) * E) with hg
  have key := integral_mul_le_Lp_mul_Lq_of_nonneg (μ := ν) Real.HolderConjugate.two_two
    (f := f) (g := g) (Filter.Eventually.of_forall fun E => (exp_pos _).le)
    (Filter.Eventually.of_forall fun E => (exp_pos _).le)
    (memlp (s / 2) (by linarith)) (memlp (t / 2) (by linarith))
  have h1 : (fun E => f E * g E) = fun E => exp (-((s + t) / 2) * E) := by
    funext E; simp only [hf, hg]; rw [← exp_add]; ring_nf
  have h2 : (fun E => f E ^ (2:ℝ)) = fun E => exp (-s * E) := by
    funext E; simp only [hf]; rw [← Real.exp_mul]; ring_nf
  have h3 : (fun E => g E ^ (2:ℝ)) = fun E => exp (-t * E) := by
    funext E; simp only [hg]; rw [← Real.exp_mul]; ring_nf
  rw [h1, h2, h3] at key
  set I := ∫ E, exp (-((s + t) / 2) * E) ∂ν
  set A := ∫ E, exp (-s * E) ∂ν
  set B := ∫ E, exp (-t * E) ∂ν
  have hI : 0 ≤ I := integral_nonneg fun _ => (exp_pos _).le
  have hA : 0 ≤ A := integral_nonneg fun _ => (exp_pos _).le
  have hB : 0 ≤ B := integral_nonneg fun _ => (exp_pos _).le
  rw [← Real.sqrt_eq_rpow, ← Real.sqrt_eq_rpow] at key
  calc I ^ 2 ≤ (√A * √B) ^ 2 := pow_le_pow_left₀ hI key 2
    _ = A * B := by rw [mul_pow, Real.sq_sqrt hA, Real.sq_sqrt hB]

#print axioms M6_child
