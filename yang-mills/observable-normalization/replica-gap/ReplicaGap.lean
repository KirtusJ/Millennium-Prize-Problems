import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open scoped BigOperators
namespace YangMills.ReplicaGap

/-- Second elementary symmetric polynomial of the spectral weights. -/
def pairs : List ℝ → ℝ
  | [] => 0
  | a :: rest => a * rest.sum + pairs rest

theorem exteriorTrace (s : List ℝ) :
    2 * pairs s = s.sum^2 - (s.map (fun a => a^2)).sum := by
  induction s with
  | nil => simp [pairs]
  | cons a r ih =>
    simp only [pairs, List.sum_cons, List.map_cons]
    nlinarith only [ih]

theorem momentUpper {ι : Type*} (s : Finset ι) (f : ι → ℝ) (m : ℝ)
    (pos : ∀ i ∈ s, 0 ≤ f i) (top : ∀ i ∈ s, f i ≤ m) :
    ∑ i ∈ s, (f i)^2 ≤ m * ∑ i ∈ s, f i := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum fun i hi => by
    simpa [pow_two] using mul_le_mul_of_nonneg_right (top i hi) (pos i hi)

theorem momentLower {ι : Type*} (s : Finset ι) (f : ι → ℝ) {k : ι} (hk : k ∈ s) :
    (f k)^2 ≤ ∑ i ∈ s, (f i)^2 :=
  Finset.single_le_sum (fun i _ => sq_nonneg (f i)) hk

/-- a is the largest normalized weight; b is the largest normalized pair.
The last two hypotheses are the moment inequalities on unordered pairs. -/
theorem thermalBracket {a b p q : ℝ} (ha : 0 < a) (hp : 0 < p) (hp1 : p < 1)
    (hq : q ≤ 1) (hpa : p ≤ a) (hap : a^2 ≤ p)
    (pairTop : p^2*(1-q) ≤ (1-p)*b) (pairSq : b^2 ≤ p^2*((1-q)/2)) :
    p*(1-q)/(1-p) ≤ b/a^2 ∧ b/a^2 ≤ Real.sqrt ((1-q)/2)/p := by
  have hd : 0 ≤ (1-q)/2 := by linarith
  have hs := Real.sq_sqrt hd
  have ht := Real.sqrt_nonneg ((1-q)/2)
  constructor
  · apply (div_le_div_iff₀ (by linarith : 0 < 1-p) (sq_pos_of_pos ha)).2
    calc
      p*(1-q)*a^2 ≤ p*(1-q)*p :=
        mul_le_mul_of_nonneg_left hap (mul_nonneg hp.le (sub_nonneg.mpr hq))
      _ ≤ b*(1-p) := by linarith only [pairTop]
  · have hb : b ≤ p*Real.sqrt ((1-q)/2) := by
      by_contra! h
      have hz := mul_self_lt_mul_self (mul_nonneg hp.le ht) h
      nlinarith only [hz, pairSq, congrArg (fun t : ℝ => p^2*t) hs]
    apply (div_le_div_iff₀ (sq_pos_of_pos ha) hp).2
    calc
      b*p ≤ (p*Real.sqrt ((1-q)/2))*p := mul_le_mul_of_nonneg_right hb hp.le
      _ = Real.sqrt ((1-q)/2)*p^2 := by ring
      _ ≤ Real.sqrt ((1-q)/2)*a^2 :=
        mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hp.le hpa 2) ht

noncomputable def swapDeficit (a b : ℝ) : ℝ := (a-b)^2/(a^2+b^2)

theorem swapBounds {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    0 ≤ swapDeficit a b ∧ swapDeficit a b ≤ 1 := by
  unfold swapDeficit
  constructor
  · positivity
  · by_cases h : a^2+b^2 = 0
    · simp [h]
    · apply (div_le_one (lt_of_le_of_ne (by positivity) (Ne.symm h))).2
      nlinarith only [mul_nonneg ha hb]

theorem swapIdentity (a b : ℝ) : (a^2+b^2)*swapDeficit a b = (a-b)^2 := by
  by_cases h : a^2+b^2 = 0
  · have ha : a = 0 := by nlinarith [sq_nonneg a, sq_nonneg b]
    have hb : b = 0 := by nlinarith [sq_nonneg a, sq_nonneg b]
    simp [ha,hb,swapDeficit]
  · unfold swapDeficit
    field_simp

/-- Sum the pointwise identity under a measure-preserving exchange of endpoints. -/
theorem swapExpectation {ι : Type*} [Fintype ι] (a b : ι → ℝ)
    (ex : ∑ i, a i^2*swapDeficit (a i) (b i) = ∑ i, b i^2*swapDeficit (a i) (b i))
    (mass : ∑ i, b i^2 = ∑ i, a i^2) :
    ∑ i, a i^2*swapDeficit (a i) (b i) = (∑ i, a i^2) - ∑ i, a i*b i := by
  have h : ∀ i, a i^2*swapDeficit (a i) (b i) + b i^2*swapDeficit (a i) (b i) =
      a i^2+b i^2-2*(a i*b i) := fun i => by
    rw [← add_mul, swapIdentity]; ring
  have eqn := Finset.sum_congr (rfl : Finset.univ = (Finset.univ : Finset ι)) (fun i _ => h i)
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum] at eqn
  linarith only [eqn,ex,mass]

theorem purityMagneticError {h k v : ℝ} (hv : 0 ≤ v)
    (hh : 0 ≤ h) (hu : h ≤ 24*v) (hk : 0 ≤ k) (ku : k ≤ 96*v) :
    |k-2*h| ≤ 96*v := abs_le.mpr ⟨by linarith, by linarith⟩

theorem vacuumCurvature {r s : ℝ} (hr : r ≠ 1) :
    s*(1+r)/2 + 2*((1+r)/2)^2*s/(1-r) = s*(1+r)/(1-r) := by
  have h : 1-r ≠ 0 := sub_ne_zero.mpr (Ne.symm hr)
  field_simp
  ring

/-- In the SU(2) electric vacuum the two-copy plaquette differences have
second moment two and fourth moment ten. Here d is the first multiplicity. -/
theorem electricRelativeVariance {d : ℝ} (hd : d ≠ 0) :
    (100*d + 6*(d*(d-1)/2)*16)/(4*d)^2 - 1 = 2+13/(4*d) := by
  field_simp
  ring

/-- Positive weights on a regular graph bound its quadratic form and the
constant vector attains that bound. -/
theorem regularGraphTop {ι : Type*} [Fintype ι] (w : ι → ι → ℝ) (v : ι → ℝ) (d : ℝ)
    (pos : ∀ i j, 0 ≤ w i j) (rowSum : ∀ i, ∑ j, w i j = d)
    (colSum : ∀ j, ∑ i, w i j = d) :
    ∑ i, ∑ j, w i j*(v i*v j) ≤ d*∑ i, (v i)^2 := by
  have major : ∀ i j, w i j*(2*(v i*v j)) ≤ w i j*((v i)^2+(v j)^2) :=
    fun i j => mul_le_mul_of_nonneg_left (by nlinarith [sq_nonneg (v i-v j)]) (pos i j)
  have h := Finset.sum_le_sum (s := Finset.univ) (fun i _ =>
    Finset.sum_le_sum (s := Finset.univ) (fun j _ => major i j))
  have rows : ∑ i, ∑ j, w i j*(v i)^2 = d*∑ i, (v i)^2 := by
    simp_rw [← Finset.sum_mul, rowSum, Finset.mul_sum]
  have cols : ∑ i, ∑ j, w i j*(v j)^2 = d*∑ i, (v i)^2 := by
    rw [Finset.sum_comm]
    simp_rw [← Finset.sum_mul, colSum, Finset.mul_sum]
  simp_rw [mul_add, Finset.sum_add_distrib] at h
  have twice : ∀ i j, w i j*(2*(v i*v j)) = 2*(w i j*(v i*v j)) := by
    intros; ring
  simp_rw [twice, ← Finset.mul_sum] at h
  linarith only [h, rows, cols]

theorem resolventTangent {r k m : ℝ} (hk : r ≠ k) (hm : r ≠ m) :
    (r+k)/(r-k) - (r+m)/(r-m) - 2*r*(k-m)/(r-m)^2 =
      2*r*(k-m)^2/((r-k)*(r-m)^2) := by
  have h₁ := sub_ne_zero.mpr hk
  have h₂ := sub_ne_zero.mpr hm
  field_simp
  ring

/-- Vacuum subtraction and the constant mode of the plaquette adjacency. -/
theorem bandCurvature (d degree c g f₂ : ℝ) :
    d*c/4 - ((-c+f₂+(d-1-degree)*c+degree*g)/4 + degree*(g-c)/4)
      = (2*c-f₂-2*degree*(g-c))/4 := by ring

end YangMills.ReplicaGap
#print axioms YangMills.ReplicaGap.exteriorTrace
#print axioms YangMills.ReplicaGap.momentUpper
#print axioms YangMills.ReplicaGap.momentLower
#print axioms YangMills.ReplicaGap.thermalBracket
#print axioms YangMills.ReplicaGap.swapBounds
#print axioms YangMills.ReplicaGap.swapIdentity
#print axioms YangMills.ReplicaGap.swapExpectation
#print axioms YangMills.ReplicaGap.purityMagneticError
#print axioms YangMills.ReplicaGap.vacuumCurvature
#print axioms YangMills.ReplicaGap.electricRelativeVariance
#print axioms YangMills.ReplicaGap.regularGraphTop
#print axioms YangMills.ReplicaGap.resolventTangent
#print axioms YangMills.ReplicaGap.bandCurvature
