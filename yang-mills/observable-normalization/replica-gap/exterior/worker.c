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
    emit("A4 LEAN namespace YangMills.ExteriorTrace\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN def pairs : List ℝ → ℝ\n");
    emit("A4 LEAN   | [] => 0\n");
    emit("A4 LEAN   | a :: s => a*s.sum + pairs s\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN def triples : List ℝ → ℝ\n");
    emit("A4 LEAN   | [] => 0\n");
    emit("A4 LEAN   | a :: s => a*pairs s + triples s\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem doubleNewton (s : List ℝ) :\n");
    emit("A4 LEAN     2*pairs s = s.sum^2 - (s.map (fun a => a^2)).sum := by\n");
    emit("A4 LEAN   induction s with\n");
    emit("A4 LEAN   | nil => simp [pairs]\n");
    emit("A4 LEAN   | cons a r ih =>\n");
    emit("A4 LEAN     simp only [pairs, List.sum_cons, List.map_cons]\n");
    emit("A4 LEAN     nlinarith only [ih]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem tripleNewton (s : List ℝ) :\n");
    emit("A4 LEAN     6*triples s = s.sum^3 - 3*s.sum*(s.map (fun a => a^2)).sum +\n");
    emit("A4 LEAN       2*(s.map (fun a => a^3)).sum := by\n");
    emit("A4 LEAN   induction s with\n");
    emit("A4 LEAN   | nil => simp [triples]\n");
    emit("A4 LEAN   | cons a r ih =>\n");
    emit("A4 LEAN     simp only [triples, List.sum_cons, List.map_cons]\n");
    emit("A4 LEAN     nlinarith only [ih, congrArg (fun x : ℝ => a*x) (doubleNewton r)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Apply to permutation products carrying their determinant signs. -/\n");
    emit("A4 LEAN theorem signedSquare {ι : Type*} (s : Finset ι) (w sign : ι → ℝ)\n");
    emit("A4 LEAN     (hs : ∀ i ∈ s, (sign i)^2=1) :\n");
    emit("A4 LEAN     (∑ i ∈ s, sign i*w i)^2 ≤ (s.card : ℝ)*∑ i ∈ s, (w i)^2 := by\n");
    emit("A4 LEAN   have h := Finset.sum_mul_sq_le_sq_mul_sq s sign w\n");
    emit("A4 LEAN   have ones : ∑ i ∈ s, (sign i)^2 = (s.card : ℝ) := by\n");
    emit("A4 LEAN     rw [Finset.sum_congr rfl hs]\n");
    emit("A4 LEAN     simp\n");
    emit("A4 LEAN   rwa [ones] at h\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem splittingUpper {a b c hi lo next : ℝ} (ha : 0 ≤ a) (hc : 0 ≤ c)\n");
    emit("A4 LEAN     (hlo : 0 < lo) (hb : lo ≤ b) (x : a ≤ hi) (y : c ≤ next) :\n");
    emit("A4 LEAN     a*c/b^2 ≤ hi*next/lo^2 := by\n");
    emit("A4 LEAN   apply div_le_div_of_nonneg_right (mul_le_mul x y hc (ha.trans x)) (sq_nonneg b) |>.trans\n");
    emit("A4 LEAN   exact div_le_div_of_nonneg_left (mul_nonneg (ha.trans x) (hc.trans y))\n");
    emit("A4 LEAN     (sq_pos_of_pos hlo) (pow_le_pow_left₀ hlo.le hb 2)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem positiveSecond {ι : Type*} (s : Finset ι) (p w : ι → ℝ) (b : ℝ)\n");
    emit("A4 LEAN     (hp : ∀ i ∈ s, 0 ≤ p i) (hw : ∀ i ∈ s, 0 ≤ w i) (hb : ∀ i ∈ s, w i ≤ b) :\n");
    emit("A4 LEAN     ∑ i ∈ s, p i*(w i)^2 ≤ b*∑ i ∈ s, p i*w i := by\n");
    emit("A4 LEAN   rw [Finset.mul_sum]\n");
    emit("A4 LEAN   apply Finset.sum_le_sum\n");
    emit("A4 LEAN   intro i hi\n");
    emit("A4 LEAN   have h := mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right (hb i hi) (hw i hi)) (hp i hi)\n");
    emit("A4 LEAN   nlinarith only [h]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem coincidentRows {ι : Type*} [Fintype ι] (p w : ι → ℝ)\n");
    emit("A4 LEAN     (hp : ∀ i, 0 < p i) (hw : ∀ i, 0 ≤ w i) (nullMean : ∑ i, p i*w i = 0) :\n");
    emit("A4 LEAN     ∀ i, w i = 0 := by\n");
    emit("A4 LEAN   intro i\n");
    emit("A4 LEAN   have h := Finset.single_le_sum (s := Finset.univ) (f := fun j => p j*w j)\n");
    emit("A4 LEAN     (fun j _ => mul_nonneg (hp j).le (hw j)) (Finset.mem_univ i)\n");
    emit("A4 LEAN   rw [nullMean] at h\n");
    emit("A4 LEAN   by_contra hne\n");
    emit("A4 LEAN   exact (not_lt_of_ge h) (mul_pos (hp i) (lt_of_le_of_ne (hw i) (Ne.symm hne)))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ExteriorTrace\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.doubleNewton\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.tripleNewton\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.signedSquare\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.splittingUpper\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.positiveSecond\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorTrace.coincidentRows\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
