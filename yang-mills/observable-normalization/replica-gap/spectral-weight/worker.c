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
    emit("A4 LEAN open scoped BigOperators\n");
    emit("A4 LEAN namespace YangMills.ScalarWeight\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Subtract the motion of the eigenvector from the motion of the probe. -/\n");
    emit("A4 LEAN theorem derivativeLeak {ι : Type*} [Fintype ι] (u f : ι → ℝ) (c : ℝ) :\n");
    emit("A4 LEAN     (∑ i, (c*u i/2 - f i*u i/2)^2) = ∑ i, ((c-f i)/2)^2*(u i)^2 := by\n");
    emit("A4 LEAN   apply Finset.sum_congr rfl\n");
    emit("A4 LEAN   intro i _\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem disconnectedCancellation {r : ℝ} (hr : r ≠ 0) (h1 : r ≠ 1) :\n");
    emit("A4 LEAN     (r+r^2)/(r-r^2) = (1+r)/(1-r) := by\n");
    emit("A4 LEAN   have h : r-r^2 ≠ 0 := by\n");
    emit("A4 LEAN     rw [show r-r^2=r*(1-r) by ring]\n");
    emit("A4 LEAN     exact mul_ne_zero hr (sub_ne_zero.mpr (Ne.symm h1))\n");
    emit("A4 LEAN   have h₂ : 1-r ≠ 0 := sub_ne_zero.mpr (Ne.symm h1)\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem effectiveExcess {ι : Type*} [Fintype ι] (w x : ι → ℝ) (n : ℕ) :\n");
    emit("A4 LEAN     (∑ i, w i*(1-(x i)^(n+1))) - (∑ i, w i*(1-(x i)^n)) =\n");
    emit("A4 LEAN       ∑ i, w i*(1-x i)*(x i)^n := by\n");
    emit("A4 LEAN   rw [← Finset.sum_sub_distrib]\n");
    emit("A4 LEAN   apply Finset.sum_congr rfl\n");
    emit("A4 LEAN   intro i _\n");
    emit("A4 LEAN   rw [pow_succ]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem excessPositive {ι : Type*} [Fintype ι] (w x : ι → ℝ) (n : ℕ)\n");
    emit("A4 LEAN     (hw : ∀ i, 0 ≤ w i) (hx : ∀ i, 0 ≤ x i) (ht : ∀ i, x i ≤ 1) :\n");
    emit("A4 LEAN     0 ≤ ∑ i, w i*(1-x i)*(x i)^n :=\n");
    emit("A4 LEAN   Finset.sum_nonneg fun i _ => mul_nonneg (mul_nonneg (hw i) (sub_nonneg.mpr (ht i)))\n");
    emit("A4 LEAN     (pow_nonneg (hx i) n)\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem hamiltonianWeight :\n");
    emit("A4 LEAN     (1/4:ℝ)*(1/6-1/(16-6))^2 + (12/8)*(1/6-1/(9-6))^2 +\n");
    emit("A4 LEAN       (36/8)*(1/6-1/(13-6))^2 = 1999/44100 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem hamiltonianGap :\n");
    emit("A4 LEAN     ((2*(1/3)-(1/5)-24*((8/21)-(1/3)))/8 : ℝ) = -71/840 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem hamiltonianDispersion : (((8/21)-(1/3))/6 : ℝ) = 1/126 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ScalarWeight\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.derivativeLeak\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.disconnectedCancellation\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.effectiveExcess\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.excessPositive\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.hamiltonianWeight\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.hamiltonianGap\n");
    emit("A4 LEAN #print axioms YangMills.ScalarWeight.hamiltonianDispersion\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
