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
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Exp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN namespace YangMills.ThinLoop\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Haar integration by parts and 1-x² ≤ 2(1-x) give the premises. -/\n");
    emit("A4 LEAN theorem conditionalContraction {r h b : ℝ} (hh : 0 ≤ h) (hmax : h ≤ 6*b)\n");
    emit("A4 LEAN     (hr : r ≤ 1) (score : 3*r ≤ 2*h*(1-r)) :\n");
    emit("A4 LEAN     r ≤ 1-1/(4*b+1) := by\n");
    emit("A4 LEAN   have hb : 0 < 4*b+1 := by linarith\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_right hmax (sub_nonneg.mpr hr)\n");
    emit("A4 LEAN   rw [le_sub_iff_add_le, ← le_sub_iff_add_le', div_le_iff₀ hb]\n");
    emit("A4 LEAN   linarith only [h,score]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A selected edge incurs a fixed contraction and at least L/19 edges are selected. -/\n");
    emit("A4 LEAN theorem loopEnvelope {q d : ℝ} {k L : ℕ} (hq : 0 ≤ q) (hd : 0 ≤ d)\n");
    emit("A4 LEAN     (factor : q ≤ 1-d) (count : L ≤ 19*k) :\n");
    emit("A4 LEAN     q^k ≤ Real.exp (-((L : ℝ)/19)*d) := by\n");
    emit("A4 LEAN   have edge : q ≤ Real.exp (-d) := by linarith only [factor, Real.add_one_le_exp (-d)]\n");
    emit("A4 LEAN   have size : (L : ℝ) ≤ 19*(k : ℝ) := by exact_mod_cast count\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     q^k ≤ (Real.exp (-d))^k := pow_le_pow_left₀ hq edge k\n");
    emit("A4 LEAN     _ = Real.exp ((k : ℝ)*(-d)) := (Real.exp_nat_mul _ _).symm\n");
    emit("A4 LEAN     _ ≤ _ := Real.exp_le_exp.mpr (by linarith only [mul_le_mul_of_nonneg_right size hd])\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem varianceFloor {mean variance second eps : ℝ} (hm : |mean| ≤ 2*eps)\n");
    emit("A4 LEAN     (hs : 1-3*eps ≤ second) (hv : variance = second-mean^2) :\n");
    emit("A4 LEAN     1-3*eps-4*eps^2 ≤ variance := by\n");
    emit("A4 LEAN   have h := mul_self_le_mul_self (abs_nonneg mean) hm\n");
    emit("A4 LEAN   rw [← sq, sq_abs] at h\n");
    emit("A4 LEAN   linarith only [h,hs,hv]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The one-step loss after physical rescaling cannot stay bounded under these premises. -/\n");
    emit("A4 LEAN theorem singlePlaquetteLoss {a V D b : ℝ} (ha : 0 < a) (hv : 0 < V)\n");
    emit("A4 LEAN     (cap : V ≤ 4) (hb : 0 ≤ b) (innovation : b ≤ 2*D) :\n");
    emit("A4 LEAN     b/(8*a) ≤ D/(a*V) := by\n");
    emit("A4 LEAN   apply (div_le_div_iff₀ (by linarith : 0 < 8*a) (mul_pos ha hv)).mpr\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left cap hb\n");
    emit("A4 LEAN   have h' : b*V ≤ 8*D := by linarith only [h,innovation]\n");
    emit("A4 LEAN   linarith only [mul_le_mul_of_nonneg_left h' ha.le]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ThinLoop\n");
    emit("A4 LEAN #print axioms YangMills.ThinLoop.conditionalContraction\n");
    emit("A4 LEAN #print axioms YangMills.ThinLoop.loopEnvelope\n");
    emit("A4 LEAN #print axioms YangMills.ThinLoop.varianceFloor\n");
    emit("A4 LEAN #print axioms YangMills.ThinLoop.singlePlaquetteLoss\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
