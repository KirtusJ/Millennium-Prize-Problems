import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Analysis.Convex.SpecificFunctions.Deriv

namespace Millennium.G4.TwoSite

set_option maxRecDepth 32768
set_option maxHeartbeats 6000000

def flip (x j : Nat) : Nat :=
  if x / 2^j % 2 == 0 then x + 2^j else x - 2^j

def lowerBits (x : Nat) : Nat → Nat
  | 0 => 0
  | j+1 => lowerBits x j + x / 2^j % 2

def link (j : Nat) (x y : Fin 8) : Int :=
  if y.val != flip x.val j then 0
  else (-(1 : Int)) ^ (lowerBits x.val j)

def signedCube (x y : Fin 8) : Int := link 0 x y + link 1 x y + link 2 x y

def compose (a b : Fin 8 → Fin 8 → Int) (x y : Fin 8) : Int :=
  (List.ofFn (fun z : Fin 8 => a x z * b z y)).sum

theorem symmetry : ∀ x y, signedCube x y = signedCube y x := by decide

-- NATIVE CHILD 1
theorem flux : ∀ (i j : Fin 3) (x y : Fin 8), i ≠ j →
    compose (link i.val) (link j.val) x y = -compose (link j.val) (link i.val) x y := by
  decide

theorem doubled_square : ∀ x y,
    compose (fun i j => 2 * signedCube i j) (fun i j => 2 * signedCube i j) x y
      = 2 * 2 * (if x = y then 3 else 0) := by decide

theorem zero_diagonal : ∀ x, signedCube x x = 0 := by decide

-- NATIVE CHILD 2
theorem spin_bound (s v q : ℝ) (hv : 0 ≤ v) (hq : 0 ≤ q) (hq2 : q^2 = 3)
    (h : s^2 ≤ 3*v^2) : s ≤ q*v := by
  have hpos := mul_nonneg hq hv
  have hs : s^2 ≤ (q*v)^2 := by simpa only [mul_pow, hq2] using h
  nlinarith [sq_nonneg (s - q*v)]

theorem gaussian_denominator (a b c : ℝ) (h : c^2-b^2=1) :
    (a+c)^2-1 = 2*a*(c+b)+(a-b)^2 := by nlinarith

open scoped BigOperators

theorem row_jensen {ι : Type*} (t : Finset ι) (w angle : ι → ℝ)
    (hw : ∀ i ∈ t, 0 ≤ w i) (hs : ∑ i ∈ t, w i = 1)
    (ha : ∀ i ∈ t, angle i ∈ Set.Icc (-(Real.pi / 2)) (Real.pi / 2)) :
    1 - Real.cos (∑ i ∈ t, w i * angle i) ≤ ∑ i ∈ t, w i * (1 - Real.cos (angle i)) := by
  have h := strictConcaveOn_cos_Icc.concaveOn.le_map_sum hw hs ha
  simp only [smul_eq_mul] at h
  simp only [mul_sub, mul_one, Finset.sum_sub_distrib, hs]
  linarith

theorem scale_bound (m a L h C d : ℝ) (ha : 0 < a) (hd : 0 < d) (hm : 0 ≤ m)
    (hbox : d ≤ a*L) (hgap : m*L ≤ C*h) : m/a ≤ C*h/d := by
  apply (div_le_div_iff₀ ha hd).2
  calc m*d ≤ m*(a*L) := mul_le_mul_of_nonneg_left hbox hm
       _ = (m*L)*a := by ring
       _ ≤ (C*h)*a := mul_le_mul_of_nonneg_right hgap ha.le

open Filter Topology in
theorem uniform_bare_scale {m a L h : ℕ → ℝ} {C d : ℝ} (hd : 0 < d)
    (ha : ∀ n, 0 < a n) (hm : ∀ n, 0 ≤ m n) (hbox : ∀ n, d ≤ a n * L n)
    (hgap : ∀ n, m n * L n ≤ C*h n) (hh : Tendsto h atTop (𝓝 0)) :
    Tendsto (fun n => m n / a n) atTop (𝓝 0) := by
  apply squeeze_zero (fun n => div_nonneg (hm n) (ha n).le)
    (fun n => scale_bound _ _ _ _ _ _ (ha n) hd (hm n) (hbox n) (hgap n))
  simpa using (hh.const_mul C).div_const d

#print axioms symmetry
#print axioms flux
#print axioms doubled_square
#print axioms zero_diagonal
#print axioms spin_bound
#print axioms gaussian_denominator
#print axioms row_jensen
#print axioms scale_bound
#print axioms uniform_bare_scale

end Millennium.G4.TwoSite
