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
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Tactic.GCongr\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace Riemann.PrimeInequality\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Normalize the explicit source bracket by the mass of the distinguished cells. -/\n");
    emit("A4 LEAN theorem normalizeBracket {n t r m b k : ℝ} (a X : ℝ)\n");
    emit("A4 LEAN     (hn : 0 < n) (ht : 0 < t) (hr : 0 < r) (hm : 0 < m)\n");
    emit("A4 LEAN     (hb : 0 < b) (hk : 0 < k) :\n");
    emit("A4 LEAN     (t*a*(1+m^2/k) + m*(2*n*m*b*X + r*k*b*X/(n*(n/X)))) /\n");
    emit("A4 LEAN       (t*m*b*(r/n)/2) =\n");
    emit("A4 LEAN     2*(n/r)*(a/b)*(1/m+m/k) + 4*(n/t)*(n/r)*X*m +\n");
    emit("A4 LEAN       2*(n/t)*X^2*(k/n^2) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Bounds for the inverse densities and the envelope scale give the four printed costs. -/\n");
    emit("A4 LEAN theorem fourCosts {X d v a x p q m z : ℝ}\n");
    emit("A4 LEAN     (hX : 1 ≤ X) (hd : 0 ≤ d) (ha : 0 ≤ a)\n");
    emit("A4 LEAN     (hx : 0 ≤ x) (hp : 0 ≤ p) (hq : 0 ≤ q) (hm : 0 ≤ m) (hz : 0 ≤ z)\n");
    emit("A4 LEAN     (hD : d ≤ X) (hV : v ≤ 2*X) (hA : a ≤ 2*x) :\n");
    emit("A4 LEAN     2*d*a*(p+q) + 4*v*d*X*m + 2*v*X^2*z ≤\n");
    emit("A4 LEAN       8*X^3*(x*p+x*q+m+z) := by\n");
    emit("A4 LEAN   have pos : 0 ≤ X := by linarith\n");
    emit("A4 LEAN   have cube : X ≤ X^3 := by nlinarith [mul_nonneg (by linarith : 0 ≤ X-1) (by nlinarith : 0 ≤ X^2+X)]\n");
    emit("A4 LEAN   have first : 2*d*a ≤ 8*X^3*x := by\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       2*d*a ≤ 2*X*(2*x) := by gcongr\n");
    emit("A4 LEAN       _ ≤ 8*X^3*x := by nlinarith [mul_le_mul_of_nonneg_right cube hx, mul_nonneg pos hx]\n");
    emit("A4 LEAN   have mid : 4*v*d*X ≤ 8*X^3 := by\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       4*v*d*X ≤ 4*(2*X)*X*X := by gcongr\n");
    emit("A4 LEAN       _ = _ := by ring\n");
    emit("A4 LEAN   have last : 2*v*X^2 ≤ 8*X^3 := by\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       2*v*X^2 ≤ 2*(2*X)*X^2 := by gcongr\n");
    emit("A4 LEAN       _ ≤ _ := by nlinarith [pow_nonneg pos 3]\n");
    emit("A4 LEAN   nlinarith only [mul_le_mul_of_nonneg_right first (add_nonneg hp hq),\n");
    emit("A4 LEAN     mul_le_mul_of_nonneg_right mid hm, mul_le_mul_of_nonneg_right last hz]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Taking the normalized mean preserves a bound valid for each translated table. -/\n");
    emit("A4 LEAN theorem translateMean {ι : Type*} (s : Finset ι) (hs : s.Nonempty)\n");
    emit("A4 LEAN     (g : ι → ℝ) (E : ℝ) (h : ∀ i ∈ s, g i ≤ E) :\n");
    emit("A4 LEAN     (∑ i ∈ s, g i) / (s.card : ℝ) ≤ E := by\n");
    emit("A4 LEAN   have pos : 0 < (s.card : ℝ) := by exact_mod_cast hs.card_pos\n");
    emit("A4 LEAN   apply (div_le_iff₀ pos).mpr\n");
    emit("A4 LEAN   simpa [mul_comm] using Finset.sum_le_sum h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end Riemann.PrimeInequality\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms Riemann.PrimeInequality.normalizeBracket\n");
    emit("A4 LEAN #print axioms Riemann.PrimeInequality.fourCosts\n");
    emit("A4 LEAN #print axioms Riemann.PrimeInequality.translateMean\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
