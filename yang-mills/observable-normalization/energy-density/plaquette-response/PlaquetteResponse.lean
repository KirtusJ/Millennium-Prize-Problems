import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.PlaquetteResponse

/-- On one excited face each of its four links contributes equally. -/
theorem onePlaquette (a b c d face : ℝ) :
    (3/4*(a+b+c+d))/3-face = (a+b+c+d)/4-face := by ring

/-- Six outer fundamental links and a shared link of Casimir j.
The two input faces each contribute its balanced mean weight. -/
theorem sharedCoefficient {j outer common av : ℝ} (positive : 0 < 9/2+j)
    (balance : 8*av=outer+2*common) :
    2*((3/4*outer+j*common)/(9/2+j)-av) =
      2*(j-3/2)*(common-av)/(9/2+j) := by
  generalize hd : (9/2:ℝ)+j = den at positive ⊢
  field_simp [positive.ne']
  rw [← hd, show outer=8*av-2*common by linarith]
  ring

theorem channelFactors (d : ℝ) :
    2*((0:ℝ)-3/2)*d/(9/2+0) = -2*d/3 ∧
    2*((2:ℝ)-3/2)*d/(9/2+2) = 2*d/13 := by constructor <;> ring

/-- Haar projection on the common link: the retained trace is a quarter
of the normalized outer trace, with squared norm one quarter. -/
theorem haarWeights :
    (1/4:ℝ)^2*(1/4)=1/64 ∧ (1/4:ℝ)^2-1/64=3/64 := by norm_num

theorem channelWeights {h : ℝ} (hh : 0 < h) (d : ℝ) :
    (-2*d/(3*h))^2*(1/64)=d^2/(144*h^2) ∧
    (2*d/(13*h))^2*(3/64)=3*d^2/(2704*h^2) := by
  constructor <;> field_simp <;> ring

theorem firstMoment {k : ℝ} (hk : 0 < k) (S : ℝ) :
    (9*k/2)*S/(144*(3*k)^2)+(13*k/2)*(3*S)/(2704*(3*k)^2)=S/(234*k) := by
  field_simp
  ring

theorem zeroPairSum {ι : Type*} (pairs : Finset ι) (d : ι → ℝ)
    (h : (∑ i ∈ pairs, (d i)^2) = 0) :
    ∀ i ∈ pairs, d i = 0 := by
  intro i hi
  have hp := Finset.single_le_sum (f := fun j => (d j)^2)
    (fun j _ => sq_nonneg (d j)) hi
  rw [h] at hp
  exact sq_eq_zero_iff.mp (le_antisymm hp (sq_nonneg _))

/-- Three distinct incident faces are sufficient to identify their common weight. -/
theorem recoverIncident {w a b c : ℝ} (h₁ : 2*w=a+b)
    (h₂ : 2*w=a+c) (h₃ : 2*w=b+c) : a=w ∧ b=w ∧ c=w := by
  exact ⟨by linarith, by linarith, by linarith⟩

theorem constantOnConnectedLinks {ι : Type*} (edge : ι → ι → Prop) (w : ι → ℝ)
    (connected : ∀ i j, Relation.ReflTransGen edge i j)
    (locallyEqual : ∀ i j, edge i j → w i = w j) (i j : ι) : w i = w j := by
  induction connected i j with
  | refl => rfl
  | tail _ step prev => exact prev.trans (locallyEqual _ _ step)

/-- Contributions at a lattice edge from four perpendicular pairs of faces
for an affine spatial test, using mesh spacing b. -/
theorem affineEdge (b g h : ℝ) :
    (b*(g+h)/4)^2+(b*(g-h)/4)^2+(b*(-g+h)/4)^2+(b*(-g-h)/4)^2 =
      b^2*(g^2+h^2)/4 := by ring

theorem affineCell (b x y z : ℝ) :
    b^2*(y^2+z^2)/4+b^2*(x^2+z^2)/4+b^2*(x^2+y^2)/4 =
      b^2*(x^2+y^2+z^2)/2 := by ring

/-- The six unordered pairs among four incident faces give the incidence
energy and the square of its residual, with exact coefficients. -/
theorem incidentSquare (a b c d : ℝ) :
    ((a+b)/2)^2+((a+c)/2)^2+((a+d)/2)^2+
    ((b+c)/2)^2+((b+d)/2)^2+((c+d)/2)^2 =
    (a^2+b^2+c^2+d^2)/2+(a+b+c+d)^2/4 := by ring

/-- An averaged face contributes its deviation about the link mean. -/
theorem faceVariance (a b c d : ℝ) :
    let m := (a+b+c+d)/4
    (a-m)^2+(b-m)^2+(c-m)^2+(d-m)^2 = a^2+b^2+c^2+d^2-4*m^2 := by
  dsimp
  ring

theorem quadraticIncreasing {x y : ℝ} (h₀ : 0 ≤ x) (h : x ≤ y) :
    x/2+x^2/4 ≤ y/2+y^2/4 := by
  nlinarith [sq_nonneg (y-x), mul_nonneg h₀ (sub_nonneg.mpr h)]

/-- Characteristic polynomial of the symmetric sector on an axial mode. -/
theorem axialRoot {s r : ℝ} (hr : r^2=s^2+8) :
    let m := 2+(s^2+s*r)/2
    (m-2)*(m-(2+s^2))=2*s^2 := by
  dsimp
  nlinarith only [show s^2*r^2=s^2*(s^2+8) by rw [hr]]

/-- Positivity on the two orthogonal output ranges gives a uniform lower
bound for a nearby map, after scaling the input columns. -/
theorem stableIndependent {V H : Type*} [NormedAddCommGroup V] [NormedAddCommGroup H]
    (T T₀ : V → H) {c err : ℝ} (he : err < c)
    (lower : ∀ v, c*‖v‖ ≤ ‖T₀ v‖)
    (close : ∀ v, ‖T₀ v-T v‖ ≤ err*‖v‖) {v : V} (hv : T v=0) : v=0 := by
  have h := close v
  rw [hv,sub_zero] at h
  have hb := (lower v).trans h
  by_contra hn
  exact (not_lt_of_ge hb) (mul_lt_mul_of_pos_right he (norm_pos_iff.mpr hn))

end YangMills.PlaquetteResponse
#print axioms YangMills.PlaquetteResponse.onePlaquette
#print axioms YangMills.PlaquetteResponse.sharedCoefficient
#print axioms YangMills.PlaquetteResponse.channelFactors
#print axioms YangMills.PlaquetteResponse.haarWeights
#print axioms YangMills.PlaquetteResponse.channelWeights
#print axioms YangMills.PlaquetteResponse.firstMoment
#print axioms YangMills.PlaquetteResponse.zeroPairSum
#print axioms YangMills.PlaquetteResponse.recoverIncident
#print axioms YangMills.PlaquetteResponse.constantOnConnectedLinks
#print axioms YangMills.PlaquetteResponse.affineEdge
#print axioms YangMills.PlaquetteResponse.affineCell
#print axioms YangMills.PlaquetteResponse.stableIndependent
#print axioms YangMills.PlaquetteResponse.incidentSquare
#print axioms YangMills.PlaquetteResponse.faceVariance
#print axioms YangMills.PlaquetteResponse.quadraticIncreasing
#print axioms YangMills.PlaquetteResponse.axialRoot
