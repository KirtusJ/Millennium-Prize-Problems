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
#if ROLE == 2
/* The sign encodes the orientation of the quaternion basis element.
   Absolute values 1,2,3,4 encode 1,i,j,k respectively. */
static int multiply_basis(int a, int b) {
    int i=__builtin_abs(a)-1, j=__builtin_abs(b)-1;
    int sign=(a*b<0)?-1:1;
    if (!i || !j) return sign*(1+i+j);
    if (i==j) return -sign;
    return sign*(7-i-j)*((i%3+1==j)?1:-1);
}
static int chosen_edge(const int *x, int dir) {
    if (x[0] || x[1] || x[3]) return 0;
    if (!x[2] && (dir==0 || dir==1)) return dir+2;
    return (x[2]==1 && dir==3)?4:0;
}
static void clover_coeff(const int *root,int i,int j,int coeff[8][3]) {
    for (int s=-1;s<=1;s+=2) for (int t=-1;t<=1;t+=2) {
        int x[4], factors[4], len=0;
        for (int a=0;a<4;++a) x[a]=root[a];
        int dirs[4]={i,j,i,j}, signs[4]={s,t,-s,-t};
        for (int k=0;k<4;++k) {
            int d=dirs[k], step=signs[k];
            if (step<0) --x[d];
            int key=chosen_edge(x,d);
            if (key) factors[len++]=step*key;
            if (step>0) ++x[d];
        }
        for (int subset=1;subset<(1<<len);++subset) {
            int mask=0, value=1;
            for (int k=0;k<len;++k) if (subset&(1<<k)) {
                value=multiply_basis(value,factors[k]);
                mask|=1<<(__builtin_abs(factors[k])-2);
            }
            if (__builtin_abs(value)>1)
                coeff[mask][__builtin_abs(value)-2]+=(value>0?1:-1)*s*t;
        }
    }
}
#endif
static int verify_count(void) {
#if ROLE == 0
    /* Test the polarized Pfaffian on 6-dimensional face coordinates. */
    for (int mask=0;mask<4096;++mask) {
        int p[4],a[4],b[4],f[6],g[6],n=0;
        for (int i=0;i<4;++i) {
            p[i]=(mask>>i)&1; a[i]=(mask>>(i+4))&1; b[i]=(mask>>(i+8))&1;
        }
        for (int i=0;i<4;++i) for (int j=i+1;j<4;++j) {
            f[n]=p[i]*a[j]-p[j]*a[i]; g[n++]=p[i]*b[j]-p[j]*b[i];
        }
        int cross=0;
        for (int i=0;i<6;++i) cross+=((i==1||i==4)?-1:1)*f[i]*g[5-i];
        if (cross) return 0;
    }
#elif ROLE == 1
    for (int c=0;c<16;++c) for (int axis=0;axis<4;++axis) {
        int rc=c^(1<<axis), a=1, b=1;
        for (int j=0;j<4;++j) {a*=1-2*((c>>j)&1);b*=1-2*((rc>>j)&1);}
        if (a!=-b) return 0;
    }
    for (int h=1;h<=8;++h) for (int i=0;i<12;++i) for (int j=i+1;j<12;++j) {
        int plane=(i+j+1)*h;
        if (2*plane-i*2*h!=(j+1)*2*h || 2*plane-(i+1)*2*h!=j*2*h) return 0;
    }
#else
    int hits=0;
    for (int site=0;site<256;++site) {
        int x[4],f[6][8][3]={0},n=0,coeff=0;
        for (int i=0;i<4;++i) x[i]=((site>>(2*i))&3)-1;
        for (int i=0;i<4;++i) for (int j=i+1;j<4;++j) clover_coeff(x,i,j,f[n++]);
        for (int i=0;i<3;++i) for (int m=1;m<7;++m) for (int k=0;k<3;++k)
            coeff+=(i==1?-1:1)*f[i][m][k]*f[5-i][7^m][k];
        if (coeff) {
            if (coeff!=-1 || x[0]||x[1]||x[2]||x[3]) return 0;
            ++hits;
        }
    }
    if (hits!=1) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Tactic.LinearCombination\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.OddClover\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A common Fourier covector kills the complementary-face pairing even\n");
    emit("A4 LEAN when the two vector potentials differ. -/\n");
    emit("A4 LEAN theorem commonCovector {R : Type*} [CommRing R]\n");
    emit("A4 LEAN     (p q r s a b c d u v w z : R) :\n");
    emit("A4 LEAN     (p*b-q*a)*(r*z-s*w) - (p*c-r*a)*(q*z-s*v) +\n");
    emit("A4 LEAN     (p*d-s*a)*(q*w-r*v) + (r*d-s*c)*(p*v-q*u) -\n");
    emit("A4 LEAN     (q*d-s*b)*(p*w-r*u) + (q*c-r*b)*(p*z-s*u) = 0 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Four oriented faces supply one centered difference in a fixed axis\n");
    emit("A4 LEAN after multiplication by its symmetric averaging factor. -/\n");
    emit("A4 LEAN theorem centeredSymbol {R : Type*} [CommRing R] (x y : R) (h : x*y=1) :\n");
    emit("A4 LEAN     (1+y)*(x-1) = x-y := by linear_combination h\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Only diagonal variances remain in the upper bound after reflection\n");
    emit("A4 LEAN has made the mean cross products nonpositive. -/\n");
    emit("A4 LEAN theorem tileBound {ι : Type*} [DecidableEq ι] (s : Finset ι)\n");
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
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The midpoint between copies of a tile of width 2h is a site plane. -/\n");
    emit("A4 LEAN theorem tileReflection (a h i j : ℤ) :\n");
    emit("A4 LEAN     2*(a+(i+j+1)*h)-(a+2*i*h) = a+2*(j+1)*h ∧\n");
    emit("A4 LEAN     2*(a+(i+j+1)*h)-(a+2*(i+1)*h) = a+2*j*h := by\n");
    emit("A4 LEAN   constructor <;> ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Covariance cancellation leaves the boundary terms in the free box. -/\n");
    emit("A4 LEAN theorem removeVolume {ι : Type*} (u : Finset ι) (C overlap : ι → ℝ)\n");
    emit("A4 LEAN     (volume : ℝ) (cancel : ∑ z ∈ u, C z = 0) :\n");
    emit("A4 LEAN     ∑ z ∈ u, overlap z*C z = ∑ z ∈ u, (overlap z-volume)*C z := by\n");
    emit("A4 LEAN   simp only [sub_mul, sum_sub_distrib, ← mul_sum, cancel, mul_zero, sub_zero]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- At h = beta^(1/40) the surface term per unit volume and the\n");
    emit("A4 LEAN accumulated pointwise error have the same power. -/\n");
    emit("A4 LEAN theorem susceptibilityBudget (h : ℝ) (hh : 0 < h) :\n");
    emit("A4 LEAN     h^3/h^4 + h^4/h^5 = 2/h := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A local density rescaling by 1/beta rescales the variance by its square. -/\n");
    emit("A4 LEAN theorem rawScale (t : ℝ) (ht : 0 < t) : (1/t)/(t^40)^2 = 1/t^81 := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A centered cube test with squared norm 1/27 converts a\n");
    emit("A4 LEAN correlation into a conditional variance bound. -/\n");
    emit("A4 LEAN theorem cubeTest (v t : ℝ) (cs : t^2 ≤ v*(1/27)) : 27*t^2 ≤ v := by\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.OddClover\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.commonCovector\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.centeredSymbol\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.tileBound\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.tileReflection\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.removeVolume\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.susceptibilityBudget\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.rawScale\n");
    emit("A4 LEAN #print axioms YangMills.OddClover.cubeTest\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
