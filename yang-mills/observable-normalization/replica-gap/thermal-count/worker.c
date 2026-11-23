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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Integrals\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ThermalCount\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem deficitIdentity {s t : ℝ} (h : 1+s ≠ 0) :\n");
    emit("A4 LEAN     1-(1+t)/(1+s)^2 = (2*s+s^2-t)/(1+s)^2 := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem deficitFactors {s t : ℝ} (hs : 0 ≤ s) (ht : 0 ≤ t) (hm : t ≤ s^2) :\n");
    emit("A4 LEAN     2*s/(1+s)^2 ≤ (2*s+s^2-t)/(1+s)^2 ∧\n");
    emit("A4 LEAN     (2*s+s^2-t)/(1+s)^2 ≤ 2*s := by\n");
    emit("A4 LEAN   have hd : 0 < (1+s)^2 := by positivity\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · exact div_le_div_of_nonneg_right (by linarith) hd.le\n");
    emit("A4 LEAN   · apply (div_le_iff₀ hd).2\n");
    emit("A4 LEAN     nlinarith [sq_nonneg s, pow_nonneg hs 3]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem rankLoss {a b e : ℝ} (hb : 0 < b) (he : 6*b-a^2 ≤ e) :\n");
    emit("A4 LEAN     6-e/b ≤ a^2/b := by\n");
    emit("A4 LEAN   apply (le_div_iff₀ hb).2\n");
    emit("A4 LEAN   rw [sub_mul, div_mul_cancel₀ _ hb.ne']\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ThermalCount\n");
    emit("A4 LEAN #print axioms YangMills.ThermalCount.deficitIdentity\n");
    emit("A4 LEAN #print axioms YangMills.ThermalCount.deficitFactors\n");
    emit("A4 LEAN #print axioms YangMills.ThermalCount.rankLoss\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
