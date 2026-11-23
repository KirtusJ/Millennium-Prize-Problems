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
static long integer_power(long base, int degree) {
    long result = 1;
    for (int i=0; i<degree; ++i) result *= base;
    return result;
}
static int verify_count(void) {
#if ROLE == 0
    /* Point masses at all eighths of [-1,1], clearing the denominators. */
    for (long j=-8; j<=8; ++j) for (int n=1; n<=12; ++n) {
        long denominator=integer_power(8,n);
        long loss=denominator-integer_power(j,n);
        if (loss>n*(8-j)*(denominator/8)) return 0;
    }
#elif ROLE == 1
    /* A positive two-point spectral law gives a positive staple determinant.
       A coherent rotation with cos(theta)=3/5 gives the opposite determinant. */
    long first_num=3, first_den=5, second_num=-7, second_den=25;
    if (second_num*first_den*first_den >= first_num*first_num*second_den) return 0;
    long a[2]={-1,2}, w[2]={1,3}, mass=4, m1=0,m2=0;
    for (int i=0;i<2;++i) {m1+=a[i]*w[i]; m2+=a[i]*a[i]*w[i];}
    if (mass*m2-m1*m1 != 27) return 0;
#else
    /* Square roots of four exact spatial weights, including the root. */
    long a[4]={5,2,7,3}, root_weight[4]={1,2,3,5}, total=0,half=0,full=0;
    for(int i=0;i<4;++i) {
        total+=a[i]; half+=a[i]*root_weight[i];
        full+=a[i]*root_weight[i]*root_weight[i];
    }
    if (half*half>=total*full || total!=17 || half!=45 || full!=151) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Sqrt\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Positivity\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.ReflectedStrip\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Bounded squared norms of shifted staples have a contractive first shift\n");
    emit("A4 LEAN once reflection positivity supplies the ordinary second-difference inequality. -/\n");
    emit("A4 LEAN theorem shiftContraction (q : ℕ → ℝ) (K : ℝ) (bound : ∀ n, q n ≤ K)\n");
    emit("A4 LEAN     (convex : ∀ n, 2*q (n+1) ≤ q n+q (n+2)) : q 1 ≤ q 0 := by\n");
    emit("A4 LEAN   have hstep (n : ℕ) : q 1-q 0 ≤ q (n+1)-q n := by\n");
    emit("A4 LEAN     induction n with\n");
    emit("A4 LEAN     | zero => simp\n");
    emit("A4 LEAN     | succ n ih =>\n");
    emit("A4 LEAN       change q 1 - q 0 ≤ q (n+2) - q (n+1)\n");
    emit("A4 LEAN       linarith [convex n]\n");
    emit("A4 LEAN   have hline (n : ℕ) : q 0+(n:ℝ)*(q 1-q 0) ≤ q n := by\n");
    emit("A4 LEAN     induction n with\n");
    emit("A4 LEAN     | zero => simp\n");
    emit("A4 LEAN     | succ n ih =>\n");
    emit("A4 LEAN       rw [Nat.cast_succ, add_mul, one_mul]\n");
    emit("A4 LEAN       linarith [hstep n]\n");
    emit("A4 LEAN   by_contra! hn\n");
    emit("A4 LEAN   have hd : 0 < q 1-q 0 := sub_pos.mpr hn\n");
    emit("A4 LEAN   obtain ⟨n,hn'⟩ := exists_nat_gt ((K-q 0)/(q 1-q 0))\n");
    emit("A4 LEAN   have hh := (div_lt_iff₀ hd).mp hn'\n");
    emit("A4 LEAN   linarith [bound n, hline n]\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- The deficit is at most linear in strip length even if the one-step\n");
    emit("A4 LEAN self-adjoint contraction has a negative part. -/\n");
    emit("A4 LEAN theorem stripDeficit (x : ℝ) (hx : |x| ≤ 1) (n : ℕ) :\n");
    emit("A4 LEAN     1-x^n ≤ (n:ℝ)*(1-x) := by\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     have hp : x^n ≤ 1 := (le_abs_self _).trans (by\n");
    emit("A4 LEAN       rw [abs_pow]\n");
    emit("A4 LEAN       exact pow_le_one₀ (abs_nonneg _) hx)\n");
    emit("A4 LEAN     have hx' := (le_abs_self x).trans hx\n");
    emit("A4 LEAN     have h := mul_nonneg (sub_nonneg.mpr hp) (sub_nonneg.mpr hx')\n");
    emit("A4 LEAN     rw [pow_succ, Nat.cast_succ]\n");
    emit("A4 LEAN     nlinarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Interpolate the half-weighted norm from unweighted and weighted norms. -/\n");
    emit("A4 LEAN theorem halfWeight {ι : Type*} (s : Finset ι) (a w : ι → ℝ)\n");
    emit("A4 LEAN     (ha : ∀ i, 0 ≤ a i) (hw : ∀ i, 0 ≤ w i) :\n");
    emit("A4 LEAN     (∑ i ∈ s, a i * Real.sqrt (w i))^2 ≤\n");
    emit("A4 LEAN         (∑ i ∈ s, a i)*(∑ i ∈ s, a i*w i) := by\n");
    emit("A4 LEAN   have hc := sum_mul_sq_le_sq_mul_sq s (fun i => Real.sqrt (a i))\n");
    emit("A4 LEAN     (fun i => Real.sqrt (a i)*Real.sqrt (w i))\n");
    emit("A4 LEAN   simpa only [← mul_assoc, ← sq, mul_pow, Real.sq_sqrt (ha _),\n");
    emit("A4 LEAN     Real.sq_sqrt (hw _)] using hc\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- The R³ and R⁴ estimates together supply the R⁷ squared norm. -/\n");
    emit("A4 LEAN theorem squaredBudget {A B Q R C : ℝ} (hB : 0 ≤ B) (hR : 0 ≤ R)\n");
    emit("A4 LEAN     (hC : 0 ≤ C) (hq : Q^2 ≤ A*B) (hA : A ≤ C*R^3)\n");
    emit("A4 LEAN     (hB' : B ≤ C*R^4) : Q^2 ≤ C^2*R^7 := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     Q^2 ≤ A*B := hq\n");
    emit("A4 LEAN     _ ≤ (C*R^3)*(C*R^4) := mul_le_mul hA hB' hB (by positivity)\n");
    emit("A4 LEAN     _ = C^2*R^7 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Testing against the correlation scale uses the seventh power of the width. -/\n");
    emit("A4 LEAN theorem errorAtScale {R c s : ℝ} (hR : 0 ≤ R) (hs : 0 < s) (h : R ≤ c*s) :\n");
    emit("A4 LEAN     R^7/s^7 ≤ c^7 := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (pow_pos hs 7)).mpr\n");
    emit("A4 LEAN   simpa only [mul_pow] using pow_le_pow_left₀ hR h 7\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Fix one side, bound its deficit by its value at length one, then\n");
    emit("A4 LEAN apply the same estimate in the perpendicular direction. -/\n");
    emit("A4 LEAN theorem rectangleDeficit (W : ℕ → ℕ → ℝ)\n");
    emit("A4 LEAN     (along : ∀ m n, 1-W m n ≤ (n:ℝ)*(1-W m 1))\n");
    emit("A4 LEAN     (across : ∀ m, 1-W m 1 ≤ (m:ℝ)*(1-W 1 1)) (m n : ℕ) :\n");
    emit("A4 LEAN     1-W m n ≤ ((m:ℝ)*(n:ℝ))*(1-W 1 1) := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     1-W m n ≤ (n:ℝ)*(1-W m 1) := along m n\n");
    emit("A4 LEAN     _ ≤ (n:ℝ)*((m:ℝ)*(1-W 1 1)) :=\n");
    emit("A4 LEAN       mul_le_mul_of_nonneg_left (across m) (Nat.cast_nonneg n)\n");
    emit("A4 LEAN     _ = _ := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ReflectedStrip\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.shiftContraction\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.stripDeficit\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.halfWeight\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.squaredBudget\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.errorAtScale\n");
    emit("A4 LEAN #print axioms YangMills.ReflectedStrip.rectangleDeficit\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
