import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.GirthShell
open scoped RealInnerProductSpace
noncomputable section

/-- Removing the normalized vacuum before taking a Gram matrix centers every column. -/
theorem centeredInner {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (u x y : H) (unit : ⟪u,u⟫ = 1) :
    ⟪x - ⟪u,x⟫ • u, y - ⟪u,y⟫ • u⟫ =
      ⟪x,y⟫ - ⟪u,x⟫ * ⟪u,y⟫ := by
  simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right, unit]
  rw [real_inner_comm x u]
  ring

/-- A rank-one vacuum can leak into a compressed quadratic form only quadratically. -/
theorem vacuumLeak {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (x u : H) (ε : ℝ) (h : |⟪u,x⟫| ≤ ε) :
    ⟪x, ⟪u,x⟫ • u⟫ ≤ ε^2 := by
  rw [real_inner_smul_right, ← real_inner_comm x u]
  nlinarith [sq_abs ⟪u,x⟫, mul_self_le_mul_self (abs_nonneg _) h]

/-- All positive lags of a finite-rank factor pass through the smaller Gram matrix. -/
theorem gramPowers {ι κ R : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ]
    [DecidableEq κ] [CommSemiring R] (A : Matrix ι κ R) (B : Matrix κ ι R) (k : ℕ) :
    (A*B)^(k+1) = A*(B*A)^k*B := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ (A*B), ih, pow_succ (B*A)]
    simp only [Matrix.mul_assoc]

/-- A rank-one perturbation of a scalar has the longitudinal eigenvalue. -/
theorem longitudinal {V : Type*} [AddCommGroup V] [Module ℂ V]
    (c : V →ₗ[ℂ] ℂ) (v : V) (d u : ℂ) :
    d • v + u • (c v • v) = (d + u*c v) • v := by
  rw [add_smul, mul_smul]

/-- Every vector in the incidence row's kernel keeps the transverse eigenvalue. -/
theorem transverse {V : Type*} [AddCommGroup V] [Module ℂ V]
    (c : V →ₗ[ℂ] ℂ) (v w : V) (d u : ℂ) (h : c w = 0) :
    d • w + u • (c w • v) = d • w := by simp [h]

-- PCP begin geometry
/-- The edge masks of every additional square meeting the exposed corner hexagon. -/
def faceMask : Fin 10 → Nat := ![0,1,2,3,4,8,12,16,32,48]

set_option maxRecDepth 8000 in
set_option maxHeartbeats 2000000 in
theorem coreCompletion : ∀ a b c : Fin 10,
    faceMask a ||| faceMask b ||| faceMask c = 63 →
    (faceMask a = 3 ∨ faceMask b = 3 ∨ faceMask c = 3) ∧
    (faceMask a = 12 ∨ faceMask b = 12 ∨ faceMask c = 12) ∧
    (faceMask a = 48 ∨ faceMask b = 48 ∨ faceMask c = 48) := by decide
-- PCP end geometry

/-- The squared modulus of the cube incidence factor. -/
theorem incidenceSymbol (a b : ℝ) (circle : a^2+b^2=1) :
    (1+a)^2+b^2=2+2*a := by linarith

theorem bandEdges (a b c : ℝ) (ha : |a|≤1) (hb : |b|≤1) (hc : |c|≤1) :
    -2 ≤ 4+2*(a+b+c) ∧ 4+2*(a+b+c) ≤ 10 := by
  rw [abs_le] at ha hb hc
  constructor <;> linarith

/-- The three-dimensional orientation block loses its rank-one part at the corner. -/
theorem corner (a b c : ℝ) (ha : -1≤a) (hb : -1≤b) (hc : -1≤c) :
    4+2*(a+b+c) = -2 ↔ a = -1 ∧ b = -1 ∧ c = -1 := by
  constructor
  · intro h
    exact ⟨by linarith, by linarith, by linarith⟩
  · rintro ⟨rfl,rfl,rfl⟩
    norm_num

/-- Incidence takes every discrete time power to its cube-space evolution. -/
theorem intertwinePowers {ι κ : Type*} [Fintype ι] [DecidableEq ι]
    [Fintype κ] [DecidableEq κ] (C : Matrix ι κ ℂ)
    (A : Matrix κ κ ℂ) (B : Matrix ι ι ℂ) (h : C*A=B*C) (k : ℕ) :
    C*A^k = B^k*C := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, pow_succ, ← Matrix.mul_assoc, ih, Matrix.mul_assoc, h, ← Matrix.mul_assoc]

/-- Norm error grows at most linearly in the number of steps for contractions. -/
theorem stepError {R : Type*} [NormedRing R] [NormOneClass R] (a b : R)
    (ha : ‖a‖ ≤ 1) (hb : ‖b‖ ≤ 1) (k : ℕ) : ‖a^k-b^k‖ ≤ k*‖a-b‖ := by
  have bounded (j : ℕ) : ‖a^j‖ ≤ 1 := by
    induction j with
    | zero => simp
    | succ j ih =>
      rw [pow_succ]
      exact (norm_mul_le _ _).trans ((mul_le_mul ih ha (norm_nonneg _) zero_le_one).trans_eq (one_mul 1))
  induction k with
  | zero => simp
  | succ k ih =>
    calc
      ‖a^(k+1)-b^(k+1)‖ = ‖a^k*(a-b)+(a^k-b^k)*b‖ := by
        simp only [pow_succ, mul_sub, sub_mul, sub_add_sub_cancel]
      _ ≤ ‖a^k‖*‖a-b‖ + ‖a^k-b^k‖*‖b‖ :=
        (norm_add_le _ _).trans (add_le_add (norm_mul_le _ _) (norm_mul_le _ _))
      _ ≤ 1*‖a-b‖ + ((k:ℝ)*‖a-b‖)*1 := by
        exact add_le_add (mul_le_mul_of_nonneg_right (bounded k) (norm_nonneg _))
          (mul_le_mul ih hb (norm_nonneg _) (mul_nonneg (Nat.cast_nonneg _) (norm_nonneg _)))
      _ = _ := by push_cast; ring

/-- Every row sum of the entrywise square of a real orthogonal projection is its diagonal. -/
theorem schurRows {ι : Type*} [Fintype ι] (P : Matrix ι ι ℝ)
    (symmetric : ∀ i j, P j i = P i j) (projector : P*P=P) (i : ι) :
    ∑ j, (P i j)^2 = P i i := by
  calc
    _ = ∑ j, P i j * P j i := by
      apply Finset.sum_congr rfl
      intro j _
      rw [symmetric i j, pow_two]
    _ = (P*P) i i := rfl
    _ = P i i := congrFun (congrFun projector i) i

/-- Dirichlet energy of three direct boundary links and three grounded neighbor branches. -/
theorem cornerEnergy (x a b c : ℝ) :
    5*x^2 ≤ 3*x^2+((x-a)^2+2*a^2)+((x-b)^2+2*b^2)+((x-c)^2+2*c^2) := by
  nlinarith [sq_nonneg (3*a-x), sq_nonneg (3*b-x), sq_nonneg (3*c-x)]

/-- The three exterior faces already exceed the infinite-volume bulk edge. -/
theorem cornerTrial (g : ℝ) (hg : g≤1/5) :
    108/25 ≤ 6*((1-g)^2+2*g^2) := by
  nlinarith [mul_nonneg (show 0 ≤ 1/5-g by linarith) (show 0 ≤ 12-18*(g+1/5) by linarith)]

theorem cubeLimits :
    (6:ℝ)*((1-1/6)^2-(1/6)^2)=4 ∧ (6:ℝ)*((1-1/6)^2+5*(1/6)^2)=5 := by norm_num

def edgeRow (x y z : ℝ) : Matrix (Fin 3) (Fin 3) ℝ := !![0,z,y; z,0,x; y,x,0]

def cubeGram (x y z : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  fun i j => ![x,y,z] i * ![x,y,z] j

/-- In the face-centered Fourier basis the two incidence terms reproduce the
    complete orientation matrix of the isotropic quartic coefficient. -/
theorem jointSymbol (x y z : ℝ) :
    cubeGram x y z + edgeRow x y z * edgeRow x y z =
    !![x^2+y^2+z^2,2*x*y,2*x*z; 2*x*y,x^2+y^2+z^2,2*y*z;
       2*x*z,2*y*z,x^2+y^2+z^2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_succ, cubeGram, edgeRow] <;> ring

-- PCP begin certificate
theorem cubeHessian : (4:ℝ)*2^8/(2^12*2^6) = 1/256 := by norm_num
-- PCP end certificate

end
#print axioms centeredInner
#print axioms vacuumLeak
#print axioms gramPowers
#print axioms longitudinal
#print axioms transverse
#print axioms incidenceSymbol
#print axioms bandEdges
#print axioms coreCompletion
#print axioms corner
#print axioms intertwinePowers
#print axioms stepError
#print axioms schurRows
#print axioms cornerEnergy
#print axioms cornerTrial
#print axioms cubeLimits
#print axioms jointSymbol
#print axioms cubeHessian
end Millennium.YangMills.GirthShell
