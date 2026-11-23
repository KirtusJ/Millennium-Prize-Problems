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
static long signal(long i) { return ((i*i+7*i+5)%23)-11; }
static int verify_count(void) {
#if ROLE == 0
    /* Expand the long third difference into R^3 adjacent third differences. */
    for (int R=1; R<=8; ++R) for (int x=0; x<9; ++x) {
        long direct=signal(x)-3*signal(x+R)+3*signal(x+2*R)-signal(x+3*R);
        long expanded=0;
        for (int i=0;i<R;++i) for (int j=0;j<R;++j) for (int k=0;k<R;++k) {
            long z=x+i+j+k;
            expanded+=signal(z)-3*signal(z+1)+3*signal(z+2)-signal(z+3);
        }
        if (direct!=expanded) return 0;
    }
#elif ROLE == 1
    /* Sum the discrete one-dimensional tent; its unnormalized mass is R². */
    for (long R=1;R<128;++R) {
        long mass=0, second=0;
        for (long x=1-R;x<R;++x) {
            long w=R-(x<0 ? -x : x);
            mass+=w; second+=w*x*x;
        }
        if (mass!=R*R || 6*second!=R*R*(R*R-1)) return 0;
    }
#else
    /* For a dyadic time block [L,4L), the late fourth gradient has
       weighted cost proportional to 1/sqrt(L)+R/L. Take L=4^k R^2. */
    long num_first=0,num_second=0,den=1L<<16;
    for (int k=0;k<9;++k) {
        num_first+=den/(1L<<k);
        num_second+=den/(1L<<(2*k));
    }
    if (num_first>=2*den || 3*num_second>=4*den) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Analysis.SpecialFunctions.Log.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.Positivity\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.SpatialPacket\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A long spatial difference is the sum of R translates of a unit difference. -/\n");
    emit("A4 LEAN theorem strideDifference (f : ℤ → ℝ) (x : ℤ) (R : ℕ) :\n");
    emit("A4 LEAN     ∑ k ∈ range R, (f (x+k)-f (x+k+1)) = f x-f (x+R) := by\n");
    emit("A4 LEAN   induction R with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ R ih =>\n");
    emit("A4 LEAN     rw [sum_range_succ, ih, Nat.cast_succ, ← add_assoc]\n");
    emit("A4 LEAN     ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A test on at most L edges per path charges at most H*L per unit of mass. -/\n");
    emit("A4 LEAN theorem pathBudget {P E : Type*} (ps : Finset P) (path : P → Finset E)\n");
    emit("A4 LEAN     (mass : P → ℝ) (charge : E → ℝ) (H L : ℝ)\n");
    emit("A4 LEAN     (hm : ∀ p ∈ ps, 0 ≤ mass p) (hh : 0 ≤ H)\n");
    emit("A4 LEAN     (hcharge : ∀ p ∈ ps, ∀ e ∈ path p, charge e ≤ H)\n");
    emit("A4 LEAN     (hlen : ∀ p ∈ ps, ((path p).card : ℝ) ≤ L) :\n");
    emit("A4 LEAN     ∑ p ∈ ps, mass p * ∑ e ∈ path p, charge e ≤\n");
    emit("A4 LEAN       (∑ p ∈ ps, mass p) * (L*H) := by\n");
    emit("A4 LEAN   rw [sum_mul]\n");
    emit("A4 LEAN   apply sum_le_sum\n");
    emit("A4 LEAN   intro p hp\n");
    emit("A4 LEAN   apply mul_le_mul_of_nonneg_left _ (hm p hp)\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     ∑ e ∈ path p, charge e ≤ ∑ _e ∈ path p, H := sum_le_sum (hcharge p hp)\n");
    emit("A4 LEAN     _ = ((path p).card : ℝ)*H := by simp\n");
    emit("A4 LEAN     _ ≤ L*H := mul_le_mul_of_nonneg_right (hlen p hp) hh\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- The split at diffusion time R² leaves a total spatially weighted cost of R⁴.\n");
    emit("A4 LEAN The four inputs are the separate termwise summations for early and late times. -/\n");
    emit("A4 LEAN theorem heatBudget (R A B C D : ℝ) (hR : 0 ≤ R)\n");
    emit("A4 LEAN     (hA : A ≤ R^2) (hB : B ≤ 2*R) (hC : R*C ≤ 3) (hD : R^2*D ≤ 2) :\n");
    emit("A4 LEAN     R^2*(A+R*B)+R^5*(C+R*D) ≤ 8*R^4 := by\n");
    emit("A4 LEAN   have h₁ := mul_le_mul_of_nonneg_left hA (sq_nonneg R)\n");
    emit("A4 LEAN   have h₂ := mul_le_mul_of_nonneg_left hB (pow_nonneg hR 3)\n");
    emit("A4 LEAN   have h₃ := mul_le_mul_of_nonneg_left hC (pow_nonneg hR 4)\n");
    emit("A4 LEAN   have h₄ := mul_le_mul_of_nonneg_left hD (pow_nonneg hR 4)\n");
    emit("A4 LEAN   linarith only [show R^2*A ≤ R^4 by nlinarith only [h₁],\n");
    emit("A4 LEAN     show R^3*B ≤ 2*R^4 by nlinarith only [h₂],\n");
    emit("A4 LEAN     show R^5*C ≤ 3*R^4 by nlinarith only [h₃],\n");
    emit("A4 LEAN     show R^6*D ≤ 2*R^4 by nlinarith only [h₄],\n");
    emit("A4 LEAN     show R^2*(A+R*B)+R^5*(C+R*D) = R^2*A+R^3*B+R^5*C+R^6*D by ring]\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- With s=β^(1/8), any R ≤ c*s has comparison error factor ≤ c⁴. -/\n");
    emit("A4 LEAN theorem packetScale {R c s : ℝ} (hR : 0 ≤ R) (hs : 0 < s)\n");
    emit("A4 LEAN     (h : R ≤ c*s) : R^4/s^4 ≤ c^4 := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ (pow_pos hs 4)).mpr\n");
    emit("A4 LEAN   simpa only [mul_pow] using pow_le_pow_left₀ hR h 4\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A resolved single reading and its norm ceiling give a gap upper bound. -/\n");
    emit("A4 LEAN theorem singleLag {m R b F W V : ℝ} (hR : 0 < R) (hb : 0 < b)\n");
    emit("A4 LEAN     (hfree : 2*b ≤ F) (herr : |W-F| ≤ b) (hnorm : V ≤ 1)\n");
    emit("A4 LEAN     (htransfer : W ≤ Real.exp (-m*R)*V) :\n");
    emit("A4 LEAN     m ≤ -Real.log b/R := by\n");
    emit("A4 LEAN   have hw : b ≤ W := by have := (abs_le.mp herr).1; linarith\n");
    emit("A4 LEAN   have h := hw.trans (htransfer.trans\n");
    emit("A4 LEAN     (mul_le_mul_of_nonneg_left hnorm (Real.exp_pos _).le))\n");
    emit("A4 LEAN   rw [mul_one] at h\n");
    emit("A4 LEAN   have ht := Real.log_le_log hb h\n");
    emit("A4 LEAN   rw [Real.log_exp] at ht\n");
    emit("A4 LEAN   apply (le_div_iff₀ hR).mpr\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A positive difference of two readings forces weight in the interior:\n");
    emit("A4 LEAN if the response outside a band is at most e/2 and the response inside\n");
    emit("A4 LEAN is at most 1/4, a total response of at least e needs band mass ≥ 2e. -/\n");
    emit("A4 LEAN theorem positiveBandMass {e outside inside band : ℝ}\n");
    emit("A4 LEAN     (hm : e ≤ outside+inside) (hout : outside ≤ e/2)\n");
    emit("A4 LEAN     (hin : inside ≤ band/4) : 2*e ≤ band := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SpatialPacket\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.strideDifference\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.pathBudget\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.heatBudget\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.packetScale\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.singleLag\n");
    emit("A4 LEAN #print axioms YangMills.SpatialPacket.positiveBandMass\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
