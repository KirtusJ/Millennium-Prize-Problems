import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Basis.VectorSpace

import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open MeasureTheory Set
open Matrix
open scoped Matrix ComplexOrder

namespace Millennium.YangMills.D4.FiniteReadings
/-- A map killing the null directions of a Gram operator factors through it. -/
theorem factorGram {X Y Z : Type*} [AddCommGroup X] [Module ℂ X] [AddCommGroup Y]
    [Module ℂ Y] [AddCommGroup Z] [Module ℂ Z] (h : X →ₗ[ℂ] Y) (k : X →ₗ[ℂ] Z)
    (kernel : LinearMap.ker h ≤ LinearMap.ker k) : ∃ s : Y →ₗ[ℂ] Z, s.comp h = k := by
  obtain ⟨sectionMap, rightInv⟩ := h.rangeRestrict.exists_rightInverse_of_surjective h.range_rangeRestrict
  obtain ⟨s, extended⟩ := (k.comp sectionMap).exists_extend
  refine ⟨s, ?_⟩
  ext x
  have inside : h (sectionMap (h.rangeRestrict x)) = h x :=
    congrArg Subtype.val (LinearMap.congr_fun rightInv (h.rangeRestrict x))
  have zero : sectionMap (h.rangeRestrict x) - x ∈ LinearMap.ker h := by
    rw [LinearMap.mem_ker, map_sub, inside, sub_self]
  have descend := LinearMap.mem_ker.mp (kernel zero)
  rw [map_sub, sub_eq_zero] at descend
  exact (LinearMap.congr_fun extended (h.rangeRestrict x)).trans descend

/-- Construct a Gram-selfadjoint representative of the shifted Hankel form,
also when the original Hermitian Gram matrix is singular. -/
theorem gramTransfer {I : Type*} [Fintype I] [DecidableEq I] (H K : Matrix I I ℂ)
    (q : ℂ) (hermitian : H.IsHermitian) (lower : K.PosSemidef)
    (upper : (q • H - K).PosSemidef) :
    ∃ T : Matrix I I ℂ, H*T = K ∧ Tᴴ*H = K := by
  have kernel : LinearMap.ker H.toLin' ≤ LinearMap.ker K.toLin' := by
    intro v hv
    change H *ᵥ v = 0 at hv
    change K *ᵥ v = 0
    apply (lower.dotProduct_mulVec_zero_iff v).mp
    have neg := upper.2 v
    simp only [sub_mulVec, smul_mulVec_assoc, hv, smul_zero, zero_sub, dotProduct_neg, neg_nonneg] at neg
    exact le_antisymm neg (lower.2 v)
  obtain ⟨s, hs⟩ := factorGram H.toLin' K.toLin' kernel
  let A := LinearMap.toMatrix' s
  have eq : A*H = K := by
    apply Matrix.toLin'.injective
    rw [Matrix.toLin'_mul]
    simpa [A] using hs
  have adj := congrArg Matrix.conjTranspose eq
  rw [conjTranspose_mul, hermitian.eq, lower.1.eq] at adj
  exact ⟨Aᴴ, adj, by simpa using eq⟩


/-- Vacuum-independent polynomial testing for the open slow-transfer interval. -/
theorem openWindow (u q : ℝ) (hq : q < 1) :
    (u-q)*(1-u) ≤ (Ioo q 1).indicator (fun _ => (1-q)^2/4) u := by
  by_cases inside : u ∈ Ioo q 1
  · rw [indicator_of_mem inside]
    nlinarith only [sq_nonneg (2*u-1-q)]
  · rw [indicator_of_not_mem inside]
    rcases le_total u q with h | h
    · exact mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr h) (sub_nonneg.mpr (h.trans hq.le))
    · by_cases eq : q = u
      · simp [eq]
      · have one : 1 ≤ u := le_of_not_gt (fun hu => inside ⟨lt_of_le_of_ne h eq,hu⟩)
        exact mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.mpr h) (sub_nonpos.mpr one)

/-- Integrate the quadratic in a measured probe state; both endpoints have zero weight
in this test. No prior information about the vacuum atom is required. -/
theorem softMass (μ : Measure ℝ) [IsFiniteMeasure μ] (q : ℝ) (hq : q < 1)
    (h : Integrable (fun u : ℝ => (u-q)*(1-u)) μ) :
    (∫ u : ℝ, (u-q)*(1-u) ∂μ) ≤ ((1-q)^2/4)*μ.real (Ioo q 1) := by
  have hind := (integrable_const ((1-q)^2/4) (μ := μ)).indicator (measurableSet_Ioo (a := q) (b := 1))
  have bound := integral_mono h hind (fun u => openWindow u q hq)
  rw [integral_indicator_const _ measurableSet_Ioo] at bound
  simpa only [smul_eq_mul, mul_comm (μ.real (Ioo q 1)) _] using bound

theorem quadraticReadings (u q : ℝ) : (u-q)*(1-u) = -u^2+(1+q)*u-q := by ring

/-- From the three measured correlations, propagate absolute error into the detector. -/
theorem threeReadingError (a b c q ε : ℝ) (hq : 0 ≤ q)
    (ha : |a| ≤ ε) (hb : |b| ≤ ε) (hc : |c| ≤ ε) :
    |(-c+(1+q)*b-q*a)| ≤ 2*(1+q)*ε := by
  rw [abs_le] at ha hb hc ⊢
  have qa := mul_le_mul_of_nonneg_left ha.1 hq
  have qb := mul_le_mul_of_nonneg_left ha.2 hq
  have bc := mul_le_mul_of_nonneg_left hb.1 (show 0 ≤ 1+q by linarith)
  have bd := mul_le_mul_of_nonneg_left hb.2 (show 0 ≤ 1+q by linarith)
  constructor <;> linarith

/-- Equality of the first entry and all forward differences reconstructs every entry. -/
theorem recoverDifferences {X : Type*} [AddCommGroup X] {n : ℕ} (source model : ℕ → X)
    (zero : source 0 = model 0)
    (diff : ∀ j < n, source j - source (j+1) = model j - model (j+1)) :
    ∀ j ≤ n, source j = model j := by
  intro j hj
  induction j with
  | zero => exact zero
  | succ j ih =>
    have prev := ih (Nat.le_of_succ_le hj)
    have h := diff j hj
    rwa [prev, sub_right_inj] at h

/-- Selfadjointness moves powers between the two polynomial factors. -/
theorem shiftPowers {X Y : Type*} (T : X → X) (B : X → X → Y)
    (symm : ∀ x y, B (T x) y = B x (T y)) (x y : X) (i j : ℕ) :
    B (T^[i] x) (T^[j] y) = B x (T^[i+j] y) := by
  induction i generalizing j with
  | zero => simp
  | succ i ih =>
    rw [Function.iterate_succ_apply', symm, ← Function.iterate_succ_apply' T j y, ih]
    rw [show i+(j+1) = (i+1)+j by omega]

/-- The Hankel construction shifts the represented lower-degree monomials exactly. -/
theorem polynomialChain {X : Type*} (T : X → X) (s : ℕ → X) (r : ℕ)
    (shift : ∀ j < r, T (s j) = s (j+1)) : ∀ j ≤ r, T^[j] (s 0) = s j := by
  intro j hj
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [Function.iterate_succ_apply', ih (Nat.le_of_succ_le hj), shift j hj]

/-- For arbitrary polarizations and any degree, compression and the first shifted
Hankel form reproduce all odd-truncation moments, including the last one. -/
theorem oddMomentRecovery {X Y I : Type*} (T : X → X) (B : X → X → Y)
    (s : ℕ → I → X) (moment : ℕ → I → I → Y) (r : ℕ)
    (symm : ∀ x y, B (T x) y = B x (T y))
    (shift : ∀ j < r, ∀ a, T (s j a) = s (j+1) a)
    (hankel : ∀ i ≤ r, ∀ j ≤ r, ∀ a b, B (s i a) (s j b) = moment (i+j) a b)
    (next : ∀ a b, B (s r a) (T (s r b)) = moment (2*r+1) a b) :
    ∀ n ≤ 2*r+1, ∀ a b, B (s 0 a) (T^[n] (s 0 b)) = moment n a b := by
  intro n hn a b
  have pw (k : ℕ) (hk : k ≤ r) (c : I) : T^[k] (s 0 c) = s k c :=
    polynomialChain T (fun j => s j c) r (fun j hj => shift j hj c) k hk
  by_cases last : n = 2*r+1
  · rw [show n = r+(r+1) by omega, ← shiftPowers T B symm, pw r le_rfl a,
        Function.iterate_succ_apply', pw r le_rfl b, next]
    rw [show r+(r+1) = 2*r+1 by omega]
  · let i := min r n
    let j := n-i
    have hi : i ≤ r := Nat.min_le_left _ _
    have hj : j ≤ r := by dsimp [i,j]; omega
    have eq : n = i+j := by dsimp [i,j]; omega
    rw [eq, ← shiftPowers T B symm, pw i hi a, pw j hj b, hankel i hi j hj]

/-- Completing the square controls the endpoint mass left by quadrature. -/
theorem endpointSquare (u c p : ℝ) :
    c^2-(2*c*(1-u)*p-(1-u)^2*p^2) = (c-(1-u)*p)^2 := by ring

/-- A normalized monomial detector separates a closed subinterval of (q,1).
Its adverse contribution below q decays geometrically. -/
theorem windowMinorant (q a b u : ℝ) (n : ℕ) (hq : 0 ≤ q) (ha : q < a)
    (hb : b < 1) (hu : u ∈ Icc (0:ℝ) 1) :
    (Icc a b).indicator (fun _ => (a-q)*(1-b)) u - q*(q/a)^n
      ≤ (u/a)^n*(u-q)*(1-u) := by
  have a0 : 0 < a := hq.trans_lt ha
  have base : 0 ≤ (u/a)^n := pow_nonneg (div_nonneg hu.1 a0.le) n
  have tail : 0 ≤ q*(q/a)^n := mul_nonneg hq (pow_nonneg (div_nonneg hq a0.le) n)
  by_cases ins : u ∈ Icc a b
  · rw [indicator_of_mem ins]
    have t : 1 ≤ (u/a)^n := one_le_pow₀ ((one_le_div a0).mpr ins.1)
    have prod := mul_le_mul (sub_le_sub_right ins.1 q) (sub_le_sub_left ins.2 1)
      (sub_nonneg.mpr hb.le) (sub_nonneg.mpr (ha.le.trans ins.1))
    have mult := mul_le_mul_of_nonneg_right t (mul_nonneg (sub_nonneg.mpr (ha.le.trans ins.1)) (sub_nonneg.mpr hu.2))
    nlinarith only [prod,mult,tail]
  · rw [indicator_of_not_mem ins]
    by_cases good : q ≤ u
    · exact (sub_nonpos.mpr tail).trans (mul_nonneg (mul_nonneg base (sub_nonneg.mpr good)) (sub_nonneg.mpr hu.2))
    · have low : u ≤ q := (le_of_not_ge good)
      have small := pow_le_pow_left₀ (div_nonneg hu.1 a0.le) (div_le_div_of_nonneg_right low a0.le) n
      have gap : (q-u)*(1-u) ≤ q := by
        have h := mul_le_mul (show q-u ≤ q by linarith [hu.1])
          (show 1-u ≤ 1 by linarith [hu.1]) (sub_nonneg.mpr hu.2) hq
        simpa using h
      have v := mul_le_mul small gap (mul_nonneg (sub_nonneg.mpr low) (sub_nonneg.mpr hu.2)) (pow_nonneg (div_nonneg hq a0.le) n)
      nlinarith only [v]

/-- Sign tests at every monomial degree rule out positive raw mass on each
closed interval strictly between the proposed transfer threshold and the vacuum. -/
theorem excludeInterior (μ : Measure ℝ) [IsFiniteMeasure μ] (q a b : ℝ)
    (hq : 0 ≤ q) (ha : q < a) (hb : b < 1) (support : ∀ᵐ u ∂μ, u ∈ Icc (0:ℝ) 1)
    (integrable : ∀ n : ℕ, Integrable (fun u : ℝ => (u/a)^n*(u-q)*(1-u)) μ)
    (tests : ∀ n : ℕ, (∫ u : ℝ, (u/a)^(2*n)*(u-q)*(1-u) ∂μ) ≤ 0) :
    μ.real (Icc a b) = 0 := by
  let w := (a-q)*(1-b)
  have hw : 0 < w := mul_pos (sub_pos.mpr ha) (sub_pos.mpr hb)
  have step (n : ℕ) : w*μ.real (Icc a b) ≤ (q*μ.real univ)*((q/a)^2)^n := by
    rw [← pow_mul]
    have hind := (integrable_const w (μ := μ)).indicator (measurableSet_Icc (a := a) (b := b))
    have hc := integrable_const (q*(q/a)^(2*n)) (μ := μ)
    have h := integral_mono_ae (hind.sub hc) (integrable (2*n))
      (support.mono (fun u hu => windowMinorant q a b u (2*n) hq ha hb hu))
    simp only [Pi.sub_apply] at h
    rw [integral_sub hind hc, integral_indicator_const _ measurableSet_Icc, integral_const] at h
    simp only [smul_eq_mul] at h
    nlinarith only [h,tests n]
  have small : q/a < 1 := (div_lt_one (hq.trans_lt ha)).mpr ha
  have nonneg : 0 ≤ q/a := div_nonneg hq (hq.trans ha.le)
  have z := tendsto_pow_atTop_nhds_zero_of_lt_one (sq_nonneg (q/a))
    (show (q/a)^2 < 1 by nlinarith only [mul_pos (sub_pos.mpr small) (show 0 < 1+q/a by linarith)])
  have lim := (tendsto_const_nhds (x := q*μ.real univ)).mul z
  have bound := le_of_tendsto_of_tendsto' (tendsto_const_nhds (x := w*μ.real (Icc a b))) lim step
  simp only [mul_zero] at bound
  exact le_antisymm (le_of_not_gt (fun h => (not_lt_of_ge bound) (mul_pos hw h))) measureReal_nonneg


/-- Recombining two character mixtures isolates the fundamental channel. -/
theorem polarizedSum (f a : ℝ) : ((f+a)+(f-a)+(f-a)+(f+a))/4 = f := by ring

/-- Two finite positive-energy nodes at or below the candidate threshold fit
the first three readings of each diagonal channel in the free example. -/
theorem diagonalCompletion :
    (0:ℝ) < 1/1024 ∧ (133:ℝ)/2552 < 1/16 ∧
    (∀ k ∈ Finset.range 3, (984064:ℝ)/16705*(1/1024)^k +
      (101761:ℝ)/16705*(133/2552)^k = (1:ℝ)/8^k+64/256^k) := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  intro k hk
  have h : k = 0 ∨ k = 1 ∨ k = 2 := by simp only [Finset.mem_range] at hk; omega
  rcases h with h | h | h <;> subst k <;> norm_num

theorem freeWitness :
    ((1:ℝ)/8-1/16)*(1-1/8) = 7/128 ∧
    4*(7:ℝ)/128/(1-1/16)^2 = 56/225 := by norm_num

/-- Spectral residual about a positive energy controls the entire complementary tail.
The interval includes both endpoints. -/
theorem residualTail (μ : Measure ℝ) [IsFiniteMeasure μ] (c R : ℝ) (hr : 0 < R)
    (h : Integrable (fun u : ℝ => (u-c)^2) μ) :
    R^2*μ.real (Icc (c-R) (c+R))ᶜ ≤ ∫ u : ℝ, (u-c)^2 ∂μ := by
  have hm := (measurableSet_Icc (a := c-R) (b := c+R)).compl
  have test := (integrable_const (R^2) (μ := μ)).indicator hm
  have point (u : ℝ) : (Icc (c-R) (c+R))ᶜ.indicator (fun _ => R^2) u ≤ (u-c)^2 := by
    by_cases out : u ∈ (Icc (c-R) (c+R))ᶜ
    · rw [indicator_of_mem out]
      change ¬ (c-R ≤ u ∧ u ≤ c+R) at out
      by_cases lo : c-R ≤ u
      · have hi : c+R ≤ u := le_of_not_ge (fun h => out ⟨lo,h⟩)
        nlinarith only [mul_nonneg (show 0 ≤ u-c-R by linarith) (show 0 ≤ u-c+R by linarith)]
      · nlinarith only [mul_nonneg (show 0 ≤ c-R-u by linarith) (show 0 ≤ c+R-u by linarith)]
    · rw [indicator_of_not_mem out]
      exact sq_nonneg _
  have bound := integral_mono test h point
  rw [integral_indicator_const _ hm] at bound
  simpa only [smul_eq_mul, mul_comm (μ.real _) _] using bound

/-- One-link vacuum projection and the scaled character residual yield a uniform band. -/
theorem weakMagneticBand (B δ norm mass inside outside : ℝ)
    (small : B ≤ 1/4096) (link : δ^2 ≤ 4*B/3)
    (radial : 1-5*δ ≤ norm) (variance : norm^2 = mass)
    (tail : outside ≤ 256*B) (split : inside+outside = mass) :
    3/4 ≤ inside ∧ outside ≤ 1/16 := by
  have distance : δ ≤ 1/54 := by
    by_contra! h
    nlinarith only [small, link, mul_pos (sub_pos.mpr h) (show 0 < δ+1/54 by linarith)]
  have lower : 49/54 ≤ norm := by linarith
  have product := mul_nonneg (sub_nonneg.mpr lower) (show 0 ≤ norm+49/54 by linarith)
  constructor <;> nlinarith only [small,tail,variance,split,product]

/-- The interval kernel on the fundamental core and its worst adverse tail give
a strict, three-reading margin in the weak magnetic coupling range. -/
theorem interactingMargin (inside outside measured : ℝ) (core : 3/4 ≤ inside)
    (tail : outside ≤ 1/16) (kernel : inside/64-outside/16 ≤ measured) :
    1/128 ≤ measured := by linarith

theorem coreKernel (u : ℝ) (lower : 1/12 ≤ u) (upper : u ≤ 1/4) :
    1/64 ≤ (u-1/16)*(1-u) := by
  have h := mul_le_mul (show (1:ℝ)/48 ≤ u-1/16 by linarith)
    (show (3:ℝ)/4 ≤ 1-u by linarith) (by norm_num) (show 0 ≤ u-1/16 by linarith)
  linarith

theorem adverseKernel (u : ℝ) (lo : 0 ≤ u) (hi : u ≤ 1) :
    -(1/16:ℝ) ≤ (u-1/16)*(1-u) := by
  nlinarith only [mul_nonneg lo (sub_nonneg.mpr hi),lo]

/-- The link Poincaré inequality and a projected eigen-equation give a quadratic
local kinetic estimate. K is the unit-round, unscaled Dirichlet form. -/
theorem localLinkKinetic (g δ K : ℝ) (hg : 0 ≤ g)
    (poincare : 3*δ^2 ≤ K) (localized : K ≤ 16*g*δ) :
    δ ≤ 16*g/3 ∧ K ≤ 256*g^2/3 := by
  have hd : δ ≤ 16*g/3 := by
    by_contra! hi
    nlinarith only [poincare,localized,mul_pos (show 0 < δ by linarith) (sub_pos.mpr hi)]
  refine ⟨hd, ?_⟩
  nlinarith only [localized,mul_le_mul_of_nonneg_left hd hg]

/-- The cutoff is propagated on a whole low-energy subspace through a product of
nonnegative one-step operator-norm bounds. -/
theorem tailProduct (f ratio : ℕ → ℝ) (start : f 0 ≤ 1) (pos : ∀ k, 0 ≤ ratio k)
    (step : ∀ k, f (k+1) ≤ ratio k*f k) (n : ℕ) :
    f n ≤ ∏ k ∈ Finset.range n, ratio k := by
  induction n with
  | zero => simpa using start
  | succ k ih =>
    rw [Finset.prod_range_succ, mul_comm]
    exact (step k).trans (mul_le_mul_of_nonneg_left ih (pos k))

theorem casimirProduct (n : ℕ) :
    (∏ k ∈ Finset.range n, (k+1)*(k+3))*2 = n.factorial*(n+2).factorial := by
  induction n with
  | zero => decide
  | succ k ih =>
    rw [Finset.prod_range_succ, show k+1+2 = (k+2)+1 by omega,
      Nat.factorial_succ (k+2), Nat.factorial_succ k]
    calc
      _ = ((∏ i ∈ Finset.range k, (i+1)*(i+3))*2)*((k+1)*(k+3)) := by ring
      _ = _ := by rw [ih]; ring

/-- Normalization of a projected variational trial vector. -/
theorem rayleighCut (numerator norm2 upper error lost : ℝ) (h : lost < 1)
    (floor : 1-lost ≤ norm2) (he : 0 ≤ error)
    (form : numerator-upper*norm2 ≤ error) :
    numerator/norm2 ≤ upper+error/(1-lost) := by
  have hd : 0 < 1-lost := sub_pos.mpr h
  have hn := hd.trans_le floor
  have cmp := div_le_div_of_nonneg_left he hd floor
  calc
    numerator/norm2 ≤ upper + error/norm2 := by
      rw [div_le_iff₀ hn, add_mul, div_mul_cancel₀ _ hn.ne']
      linarith
    _ ≤ _ := add_le_add_left cmp _

theorem gapEnclosure (e0 e1 r0 r1 err0 err1 : ℝ) (a : e0 ≤ r0) (b : r0 ≤ e0+err0)
    (c : e1 ≤ r1) (d : r1 ≤ e1+err1) :
    r1-r0-err1 ≤ e1-e0 ∧ e1-e0 ≤ r1-r0+err0 := by constructor <;> linarith

/-- Exact leading determinants of the 9-state Jacobi matrix scaled by 2d. -/
def leading (d m : ℤ) : ℕ → ℤ × ℤ
  | 0 => (0,1)
  | n+1 =>
    let p := leading d m n
    (p.2, 2*(d*((n:ℤ)*(n+2)+1)-m)*p.2-d^2*p.1)

def sturmCount (m : ℤ) : ℕ :=
  ((List.range 9).filter (fun i => (leading (10^12) m (i+1)).1 *
    (leading (10^12) m (i+1)).2 < 0)).length

def endpoints : List ℤ := [918058176624,918058176625,4031921988130,4031921988131]

theorem sturmCounts :
    endpoints.map sturmCount = [0,1,1,2] ∧
    endpoints.all (fun m => (List.range 10).all (fun i => (leading (10^12) m i).2 != 0)) = true := by decide

def rotorDen : ℕ → ℕ
  | 0 => 1
  | k+1 => if k = 0 then 1 else ((k+1)*(k+3)-5)*rotorDen k

def rotorTail (k : ℕ) : ℚ := 1/(rotorDen k : ℚ)

theorem rotorCutError :
    (5*(rotorTail 9)^2+(rotorTail 8)*(rotorTail 9)/2)/(1-(rotorTail 9)^2)
    = 4/6953764855522223076923 := by
  have a : rotorDen 8 = 3198555000 := by decide
  have b : rotorDen 9 = 300664170000 := by decide
  norm_num [rotorTail,a,b]

/-- A transfer factor removes the equal-time reading while preserving a certified
margin. The negative part is at most q²/4, including at zero transfer. -/
theorem positiveTimeKernel (u q : ℝ) (lo : 0 ≤ u) (hi : u ≤ 1) :
    -q^2/4 ≤ u*(u-q)*(1-u) := by
  by_cases h : q ≤ u
  · exact (by nlinarith only [sq_nonneg q] : -q^2/4 ≤ 0).trans
      (mul_nonneg (mul_nonneg lo (sub_nonneg.mpr h)) (sub_nonneg.mpr hi))
  · have s := mul_nonneg (mul_nonneg lo (sub_nonneg.mpr (le_of_not_ge h))) lo
    nlinarith only [s,sq_nonneg (2*u-q)]

theorem positiveTimeMargin (inside outside measured : ℝ) (core : 3/4 ≤ inside)
    (tail : outside ≤ 1/16) (kernel : inside/768-outside/1024 ≤ measured) :
    15/16384 ≤ measured := by linarith

-- BEGIN PCP OS generated electric readings
def scaledEntries : List (ℤ × ℤ) := [(65, -63), (96, -32), (1088, 960), (32832, 32704)]

theorem generatedReadings : scaledEntries = (List.range 4).map (fun k => (((32:ℤ)^k+64), ((32:ℤ)^k-64))) := by decide

#print axioms factorGram
#print axioms gramTransfer
#print axioms openWindow
#print axioms softMass
#print axioms quadraticReadings
#print axioms threeReadingError
#print axioms recoverDifferences
#print axioms shiftPowers
#print axioms polynomialChain
#print axioms oddMomentRecovery
#print axioms endpointSquare
#print axioms windowMinorant
#print axioms excludeInterior
#print axioms polarizedSum
#print axioms diagonalCompletion
#print axioms freeWitness
#print axioms residualTail
#print axioms weakMagneticBand
#print axioms interactingMargin
#print axioms coreKernel
#print axioms adverseKernel
#print axioms localLinkKinetic
#print axioms tailProduct
#print axioms casimirProduct
#print axioms rayleighCut
#print axioms gapEnclosure
#print axioms sturmCounts
#print axioms rotorCutError
#print axioms positiveTimeKernel
#print axioms positiveTimeMargin
#print axioms generatedReadings

end Millennium.YangMills.D4.FiniteReadings
