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
static int verify_count(void) {
#if ROLE == 0
    /* The temporal ramp has the prescribed jump at zero, equal
       residual flux on each layer, and cost b squared divided by L. */
    for (int L=2; L<=128; ++L) {
        int energy=0;
        for (int t=0; t<L; ++t) {
            int left=(t==0 ? 0 : L-t);
            int right=L-t-1;
            int diff=right-left-(t==0 ? L : 0);
            if (diff!=-1) return 0;
            energy+=diff*diff;
        }
        if (energy!=L) return 0;
    }
#elif ROLE == 1
    /* Count the three-dimensional max-coordinate shells entering
       the uniform point-evaluation bound without floating point. */
    int count[33]={0};
    for (int x=1; x<=32; ++x) for (int y=1; y<=32; ++y)
        for (int z=1; z<=32; ++z) {
            int k=(x>y ? x : y);
            if (z>k) k=z;
            ++count[k];
        }
    for (int k=1; k<=32; ++k)
        if (count[k]!=3*k*k-3*k+1 || count[k]>3*k*k) return 0;
#else
    /* Integer controls for the product-law TV inequality. The
       coordinates range over positive unnormalized two-point laws. */
    for (int a=1; a<=8; ++a) for (int b=1; b<=8; ++b)
        for (int c=1; c<=8; ++c) for (int d=1; d<=8; ++d) {
            int diff=a*(c+d)-c*(a+b);
            int exchanged=a*d-c*b;
            if (diff!=exchanged) return 0;
        }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.TemporalLines\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Subtracting the minimizing ramp leaves its constant temporal flux\n");
    emit("A4 LEAN orthogonal to every variation with equal endpoint values. -/\n");
    emit("A4 LEAN theorem rampEnergy {ι : Type*} (s : Finset ι) (r : ι → ℝ) (b : ℝ)\n");
    emit("A4 LEAN     (hr : ∑ i ∈ s, r i = 0) :\n");
    emit("A4 LEAN     ∑ i ∈ s, (r i - b)^2 = (∑ i ∈ s, (r i)^2) + s.card*b^2 := by\n");
    emit("A4 LEAN   simp_rw [sub_sq]\n");
    emit("A4 LEAN   simp only [sum_add_distrib, sum_sub_distrib, ← sum_mul, ← mul_sum,\n");
    emit("A4 LEAN     hr, mul_zero, zero_mul, sub_zero, sum_const, nsmul_eq_mul]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The shell mean cancels even when it is random. -/\n");
    emit("A4 LEAN theorem meanCancel (m x y : ℝ) : (m+x)-(m+y)=x-y := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A uniform diagonal evaluation bound and the Dirichlet energy bound\n");
    emit("A4 LEAN give a fourth-power budget for all zero-shell free links. -/\n");
    emit("A4 LEAN theorem fourthBudget {ι : Type*} (s : Finset ι) (v : ι → ℝ) (B E : ℝ)\n");
    emit("A4 LEAN     (hB : 0 ≤ B) (h : ∀ i ∈ s, (v i)^2 ≤ B)\n");
    emit("A4 LEAN     (he : ∑ i ∈ s, (v i)^2 ≤ E) :\n");
    emit("A4 LEAN     ∑ i ∈ s, (v i)^4 ≤ B*E := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ∑ i ∈ s, B*(v i)^2 := by\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       calc\n");
    emit("A4 LEAN         _ = (v i)^2 * (v i)^2 := by ring\n");
    emit("A4 LEAN         _ ≤ _ := mul_le_mul_of_nonneg_right (h i hi) (sq_nonneg _)\n");
    emit("A4 LEAN     _ ≤ _ := by rw [← mul_sum]; exact mul_le_mul_of_nonneg_left he hB\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The quadratic action error has one mixed and one squared remainder. -/\n");
    emit("A4 LEAN theorem quadraticError (a b d e : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)\n");
    emit("A4 LEAN     (hd : |a-b| ≤ e) (hs : a+b ≤ 2*d+e) :\n");
    emit("A4 LEAN     |a^2-b^2| ≤ e*(2*d+e) := by\n");
    emit("A4 LEAN   have he := (abs_nonneg (a-b)).trans hd\n");
    emit("A4 LEAN   rw [show a^2-b^2=(a-b)*(a+b) by ring, abs_mul, abs_of_nonneg (add_nonneg ha hb)]\n");
    emit("A4 LEAN   exact mul_le_mul hd hs (add_nonneg ha hb) he\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Comparison with the reversed product cancels all normalizers. -/\n");
    emit("A4 LEAN theorem exchangedRatio (a b c d m n : ℝ) (ha : a ≠ 0) (hd : d ≠ 0)\n");
    emit("A4 LEAN     (hm : m ≠ 0) (hn : n ≠ 0) :\n");
    emit("A4 LEAN     ((b/m)*(c/n))/((a/m)*(d/n)) = (b*c)/(a*d) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Coupling the two conditional replicas loses at most twice the\n");
    emit("A4 LEAN one-copy probability of disagreement. -/\n");
    emit("A4 LEAN theorem twoCopies (p : ℝ) : 1-(1-p)^2 ≤ 2*p := by nlinarith [sq_nonneg p]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.TemporalLines\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.rampEnergy\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.meanCancel\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.fourthBudget\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.quadraticError\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.exchangedRatio\n");
    emit("A4 LEAN #print axioms YangMills.TemporalLines.twoCopies\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
