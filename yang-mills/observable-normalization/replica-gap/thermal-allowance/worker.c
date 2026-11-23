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
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ThermalAllowance\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem twoBins (a b c d : ℝ) :\n");
    emit("A4 LEAN     (a^2+b^2)^2 + 2*(a*c+b*d)^2 + (c^2+d^2)^2 =\n");
    emit("A4 LEAN     (a^2+b^2+c^2+d^2)^2 - 2*(a*d-b*c)^2 := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem endpointMixture (z c : ℝ) (h0 : 0 ≤ c) (h1 : c ≤ 1) :\n");
    emit("A4 LEAN     (z-c)^2 ≤ (1-c)*z^2+c*(1-z)^2 := by\n");
    emit("A4 LEAN   nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem atomCap (q u : ℝ) (hq : 0 ≤ q) (hhalf : q ≤ 1/2)\n");
    emit("A4 LEAN     (hu : 0 ≤ u) (hu1 : u ≤ 1) : q*u*(1-q*u) ≤ q*(1-q) := by\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left hu1 hq\n");
    emit("A4 LEAN   have hpos : 0 ≤ 1-q-q*u := by linarith\n");
    emit("A4 LEAN   nlinarith [mul_nonneg (show 0 ≤ q-q*u by linarith) hpos]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem purityCap (p q : ℝ) (bound : p ≤ (1-q)^2+q^2) :\n");
    emit("A4 LEAN     q*(1-q) ≤ (1-p)/2 := by nlinarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem bestLag (a b r : ℝ) (ordered : b ≤ a) (hr : 0 ≤ r) :\n");
    emit("A4 LEAN     b-r*a ≤ (1-r)*b := by nlinarith [mul_nonneg hr (sub_nonneg.mpr ordered)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ThermalAllowance\n");
    emit("A4 LEAN #print axioms YangMills.ThermalAllowance.twoBins\n");
    emit("A4 LEAN #print axioms YangMills.ThermalAllowance.endpointMixture\n");
    emit("A4 LEAN #print axioms YangMills.ThermalAllowance.atomCap\n");
    emit("A4 LEAN #print axioms YangMills.ThermalAllowance.purityCap\n");
    emit("A4 LEAN #print axioms YangMills.ThermalAllowance.bestLag\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
