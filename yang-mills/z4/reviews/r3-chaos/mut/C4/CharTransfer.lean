/-
Worker r2-char (formalizer) for Director Z4.

Convention (stated once, used everywhere):
  conv w f x  = ∑ y, w y * f (x * y⁻¹)          (convolution operator T_w)
  coeff w ψ   = ∑ y, w y * ψ y⁻¹                 (character coefficient c_ψ)
  kern w 0    = w
  kern w (n+1) x = ∑ g, kern w n g * w (g⁻¹ * x)
so that kern w (N-1) x = ∑_{g_1..g_{N-1}} w g_1 * w (g_1⁻¹ g_2) * ... * w (g_{N-1}⁻¹ x),
the kernel of the N-fold chain (N plaquettes around the circle).

F1 conv_char      : T_w ψ = c_ψ • ψ for every multiplicative ψ : G → ℂ.
F2 iterate_char   : T_w^[N] ψ = c_ψ^N • ψ for every N.
F3 iterate_eq_kern: T_w^[n+1] f = conv (kern w n) f  for every f (identification
                    of the (n+1)-fold transfer step with the chain kernel).
F4 coeff_real_even: w real and even, |ψ| = 1, ψ multiplicative ⇒
                    c_ψ = ↑(∑ y, w y * Re ψ y)  (so c_ψ is real).
   coeff_eq_lam1 / coeff_one_eq_lam0: with w y = exp (b * c y) this is exactly
   lam1 c (Re ψ) b, resp. lam0 c b, of input/LevelsControl.lean (definitions
   copied verbatim below under the same names; that file is not modified).
   Z_n reading: G = Multiplicative (ZMod n), c j = cos(2πj/n), ψ_1 j = exp(2πij/n),
   Re ψ_1 = χ of LevelsControl; ψ = 1 gives lam0. The Z_n instance is not
   instantiated here.

Hypothesis shortening: F1–F3 need only [Group G] [Fintype G]; commutativity and
DecidableEq are not used. F4 needs evenness of w and ‖ψ y‖ = 1.
-/
import Mathlib

open Finset

namespace Z4Char

noncomputable section

variable {G : Type*} [Group G] [Fintype G]

/-- Convolution (transfer) operator: `(T_w f) x = ∑ y, w y * f (x * y⁻¹)`. -/
def conv (w f : G → ℂ) : G → ℂ := fun x => ∑ y, w y * f (x * y⁻¹)

/-- Character coefficient `c_ψ = ∑ y, w y * ψ y⁻¹`. -/
def coeff (w ψ : G → ℂ) : ℂ := ∑ y, w y * ψ y⁻¹

/-- Chain kernel: `kern w n` is the (n+1)-fold convolution power of `w`. -/
def kern (w : G → ℂ) : ℕ → G → ℂ
  | 0 => w
  | n + 1 => fun x => ∑ g, kern w n g * w (g⁻¹ * x)

theorem conv_smul (w f : G → ℂ) (a : ℂ) : conv w (a • f) = a • conv w f := by
  funext x
  simp only [conv, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun y _ => by ring

/-- F1. -/
theorem conv_char (w ψ : G → ℂ) (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) :
    conv w ψ = coeff w ψ • ψ := by
  funext x
  simp only [conv, coeff, Pi.smul_apply, smul_eq_mul, hψ, Finset.sum_mul]
  refine Finset.sum_congr rfl fun y _ => by ring

/-- F2. -/
theorem iterate_char (w ψ : G → ℂ) (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (N : ℕ) :
    (conv w)^[N] ψ = coeff w ψ ^ N • ψ := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply', ih, conv_smul, conv_char w ψ hψ, smul_smul, pow_succ]

/-- F3. -/
theorem iterate_eq_kern (w f : G → ℂ) (n : ℕ) :
    (conv w)^[n + 1] f = conv (kern w n) f := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply', ih]
    funext x
    simp only [conv, kern, Finset.mul_sum, Finset.sum_mul]
    conv_rhs => rw [Finset.sum_comm]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun g _ => ?_
    refine Fintype.sum_equiv (Equiv.mulLeft g) _ _ fun y => ?_
    simp only [Equiv.coe_mulLeft, inv_mul_cancel_left, mul_inv_rev, mul_assoc]
    ring

/-- F4. -/
theorem coeff_real_even (w : G → ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y)
    (heven : ∀ y, w y⁻¹ = w y) :
    coeff (fun y => (w y : ℂ)) ψ = ((∑ y, w y * (ψ y).re : ℝ) : ℂ) := by
  have h1 : ψ 1 = 1 := by
    have h := hψ 1 1
    rw [mul_one] at h
    have hne : ψ 1 ≠ 0 := by
      intro h0; have := hu 1; rw [h0, norm_zero] at this; exact zero_ne_one this
    exact (mul_left_cancel₀ hne (h.symm.trans (mul_one _).symm))
  have hinv : ∀ y, ψ y⁻¹ = (starRingEnd ℂ) (ψ y) := by
    intro y
    have hy : ψ y * ψ y⁻¹ = 1 := by rw [← hψ, mul_inv_cancel, h1]
    have hc : ψ y * (starRingEnd ℂ) (ψ y) = 1 := by
      rw [Complex.mul_conj, Complex.normSq_eq_norm_sq, hu y]; simp
    have hne : ψ y ≠ 0 := by
      intro h0; have := hu y; rw [h0, norm_zero] at this; exact zero_ne_one this
    exact mul_left_cancel₀ hne (hy.trans hc.symm)
  -- c = ∑ w y * conj ψ y, and by evenness c = ∑ w y * ψ y
  have hA : coeff (fun y => (w y : ℂ)) ψ = ∑ y, (w y : ℂ) * (starRingEnd ℂ) (ψ y) := by
    simp only [coeff, hinv]
  have hB : coeff (fun y => (w y : ℂ)) ψ = ∑ y, (w y : ℂ) * ψ y := by
    unfold coeff
    refine Fintype.sum_equiv (Equiv.inv G) _ _ fun y => ?_
    simp [heven]
  have h2 : 2 * coeff (fun y => (w y : ℂ)) ψ = 2 * ((∑ y, w y * (ψ y).re : ℝ) : ℂ) := by
    rw [two_mul]
    nth_rewrite 1 [hA]
    rw [hB, ← Finset.sum_add_distrib, Complex.ofReal_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun y _ => ?_
    rw [← mul_add, add_comm, Complex.add_conj]
    push_cast; ring
  exact mul_left_cancel₀ two_ne_zero h2

/-! Link to input/LevelsControl.lean (definitions copied verbatim, same names). -/

noncomputable def lam0 (c : G → ℝ) (b : ℝ) : ℝ := ∑ j, Real.exp (b * c j)
noncomputable def lam1 (c χ : G → ℝ) (b : ℝ) : ℝ := ∑ j, Real.exp (b * c j) * χ j

/-- With the weight `exp (b * c y)`, `c` even, the character coefficient of a
unitary multiplicative ψ is `lam1 c (Re ψ) b` of LevelsControl.lean. -/
theorem coeff_eq_lam1 (c : G → ℝ) (b : ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)
    (heven : ∀ y, c y⁻¹ = c y) :
    coeff (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)) ψ = ((lam1 c (fun y => (ψ y).re) b : ℝ) : ℂ) :=
  coeff_real_even (fun y => Real.exp (b * c y)) ψ hψ hu (fun y => by simp [heven])

/-- The trivial character gives `lam0 c b` (no evenness needed). -/
theorem coeff_one_eq_lam0 (c : G → ℝ) (b : ℝ) :
    coeff (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)) (fun _ => 1) = ((lam0 c b : ℝ) : ℂ) := by
  simp [coeff, lam0]

/-- Transfer eigenvalue on the N-plaquette circle, in LevelsControl's notation. -/
theorem iterate_eq_lam1_pow (c : G → ℝ) (b : ℝ) (ψ : G → ℂ)
    (hψ : ∀ x y, ψ (x * y) = ψ x * ψ y) (hu : ∀ y, ‖ψ y‖ = 1)
    (heven : ∀ y, c y⁻¹ = c y) (N : ℕ) :
    (conv (fun y => ((Real.exp (b * c y) : ℝ) : ℂ)))^[N] ψ =
      (((lam1 c (fun y => (ψ y).re) b : ℝ) : ℂ)) ^ N • ψ := by
  rw [iterate_char _ ψ hψ, coeff_eq_lam1 c b ψ hψ hu heven]

end

end Z4Char

#print axioms Z4Char.conv_char
#print axioms Z4Char.iterate_char
#print axioms Z4Char.iterate_eq_kern
#print axioms Z4Char.coeff_real_even
#print axioms Z4Char.coeff_eq_lam1
#print axioms Z4Char.coeff_one_eq_lam0
#print axioms Z4Char.iterate_eq_lam1_pow
