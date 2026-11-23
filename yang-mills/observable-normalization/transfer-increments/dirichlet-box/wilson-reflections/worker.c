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
    /* A cut between block-center indices r-1,r has the same reflected
       anchors for site cuts along the face and bond cuts transverse to it. */
    for(int side=4;side<=64;side+=2) {
        for(int n=1;n<=side-2;++n) {
            if(n>1 && n%2) continue;
            int r=(n==1?0:n/2-1), left=0, right=0;
            for(int x=0;x<side;++x) {
                int y=(2*r-1-x+2*side)%side;
                if(y==x || (2*r-1-y+2*side)%side!=x) return 0;
                int positive=(x-r+side)%side<side/2;
                if((y-r+side)%side<side/2 ? positive : !positive) return 0;
                if((positive && x<n) || (!positive && y<n)) ++right;
                if((!positive && x<n) || (positive && y<n)) ++left;
            }
            if(left!=(n==1?0:n-2) || right!=(n==1?2:n+2)) return 0;
        }
    }
#elif ROLE == 1
    for(int L=4;L<=10;L+=2) {
        int free_edges=0, kept=0, hits=0, inverted=0;
        for(int t=0;t<L;++t) for(int x=0;x<L;++x)
        for(int y=0;y<L;++y) for(int z=0;z<L;++z) {
            free_edges+=3+(t==L-1);
            kept+=3*(t<L-1);
            for(int i=0;i<4;++i) for(int j=i+1;j<4;++j) {
                hits+=2*(i!=0 || t==L-1)+2*(j!=0 || t==L-1);
                /* Direction 2 takes value (-1)^x, x is coordinate 1. */
                if((i==1 && j==2) && ((x+1)%L)%2!=x%2) ++inverted;
            }
        }
        int v=L*L*L*L;
        if(free_edges!=3*v+v/L || hits!=6*free_edges ||
           kept!=3*(v-v/L) || inverted!=v) return 0;
    }
#else
    /* Exact signed contraction eigenvalues, including negative ones,
       in the independent-link trial measure inequality. */
    for(int den=1;den<=24;++den) for(int a=-den;a<=den;++a) {
        int p=1, q=1;
        for(int k=1;k<=4;++k) {
            p*=a;
            q*=den;
            if(q-p>k*(den-a)*(q/den)) return 0;
        }
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Data.Real.Sqrt\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Positivity\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.WilsonReflections\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The forward pullback takes a half-space site to another such site. -/\n");
    emit("A4 LEAN theorem forwardSite (t : ℤ) (ht : 0 ≤ t) : 0 ≤ t+1 := by omega\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Bond reflection of the translated label is site reflection of the original. -/\n");
    emit("A4 LEAN theorem adjacentReflection (t : ℤ) : 1-(t+1) = -t := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- First slope of the even log-moments is below the secant slope\n");
    emit("A4 LEAN on each finite interval. Only inequalities inside the interval enter. -/\n");
    emit("A4 LEAN theorem evenChord (f : ℕ → ℝ) (m : ℕ)\n");
    emit("A4 LEAN     (hc : ∀ n, n+2 ≤ m → 2*f (n+1) ≤ f n+f (n+2)) :\n");
    emit("A4 LEAN     (m:ℝ)*(f 1-f 0) ≤ f m-f 0 := by\n");
    emit("A4 LEAN   have step (i : ℕ) (hi : i+1 ≤ m) : f 1-f 0 ≤ f (i+1)-f i := by\n");
    emit("A4 LEAN     induction i with\n");
    emit("A4 LEAN     | zero => simp\n");
    emit("A4 LEAN     | succ i ih =>\n");
    emit("A4 LEAN       have h := ih (by omega)\n");
    emit("A4 LEAN       have h' := hc i (by omega)\n");
    emit("A4 LEAN       change f 1-f 0 ≤ f (i+2)-f (i+1)\n");
    emit("A4 LEAN       linarith\n");
    emit("A4 LEAN   have run (i : ℕ) (hi : i ≤ m) : (i:ℝ)*(f 1-f 0) ≤ f i-f 0 := by\n");
    emit("A4 LEAN     induction i with\n");
    emit("A4 LEAN     | zero => simp\n");
    emit("A4 LEAN     | succ i ih =>\n");
    emit("A4 LEAN       have h := ih (by omega)\n");
    emit("A4 LEAN       have h' := step i hi\n");
    emit("A4 LEAN       rw [Nat.cast_succ, add_mul, one_mul]\n");
    emit("A4 LEAN       linarith\n");
    emit("A4 LEAN   exact run m le_rfl\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- One layer is controlled by the full even period after reflection. -/\n");
    emit("A4 LEAN theorem layerBound (u v w : ℝ) (m : ℕ) (h : 2*u ≤ v) (hch : (m:ℝ)*v ≤ w) :\n");
    emit("A4 LEAN     (2*(m:ℝ))*u ≤ w := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ = (m:ℝ)*(2*u) := by ring\n");
    emit("A4 LEAN     _ ≤ (m:ℝ)*v := mul_le_mul_of_nonneg_left h (by positivity)\n");
    emit("A4 LEAN     _ ≤ w := hch\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Independent central link matrices give the power of their mean\n");
    emit("A4 LEAN on each plaquette. Its deficit is bounded by the incidence count. -/\n");
    emit("A4 LEAN theorem trialDeficit (x : ℝ) (hx : |x| ≤ 1) (k : ℕ) :\n");
    emit("A4 LEAN     1-x^k ≤ (k:ℝ)*(1-x) := by\n");
    emit("A4 LEAN   induction k with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ k ih =>\n");
    emit("A4 LEAN     have hpow : x^k ≤ 1 := (le_abs_self _).trans (by\n");
    emit("A4 LEAN       rw [abs_pow]\n");
    emit("A4 LEAN       exact pow_le_one₀ (abs_nonneg _) hx)\n");
    emit("A4 LEAN     have hpos : 0 ≤ 1-x := by linarith [(le_abs_self x).trans hx]\n");
    emit("A4 LEAN     have h := mul_le_mul_of_nonneg_right hpow hpos\n");
    emit("A4 LEAN     rw [pow_succ, Nat.cast_succ]\n");
    emit("A4 LEAN     nlinarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The SU(2) Haar radial integral after scaling has an increasing\n");
    emit("A4 LEAN weight on the old integration interval. -/\n");
    emit("A4 LEAN theorem radialWeight (x s t : ℝ) (hx : 0 ≤ x) (hs : 0 < s) (hst : s ≤ t) :\n");
    emit("A4 LEAN     Real.sqrt (2-x/s) ≤ Real.sqrt (2-x/t) := by\n");
    emit("A4 LEAN   apply Real.sqrt_le_sqrt\n");
    emit("A4 LEAN   have h := div_le_div_of_nonneg_left hx hs hst\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Dropping the two finite-size logarithmic corrections only takes\n");
    emit("A4 LEAN place after fixing the coupling and sending this side to infinity. -/\n");
    emit("A4 LEAN theorem seamIdentity (z w m : ℝ) :\n");
    emit("A4 LEAN     3*(1-m)*z - (3+m)*w = 3*(z-w) - m*(3*z+w) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.WilsonReflections\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.forwardSite\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.adjacentReflection\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.evenChord\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.layerBound\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.trialDeficit\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.radialWeight\n");
    emit("A4 LEAN #print axioms YangMills.WilsonReflections.seamIdentity\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
