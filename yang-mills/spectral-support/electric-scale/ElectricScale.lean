import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

open MeasureTheory Set

namespace Millennium.YangMills.D4.ElectricScale

/-- An adjacent-shell ground-state transform. The two positive weights can be
the entries of the Dirichlet--Neumann sine vector. -/
theorem edgeTransform (a b u v : ℝ) (hu : 0 < u) (hv : 0 < v) :
    (b-a)^2 - (1-v/u)*a^2 - (1-u/v)*b^2 =
    u*v*(a/u-b/v)^2 := by
  field_simp
  ring

/-- Summing an arbitrary chain of adjacent-shell estimates. The endpoint
and the last edge are kept explicit so a free right end contributes no edge. -/
theorem chainForm (a u : ℕ → ℝ) (hu : ∀ i, 0 < u i) (d : ℕ) :
    ∑ i ∈ Finset.range d, ((1-u (i+1)/u i)*(a i)^2 +
        (1-u i/u (i+1))*(a (i+1))^2) ≤
      ∑ i ∈ Finset.range d, (a (i+1)-a i)^2 := by
  apply Finset.sum_le_sum
  intro i _
  have ht := edgeTransform (a i) (a (i+1)) (u i) (u (i+1)) (hu i) (hu (i+1))
  have hp := mul_nonneg (mul_nonneg (hu i).le (hu (i+1)).le)
    (sq_nonneg (a i/u i - a (i+1)/u (i+1)))
  linarith

/-- Exact scalar recursions for the finite Dirichlet--Neumann matrix. -/
theorem interiorRow (l u r c : ℝ) (hu : u ≠ 0) (h : l+r=2*c*u) :
    (1-l/u)+(1-r/u)=2*(1-c) := by
  field_simp
  linarith

theorem freeEnd (l u c : ℝ) (hu : u ≠ 0) (h : l+u=2*c*u) :
    1-l/u=2*(1-c) := by
  field_simp
  linarith

/-- Collect a chain's two endpoint contributions at each vertex. -/
theorem collectRows (L R w : ℕ → ℝ) (d : ℕ) :
    L 0*w 0 + ∑ i ∈ Finset.range d, (R i*w i + L (i+1)*w (i+1)) =
    (∑ i ∈ Finset.range d, (L i+R i)*w i) + L d*w d := by
  induction d with
  | zero => simp
  | succ d ih =>
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    linarith only [ih, show (L d+R d)*w d=L d*w d+R d*w d by ring]

/-- A positive eigenvector gives the spectral lower bound for the whole prefix,
including either a one-site chain or any number of interior rows. -/
theorem prefixBound (a u : ℕ → ℝ) (hu : ∀ i, 0 < u i) (L : ℕ → ℝ)
    (d : ℕ) (k : ℝ) (hl : L 0=1)
    (hnext : ∀ i, L (i+1)=1-u i/u (i+1))
    (hi : ∀ i < d, L i+(1-u (i+1)/u i)=k) (he : L d=k) :
    k*(∑ i ∈ Finset.range (d+1), (a i)^2) ≤
    (a 0)^2+∑ i ∈ Finset.range d, (a (i+1)-a i)^2 := by
  have hc := collectRows L (fun i => 1-u (i+1)/u i) (fun i => (a i)^2) d
  simp only [hl, one_mul, hnext, he] at hc
  have hr : (∑ i ∈ Finset.range d, (L i + (1-u (i+1)/u i))*(a i)^2) =
      ∑ i ∈ Finset.range d, k*(a i)^2 := by
    apply Finset.sum_congr rfl
    intro i h
    rw [hi i (Finset.mem_range.mp h)]
  rw [hr, ← Finset.mul_sum] at hc
  rw [Finset.sum_range_succ, mul_add]
  linarith only [hc, chainForm a u hu d]

/-- Pointwise shell probability variation at the boundary between two bins. -/
theorem shellVariation (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    |a^2-b^2| = |a-b| * (a+b) := by
  rw [show a^2-b^2=(a-b)*(a+b) by ring, abs_mul, abs_of_nonneg (add_nonneg ha hb)]

/-- The rescaled form pays for both the derivative and the oscillator moment,
including the one-cell error in the moment estimate. -/
theorem scaledEnergy (h K eps D M E : ℝ) (hh : 0 < h)
    (hD : D*h^2 ≤ 2*eps) (hM : M ≤ h^2*(K+1))
    (hE : h^2*K/4+eps/h^2 ≤ E) :
    D/2 + M/4 ≤ E+h^2/4 := by
  have hD' : D ≤ 2*eps/h^2 := (le_div_iff₀ (sq_pos_of_pos hh)).2 hD
  linarith only [hD', hM, hE, show 2*eps/h^2=2*(eps/h^2) by ring,
    show h^2*(K+1)=h^2*K+h^2 by ring]

/-- The involution for an odd center twist anticommutes with the plaquette
trace. A quadratic expectation bound for all linear combinations gives
the disk for the two mean values. -/
theorem centerDisk (x z : ℝ) (h : ∀ a b : ℝ, (a*x+b*z)^2 ≤ a^2+b^2) :
    x^2+z^2 ≤ 1 := by
  have hh := h x z
  by_contra! hn
  have hp := mul_pos (by linarith : 0 < x^2+z^2) (by linarith : 0 < x^2+z^2-1)
  nlinarith only [hh, hp]

theorem centerError (x z eps : ℝ) (hx : x=1-eps) (h : x^2+z^2≤1) :
    z^2 ≤ 2*eps-eps^2 := by nlinarith

/-- Two radial shells defeat the hard-cutoff constant for an untruncated
vector. Entries are squared norms multiplied by five. -/
theorem wrongEndpoint : (4:ℚ)/5 > 1-(2:ℚ)/5 := by norm_num

/-- Spectral mass below half the classical twist energy. The input second
moment is the squared norm of the normalized Hamiltonian residual. -/
theorem lowTwistMass (μ : Measure ℝ) [IsFiniteMeasure μ] (V : ℝ) (hv : 0 < V)
    (h : Integrable (fun y : ℝ => (y-V)^2) μ) :
    (V/2)^2*μ.real (Iic (V/2)) ≤ ∫ y : ℝ, (y-V)^2 ∂μ := by
  have hm := measurableSet_Iic (a := V/2)
  have test := (integrable_const ((V/2)^2) (μ := μ)).indicator hm
  have point (y : ℝ) : (Iic (V/2)).indicator (fun _ => (V/2)^2) y ≤ (y-V)^2 := by
    by_cases mem : y ∈ Iic (V/2)
    · rw [indicator_of_mem mem]
      change y ≤ V/2 at mem
      nlinarith only [mul_nonneg (show 0 ≤ V/2-y by linarith)
        (show 0 ≤ 3*V/2-y by linarith)]
    · rw [indicator_of_not_mem mem]
      exact sq_nonneg _
  have bound := integral_mono test h point
  rw [integral_indicator_const _ hm] at bound
  simpa only [smul_eq_mul,mul_comm (μ.real _) _] using bound

/-- A relative SU(2) residual controls low-energy mass independently of the
number of odd faces. The ratio of the residual to V is at most sqrt(2 eps). -/
theorem twistLeakage (V eps m : ℝ) (hv : 0 < V) (h : (V/2)^2*m ≤ 2*eps*V^2) :
    m ≤ 8*eps := by
  by_contra! hn
  have hp := mul_pos (sq_pos_of_pos hv) (show 0 < m-8*eps by linarith)
  nlinarith only [hp,h]

/-- The tangent bound for the mesh-time Laplace transform. -/
theorem meshTangent (s E A : ℝ) :
    Real.exp (-s*A) * (1+s*A-s*E) ≤ Real.exp (-s*E) := by
  have h := Real.add_one_le_exp (s*A-s*E)
  have hh := mul_le_mul_of_nonneg_left h (Real.exp_pos (-s*A)).le
  rw [← Real.exp_add, show -s*A+(s*A-s*E)=-s*E by ring] at hh
  linarith only [hh, show Real.exp (-s*A)*((s*A-s*E)+1) =
    Real.exp (-s*A)*(1+s*A-s*E) by ring]

/-- Positive mesh-time signal from a measured mass and its first moment. -/
theorem meshSurvival (μ : Measure ℝ) [IsFiniteMeasure μ] (s A : ℝ)
    (hE : Integrable (fun E : ℝ => E) μ)
    (hL : Integrable (fun E : ℝ => Real.exp (-s*E)) μ)
    (hs : 0 ≤ s) (budget : (∫ E : ℝ, E ∂μ) ≤ A*μ.real univ) :
    μ.real univ * Real.exp (-s*A) ≤ ∫ E : ℝ, Real.exp (-s*E) ∂μ := by
  have line := (integrable_const (1+s*A) (μ := μ)).sub (hE.const_mul s)
  have bound := integral_mono (line.const_mul (Real.exp (-s*A))) hL (meshTangent s · A)
  change (∫ E : ℝ, Real.exp (-s*A)*((1+s*A)-s*E) ∂μ) ≤ _ at bound
  rw [integral_const_mul, integral_sub (integrable_const _) (hE.const_mul s),
    integral_const, integral_const_mul, smul_eq_mul] at bound
  have hh := mul_le_mul_of_nonneg_left budget hs
  have hl : μ.real univ ≤ μ.real univ*(1+s*A)-s*(∫ E : ℝ, E ∂μ) := by
    nlinarith only [hh]
  calc
    _ = Real.exp (-s*A)*μ.real univ := mul_comm _ _
    _ ≤ _ := (mul_le_mul_of_nonneg_left hl (Real.exp_pos _).le).trans bound

def bitParity (n : Nat) : Nat := (List.range 6).countP (fun i => n.testBit i) % 2

def faceKernel (rows : List Nat) : List Nat :=
  (List.range 64).filter (fun n => rows.all (fun row => bitParity (n &&& row) == 0))

def annihilator (kernel : List Nat) : List Nat :=
  (List.range 64).filter (fun n => kernel.all (fun z => bitParity (n &&& z) == 0))

def twistEnergy (rows : List Nat) (z : Nat) : Nat :=
  2 * rows.countP (fun row => bitParity (row &&& z) == 1)

-- BEGIN PCP OS generated star flux
def starRows : List Nat := [5, 9, 17, 33, 6, 10, 18, 34, 20, 36, 24, 40]

def starFlat : List Nat := [0, 63]

def starFlux : List Nat := [0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30, 33, 34, 36, 39, 40, 43, 45, 46, 48, 51, 53, 54, 57, 58, 60, 63]

set_option maxRecDepth 8192
set_option maxHeartbeats 1600000
theorem starCalculation : faceKernel starRows = starFlat ∧ starFlat = [0,63] ∧ annihilator starFlat = starFlux ∧ starFlux = (List.range 64).filter (fun b => bitParity b == 0) ∧ starFlux.length = 32 := by decide

def energyHistogram : List (Nat × Nat) := [(0, 1), (8, 6), (12, 16), (16, 9)]

theorem starSpectrum : energyHistogram = [(0,1),(8,6),(12,16),(16,9)] ∧ ((List.range 25).map (fun e => (e, ((List.range 32).map (twistEnergy starRows)).count e))).filter (fun p => p.2 != 0) = energyHistogram := by decide

#print axioms edgeTransform
#print axioms chainForm
#print axioms interiorRow
#print axioms collectRows
#print axioms prefixBound
#print axioms freeEnd
#print axioms shellVariation
#print axioms scaledEnergy
#print axioms centerDisk
#print axioms centerError
#print axioms wrongEndpoint
#print axioms lowTwistMass
#print axioms twistLeakage
#print axioms starSpectrum
#print axioms meshTangent
#print axioms meshSurvival
#print axioms starCalculation

end Millennium.YangMills.D4.ElectricScale
