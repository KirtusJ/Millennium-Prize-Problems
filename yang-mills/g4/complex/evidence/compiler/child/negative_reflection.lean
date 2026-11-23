import Mathlib.Analysis.Complex.Basic
import Mathlib.Topology.Algebra.Monoid
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

open scoped BigOperators Topology
open Filter

noncomputable section

namespace Millennium.G4.ComplexRP

universe u v w

def NonnegativeComplex (z : ℂ) : Prop :=
  z.im = 0 ∧ 0 ≤ z.re

/-- The test index is finite. The label map may repeat labels. -/
def pairing {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (c d : J → ℂ) : ℂ :=
  ∑ i : J, ∑ j : J, starRingEnd ℂ (c i) * d j * K (idx i) (idx j)

def Q {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (c : J → ℂ) : ℂ :=
  pairing K idx c c

theorem nonnegativeComplex_of_tendsto {A : Type w}
    {l : Filter A} [NeBot l] {f : A → ℂ} {z : ℂ}
    (hlim : Tendsto f l (𝓝 z))
    (hpos : ∀ᶠ a in l, NonnegativeComplex (f a)) :
    NonnegativeComplex z := by
  constructor
  · have hclosed : IsClosed ({0} : Set ℝ) := isClosed_singleton
    have hz : z.im ∈ ({0} : Set ℝ) :=
      hclosed.mem_of_tendsto ((Complex.continuous_im.tendsto z).comp hlim)
        (hpos.mono fun _ ha => Set.mem_singleton_iff.mpr ha.1)
    exact Set.mem_singleton_iff.mp hz
  · have hclosed : IsClosed (Set.Ici (0 : ℝ)) := isClosed_Ici
    exact hclosed.mem_of_tendsto
      ((Complex.continuous_re.tendsto z).comp hlim)
      (hpos.mono fun _ ha => ha.2)

theorem pairing_tendsto {A : Type w} {I : Type u} {J : Type v}
    [Fintype J] {l : Filter A} {K : A → I → I → ℂ}
    {L : I → I → ℂ}
    (hK : ∀ a b : I, Tendsto (fun n => K n a b) l (𝓝 (L a b)))
    (idx : J → I) (c d : J → ℂ) :
    Tendsto (fun n => pairing (K n) idx c d) l (𝓝 (pairing L idx c d)) := by
  unfold pairing
  refine tendsto_finset_sum Finset.univ ?_
  intro i _
  refine tendsto_finset_sum Finset.univ ?_
  intro j _
  exact tendsto_const_nhds.mul (hK (idx i) (idx j))

theorem Q_nonnegative_of_entrywise_tendsto {A : Type w}
    {I : Type u} {J : Type v} [Fintype J]
    {l : Filter A} [NeBot l] {K : A → I → I → ℂ} {L : I → I → ℂ}
    (hK : ∀ a b : I, Tendsto (fun n => K n a b) l (𝓝 (L a b)))
    (idx : J → I) (c : J → ℂ)
    (hpos : ∀ᶠ n in l, NonnegativeComplex (Q (K n) idx c)) :
    NonnegativeComplex (Q L idx c) :=
  nonnegativeComplex_of_tendsto (pairing_tendsto hK idx c c) hpos

/-- The cutoff is quantified inside the finite test. -/
theorem all_finite_tests_nonnegative_of_entrywise_tendsto
    {I : Type u} {K : ℕ → I → I → ℂ} {L : I → I → ℂ}
    (hK : ∀ a b : I, Tendsto (fun n => K n a b) atTop (𝓝 (L a b)))
    (hpos : ∀ (J : Type v) [Fintype J] (idx : J → I) (c : J → ℂ),
      ∃ N : ℕ, ∀ n ≥ N, NonnegativeComplex (Q (K n) idx c)) :
    ∀ (J : Type v) [Fintype J] (idx : J → I) (c : J → ℂ),
      NonnegativeComplex (Q L idx c) := by
  intro J _ idx c
  exact Q_nonnegative_of_entrywise_tendsto hK idx c
    (Filter.eventually_atTop.2 (hpos J idx c))

-- NATIVE CHILD 1

theorem pairing_add_left {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (c₁ c₂ d : J → ℂ) :
    pairing K idx (fun i => c₁ i + c₂ i) d =
      pairing K idx c₁ d + pairing K idx c₂ d := by
  simp only [pairing, map_add, add_mul, Finset.sum_add_distrib]

theorem pairing_add_right {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (c d₁ d₂ : J → ℂ) :
    pairing K idx c (fun j => d₁ j + d₂ j) =
      pairing K idx c d₁ + pairing K idx c d₂ := by
  simp only [pairing, mul_add, add_mul, Finset.sum_add_distrib]

theorem pairing_mul_left {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (a : ℂ) (c d : J → ℂ) :
    pairing K idx (fun i => a * c i) d =
      starRingEnd ℂ a * pairing K idx c d := by
  simp only [pairing, map_mul, Finset.mul_sum, mul_assoc]

theorem pairing_mul_right {I : Type u} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (idx : J → I) (a : ℂ) (c d : J → ℂ) :
    pairing K idx c (fun j => a * d j) = a * pairing K idx c d := by
  simp only [pairing, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  ring

theorem Q_pullback {I : Type u} {B : Type w} {J : Type v} [Fintype J]
    (K : I → I → ℂ) (p : B → I) (idx : J → B) (c : J → ℂ) :
    Q (fun a b => K (p a) (p b)) idx c = Q K (p ∘ idx) c :=
  rfl

theorem pullback_nonnegative {I : Type u} {B : Type w}
    (K : I → I → ℂ) (p : B → I)
    (hK : ∀ (J : Type v) [Fintype J] (idx : J → I) (c : J → ℂ),
      NonnegativeComplex (Q K idx c)) :
    ∀ (J : Type v) [Fintype J] (idx : J → B) (c : J → ℂ),
      NonnegativeComplex (Q (fun a b => K (p a) (p b)) idx c) := by
  intro J _ idx c
  rw [Q_pullback]
  exact hK J (p ∘ idx) c

@[simp] theorem pairing_zero_kernel {I : Type u} {J : Type v} [Fintype J]
    (idx : J → I) (c d : J → ℂ) :
    pairing (fun _ _ : I => 0) idx c d = 0 := by
  simp [pairing]

theorem zero_kernel_nonnegative {I : Type u} {J : Type v} [Fintype J]
    (idx : J → I) (c : J → ℂ) :
    NonnegativeComplex (Q (fun _ _ : I => 0) idx c) := by
  simp [Q, NonnegativeComplex]

theorem one_point_identity_control :
    Q (fun _ _ : Fin 1 => (1 : ℂ)) id (fun _ => Complex.I) = 1 ∧
    (∑ _i : Fin 1, ∑ _j : Fin 1, Complex.I * Complex.I * (1 : ℂ)) = -1 := by
  have hstar : starRingEnd ℂ Complex.I = -Complex.I := by
    apply Complex.ext <;> simp
  have hsquare : Complex.I * Complex.I = (-1 : ℂ) := by
    apply Complex.ext <;>
      norm_num [Complex.mul_re, Complex.mul_im]
  constructor
  · simp [Q, pairing, Fin.sum_univ_one, hstar, neg_mul, hsquare]
  · simp [Fin.sum_univ_one, hsquare]

theorem one_point_imaginary_control :
    let z := Q (fun _ _ : Fin 1 => Complex.I) id (fun _ => 1)
    z.re = 0 ∧ z.im = 1 ∧ ¬ NonnegativeComplex z := by
  have hQ : Q (fun _ _ : Fin 1 => Complex.I) id (fun _ => 1) = Complex.I := by
    simp [Q, pairing, Fin.sum_univ_one]
  change
    (Q (fun _ _ : Fin 1 => Complex.I) id (fun _ => 1)).re = 0 ∧
    (Q (fun _ _ : Fin 1 => Complex.I) id (fun _ => 1)).im = 1 ∧
    ¬ NonnegativeComplex (Q (fun _ _ : Fin 1 => Complex.I) id (fun _ => 1))
  rw [hQ]
  refine ⟨rfl, rfl, ?_⟩
  intro h
  have him : (1 : ℝ) = 0 := h.1
  exact one_ne_zero him

-- NATIVE CHILD 2

def reflectedPairing {X : Type w} [Fintype X]
    (weight : X → ℂ) (theta : X → X) (F G : X → ℂ) : ℂ :=
  ∑ x : X, weight x * starRingEnd ℂ (F x) * G x

def reflectedKernel {X : Type w} {I : Type u} [Fintype X]
    (weight : X → ℂ) (theta : X → X) (f : I → X → ℂ) : I → I → ℂ :=
  fun a b => reflectedPairing weight theta (f a) (f b)

theorem reflectedPairing_expansion {X : Type w} {I : Type u} {J : Type v}
    [Fintype X] [Fintype J] (weight : X → ℂ) (theta : X → X)
    (f : I → X → ℂ) (idx : J → I) (c d : J → ℂ) :
    reflectedPairing weight theta
        (fun x => ∑ i : J, c i * f (idx i) x)
        (fun x => ∑ j : J, d j * f (idx j) x) =
      pairing (reflectedKernel weight theta f) idx c d := by
  let term (x : X) (i j : J) : ℂ :=
    starRingEnd ℂ (c i) * d j *
      (weight x * starRingEnd ℂ (f (idx i) (theta x)) * f (idx j) x)
  calc
    reflectedPairing weight theta
        (fun x => ∑ i : J, c i * f (idx i) x)
        (fun x => ∑ j : J, d j * f (idx j) x) =
        ∑ x : X, ∑ i : J, ∑ j : J, term x i j := by
      simp only [reflectedPairing, map_sum, map_mul]
      apply Finset.sum_congr rfl
      intro x _
      rw [show weight x * (∑ i : J, starRingEnd ℂ (c i) *
          starRingEnd ℂ (f (idx i) (theta x))) =
          ∑ i : J, weight x * (starRingEnd ℂ (c i) *
            starRingEnd ℂ (f (idx i) (theta x))) by rw [Finset.mul_sum]]
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      dsimp only [term]
      ring
    _ = ∑ i : J, ∑ x : X, ∑ j : J, term x i j := Finset.sum_comm
    _ = ∑ i : J, ∑ j : J, ∑ x : X, term x i j := by
      apply Finset.sum_congr rfl
      intro i _
      exact Finset.sum_comm
    _ = pairing (reflectedKernel weight theta f) idx c d := by
      simp only [pairing, reflectedKernel, reflectedPairing, Finset.mul_sum, term]

/-- Regulators may have different finite configuration spaces, but share test labels. -/
theorem reflected_regulator_limit {I : Type u} {X : ℕ → Type w}
    [∀ n, Fintype (X n)] (weight : ∀ n, X n → ℂ)
    (theta : ∀ n, X n → X n) (f : ∀ n, I → X n → ℂ) (L : I → I → ℂ)
    (hK : ∀ a b : I, Tendsto
      (fun n => reflectedKernel (weight n) (theta n) (f n) a b) atTop (𝓝 (L a b)))
    (hpos : ∀ (J : Type v) [Fintype J] (idx : J → I) (c : J → ℂ),
      ∀ᶠ n in atTop, NonnegativeComplex (reflectedPairing (weight n) (theta n)
        (fun x => ∑ i : J, c i * f n (idx i) x)
        (fun x => ∑ i : J, c i * f n (idx i) x))) :
    ∀ (J : Type v) [Fintype J] (idx : J → I) (c : J → ℂ),
      NonnegativeComplex (Q L idx c) := by
  intro J _ idx c
  apply Q_nonnegative_of_entrywise_tendsto hK idx c
  filter_upwards [hpos J idx c] with n hn
  simpa only [reflectedPairing_expansion, Q] using hn

def pushforwardWeight {X : Type w} {Y : Type u} [Fintype X] [DecidableEq Y]
    (weight : X → ℂ) (q : X → Y) (y : Y) : ℂ :=
  ∑ x : X, if q x = y then weight x else 0

/-- Exact finite pushforward; no fresh averaging or new quotient action is inserted. -/
theorem reflectedPairing_pushforward {X : Type w} {Y : Type u}
    [Fintype X] [Fintype Y] [DecidableEq Y]
    (weight : X → ℂ) (q : X → Y) (thetaX : X → X) (thetaY : Y → Y)
    (commutes : ∀ x, q (thetaX x) = thetaY (q x)) (F G : Y → ℂ) :
    reflectedPairing (pushforwardWeight weight q) thetaY F G =
      reflectedPairing weight thetaX (F ∘ q) (G ∘ q) := by
  unfold reflectedPairing pushforwardWeight
  simp only [Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x _
  simp [ite_mul, Function.comp_apply, commutes x]

theorem pushforward_nonnegative {X : Type w} {Y : Type u}
    [Fintype X] [Fintype Y] [DecidableEq Y]
    (weight : X → ℂ) (q : X → Y) (thetaX : X → X) (thetaY : Y → Y)
    (commutes : ∀ x, q (thetaX x) = thetaY (q x)) (F : Y → ℂ)
    (hpos : NonnegativeComplex (reflectedPairing weight thetaX (F ∘ q) (F ∘ q))) :
    NonnegativeComplex (reflectedPairing (pushforwardWeight weight q) thetaY F F) := by
  rw [reflectedPairing_pushforward weight q thetaX thetaY commutes F F]
  exact hpos

-- A Hermitian kernel can pass all real two-coordinate tests and fail a complex test.
def complexOnlyKernel (i j : Fin 2) : ℂ :=
  if i = j then 1 else if i = 0 then 2 * Complex.I else -2 * Complex.I

theorem complexOnlyKernel_hermitian (i j : Fin 2) :
    starRingEnd ℂ (complexOnlyKernel j i) = complexOnlyKernel i j := by
  fin_cases i <;> fin_cases j <;>
    apply Complex.ext <;> norm_num [complexOnlyKernel, Complex.mul_re, Complex.mul_im]

theorem real_coefficients_control (a b : ℝ) :
    Q complexOnlyKernel id (fun i : Fin 2 => if i = 0 then (a : ℂ) else (b : ℂ)) =
        ((a ^ 2 + b ^ 2 : ℝ) : ℂ) ∧
    NonnegativeComplex (Q complexOnlyKernel id
      (fun i : Fin 2 => if i = 0 then (a : ℂ) else (b : ℂ))) := by
  have heq : Q complexOnlyKernel id
      (fun i : Fin 2 => if i = 0 then (a : ℂ) else (b : ℂ)) =
        ((a ^ 2 + b ^ 2 : ℝ) : ℂ) := by
    simp [Q, pairing, Fin.sum_univ_two, complexOnlyKernel]
    ring
  rw [heq]
  exact ⟨rfl, ⟨rfl, add_nonneg (sq_nonneg a) (sq_nonneg b)⟩⟩

theorem complex_coefficients_negative :
    Q complexOnlyKernel id (fun i : Fin 2 => if i = 0 then 1 else Complex.I) = -2 := by
  apply Complex.ext <;>
    norm_num [Q, pairing, Fin.sum_univ_two, complexOnlyKernel, Complex.mul_re, Complex.mul_im]

def swap (i : Fin 2) : Fin 2 := if i = 0 then 1 else 0
def alternating (i : Fin 2) : ℂ := if i = 0 then 1 else -1

theorem swap_involutive (i : Fin 2) : swap (swap i) = i := by
  fin_cases i <;> norm_num [swap]

theorem positive_weights_normalized :
    (∑ _ : Fin 2, (1 / 2 : ℝ)) = 1 ∧ (0 : ℝ) < 1 / 2 := by
  norm_num [Fin.sum_univ_two]

theorem reflection_sensitive_control :
    reflectedPairing (fun _ : Fin 2 => 1 / 2) swap alternating alternating = -1 ∧
    reflectedPairing (fun _ : Fin 2 => 1 / 2) id alternating alternating = 1 := by
  norm_num [reflectedPairing, Fin.sum_univ_two, swap, alternating]

#print axioms NonnegativeComplex
#print axioms pairing
#print axioms Q
#print axioms nonnegativeComplex_of_tendsto
#print axioms pairing_tendsto
#print axioms Q_nonnegative_of_entrywise_tendsto
#print axioms all_finite_tests_nonnegative_of_entrywise_tendsto
#print axioms pairing_add_left
#print axioms pairing_add_right
#print axioms pairing_mul_left
#print axioms pairing_mul_right
#print axioms Q_pullback
#print axioms pullback_nonnegative
#print axioms pairing_zero_kernel
#print axioms zero_kernel_nonnegative
#print axioms one_point_identity_control
#print axioms one_point_imaginary_control
#print axioms reflectedPairing
#print axioms reflectedKernel
#print axioms reflectedPairing_expansion
#print axioms reflected_regulator_limit
#print axioms pushforwardWeight
#print axioms reflectedPairing_pushforward
#print axioms pushforward_nonnegative
#print axioms complexOnlyKernel
#print axioms complexOnlyKernel_hermitian
#print axioms real_coefficients_control
#print axioms complex_coefficients_negative
#print axioms swap
#print axioms alternating
#print axioms swap_involutive
#print axioms positive_weights_normalized
#print axioms reflection_sensitive_control

end Millennium.G4.ComplexRP
