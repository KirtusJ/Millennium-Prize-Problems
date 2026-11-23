import Mathlib.Data.Complex.ExponentialBounds
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace YangMills.FlowReflection

theorem shiftedDistance (u v R : ℝ) : u - (-2*R-v) = u+v+2*R := by ring

theorem fixedExponential (w R u v : ℝ) :
    Real.exp (-w*(u+v+2*R)) =
      Real.exp (-2*w*R)*Real.exp (-w*u)*Real.exp (-w*v) := by
  rw [← Real.exp_add, ← Real.exp_add]
  congr 1
  ring

theorem rankOnePositive {ι : Type*} (I : Finset ι) (c g : ι → ℝ) (d : ℝ) (hd : 0 ≤ d) :
    0 ≤ ∑ i ∈ I, ∑ j ∈ I, c i * c j * (d*g i*g j) := by
  have he : (∑ i ∈ I, ∑ j ∈ I, c i * c j * (d*g i*g j)) =
      d*((∑ i ∈ I, c i*g i)*(∑ j ∈ I, c j*g j)) := by
    simp only [Finset.sum_mul, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he]
  exact mul_nonneg hd (mul_self_nonneg _)

theorem heatDeficit {v : ℝ} (h0 : 0 ≤ v) (h1 : v ≤ 1) :
    0 ≤ 1 - (1-v)^2 ∧ 1 - (1-v)^2 ≤ 2*v := by
  constructor
  · nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]
  · nlinarith [sq_nonneg v]

/-- The connected OS form for coefficients (3,-64,25). -/
def three (m : ℕ → ℝ) : ℝ :=
  3*(3*m 1-64*m 2+25*m 3)-64*(3*m 2-64*m 3+25*m 4)+25*(3*m 3-64*m 4+25*m 5)

theorem collected (m : ℕ → ℝ) : three m =
    9*m 1-384*m 2+4246*m 3-3200*m 4+625*m 5 := by unfold three; ring

theorem gridDrop (v : ℕ → ℝ) (hp : ∀ j, 0 ≤ v j-2*v (j+1)+v (j+2)) (n : ℕ) :
    v 0-v n ≤ n*(v 0-v 1) := by
  have hstep : ∀ j : ℕ, v j-v (j+1) ≤ v 0-v 1 := by
    intro j
    induction j with
    | zero => exact le_rfl
    | succ j ih => linarith [hp j]
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Nat.cast_succ, add_mul, one_mul]
    linarith [hstep n]

/-- A quadratic increment bound and all reflected second differences force zero drop. -/
theorem cuspRigidity (C : ℝ → ℝ) (K t : ℝ) (ht : 0 < t)
    (hp : ∀ (h : ℝ), 0 < h → ∀ j : ℕ,
      0 ≤ C (j*h)-2*C ((j+1:ℕ)*h)+C ((j+2:ℕ)*h))
    (hs : ∀ h : ℝ, 0 < h → C 0-C h ≤ K*h^2) : C 0 ≤ C t := by
  by_contra! hd
  obtain ⟨n, hn⟩ := exists_nat_gt (max 0 (K*t^2/(C 0-C t)))
  have hn0 : (0:ℝ) < n := lt_of_le_of_lt (le_max_left _ _) hn
  have hn1 : K*t^2/(C 0-C t) < n := lt_of_le_of_lt (le_max_right _ _) hn
  have hh := div_pos ht hn0
  have h := gridDrop (fun j : ℕ => C ((j:ℝ)*(t/n))) (hp _ hh) n
  simp only [Nat.cast_zero, zero_mul, Nat.cast_one, one_mul] at h
  rw [show (n:ℝ)*(t/n)=t by field_simp] at h
  have h' := h.trans (mul_le_mul_of_nonneg_left (hs _ hh) hn0.le)
  have h'' : (C 0-C t)*n ≤ K*t^2 := by
    calc
      _ ≤ ((n:ℝ)*(K*(t/n)^2))*n := mul_le_mul_of_nonneg_right h' hn0.le
      _ = _ := by field_simp
                  ring
  exact (not_lt_of_ge h'') (by nlinarith [(div_lt_iff₀ (sub_pos.mpr hd)).mp hn1])

/-- s = 1/8, T = h = 1; the common positive factor B is divided out. -/
noncomputable def moment (k : ℕ) : ℝ :=
  (1-(1+(k:ℝ)^2)*Real.exp (-((k:ℝ)^2)))^2 / (k:ℝ)^8

theorem baseInterval : 3678/10000 ≤ Real.exp (-1) ∧ Real.exp (-1) ≤ 3680/10000 := by
  rw [Real.exp_neg, inv_eq_one_div]
  constructor
  · apply (le_div_iff₀ (Real.exp_pos _)).2
    linarith [Real.exp_one_lt_d9]
  · apply (div_le_iff₀ (Real.exp_pos _)).2
    linarith [Real.exp_one_gt_d9]

theorem exponentialPower (k : ℕ) :
    Real.exp (-((k:ℝ)^2)) = Real.exp (-1)^ (k^2) := by
  rw [← Real.exp_nat_mul]
  push_cast
  ring_nf

def side (k : ℕ) (q : ℝ) : ℝ := 1-(1+(k:ℝ)^2)*q^(k^2)

theorem sides (k : ℕ) : side k (3680/10000) ≤ side k (Real.exp (-1)) ∧
    side k (Real.exp (-1)) ≤ side k (3678/10000) := by
  have hl := pow_le_pow_left₀ (show 0 ≤ (3678/10000:ℝ) by norm_num) baseInterval.1 (k^2)
  have hu := pow_le_pow_left₀ (Real.exp_pos (-1)).le baseInterval.2 (k^2)
  have hc : 0 ≤ 1+(k:ℝ)^2 := by positivity
  exact ⟨sub_le_sub_left (mul_le_mul_of_nonneg_left hu hc) 1,
         sub_le_sub_left (mul_le_mul_of_nonneg_left hl hc) 1⟩

theorem enclose (k : ℕ) (lo hi : ℝ) (h0 : 0 ≤ side k (3680/10000))
    (hl : lo ≤ (side k (3680/10000))^2 / (k:ℝ)^8)
    (hu : (side k (3678/10000))^2 / (k:ℝ)^8 ≤ hi) : lo ≤ moment k ∧ moment k ≤ hi := by
  rw [moment, exponentialPower]
  change lo ≤ (side k (Real.exp (-1)))^2 / (k:ℝ)^8 ∧ _ ≤ hi
  have H := sides k
  exact ⟨hl.trans (div_le_div_of_nonneg_right (pow_le_pow_left₀ h0 H.1 2) (by positivity)),
    (div_le_div_of_nonneg_right (pow_le_pow_left₀ (h0.trans H.1) H.2 2) (by positivity)).trans hu⟩
theorem explicitNegative : three moment ≤ -100151644/10000000000 := by
  have h1 := enclose 1 (696960000/10000000000) (699073600/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])
  have h2 := enclose 2 (32227030/10000000000) (32241167/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])
  have h3 := enclose 3 (1520387/10000000000) (1520406/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])
  have h4 := enclose 4 (152587/10000000000) (152588/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])
  have h5 := enclose 5 (25599/10000000000) (25600/10000000000) (by norm_num [side]) (by norm_num [side]) (by norm_num [side])
  rw [collected]
  linarith [h1.2,h2.1,h3.2,h4.1,h5.2]

theorem signedTest : three moment < 0 := lt_of_le_of_lt explicitNegative (by norm_num)

theorem samePlaneError {Q A e : ℝ} (bound : -(2*A*e+e^2) ≤ Q) (h : Q < 0) :
    -Q ≤ 2*A*e+e^2 ∧ 0 < 2*A*e+e^2 := by constructor <;> linarith

end YangMills.FlowReflection
open YangMills.FlowReflection
#print axioms shiftedDistance
#print axioms fixedExponential
#print axioms rankOnePositive
#print axioms heatDeficit
#print axioms collected
#print axioms baseInterval
#print axioms exponentialPower
#print axioms sides
#print axioms enclose
#print axioms explicitNegative
#print axioms signedTest
#print axioms samePlaneError
#print axioms gridDrop
#print axioms cuspRigidity
