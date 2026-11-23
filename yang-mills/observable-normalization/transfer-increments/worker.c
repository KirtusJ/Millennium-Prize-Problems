/* A bounded proof-template worker for the PCP OS user ABI. ROLE selects a subgoal. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;
static long sys(long n,long a,long b,long c) {
    long result;
    __asm__ volatile("syscall":"=a"(result):"a"(n),"D"(a),"S"(b),"d"(c):"rcx","r11","memory");
    return result;
}
static void emit(const char *s) {
    unsigned len=0;
    while(s[len]) ++len;
    while(len){
        long k=sys(1,1,(long)s,len);
        if(k<=0 || (unsigned long)k>len){sys(60,1,0,0);__builtin_unreachable();}
        len-=(unsigned)k;s+=k;
    }
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Topology.Instances.Real.Lemmas\n");
    emit("A4 LEAN import Mathlib.Algebra.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Exp\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Filter Topology\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.Observable\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Iterating a positive contraction loses at most k times its one-step defect. -/\n");
    emit("A4 LEAN theorem powerLoss (x : ℝ) (hx : 0 ≤ x) (h1 : x ≤ 1) (k : ℕ) :\n");
    emit("A4 LEAN     1 - x ^ k ≤ k * (1 - x) := by\n");
    emit("A4 LEAN   induction k with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ k ih =>\n");
    emit("A4 LEAN     have hp : x ^ k ≤ 1 := pow_le_one₀ hx h1\n");
    emit("A4 LEAN     have h := mul_le_mul_of_nonneg_right hp (sub_nonneg.mpr h1)\n");
    emit("A4 LEAN     rw [pow_succ, Nat.cast_succ]\n");
    emit("A4 LEAN     linarith\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The cutoff input is the one-step Dirichlet form of this same observable. -/\n");
    emit("A4 LEAN theorem spectralPowerLoss {ι : Type*} (s : Finset ι) (w x : ι → ℝ)\n");
    emit("A4 LEAN     (hw : ∀ i ∈ s, 0 ≤ w i) (hx : ∀ i ∈ s, 0 ≤ x i ∧ x i ≤ 1) (k : ℕ) :\n");
    emit("A4 LEAN     (∑ i ∈ s, w i) - (∑ i ∈ s, w i * x i ^ k) ≤\n");
    emit("A4 LEAN       k * (∑ i ∈ s, w i * (1 - x i)) := by\n");
    emit("A4 LEAN   rw [← Finset.sum_sub_distrib, Finset.mul_sum]\n");
    emit("A4 LEAN   apply Finset.sum_le_sum\n");
    emit("A4 LEAN   intro i hi\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left (powerLoss (x i) (hx i hi).1 (hx i hi).2 k) (hw i hi)\n");
    emit("A4 LEAN   linarith only [h]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Apply a separate one-step defect bound to each factor in a Bessel ratio. -/\n");
    emit("A4 LEAN theorem productLoss (xs : List ℝ) (unit : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ 1) :\n");
    emit("A4 LEAN     1 - xs.prod ≤ (xs.map (fun x => 1 - x)).sum := by\n");
    emit("A4 LEAN   induction xs with\n");
    emit("A4 LEAN   | nil => simp\n");
    emit("A4 LEAN   | cons x xs ih =>\n");
    emit("A4 LEAN     have hx := unit x (List.mem_cons_self ..)\n");
    emit("A4 LEAN     have ht : ∀ y ∈ xs, 0 ≤ y ∧ y ≤ 1 :=\n");
    emit("A4 LEAN       fun y hy => unit y (List.mem_cons_of_mem _ hy)\n");
    emit("A4 LEAN     have tail := ih ht\n");
    emit("A4 LEAN     have nonneg : 0 ≤ (xs.map (fun y => 1 - y)).sum := by\n");
    emit("A4 LEAN       apply List.sum_nonneg\n");
    emit("A4 LEAN       intro z hz\n");
    emit("A4 LEAN       obtain ⟨y, hy, rfl⟩ := List.mem_map.mp hz\n");
    emit("A4 LEAN       exact sub_nonneg.mpr (ht y hy).2\n");
    emit("A4 LEAN     have hscale := mul_le_mul_of_nonneg_left tail hx.1\n");
    emit("A4 LEAN     have hcap := mul_le_mul_of_nonneg_right hx.2 nonneg\n");
    emit("A4 LEAN     simp only [List.prod_cons, List.map_cons, List.sum_cons]\n");
    emit("A4 LEAN     linarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- This interface allows different cutoffs and step counts, with a shared time budget. -/\n");
    emit("A4 LEAN theorem positiveTransferLimit {C V D a : ℕ → ℝ} {k : ℕ → ℕ} {c v M t : ℝ}\n");
    emit("A4 LEAN     (lim : Tendsto C atTop (𝓝 c)) (margin : 0 < v - t * M) (hM : 0 ≤ M)\n");
    emit("A4 LEAN     (controls : ∀ᶠ n in atTop, v ≤ V n ∧ V n - C n ≤ k n * D n ∧\n");
    emit("A4 LEAN       D n ≤ a n * M ∧ k n * a n ≤ t) :\n");
    emit("A4 LEAN     v - t * M ≤ c ∧ 0 < c := by\n");
    emit("A4 LEAN   have hl : v - t * M ≤ c := by\n");
    emit("A4 LEAN     apply ge_of_tendsto lim\n");
    emit("A4 LEAN     filter_upwards [controls] with n hn\n");
    emit("A4 LEAN     rcases hn with ⟨hv, hdrop, hdef, htime⟩\n");
    emit("A4 LEAN     have hk : 0 ≤ (k n : ℝ) := Nat.cast_nonneg _\n");
    emit("A4 LEAN     have hbound : (k n : ℝ) * D n ≤ t * M := calc\n");
    emit("A4 LEAN       _ ≤ (k n : ℝ) * (a n * M) := mul_le_mul_of_nonneg_left hdef hk\n");
    emit("A4 LEAN       _ = ((k n : ℝ) * a n) * M := (mul_assoc _ _ _).symm\n");
    emit("A4 LEAN       _ ≤ t * M := mul_le_mul_of_nonneg_right htime hM\n");
    emit("A4 LEAN     linarith\n");
    emit("A4 LEAN   exact ⟨hl, margin.trans_le hl⟩\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- B4's proposed tangent at q works at every nonnegative separation. -/\n");
    emit("A4 LEAN theorem tangentMomentBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ)\n");
    emit("A4 LEAN     {v q t : ℝ} (hq : 0 ≤ q) (ht : 0 ≤ t) (hw : ∀ i ∈ s, 0 ≤ w i)\n");
    emit("A4 LEAN     (mass : v ≤ ∑ i ∈ s, w i) (moment : (∑ i ∈ s, w i * E i) ≤ v * q) :\n");
    emit("A4 LEAN     v * Real.exp (-t * q) ≤ ∑ i ∈ s, w i * Real.exp (-t * E i) := by\n");
    emit("A4 LEAN   let b := Real.exp (-t * q)\n");
    emit("A4 LEAN   have hb : 0 ≤ b := (Real.exp_pos _).le\n");
    emit("A4 LEAN   have hcoef : 0 ≤ 1 + t * q := by linarith [mul_nonneg ht hq]\n");
    emit("A4 LEAN   have hmass := mul_le_mul_of_nonneg_left mass hcoef\n");
    emit("A4 LEAN   have hmom := mul_le_mul_of_nonneg_left moment ht\n");
    emit("A4 LEAN   have hmin : v ≤ (1+t*q) * (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i) := by\n");
    emit("A4 LEAN     linarith only [hmass, hmom]\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     v * b ≤ ((1+t*q) * (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i)) * b :=\n");
    emit("A4 LEAN       mul_le_mul_of_nonneg_right hmin hb\n");
    emit("A4 LEAN     _ = ∑ i ∈ s, w i * (b * ((t*q - t*E i) + 1)) := by\n");
    emit("A4 LEAN       rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib, Finset.sum_mul]\n");
    emit("A4 LEAN       apply Finset.sum_congr rfl\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       ring\n");
    emit("A4 LEAN     _ ≤ _ := by\n");
    emit("A4 LEAN       apply Finset.sum_le_sum\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       apply mul_le_mul_of_nonneg_left _ (hw i hi)\n");
    emit("A4 LEAN       calc\n");
    emit("A4 LEAN         b * ((t*q - t*E i) + 1) ≤ b * Real.exp (t*q - t*E i) :=\n");
    emit("A4 LEAN           mul_le_mul_of_nonneg_left (Real.add_one_le_exp _) hb\n");
    emit("A4 LEAN         _ = Real.exp (-t*E i) := by\n");
    emit("A4 LEAN           dsimp [b]\n");
    emit("A4 LEAN           rw [← Real.exp_add]\n");
    emit("A4 LEAN           congr 1\n");
    emit("A4 LEAN           ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sharpMomentBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ)\n");
    emit("A4 LEAN     {v M t : ℝ} (hv : 0 < v) (hM : 0 ≤ M) (ht : 0 ≤ t)\n");
    emit("A4 LEAN     (hw : ∀ i ∈ s, 0 ≤ w i) (mass : v ≤ ∑ i ∈ s, w i)\n");
    emit("A4 LEAN     (moment : (∑ i ∈ s, w i * E i) ≤ M) :\n");
    emit("A4 LEAN     v * Real.exp (-t * (M / v)) ≤ ∑ i ∈ s, w i * Real.exp (-t * E i) := by\n");
    emit("A4 LEAN   apply tangentMomentBound s w E (div_nonneg hM hv.le) ht hw mass\n");
    emit("A4 LEAN   simpa [mul_div_cancel₀ M hv.ne', mul_comm v (M / v)] using moment\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.Observable\n");
    emit("A4 LEAN #print axioms YangMills.Observable.powerLoss\n");
    emit("A4 LEAN #print axioms YangMills.Observable.spectralPowerLoss\n");
    emit("A4 LEAN #print axioms YangMills.Observable.positiveTransferLimit\n");
    emit("A4 LEAN #print axioms YangMills.Observable.productLoss\n");
    emit("A4 LEAN #print axioms YangMills.Observable.tangentMomentBound\n");
    emit("A4 LEAN #print axioms YangMills.Observable.sharpMomentBound\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
