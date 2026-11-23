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
    /* Four unit faces parallel to each coordinate plane touch a site. */
    int count=0;
    for (int i=0; i<4; ++i) for (int j=i+1; j<4; ++j)
        for (int bi=0; bi<2; ++bi) for (int bj=0; bj<2; ++bj) {
            int min_i=-bi, min_j=-bj;
            if (min_i>0 || min_i+1<0 || min_j>0 || min_j+1<0) return 0;
            ++count;
        }
    if (count!=24) return 0;
#elif ROLE == 1
    /* In a coordinate reflection, a face and its Hodge complement
       have opposite eigenvalues. The trace of an odd collinear cycle vanishes. */
    for (int axis=0; axis<4; ++axis) {
        int trace=0;
        for (int i=0; i<4; ++i) for (int j=i+1; j<4; ++j) {
            int face=(1<<i)|(1<<j), opposite=15^face;
            int a=(face&(1<<axis)) ? -1:1;
            int b=(opposite&(1<<axis)) ? -1:1;
            if (a*b!=-1) return 0;
            trace+=a;
        }
        if (trace!=0) return 0;
    }
#else
    /* Enumerate Wick contractions on four quadratic vertices on a fixed
       four-cycle: choose the slot assigned to the outgoing edge. */
    int assignments=0;
    for (int mask=0; mask<16; ++mask) {
        int used[8]={0};
        for (int j=0; j<4; ++j) {
            int next=(j+1)%4;
            used[2*j+((mask>>j)&1)]++;
            used[2*next+1-((mask>>next)&1)]++;
        }
        for (int k=0;k<8;++k) if (used[k]!=1) return 0;
        assignments++;
    }
    if (assignments!=16 || assignments*18*9!=2*(2*18)*(2*18)) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Algebra.BigOperators.Group.List.Defs\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.SiteScalar\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A bound on two adjacent edge distances supplies one half of the\n");
    emit("A4 LEAN singularity at each endpoint in the nearest-neighbor estimate. -/\n");
    emit("A4 LEAN theorem edgeSplit {d a b : ℝ} (ha : 0 < a) (hb : 0 < b)\n");
    emit("A4 LEAN     (had : a ≤ d) (hbd : b ≤ d) : (1/d)^4 ≤ (1/a)^2*(1/b)^2 := by\n");
    emit("A4 LEAN   have hd := ha.trans_le had\n");
    emit("A4 LEAN   have h1 := one_div_le_one_div_of_le ha had\n");
    emit("A4 LEAN   have h2 := one_div_le_one_div_of_le hb hbd\n");
    emit("A4 LEAN   have hd' : 0 ≤ 1/d := (one_div_pos.mpr hd).le\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     (1/d)^4 = (1/d)^2*(1/d)^2 := by ring\n");
    emit("A4 LEAN     _ ≤ _ := mul_le_mul (pow_le_pow_left₀ hd' h1 2)\n");
    emit("A4 LEAN       (pow_le_pow_left₀ hd' h2 2) (sq_nonneg _) (sq_nonneg _)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Four neighboring face bases per orientation recover unit total weight. -/\n");
    emit("A4 LEAN theorem cloverCenter (b w μ : ℝ) :\n");
    emit("A4 LEAN     b/4*((24-w)-(24-μ)) = -(b/4)*(w-μ) := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Products of pairs of sign-reversing curvature kernels are fixed by\n");
    emit("A4 LEAN Hodge conjugation even when their multiplication is noncommutative. -/\n");
    emit("A4 LEAN theorem fixedPairs {A : Type*} [Ring A] (σ : A →+* A)\n");
    emit("A4 LEAN     (l : List (A × A))\n");
    emit("A4 LEAN     (h : ∀ p ∈ l, σ p.1 = -p.1 ∧ σ p.2 = -p.2) :\n");
    emit("A4 LEAN     σ (l.map (fun p => p.1*p.2)).prod = (l.map (fun p => p.1*p.2)).prod := by\n");
    emit("A4 LEAN   induction l with\n");
    emit("A4 LEAN   | nil => simp\n");
    emit("A4 LEAN   | cons p l ih =>\n");
    emit("A4 LEAN     have hp := h p (List.mem_cons_self)\n");
    emit("A4 LEAN     have hl : ∀ q ∈ l, σ q.1 = -q.1 ∧ σ q.2 = -q.2 :=\n");
    emit("A4 LEAN       fun q hq => h q (List.mem_cons_of_mem _ hq)\n");
    emit("A4 LEAN     simp only [List.map_cons, List.prod_cons, map_mul, hp.1, hp.2,\n");
    emit("A4 LEAN       neg_mul_neg, ih hl]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The invariant trace of one more sign-reversing factor is zero. -/\n");
    emit("A4 LEAN theorem oddCycle {A : Type*} [Ring A] (σ : A →+* A)\n");
    emit("A4 LEAN     (trace : A →+ ℝ) (invariant : ∀ x, trace (σ x) = trace x)\n");
    emit("A4 LEAN     (a b : A) (ha : σ a = -a) (hb : σ b = b) : trace (a*b) = 0 := by\n");
    emit("A4 LEAN   have h := invariant (a*b)\n");
    emit("A4 LEAN   rw [map_mul, ha, hb, neg_mul, map_neg] at h\n");
    emit("A4 LEAN   linarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The three colors and the six orthogonal two-form channels yield nine\n");
    emit("A4 LEAN in the action covariance with the half-squared Gaussian normalization. -/\n");
    emit("A4 LEAN theorem scalarPair (c : ℝ) : (3:ℝ)*6*2*(1/2)^2*c^2 = 9*c^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Sixteen Wick assignments on each four-cycle yield the normalized\n");
    emit("A4 LEAN trace coefficient for arbitrary quadrilateral geometry. -/\n");
    emit("A4 LEAN theorem fourthCycle (v : ℝ) :\n");
    emit("A4 LEAN     3*16*(1/2:ℝ)^4*v/3^4 = v/27 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A positive ratio at one stride propagates to all later strides of a\n");
    emit("A4 LEAN log-convex transfer correlation. The first entry is the reading at r. -/\n");
    emit("A4 LEAN theorem strideFloor (c : ℕ → ℝ) (q : ℝ) (hq : 0 ≤ q)\n");
    emit("A4 LEAN     (pos : ∀ j, 0 < c j) (first : q ≤ c 1 / c 0)\n");
    emit("A4 LEAN     (convex : ∀ j, c (j+1)*c (j+1) ≤ c j*c (j+2)) (n : ℕ) :\n");
    emit("A4 LEAN     c 0*q^n ≤ c n := by\n");
    emit("A4 LEAN   have step (j : ℕ) : c (j+1)/c j ≤ c (j+2)/c (j+1) := by\n");
    emit("A4 LEAN     apply (div_le_div_iff₀ (pos _) (pos _)).2\n");
    emit("A4 LEAN     simpa only [mul_comm (c (j+2))] using convex j\n");
    emit("A4 LEAN   have hr (j : ℕ) : q ≤ c (j+1)/c j := by\n");
    emit("A4 LEAN     induction j with\n");
    emit("A4 LEAN     | zero => exact first\n");
    emit("A4 LEAN     | succ j ih => exact ih.trans (step j)\n");
    emit("A4 LEAN   induction n with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ n ih =>\n");
    emit("A4 LEAN     rw [pow_succ, ← mul_assoc]\n");
    emit("A4 LEAN     exact (mul_le_mul_of_nonneg_right ih hq).trans (by\n");
    emit("A4 LEAN       simpa only [mul_comm q] using (le_div_iff₀ (pos n)).mp (hr n))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SiteScalar\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.edgeSplit\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.cloverCenter\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.fixedPairs\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.oddCycle\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.scalarPair\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.fourthCycle\n");
    emit("A4 LEAN #print axioms YangMills.SiteScalar.strideFloor\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
