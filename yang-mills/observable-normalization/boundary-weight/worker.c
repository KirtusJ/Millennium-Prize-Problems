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
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Group.Finset\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.BoundaryWeight\n");
    emit("A4 LEAN open scoped BigOperators\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Compare a deep face with every face of the same orientation in a smaller cube. -/\n");
    emit("A4 LEAN theorem translatedAverage {ι : Type*} (s : Finset ι) (row : ι → ℝ)\n");
    emit("A4 LEAN     (a b : ℝ) (hs : 0 < (s.card : ℝ))\n");
    emit("A4 LEAN     (order : ∀ i ∈ s, a ≤ row i)\n");
    emit("A4 LEAN     (total : ∑ i ∈ s, row i ≤ s.card * b) : a ≤ b := by\n");
    emit("A4 LEAN   have h := Finset.sum_le_sum order\n");
    emit("A4 LEAN   simp only [Finset.sum_const, nsmul_eq_mul] at h\n");
    emit("A4 LEAN   exact le_of_mul_le_mul_left (h.trans total) hs\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A lower Rayleigh bound forces a positive fraction into the boundary layer. -/\n");
    emit("A4 LEAN theorem boundaryFraction (d e w : ℝ) (he : e < 1)\n");
    emit("A4 LEAN     (budget : 4+d ≤ 5*w+(4+e)*(1-w)) :\n");
    emit("A4 LEAN     (d-e)/(1-e) ≤ w := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (by linarith : 0 < 1-e)).2\n");
    emit("A4 LEAN   linarith only [budget]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem cubeAverage (r : ℝ) (hr : 0 < r) :\n");
    emit("A4 LEAN     6*(3*r^2*(r+1)-r^3)/(3*r^2*(r+1)) = 4+2/(r+1) := by\n");
    emit("A4 LEAN   have hp : r+1 ≠ 0 := by linarith\n");
    emit("A4 LEAN   field_simp [ne_of_gt hr, hp]\n");
    emit("A4 LEAN   <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.BoundaryWeight\n");
    emit("A4 LEAN #print axioms YangMills.BoundaryWeight.translatedAverage\n");
    emit("A4 LEAN #print axioms YangMills.BoundaryWeight.boundaryFraction\n");
    emit("A4 LEAN #print axioms YangMills.BoundaryWeight.cubeAverage\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
