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
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Analysis.Convex.Jensen\n");
    emit("A4 LEAN import Mathlib.Analysis.Convex.Mul\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.Observable\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Squared fundamental trace-gradient in SU(2) quaternion coordinates. -/\n");
    emit("A4 LEAN theorem traceGradient {a b c d : ℝ}\n");
    emit("A4 LEAN     (unit : a^2+b^2+c^2+d^2 = 1) :\n");
    emit("A4 LEAN     (-b)^2 + (-c)^2 + (-d)^2 = 1 - (2*a)^2/4 := by\n");
    emit("A4 LEAN   linarith only [unit]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Chain rule factor for the adjoint character A=F²−1. -/\n");
    emit("A4 LEAN theorem adjointGradient (F : ℝ) :\n");
    emit("A4 LEAN     (2*F)^2 * (1-F^2/4) = ((F^2-1)+1)*(3-(F^2-1)) := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Jensen's bound on the transfer spectral measure normalized to unit mass. -/\n");
    emit("A4 LEAN theorem normalizedStepBound {ι : Type*} (s : Finset ι) (p x : ι → ℝ)\n");
    emit("A4 LEAN     (hp : ∀ i ∈ s, 0 ≤ p i) (sum : ∑ i ∈ s, p i = 1)\n");
    emit("A4 LEAN     (hx : ∀ i ∈ s, 0 ≤ x i) (k : ℕ) :\n");
    emit("A4 LEAN     (1 - ∑ i ∈ s, p i * (1 - x i)) ^ k ≤ ∑ i ∈ s, p i * x i ^ k := by\n");
    emit("A4 LEAN   have he : (∑ i ∈ s, p i * (1 - x i)) = 1 - ∑ i ∈ s, p i * x i := by\n");
    emit("A4 LEAN     simp only [mul_sub, mul_one, Finset.sum_sub_distrib, sum]\n");
    emit("A4 LEAN   rw [he, sub_sub_cancel]\n");
    emit("A4 LEAN   simpa only [smul_eq_mul] using\n");
    emit("A4 LEAN     (convexOn_pow (𝕜 := ℝ) k).map_sum_le hp sum (p := x) hx\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A one-atom transfer distribution attains the normalized bound. -/\n");
    emit("A4 LEAN theorem singleAtomStep (x : ℝ) (k : ℕ) : (1 - (1 - x)) ^ k = x ^ k := by\n");
    emit("A4 LEAN   rw [sub_sub_cancel]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.Observable\n");
    emit("A4 LEAN #print axioms YangMills.Observable.traceGradient\n");
    emit("A4 LEAN #print axioms YangMills.Observable.adjointGradient\n");
    emit("A4 LEAN #print axioms YangMills.Observable.normalizedStepBound\n");
    emit("A4 LEAN #print axioms YangMills.Observable.singleAtomStep\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
