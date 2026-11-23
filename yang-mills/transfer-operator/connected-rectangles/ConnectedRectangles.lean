import Mathlib.Topology.MetricSpace.Pseudo.Basic
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.ConnectedRectangles
open MeasureTheory
noncomputable section

/-- The unfixed leaf gauge can absorb both spatial boundary matrices. -/
theorem leaf {G : Type*} [Group G] [MeasurableSpace G] [MeasurableMul G]
    (μ : Measure G) [μ.IsMulLeftInvariant] [μ.IsMulRightInvariant]
    (f : G → ℝ) (a b : G) :
    (∫ g, f (a*g*b) ∂μ) = ∫ g, f g ∂μ := by
  calc
    _ = ∫ g, f (g*b) ∂μ := integral_mul_left_eq_self (μ := μ) (fun g => f (g*b)) a
    _ = _ := integral_mul_right_eq_self (μ := μ) f b

theorem productCut (a b la lb : ℝ) (ha : a ≠ 0) (hb : b ≠ 0) :
    la*lb/(a*b)-(la*b/(a*b))*(a*lb/(a*b))=0 := by field_simp; ring

theorem affineFloor (x l u s t d : ℝ) (hl : l ≤ x) (hu : x ≤ u)
    (left : d ≤ s*l+t) (right : d ≤ s*u+t) : d ≤ s*x+t := by
  by_cases h : 0 ≤ s
  · nlinarith [mul_nonneg h (sub_nonneg.mpr hl)]
  · nlinarith [mul_nonpos_of_nonpos_of_nonneg (le_of_not_ge h) (sub_nonneg.mpr hu)]

def cost (n m k a b : ℝ) : ℝ := 2*(n*m-a*b)+2*k*(a+b)

-- PCP begin geometry
/-- Every nonempty section costs at least the smaller of the full walls and the unit tube. -/
theorem rectangleFloor {a b n m k : ℝ} (ha : 1 ≤ a) (han : a ≤ n)
    (hb : 1 ≤ b) (hbm : b ≤ m) (hk : 1 ≤ k) :
    min (cost n m k 1 1) (cost n m k n m) ≤ cost n m k a b := by
  let d := min (cost n m k 1 1) (cost n m k n m)
  have h₁ : d ≤ cost n m k 1 1 := min_le_left _ _
  have h₂ : d ≤ cost n m k n m := min_le_right _ _
  have along (y : ℝ) (left : d ≤ cost n m k 1 y) (right : d ≤ cost n m k n y) :
      d ≤ cost n m k a y := by
    unfold cost at *
    apply affineFloor a 1 n (2*k-2*y) (2*n*m+2*k*y) d ha han (by linarith) (by linarith) |>.trans
    linarith
  have across (x : ℝ) (left : d ≤ cost n m k x 1) (right : d ≤ cost n m k x m) :
      d ≤ cost n m k x b := by
    unfold cost at *
    apply affineFloor b 1 m (2*k-2*x) (2*n*m+2*k*x) d hb hbm (by linarith) (by linarith) |>.trans
    linarith
  have h₃ : cost n m k 1 1 ≤ cost n m k 1 m := by
    unfold cost
    nlinarith [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr (hb.trans hbm))]
  have h₄ : cost n m k 1 1 ≤ cost n m k n 1 := by
    unfold cost
    nlinarith [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr (ha.trans han))]
  exact across a (along 1 h₁ (h₁.trans h₄)) (along m (h₁.trans h₃) h₂)
-- PCP end geometry

theorem nonemptySection {a b n m k z h v : ℝ} (ha : 1 ≤ a) (han : a ≤ n)
    (hb : 1 ≤ b) (hbm : b ≤ m) (hk : 1 ≤ k) (area : z ≤ a*b)
    (horizontal : 2*(n*m-z) ≤ h) (vertical : 2*k*(a+b) ≤ v) :
    min (cost n m k 1 1) (cost n m k n m) ≤ h+v := by
  apply (rectangleFloor ha han hb hbm hk).trans
  unfold cost
  linarith

/-- In each occupied line, a maximal element exposes a face in the increasing direction. -/
theorem exposedLines {α : Type*} [DecidableEq α] (s : Finset α)
    (line height : α → ℤ) (step : α → α) (fixedLine : ∀ x, line (step x) = line x)
    (increasing : ∀ x, height x < height (step x)) :
    (s.image line).card ≤ (s.filter (fun x => step x ∉ s)).card := by
  classical
  have cover : s.image line ⊆ (s.filter (fun x => step x ∉ s)).image line := by
    intro y hy
    obtain ⟨z, hz, hzy⟩ := Finset.mem_image.mp hy
    let t := s.filter (fun x => line x = y)
    have ht : t.Nonempty := ⟨z, Finset.mem_filter.mpr ⟨hz,hzy⟩⟩
    obtain ⟨x,hx,highest⟩ := t.exists_max_image height ht
    obtain ⟨inside,same⟩ := Finset.mem_filter.mp hx
    have outside : step x ∉ s := by
      intro bad
      have hit : step x ∈ t := Finset.mem_filter.mpr ⟨bad,(fixedLine x).trans same⟩
      exact (not_lt_of_ge (highest _ hit)) (increasing x)
    exact Finset.mem_image.mpr ⟨x,Finset.mem_filter.mpr ⟨inside,outside⟩,same⟩
  exact (Finset.card_le_card cover).trans Finset.card_image_le

def perimeter (s : Finset (ℤ × ℤ)) : ℕ :=
  (s.filter (fun x => (x.1+1,x.2) ∉ s)).card + (s.filter (fun x => (x.1-1,x.2) ∉ s)).card +
  (s.filter (fun x => (x.1,x.2+1) ∉ s)).card + (s.filter (fun x => (x.1,x.2-1) ∉ s)).card

theorem projectedPerimeter (s : Finset (ℤ × ℤ)) :
    2*((s.image Prod.fst).card+(s.image Prod.snd).card) ≤ perimeter s := by
  have east := exposedLines s Prod.snd Prod.fst (fun x => (x.1+1,x.2)) (fun _ => rfl) (by intro x; simp)
  have west := exposedLines s Prod.snd (fun x => -x.1) (fun x => (x.1-1,x.2)) (fun _ => rfl)
    (by intro x; dsimp; omega)
  have north := exposedLines s Prod.fst Prod.snd (fun x => (x.1,x.2+1)) (fun _ => rfl) (by intro x; simp)
  have south := exposedLines s Prod.fst (fun x => -x.2) (fun x => (x.1,x.2-1)) (fun _ => rfl)
    (by intro x; dsimp; omega)
  calc
    _ = (s.image Prod.snd).card+(s.image Prod.snd).card+(s.image Prod.fst).card+
          (s.image Prod.fst).card := by omega
    _ ≤ _ := Nat.add_le_add (Nat.add_le_add (Nat.add_le_add east west) north) south

theorem projectedArea (s : Finset (ℤ × ℤ)) :
    s.card ≤ (s.image Prod.fst).card*(s.image Prod.snd).card := by
  rw [← Finset.card_product]
  apply Finset.card_le_card
  intro x hx
  exact Finset.mem_product.mpr ⟨Finset.mem_image_of_mem _ hx, Finset.mem_image_of_mem _ hx⟩

/-- The connected section bound for the actual edge boundary of a finite cell set. -/
theorem planarSection (s : Finset (ℤ × ℤ)) (hs : s.Nonempty) (n m k : ℝ)
    (cols : ((s.image Prod.fst).card : ℝ) ≤ n) (rows : ((s.image Prod.snd).card : ℝ) ≤ m)
    (hk : 1 ≤ k) :
    min (cost n m k 1 1) (cost n m k n m) ≤ 2*(n*m-s.card)+k*perimeter s := by
  have one (p : ℤ × ℤ → ℤ) : (1:ℝ) ≤ (s.image p).card := by
    exact_mod_cast (Finset.card_pos.mpr (hs.image p))
  have ar : (s.card:ℝ) ≤ ((s.image Prod.fst).card:ℝ)*(s.image Prod.snd).card := by
    exact_mod_cast projectedArea s
  have pe : 2*(((s.image Prod.fst).card:ℝ)+(s.image Prod.snd).card) ≤ perimeter s := by
    exact_mod_cast projectedPerimeter s
  apply nonemptySection (one Prod.fst) cols (one Prod.snd) rows hk ar le_rfl
  nlinarith [mul_nonneg (by linarith : 0 ≤ k) (sub_nonneg.mpr pe)]

theorem emptySection (n m k h v : ℝ) (horizontal : 2*n*m ≤ h)
    (vertical : 4*k ≤ v) : cost n m k 1 1 < h+v := by unfold cost; linarith

/-- A closed sequence pays for both horizontal excursions to an arbitrary slice. -/
theorem returnCost {X : Type*} [PseudoMetricSpace X] (s : ℕ → X) {j k : ℕ}
    (hj : j ≤ k) (back : s k = s 0) :
    2*dist (s 0) (s j) ≤ ∑ i ∈ Finset.range k, dist (s i) (s (i+1)) := by
  have a := dist_le_range_sum_dist s j
  have b := dist_le_Ico_sum_dist s hj
  rw [back, dist_comm (s j) (s 0)] at b
  have c := Finset.sum_range_add_sum_Ico (fun i => dist (s i) (s (i+1))) hj
  linarith

/-- Minimize the true cut cost, allowing projected-empty cuts to retain their
four-face lower bound. No projected slice is assumed to be a rectangle. -/
theorem slicedFloor {X : Type*} [PseudoMetricSpace X] (s : ℕ → X) (v : ℕ → ℝ)
    {k : ℕ} (hk : 0 < k) (back : s (k+1) = s 0) {d : ℝ}
    (h : ∀ i ∈ Finset.range k, d ≤ 2*dist (s 0) (s (i+1)) + k*v i) :
    d ≤ (∑ i ∈ Finset.range (k+1), dist (s i) (s (i+1))) + ∑ i ∈ Finset.range k, v i := by
  obtain ⟨j, hj, least⟩ := Finset.exists_min_image (Finset.range k) v ⟨0, Finset.mem_range.mpr hk⟩
  have horiz := returnCost s (Nat.succ_le_succ (Nat.le_of_lt (Finset.mem_range.mp hj))) back
  have vert := Finset.sum_le_sum least
  simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at vert
  exact (h j hj).trans (add_le_add horiz vert)

theorem socketMultiplicity (a z : ℝ) : z + a*z = (a+1)*z := by ring

theorem crossoverShift (A P : ℝ) (hp : 4 < P) (rect : 16*A ≤ P^2) :
    (2*A-2)/(P-4)-2*A/P ≤ 1/2 := by
  have hP : 0 < P := by linarith
  have h : 0 < P-4 := by linarith
  rw [div_sub_div _ _ (ne_of_gt h) (ne_of_gt hP)]
  apply (div_le_iff₀ (mul_pos h hP)).mpr
  nlinarith

-- PCP begin certificate
theorem polymerBudget : (2:ℝ)*21/(256-80)<1 := by norm_num
-- PCP end certificate

theorem pinnedBudget (u : ℝ) (hu : u ≤ 1/256) :
    2*21*u ≤ 1-80*u := by linarith

/-- The induction step in the zero-free polymer ratio bound. -/
theorem deletionRatio (q : ℂ) {u : ℝ} (hq : ‖q‖ ≤ u) (hu : u ≤ 1/2) :
    1+q ≠ 0 ∧ ‖(1+q)⁻¹‖ ≤ Real.exp (2*u) := by
  have triangle : (1:ℝ) ≤ ‖1+q‖+‖q‖ := by
    have ht := norm_sub_le (1+q) q
    simpa using ht
  have hnorm : 0 < ‖1+q‖ := by linarith
  have h₁ : 0 ≤ u := (norm_nonneg q).trans hq
  refine ⟨norm_pos_iff.mp hnorm, ?_⟩
  rw [norm_inv]
  apply le_trans _ (Real.add_one_le_exp (2*u))
  rw [inv_eq_one_div, div_le_iff₀ hnorm]
  nlinarith [mul_nonneg h₁ (show 0 ≤ 1-2*u by linarith),
    mul_nonneg (show 0 ≤ 2*u+1 by linarith) (show 0 ≤ ‖1+q‖-(1-u) by linarith)]

theorem branchOdds (A s : ℝ) (ha : 0 < A) :
    Real.exp (-(s-Real.log A))/A = Real.exp (-s) := by
  rw [neg_sub, Real.exp_sub, Real.exp_log ha, Real.exp_neg]
  field_simp
  ring

theorem mixedPathFloor {X : Type*} [PseudoMetricSpace X] (s : ℕ → X) (k : ℕ) (v : ℕ → ℝ)
    (cuts : ∀ i ∈ Finset.range k, 4 ≤ v i) :
    dist (s 0) (s (k+1)) + 4*k ≤
    (∑ i ∈ Finset.range (k+1), dist (s i) (s (i+1))) + ∑ i ∈ Finset.range k, v i := by
  apply add_le_add (dist_le_range_sum_dist s (k+1))
  simpa [mul_comm] using Finset.sum_le_sum cuts

/-- Squared overlap after summing the mutually orthogonal unit-cell directions. -/
theorem collectiveOverlap (a b c : ℝ) (ha : a ≠ 0) (hc : c ≠ 0) :
    (a*b*c)^2/(a*c)=a*b^2*c := by field_simp; ring

theorem perimeterResidual (a b c d : ℝ) :
    (d+a*b^2*c)-2*b*(a*b*c)+b^2*(a*c)=d := by ring

theorem centeredMoment {α : Type*} [MeasurableSpace α] (μ : Measure α) (x : α → ℝ)
    (h₀ : Integrable (fun _ : α => (1:ℝ)) μ) (h₁ : Integrable x μ)
    (h₂ : Integrable (fun i => (x i)^2) μ) :
    (∫ i, (x i-1)^2 ∂μ) =
      (∫ i, (x i)^2 ∂μ)-2*(∫ i, x i ∂μ)+(∫ _ : α, (1:ℝ) ∂μ) := by
  simp_rw [show ∀ i, (x i-1)^2=(x i)^2-2*x i+1 by intro i; ring]
  have hs : Integrable (fun i => (x i)^2-2*x i) μ := h₂.sub (h₁.const_mul 2)
  rw [integral_add hs h₀, integral_sub h₂ (h₁.const_mul 2), integral_const_mul]

/-- Three readings also bound the squared relative error in a nominated transfer value. -/
theorem concentrationBudget (m₀ m₁ m₂ ε : ℝ) (h₀ : |m₀-1| ≤ ε)
    (h₁ : |m₁-1| ≤ ε) (h₂ : |m₂-1| ≤ ε) : m₂-2*m₁+m₀ ≤ 4*ε := by
  have a := abs_le.mp h₀
  have b := abs_le.mp h₁
  have c := abs_le.mp h₂
  linarith

theorem commonSpacing (m σ b : ℝ) (hb : b ≠ 0) (hs : σ ≠ 0) :
    (m/b)^2/(σ/b^2)=m^2/σ := by field_simp

theorem scaleError (g L e d : ℝ) (h : L+d ≠ 0) :
    (g*L+e)^2/(L+d)-g^2*L=((2*g*e-g^2*d)*L+e^2)/(L+d) := by
  field_simp
  ring

theorem vacuumTie (w h : ℝ) (p : 0 < h) (hw : w=4*h) :
    w/(w+h)=4/5 ∧ h/(w+h)=1/5 := by
  subst w
  constructor <;> field_simp <;> ring

end
end Millennium.YangMills.ConnectedRectangles

#print axioms Millennium.YangMills.ConnectedRectangles.leaf
#print axioms Millennium.YangMills.ConnectedRectangles.productCut
#print axioms Millennium.YangMills.ConnectedRectangles.affineFloor
#print axioms Millennium.YangMills.ConnectedRectangles.rectangleFloor
#print axioms Millennium.YangMills.ConnectedRectangles.nonemptySection
#print axioms Millennium.YangMills.ConnectedRectangles.emptySection
#print axioms Millennium.YangMills.ConnectedRectangles.socketMultiplicity
#print axioms Millennium.YangMills.ConnectedRectangles.crossoverShift
#print axioms Millennium.YangMills.ConnectedRectangles.polymerBudget
#print axioms Millennium.YangMills.ConnectedRectangles.pinnedBudget
#print axioms Millennium.YangMills.ConnectedRectangles.centeredMoment
#print axioms Millennium.YangMills.ConnectedRectangles.concentrationBudget
#print axioms Millennium.YangMills.ConnectedRectangles.vacuumTie

#print axioms Millennium.YangMills.ConnectedRectangles.returnCost
#print axioms Millennium.YangMills.ConnectedRectangles.slicedFloor

#print axioms Millennium.YangMills.ConnectedRectangles.deletionRatio
#print axioms Millennium.YangMills.ConnectedRectangles.branchOdds

#print axioms Millennium.YangMills.ConnectedRectangles.mixedPathFloor
#print axioms Millennium.YangMills.ConnectedRectangles.collectiveOverlap
#print axioms Millennium.YangMills.ConnectedRectangles.perimeterResidual

#print axioms Millennium.YangMills.ConnectedRectangles.commonSpacing
#print axioms Millennium.YangMills.ConnectedRectangles.scaleError

#print axioms Millennium.YangMills.ConnectedRectangles.exposedLines
#print axioms Millennium.YangMills.ConnectedRectangles.projectedPerimeter
#print axioms Millennium.YangMills.ConnectedRectangles.projectedArea
#print axioms Millennium.YangMills.ConnectedRectangles.planarSection
