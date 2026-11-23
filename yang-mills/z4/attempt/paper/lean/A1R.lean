import Mathlib

/-!
# A1R: elementary inequalities of Theorem R (A1_REDUCTION.md), finite atom sums

Predicates fixed before the first run (rule 3):
* every theorem below compiles with no `sorry`;
* `#print axioms` for each shows only `propext`, `Classical.choice`, `Quot.sound`.
Hypotheses are kept minimal: each theorem states exactly what it uses.
-/

open Real Finset BigOperators

namespace A1R

variable {ι : Type*}

/-- C(t) = ∑_i w_i exp(-t E_i). -/
noncomputable def C (s : Finset ι) (w E : ι → ℝ) (t : ℝ) : ℝ :=
  ∑ i ∈ s, w i * exp (-(t * E i))

/-- Tail above K, in the normalization at t = 1: ∑_{E_i > K} w_i exp(-E_i). -/
noncomputable def T (s : Finset ι) (w E : ι → ℝ) (K : ℝ) : ℝ :=
  ∑ i ∈ s.filter (fun i => K < E i), w i * exp (-(E i))

/-- Mean energy Ebar = (∑ w_i E_i e^{-E_i}) / C(1). -/
noncomputable def Ebar (s : Finset ι) (w E : ι → ℝ) : ℝ :=
  (∑ i ∈ s, w i * E i * exp (-(E i))) / C s w E 1

lemma C_one (s : Finset ι) (w E : ι → ℝ) : C s w E 1 = ∑ i ∈ s, w i * exp (-(E i)) := by
  simp [C]

lemma C_nonneg (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (t : ℝ) :
    0 ≤ C s w E t :=
  Finset.sum_nonneg fun i hi => mul_nonneg (hw i hi) (exp_pos _).le

/-- L2 (general form). Uses only w ≥ 0 and c ≤ 1. No E ≥ 1, no c > 0, no sign of D. -/
theorem L2 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (c D : ℝ) (hc : c ≤ 1)
    (hC : C s w E c ≤ D * C s w E 1) (K : ℝ) :
    T s w E K ≤ D * exp (-((1 - c) * K)) * C s w E 1 := by
  have step : T s w E K ≤ exp (-((1 - c) * K)) * C s w E c := by
    unfold T C
    rw [Finset.mul_sum]
    calc ∑ i ∈ s.filter (fun i => K < E i), w i * exp (-(E i))
        ≤ ∑ i ∈ s.filter (fun i => K < E i), exp (-((1 - c) * K)) * (w i * exp (-(c * E i))) := by
          apply Finset.sum_le_sum
          intro i hi
          rw [Finset.mem_filter] at hi
          have h1 : exp (-(E i)) ≤ exp (-((1 - c) * K)) * exp (-(c * E i)) := by
            rw [← exp_add]
            apply exp_le_exp.mpr
            nlinarith [hi.2]
          calc w i * exp (-(E i)) ≤ w i * (exp (-((1 - c) * K)) * exp (-(c * E i))) :=
                mul_le_mul_of_nonneg_left h1 (hw i hi.1)
            _ = _ := by ring
      _ ≤ ∑ i ∈ s, exp (-((1 - c) * K)) * (w i * exp (-(c * E i))) := by
          apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
          intro i hi _
          exact mul_nonneg (exp_pos _).le (mul_nonneg (hw i hi) (exp_pos _).le)
  calc T s w E K ≤ exp (-((1 - c) * K)) * C s w E c := step
    _ ≤ exp (-((1 - c) * K)) * (D * C s w E 1) := mul_le_mul_of_nonneg_left hC (exp_pos _).le
    _ = D * exp (-((1 - c) * K)) * C s w E 1 := by ring

/-- L1 (R2, tightness) as the case c = 1/2 of L2. Uses only w ≥ 0. -/
theorem L1 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (D : ℝ)
    (hC : C s w E (1 / 2) ≤ D * C s w E 1) (K : ℝ) :
    T s w E K ≤ D * exp (-K / 2) * C s w E 1 := by
  have h := L2 s w E hw (1 / 2) D (by norm_num) hC K
  have e : -((1 - 1 / 2 : ℝ) * K) = -K / 2 := by ring
  rwa [e] at h

/-- L3 (R4 upper). Uses w ≥ 0, E_i ≥ 1, t ≥ 1. -/
theorem L3 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hE : ∀ i ∈ s, 1 ≤ E i)
    (t : ℝ) (ht : 1 ≤ t) : C s w E t ≤ exp (-(t - 1)) * C s w E 1 := by
  unfold C
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have h1 : exp (-(t * E i)) ≤ exp (-(t - 1)) * exp (-(1 * E i)) := by
    rw [← exp_add]
    apply exp_le_exp.mpr
    nlinarith [hE i hi]
  calc w i * exp (-(t * E i)) ≤ w i * (exp (-(t - 1)) * exp (-(1 * E i))) :=
        mul_le_mul_of_nonneg_left h1 (hw i hi)
    _ = _ := by ring

/-- L4 (R4 lower, Jensen via the tangent line of exp). Uses only w ≥ 0 and C(1) > 0;
holds for EVERY real t (t ≥ 1 is not needed), and E ≥ 1 is not needed. -/
theorem L4 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hpos : 0 < C s w E 1)
    (t : ℝ) : C s w E 1 * exp (-(t - 1) * Ebar s w E) ≤ C s w E t := by
  obtain ⟨m, hm⟩ : ∃ m : ℝ, m = -(t - 1) * Ebar s w E := ⟨_, rfl⟩
  rw [← hm]
  have tang : ∀ x : ℝ, exp m * (1 + x - m) ≤ exp x := by
    intro x
    have := add_one_le_exp (x - m)
    have h2 : exp x = exp m * exp (x - m) := by rw [← exp_add]; ring_nf
    rw [h2]
    have := mul_le_mul_of_nonneg_left this (exp_pos m).le
    linarith
  have key : ∀ i ∈ s, w i * exp (-(E i)) * (exp m * (1 + (-(t - 1) * E i) - m))
      ≤ w i * exp (-(t * E i)) := by
    intro i hi
    have h3 : exp (-(t * E i)) = exp (-(E i)) * exp (-(t - 1) * E i) := by
      rw [← exp_add]; ring_nf
    rw [h3]
    have := mul_le_mul_of_nonneg_left (tang (-(t - 1) * E i))
      (mul_nonneg (hw i hi) (exp_pos (-(E i))).le)
    linarith
  have hsum := Finset.sum_le_sum key
  have hEb : (∑ i ∈ s, w i * E i * exp (-(E i))) = Ebar s w E * C s w E 1 := by
    unfold Ebar; field_simp [hpos.ne']
  have lhs : ∑ i ∈ s, w i * exp (-(E i)) * (exp m * (1 + (-(t - 1) * E i) - m))
      = exp m * (1 - m) * (∑ i ∈ s, w i * exp (-(E i)))
        + exp m * (-(t - 1)) * (∑ i ∈ s, w i * E i * exp (-(E i))) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl; intro i _; ring
  rw [lhs, hEb, ← C_one] at hsum
  have : exp m * (1 - m) * C s w E 1 + exp m * (-(t - 1)) * (Ebar s w E * C s w E 1)
      = C s w E 1 * exp m := by
    rw [hm]; ring
  rw [this] at hsum
  exact hsum

/-- L5 (mean energy). Uses w ≥ 0, C(1) > 0, C(1/2) ≤ D C(1). No E ≥ 1 needed. -/
theorem L5 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hpos : 0 < C s w E 1)
    (D : ℝ) (hC : C s w E (1 / 2) ≤ D * C s w E 1) : Ebar s w E ≤ 2 * log D := by
  have h4 := L4 s w E hw hpos (1 / 2)
  have h5 : C s w E 1 * exp (Ebar s w E / 2) ≤ D * C s w E 1 := by
    have e : -((1 / 2 : ℝ) - 1) * Ebar s w E = Ebar s w E / 2 := by ring
    rw [e] at h4; linarith
  have h6 : exp (Ebar s w E / 2) ≤ D := by
    have := h5; rw [mul_comm D] at this
    exact le_of_mul_le_mul_left this hpos
  have h7 : Ebar s w E / 2 ≤ log D := by
    rw [← log_exp (Ebar s w E / 2)]
    exact log_le_log (exp_pos _) h6
  linarith

/-- The remark "D ≥ 1 follows" needs E ≥ 0 (here: E ≥ 1 gives D ≥ e^{1/2}). -/
theorem D_ge (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hE : ∀ i ∈ s, 1 ≤ E i)
    (hpos : 0 < C s w E 1)
    (D : ℝ) (hC : C s w E (1 / 2) ≤ D * C s w E 1) : exp (1 / 2) ≤ D := by
  have h : exp (1 / 2) * C s w E 1 ≤ C s w E (1 / 2) := by
    unfold C; rw [Finset.mul_sum]
    apply Finset.sum_le_sum; intro i hi
    have : exp (1 / 2) * exp (-(1 * E i)) ≤ exp (-(1 / 2 * E i)) := by
      rw [← exp_add]; apply exp_le_exp.mpr; nlinarith [hE i hi]
    nlinarith [hw i hi]
  have := h.trans hC
  exact le_of_mul_le_mul_right this hpos

/-- Without E ≥ 0 the remark "D ≥ 1" is false: one atom at E = -2 gives C(1/2)/C(1) = e^{-1}. -/
theorem D_ge_one_needs_E_nonneg :
    C ({()} : Finset Unit) (fun _ => 1) (fun _ => -2) (1 / 2)
      ≤ exp (-1) * C ({()} : Finset Unit) (fun _ => 1) (fun _ => -2) 1 ∧
    0 < C ({()} : Finset Unit) (fun _ => 1) (fun _ => -2) 1 ∧ exp (-1) < 1 := by
  refine ⟨?_, ?_, ?_⟩
  · simp only [C, Finset.sum_singleton, one_mul]
    rw [← exp_add]; apply le_of_eq; congr 1; norm_num
  · simp only [C, Finset.sum_singleton, one_mul]; exact exp_pos _
  · rw [← exp_zero]; exact exp_lt_exp.mpr (by norm_num)

/-- L6. E_i ∈ [1,2] ⇒ C(1/2) ≤ e · C(1). Only E_i ≤ 2 (and w ≥ 0) is used. -/
theorem L6 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hE : ∀ i ∈ s, E i ≤ 2) :
    C s w E (1 / 2) ≤ exp 1 * C s w E 1 := by
  unfold C; rw [Finset.mul_sum]
  apply Finset.sum_le_sum; intro i hi
  have : exp (-(1 / 2 * E i)) ≤ exp 1 * exp (-(1 * E i)) := by
    rw [← exp_add]; apply exp_le_exp.mpr; nlinarith [hE i hi]
  nlinarith [hw i hi]

/-- L6 sharpness: the constant e is attained (one atom at E = 2), so no D < e works,
in particular not e^{1/2}. -/
theorem L6_sharp :
    C ({()} : Finset Unit) (fun _ => 1) (fun _ => 2) (1 / 2)
      = exp 1 * C ({()} : Finset Unit) (fun _ => 1) (fun _ => 2) 1 ∧
    0 < C ({()} : Finset Unit) (fun _ => 1) (fun _ => 2) 1 := by
  refine ⟨?_, ?_⟩
  · simp only [C, Finset.sum_singleton, one_mul]
    rw [← exp_add]; congr 1; norm_num
  · simp only [C, Finset.sum_singleton, one_mul]; exact exp_pos _

theorem L6_sharp' (D : ℝ) (hD : D < exp 1) :
    ¬ (C ({()} : Finset Unit) (fun _ => 1) (fun _ => 2) (1 / 2)
      ≤ D * C ({()} : Finset Unit) (fun _ => 1) (fun _ => 2) 1) := by
  obtain ⟨h1, h2⟩ := L6_sharp
  rw [h1]; intro h
  have := le_of_mul_le_mul_right h h2
  linarith

/-- Mutation control: L1 with exp(-K/2) replaced by exp(-K) is FALSE.
One atom (w = 1, E = 2) with D = e (admissible by L6_sharp), K = 3/2. -/
theorem mutation_false :
    ¬ (∀ (s : Finset Unit) (w E : Unit → ℝ) (D : ℝ), (∀ i ∈ s, 0 ≤ w i) →
        C s w E (1 / 2) ≤ D * C s w E 1 →
        ∀ K : ℝ, T s w E K ≤ D * exp (-K) * C s w E 1) := by
  intro h
  have := h {()} (fun _ => 1) (fun _ => 2) (exp 1) (by simp) (le_of_eq L6_sharp.1) (3 / 2)
  simp only [T, C, Finset.sum_singleton, one_mul] at this
  rw [Finset.filter_true_of_mem (by intro i _; norm_num), Finset.sum_singleton,
    ← exp_add, ← exp_add, exp_le_exp] at this
  norm_num at this

/-- Per-atom layer-cake on integer levels: e^{aE} ≤ 1 + ∑_{k<N, k<E} (e^{a(k+1)} - e^{ak}) when E ≤ N, a ≥ 0. -/
lemma layer (a : ℝ) (ha : 0 ≤ a) : ∀ (N : ℕ) (x : ℝ), x ≤ N →
    exp (a * x) ≤ 1 + ∑ k ∈ Finset.range N,
      (if (k : ℝ) < x then exp (a * (k + 1)) - exp (a * k) else 0) := by
  intro N
  induction N with
  | zero =>
    intro x hx
    simp only [Finset.range_zero, Finset.sum_empty, add_zero]
    have : a * x ≤ 0 := by
      have : x ≤ 0 := by simpa using hx
      nlinarith
    calc exp (a * x) ≤ exp 0 := exp_le_exp.mpr this
      _ = 1 := exp_zero
  | succ n ih =>
    intro x hx
    rw [Finset.sum_range_succ]
    by_cases hxn : x ≤ n
    · have h1 := ih x hxn
      have h2 : 0 ≤ (if (n : ℝ) < x then exp (a * (n + 1)) - exp (a * n) else 0) := by
        split_ifs
        · have : exp (a * n) ≤ exp (a * (n + 1)) := exp_le_exp.mpr (by nlinarith)
          linarith
        · exact le_refl 0
      linarith
    · push_neg at hxn
      rw [if_pos hxn]
      have hall : ∑ k ∈ Finset.range n,
          (if (k : ℝ) < x then exp (a * (k + 1)) - exp (a * k) else 0)
          = ∑ k ∈ Finset.range n, (exp (a * ((k + 1 : ℕ) : ℝ)) - exp (a * (k : ℕ))) := by
        apply Finset.sum_congr rfl
        intro k hk
        have hk' : (k : ℝ) < x := by
          have : (k : ℝ) < n := by exact_mod_cast Finset.mem_range.mp hk
          linarith
        rw [if_pos hk']; push_cast; ring_nf
      rw [hall, Finset.sum_range_sub (fun k : ℕ => exp (a * (k : ℝ)))]
      have hx' : x ≤ (n : ℝ) + 1 := by push_cast at hx; linarith
      have : exp (a * x) ≤ exp (a * (n + 1)) := exp_le_exp.mpr (by nlinarith)
      simp only [Nat.cast_zero, mul_zero, exp_zero]
      linarith

/-- L7 (converse of (C) from the tail bound, finite sums). Hypotheses: w ≥ 0, D ≥ 0,
the tail bound at every K (only integer K ≥ 0 are used), 0 ≤ a < 1/2 where a = 1 - c.
Conclusion: ∑ w e^{-(1-a)E} ≤ (1 + D (e^a - 1)/(1 - e^{a - 1/2})) C(1).
No E ≥ 1 is used. -/
theorem L7 (s : Finset ι) (w E : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (D : ℝ) (hD : 0 ≤ D)
    (hT : ∀ K : ℝ, T s w E K ≤ D * exp (-K / 2) * C s w E 1)
    (a : ℝ) (ha0 : 0 ≤ a) (ha : a < 1 / 2) :
    C s w E (1 - a) ≤ (1 + D * (exp a - 1) / (1 - exp (a - 1 / 2))) * C s w E 1 := by
  obtain ⟨N, hN⟩ : ∃ N : ℕ, ∀ i ∈ s, E i ≤ N :=
    ⟨∑ i ∈ s, ⌈E i⌉₊, fun i hi => (Nat.le_ceil _).trans (by
      exact_mod_cast Finset.single_le_sum (f := fun i => ⌈E i⌉₊) (fun _ _ => Nat.zero_le _) hi)⟩
  set d : ℕ → ℝ := fun k => exp (a * (k + 1)) - exp (a * k) with hd
  set q := exp (a - 1 / 2) with hq
  have hq1 : q < 1 := by
    have : exp (a - 1 / 2) < exp 0 := exp_lt_exp.mpr (by linarith)
    rwa [exp_zero] at this
  have hq0 : 0 ≤ q := (exp_pos _).le
  -- step 1: per atom
  have step1 : C s w E (1 - a) ≤ ∑ i ∈ s, w i * exp (-(E i)) *
      (1 + ∑ k ∈ Finset.range N, (if (k : ℝ) < E i then d k else 0)) := by
    unfold C
    apply Finset.sum_le_sum
    intro i hi
    have h := layer a ha0 N (E i) (hN i hi)
    have e : exp (-((1 - a) * E i)) = exp (-(E i)) * exp (a * E i) := by
      rw [← exp_add]; ring_nf
    rw [e, ← mul_assoc]
    exact mul_le_mul_of_nonneg_left h (mul_nonneg (hw i hi) (exp_pos _).le)
  -- step 2: swap sums
  have step2 : ∑ i ∈ s, w i * exp (-(E i)) *
      (1 + ∑ k ∈ Finset.range N, (if (k : ℝ) < E i then d k else 0))
      = C s w E 1 + ∑ k ∈ Finset.range N, d k * T s w E k := by
    rw [C_one]
    simp only [mul_add, mul_one, Finset.sum_add_distrib, Finset.mul_sum]
    congr 1
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro k _
    unfold T
    rw [Finset.mul_sum, Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro i _
    split_ifs <;> ring
  -- step 3: bound each layer
  have step3 : ∑ k ∈ Finset.range N, d k * T s w E k
      ≤ ∑ k ∈ Finset.range N, D * (exp a - 1) * C s w E 1 * q ^ k := by
    apply Finset.sum_le_sum
    intro k _
    have hdk : 0 ≤ d k := by
      simp only [hd]; have := exp_le_exp.mpr (show a * (k : ℝ) ≤ a * (k + 1) by nlinarith)
      linarith
    have hdk' : d k = (exp a - 1) * exp (a * k) := by
      simp only [hd]; rw [sub_mul, ← exp_add]; ring_nf
    have hqk : exp (a * k) * exp (-(k : ℝ) / 2) = q ^ k := by
      rw [hq, ← exp_nat_mul, ← exp_add]; ring_nf
    calc d k * T s w E k ≤ d k * (D * exp (-(k : ℝ) / 2) * C s w E 1) :=
          mul_le_mul_of_nonneg_left (hT k) hdk
      _ = D * (exp a - 1) * C s w E 1 * (exp (a * k) * exp (-(k : ℝ) / 2)) := by
          rw [hdk']; ring
      _ = _ := by rw [hqk]
  -- step 4: geometric series
  have hC1 : 0 ≤ C s w E 1 := C_nonneg s w E hw 1
  have hea : 0 ≤ exp a - 1 := by have := add_one_le_exp a; linarith
  have geo : ∑ k ∈ Finset.range N, q ^ k ≤ 1 / (1 - q) := by
    rw [geom_sum_eq hq1.ne, ← neg_div_neg_eq, neg_sub, neg_sub,
      div_le_div_iff_of_pos_right (by linarith)]
    linarith [pow_nonneg hq0 N]
  have s4 : ∑ k ∈ Finset.range N, D * (exp a - 1) * C s w E 1 * q ^ k
      = D * (exp a - 1) * C s w E 1 * ∑ k ∈ Finset.range N, q ^ k := by
    rw [Finset.mul_sum]
  have hK : 0 ≤ D * (exp a - 1) * C s w E 1 := mul_nonneg (mul_nonneg hD hea) hC1
  have hq1' : (1 - q) ≠ 0 := by linarith
  calc C s w E (1 - a) ≤ C s w E 1 + ∑ k ∈ Finset.range N, d k * T s w E k :=
        step1.trans (le_of_eq step2)
    _ ≤ C s w E 1 + D * (exp a - 1) * C s w E 1 * ∑ k ∈ Finset.range N, q ^ k := by
        rw [← s4]; linarith
    _ ≤ C s w E 1 + D * (exp a - 1) * C s w E 1 * (1 / (1 - q)) :=
        add_le_add_left (mul_le_mul_of_nonneg_left geo hK) _
    _ = (1 + D * (exp a - 1) / (1 - q)) * C s w E 1 := by
        field_simp; ring

end A1R

#print axioms A1R.L1
#print axioms A1R.L2
#print axioms A1R.L3
#print axioms A1R.L4
#print axioms A1R.L5
#print axioms A1R.D_ge
#print axioms A1R.D_ge_one_needs_E_nonneg
#print axioms A1R.L6
#print axioms A1R.L6_sharp'
#print axioms A1R.mutation_false
#print axioms A1R.L7
