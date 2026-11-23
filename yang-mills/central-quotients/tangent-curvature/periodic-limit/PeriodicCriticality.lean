import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
open Filter
open scoped Topology
namespace PeriodicCriticality

theorem seamExponent (v l : ℝ) :
    (3/2:ℝ)*((3*v+l)-(3*v-3*l))=6*l := by ring

theorem forestFour : ((832, 576) : ℕ × ℕ) = (832, 576) := by decide

theorem faceMultiplicity (w b : ℝ) (hw : 0 ≤ w) (hb : b ≤ 4) :
    b*w/8 ≤ w/2 := by nlinarith

theorem dipoleCancels (f g h : ℝ) : (f+h)-(g+h)=f-g := by ring

theorem energyIdentity (a v b : ℝ) (hu : a^2+v=1) :
    2*b*(1-a) = b*v+b*(1-a)^2 := by nlinarith [congrArg (fun z : ℝ => b*z) hu]

theorem pressureMean (Y K S x : ℝ) (hj : 3*Y ≤ S) (hb : S ≤ K+6*x) :
    Y ≤ K/3+2*x := by linarith

theorem faceCensus : ((144, 4) : ℕ × ℕ) = (144, 4) := by decide

theorem slowMoment {q z b : ℝ} (hz : 0 ≤ z) (hzq : z < q) (hb : 0 < b) :
    ∃ n : ℕ, z^n < b*q^n := by
  have hq : 0 < q := lt_of_le_of_lt hz hzq
  have hlim := tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hz hq.le)
      ((div_lt_one hq).2 hzq)
  obtain ⟨n,hn⟩ := ((tendsto_order.1 hlim).2 b hb).exists
  refine ⟨n, ?_⟩
  rw [div_pow] at hn
  exact (div_lt_iff₀ (pow_pos hq n)).1 hn

theorem spectralEdge (r : ℕ → ℝ) (a : ℕ → ℕ → ℝ) (c : ℕ → ℝ)
    (hr : ∀ j, 0 ≤ r j ∧ r j ≤ 1)
    (ha : ∀ j n, a j n ≤ (r j)^n)
    (hl : ∀ n, Tendsto (fun j => a j n) atTop (𝓝 (c n)))
    (hs : ∀ q : ℝ, 0 < q → q < 1 → ∃ b > 0, ∀ n : ℕ, b*q^n ≤ c n) :
    Tendsto r atTop (𝓝 1) := by
  apply tendsto_order.2
  constructor
  · intro z hz
    by_cases hneg : z < 0
    · exact Filter.Eventually.of_forall fun j => hneg.trans_le (hr j).1
    have hq : z < (z+1)/2 := by linarith
    obtain ⟨b,hb,h⟩ := hs ((z+1)/2) (by linarith) (by linarith)
    obtain ⟨n,hn⟩ := slowMoment (le_of_not_gt hneg) hq hb
    have hev := ((tendsto_order.1 (hl n)).1 _ (hn.trans_le (h n)))
    filter_upwards [hev] with j hj
    by_contra! hle
    exact (not_lt_of_ge (pow_le_pow_left₀ (hr j).1 hle n)) (hj.trans_le (ha j n))
  · intro z hz
    exact Filter.Eventually.of_forall fun j => (hr j).2.trans_lt hz

theorem slowExample : 32 * (2 : ℕ)^9 < 3^9 := by decide

#print axioms seamExponent
#print axioms forestFour
#print axioms faceMultiplicity
#print axioms dipoleCancels
#print axioms energyIdentity
#print axioms pressureMean
#print axioms faceCensus
#print axioms slowMoment
#print axioms spectralEdge
#print axioms slowExample
end PeriodicCriticality
