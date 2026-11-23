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
    emit("A4 CHILD bounds\n");
    emit("A4 LEAN import Mathlib.Topology.Instances.Real.Lemmas\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Exp\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN open Filter Topology\n");
    emit("A4 LEAN namespace YangMills.Observable\n");
    emit("A4 LEAN theorem separatedTimeWitness {C : Nat → ℝ} {c lo hi : ℝ}\n");
    emit("A4 LEAN     (lim : Tendsto C atTop (𝓝 c)) (pos : 0 < lo)\n");
    emit("A4 LEAN     (lower : ∀ᶠ n in atTop, lo ≤ C n) (upper : ∀ᶠ n in atTop, C n ≤ hi) :\n");
    emit("A4 LEAN     lo ≤ c ∧ c ≤ hi ∧ 0 < c := by\n");
#elif ROLE == 1
    emit("A4 CHILD positivity\n");
    emit("A4 LEAN   have hlo : lo ≤ c := ge_of_tendsto lim lower\n");
    emit("A4 LEAN   have hhi : c ≤ hi := le_of_tendsto lim upper\n");
#else
    emit("A4 LEAN   exact ⟨hlo, hhi, lt_of_lt_of_le pos hlo⟩\n");
    emit("A4 LEAN theorem momentLowerBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ) (t : ℝ)\n");
    emit("A4 LEAN     (hw : ∀ i ∈ s, 0 ≤ w i) :\n");
    emit("A4 LEAN     (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i) ≤\n");
    emit("A4 LEAN       ∑ i ∈ s, w i * Real.exp (-t * E i) := by\n");
    emit("A4 LEAN   rw [Finset.mul_sum, ← Finset.sum_sub_distrib]\n");
    emit("A4 LEAN   apply Finset.sum_le_sum\n");
    emit("A4 LEAN   intro i hi\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     w i - t * (w i * E i) = w i * ((-t * E i) + 1) := by ring\n");
    emit("A4 LEAN     _ ≤ _ := mul_le_mul_of_nonneg_left (Real.add_one_le_exp _) (hw i hi)\n");
    emit("A4 LEAN end YangMills.Observable\n");
    emit("A4 LEAN #print axioms YangMills.Observable.separatedTimeWitness\n");
#endif
#if ROLE == 2
    emit("A4 LEAN #print axioms YangMills.Observable.momentLowerBound\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
