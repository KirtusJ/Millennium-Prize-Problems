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
    for (long j = -8; j < 8; ++j) {
        for (long k = j + 1; k <= 8; ++k) {
            long midpoint = j + k + 1;
            if (2*midpoint-2*j-1 != 2*k+1 ||
                2*midpoint-(2*j+1)-1 != 2*k ||
                2*j+2 > midpoint || 2*k < midpoint) return 0;
        }
    }
#elif ROLE == 1
    /* I-A_L has numerator L delta_0 - 1_[0,L). Its primitive is a triangle. */
    for (long l = 2; l <= 32; l += 2) {
        long previous=0, total=0;
        for (long i=0; i<l; ++i) {
            long u=l-1-i;
            if (u-previous != (i==0 ? l-1 : -1)) return 0;
            previous=u;
            total+=u;
        }
        if (previous || 2*total != l*(l-1)) return 0;
    }
#else
    /* Gamma(8,1) mixed Laplace moments at integer orders. */
    for (long j=0; j<=6; ++j) {
        long d=1, half=1;
        for (int i=0; i<8; ++i) { d*=j+1; half*=2*(j+1); }
        if (half != 256*d) return 0;
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.LocalAction\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Site reflection in the midpoint exchanges the two positively oriented\n");
    emit("A4 LEAN face bases within a pair, with their order reversed. -/\n");
    emit("A4 LEAN theorem pairReflection (j k : ℤ) :\n");
    emit("A4 LEAN     2*(j+k+1)-(2*j)-1 = 2*k+1 ∧\n");
    emit("A4 LEAN     2*(j+k+1)-(2*j+1)-1 = 2*k := by\n");
    emit("A4 LEAN   constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Nonpositive mean inner products between different blocks leave only\n");
    emit("A4 LEAN diagonal contributions to the upper bound for their sum. -/\n");
    emit("A4 LEAN theorem blockSum {ι : Type*} [DecidableEq ι] (s : Finset ι)\n");
    emit("A4 LEAN     (K : ι → ι → ℝ) (D : ℝ) (diag : ∀ i ∈ s, K i i ≤ D)\n");
    emit("A4 LEAN     (off : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → K i j ≤ 0) :\n");
    emit("A4 LEAN     (∑ i ∈ s, ∑ j ∈ s, K i j) ≤ (s.card:ℝ)*D := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ∑ i ∈ s, ∑ j ∈ s, (if j=i then D else 0) := by\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro j hj\n");
    emit("A4 LEAN       by_cases eq : j=i\n");
    emit("A4 LEAN       · subst j\n");
    emit("A4 LEAN         simpa using diag i hi\n");
    emit("A4 LEAN       · simpa [eq] using off i hi j hj (Ne.symm eq)\n");
    emit("A4 LEAN     _ = _ := by simp\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Quaternion magnitude converts the scaled imaginary curvature back to\n");
    emit("A4 LEAN the Wilson action with one explicit quadratic remainder. -/\n");
    emit("A4 LEAN theorem actionRemainder (b x y f : ℝ) (h : y=b*(1-x))\n");
    emit("A4 LEAN     (hf : f=b*(1-x^2)) : b*(2*y-f)=y^2 := by\n");
    emit("A4 LEAN   rw [h,hf]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Connected covariance of two sums of three squared Gaussian colors,\n");
    emit("A4 LEAN including the normalization of each scalar action by one half. -/\n");
    emit("A4 LEAN theorem wickAction (v g : ℝ) :\n");
    emit("A4 LEAN     (3*(v^2+2*g^2)+6*v^2)/4 - (3*v/2)^2 = 3*g^2/2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Combining a reflected-mean error with a cubic primitive cost after\n");
    emit("A4 LEAN writing s for the eighth root of the coupling. -/\n");
    emit("A4 LEAN theorem balance (s : ℝ) (hs : 0 < s) :\n");
    emit("A4 LEAN     1/s + s^3/s^4 = 2/s := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Fixed positive-time tilt converts centered covariance readings into\n");
    emit("A4 LEAN normalized moments, with a denominator bounded away from zero. -/\n");
    emit("A4 LEAN theorem tiltError (A B C D e f : ℝ) (hB : 0 < B) (hD : 0 < D)\n");
    emit("A4 LEAN     (hC : |C| ≤ D) (hA : |A-C| ≤ e) (hBD : |B-D| ≤ f) :\n");
    emit("A4 LEAN     |A/B-C/D| ≤ (e+f)/B := by\n");
    emit("A4 LEAN   have eq : A/B-C/D = ((A-C) + (C/D)*(D-B))/B := by\n");
    emit("A4 LEAN     field_simp\n");
    emit("A4 LEAN     ring\n");
    emit("A4 LEAN   have hc' : |C/D| ≤ 1 := by\n");
    emit("A4 LEAN     rw [abs_div, abs_of_pos hD, div_le_one hD]\n");
    emit("A4 LEAN     exact hC\n");
    emit("A4 LEAN   rw [eq, abs_div, abs_of_pos hB]\n");
    emit("A4 LEAN   apply div_le_div_of_nonneg_right _ hB.le\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ |A-C| + |(C/D)*(D-B)| := abs_add_le _ _\n");
    emit("A4 LEAN     _ ≤ e + f := by\n");
    emit("A4 LEAN       rw [abs_mul, abs_sub_comm D B]\n");
    emit("A4 LEAN       exact add_le_add hA ((mul_le_mul_of_nonneg_right hc' (abs_nonneg _)).trans (by simpa using hBD))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.LocalAction\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.pairReflection\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.blockSum\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.actionRemainder\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.wickAction\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.balance\n");
    emit("A4 LEAN #print axioms YangMills.LocalAction.tiltError\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
