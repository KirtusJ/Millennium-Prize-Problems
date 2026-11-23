import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Data.Finsupp.Basic
import Mathlib.Order.Filter.Finite
import Mathlib.Tactic.Linarith

noncomputable section
open Filter
open scoped BigOperators Topology

namespace Millennium.G4.FixedBlocks

variable {G H : Type*} [AddCommGroup G] [NormedAddCommGroup H] [NormedSpace ℝ H]

def weightMass (w : G →₀ ℝ) : ℝ := w.sum (fun _ t => |t|)

def reading (w : G →₀ ℝ) (X : G → H) : H := w.sum (fun x t => t • X x)

def translate (u : G) (w : G →₀ ℝ) : G →₀ ℝ := w.mapDomain (fun x => x+u)

theorem reading_translate (u : G) (w : G →₀ ℝ) (X : G → H) :
    reading (translate u w) X = reading w (fun x => X (x+u)) := by
  exact Finsupp.sum_mapDomain_index (fun _ => zero_smul ℝ _)
    (fun _ _ _ => add_smul _ _ _)

theorem reading_sub (w v : G →₀ ℝ) (X : G → H) :
    reading (w-v) X = reading w X - reading v X := by
  exact Finsupp.sum_sub_index (fun _ _ _ => sub_smul _ _ _)

theorem reading_bound (w : G →₀ ℝ) (X : G → H) (B : ℝ) (hB : ∀ x, ‖X x‖ ≤ B) :
    ‖reading w X‖ ≤ weightMass w * B := by
  classical
  unfold reading weightMass Finsupp.sum
  rw [Finset.sum_mul]
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro x _
  rw [norm_smul, Real.norm_eq_abs]
  exact mul_le_mul_of_nonneg_left (hB x) (abs_nonneg _)

def block (T : Finset G) (a : G → ℝ) (X : G → H) (x : G) : H :=
  ∑ u ∈ T, a u • X (x+u)

theorem reading_block (T : Finset G) (a : G → ℝ) (w : G →₀ ℝ) (X : G → H) :
    reading w (block T a X) = ∑ u ∈ T, a u • reading (translate u w) X := by
  classical
  simp_rw [reading_translate]
  simp only [reading, Finsupp.sum, block, Finset.smul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun x _ => smul_comm _ _ _

-- NATIVE CHILD 1

theorem reading_decomposition (T : Finset G) (a : G → ℝ) (ha : ∑ u ∈ T, a u = 1)
    (w : G →₀ ℝ) (X : G → H) :
    reading w X =
      (∑ u ∈ T, a u • reading (w - translate u w) X) + reading w (block T a X) := by
  rw [reading_block, ← Finset.sum_add_distrib]
  simp_rw [reading_sub, smul_sub, sub_add_cancel]
  rw [← Finset.sum_smul, ha, one_smul]

/-- A finite block and the variation of the translated deterministic weights control the reading. -/
theorem fixed_block_bound (T : Finset G) (a : G → ℝ)
    (ha : ∑ u ∈ T, a u = 1) (ha₀ : ∀ u ∈ T, 0 ≤ a u)
    (w : G →₀ ℝ) (X : G → H) (A B δ η : ℝ)
    (hB₀ : 0 ≤ B) (hη₀ : 0 ≤ η) (hw : weightMass w ≤ A)
    (hX : ∀ x, ‖X x‖ ≤ B) (hδ : ∀ u ∈ T, weightMass (w - translate u w) ≤ δ)
    (hη : ∀ x, ‖block T a X x‖ ≤ η) :
    ‖reading w X‖ ≤ δ*B + A*η := by
  have herr : ‖∑ u ∈ T, a u • reading (w - translate u w) X‖ ≤ δ*B := by
    calc
      _ ≤ ∑ u ∈ T, ‖a u • reading (w - translate u w) X‖ := norm_sum_le _ _
      _ ≤ ∑ u ∈ T, a u * (δ*B) := by
        apply Finset.sum_le_sum
        intro u hu
        rw [norm_smul, Real.norm_eq_abs, abs_of_nonneg (ha₀ u hu)]
        exact mul_le_mul_of_nonneg_left ((reading_bound _ X B hX).trans
          (mul_le_mul_of_nonneg_right (hδ u hu) hB₀)) (ha₀ u hu)
      _ = δ*B := by rw [← Finset.sum_mul, ha, one_mul]
  rw [reading_decomposition T a ha w X]
  exact (norm_add_le _ _).trans (add_le_add herr
    ((reading_bound _ _ η hη).trans (mul_le_mul_of_nonneg_right hw hη₀)))

-- NATIVE CHILD 2

/-- The normed spaces may change with the regulator. Only the admissible shifts
in the single finite block chosen for each accuracy enter the eventual estimate. -/
theorem concentration_of_fixed_blocks
    {E : ℕ → Type*} [∀ n, NormedAddCommGroup (E n)] [∀ n, NormedSpace ℝ (E n)]
    (w : ℕ → G →₀ ℝ) (X : (n : ℕ) → G → E n) (allowed : Set G)
    (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hw : ∀ n, weightMass (w n) ≤ A) (hX : ∀ n x, ‖X n x‖ ≤ B)
    (hs : ∀ u ∈ allowed, ∀ δ : ℝ, 0 < δ →
      ∀ᶠ n in atTop, weightMass (w n - translate u (w n)) ≤ δ)
    (hb : ∀ δ : ℝ, 0 < δ → ∃ (T : Finset G) (a : G → ℝ),
      (∀ u ∈ T, u ∈ allowed) ∧ (∑ u ∈ T, a u = 1) ∧ (∀ u ∈ T, 0 ≤ a u) ∧
      ∀ᶠ n in atTop, ∀ x, ‖block T a (X n) x‖ ≤ δ) :
    Tendsto (fun n => ‖reading (w n) (X n)‖) atTop (𝓝 0) := by
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  let δ := ε/(A+B+1)
  have hd : 0 < A+B+1 := by linarith
  have hδ : 0 < δ := div_pos hε hd
  obtain ⟨T,a,hT,ha,ha₀,he⟩ := hb δ hδ
  have hall := (Filter.eventually_all_finset T).2 (fun u hu => hs u (hT u hu) δ hδ)
  filter_upwards [he,hall] with n hblock htrans
  have h := fixed_block_bound T a ha ha₀ (w n) (X n) A B δ δ hB hδ.le
    (hw n) (hX n) htrans hblock
  rw [Real.dist_eq, sub_zero, abs_of_nonneg (norm_nonneg _)]
  have heq : δ*(A+B+1) = ε := div_mul_cancel₀ _ (ne_of_gt hd)
  nlinarith

/-- A summable stationary covariance gives the row bound with a constant
independent of the finite set. This implication also allows signed entries. -/
theorem squared_mean_of_row_bound {ι V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    (T : Finset ι) (hT : T.Nonempty) (v : ι → V) (C : ℝ)
    (hrow : ∀ i ∈ T, ∑ j ∈ T, |@inner ℝ V _ (v i) (v j)| ≤ C) :
    ‖(T.card : ℝ)⁻¹ • ∑ i ∈ T, v i‖^2 ≤ C / T.card := by
  have hN : (0 : ℝ) < T.card := by exact_mod_cast Finset.card_pos.mpr hT
  have hs : ‖∑ i ∈ T, v i‖^2 ≤ (T.card : ℝ)*C := by
    rw [← real_inner_self_eq_norm_sq, sum_inner]
    simp_rw [inner_sum]
    calc
      _ ≤ ∑ _i ∈ T, C := by
        apply Finset.sum_le_sum
        intro i hi
        exact (Finset.sum_le_sum (fun j _ => le_abs_self _)).trans (hrow i hi)
      _ = _ := by simp
  rw [norm_smul, Real.norm_eq_abs, abs_of_nonneg (inv_nonneg.mpr hN.le), mul_pow]
  calc
    _ ≤ ((T.card : ℝ)⁻¹)^2 * ((T.card : ℝ)*C) :=
      mul_le_mul_of_nonneg_left hs (sq_nonneg _)
    _ = _ := by field_simp; ring

#print axioms weightMass
#print axioms reading
#print axioms translate
#print axioms reading_translate
#print axioms reading_sub
#print axioms reading_bound
#print axioms block
#print axioms reading_block
#print axioms reading_decomposition
#print axioms fixed_block_bound
#print axioms concentration_of_fixed_blocks
#print axioms squared_mean_of_row_bound

end Millennium.G4.FixedBlocks
