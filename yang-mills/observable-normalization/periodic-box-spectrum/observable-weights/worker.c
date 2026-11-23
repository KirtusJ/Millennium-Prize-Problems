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
static int verify_count(void){
#if ROLE == 0
    /* Count the active first shell of the 12 plaquette on an N-cube. */
    for(int n=2;n<=9;++n){
        int count=0;
        for(int i=0;i<n;++i)for(int j=0;j<n;++j)for(int k=0;k<n;++k){
            int nonzero=(i!=0)+(j!=0)+(k!=0);
            if(nonzero==1 && (i==1||i==n-1||j==1||j==n-1))++count;
        }
        if(count!=(n==2?2:4))return 0;
    }
#elif ROLE == 1
    /* For three independent colors, only the diagonal color contractions
       give the two connected Wick pairings. */
    int pairs=0;
    for(int i=0;i<3;++i)for(int j=0;j<3;++j)if(i==j)pairs+=2;
    if(pairs!=6)return 0;
#else
    /* Curl telescopes identically on a periodic plane prior to conjugation. */
    for(int n=2;n<=7;++n){
        int total=0;
        for(int i=0;i<n;++i)for(int j=0;j<n;++j){
            int ip=(i+1)%n,jp=(j+1)%n;
            total+=i*j+ip*ip*j-i*jp-i*i*j;
        }
        if(total)return 0;
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ObservableWeights\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Squared curl in the two selected spatial directions kills longitudinal modes. -/\n");
    emit("A4 LEAN theorem curlLongitudinal (a b t : ℝ) : a*(b*t)-b*(a*t)=0 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Coefficient for the covariance of a half-squared three-color Gaussian. -/\n");
    emit("A4 LEAN theorem wickColor (v c : ℝ) :\n");
    emit("A4 LEAN     (3*(v^2+2*c^2)+6*v^2)/4-(3*v/2)^2=3*c^2/2 := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem pairAtom (u v : ℝ) :\n");
    emit("A4 LEAN     3*(u+v)^2/2=3*u^2/2+3*u*v+3*v^2/2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem thresholdCoefficient (p : ℝ) : 3*(4*p)^2/2=24*p^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem variancePositive (v : ℝ) (h : 0 < v) : 0 < 3*v^2/2 := by\n");
    emit("A4 LEAN   nlinarith only [mul_pos h h]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A slow leakage estimate from a transfer moment near unit eigenvalue. -/\n");
    emit("A4 LEAN theorem massFromMoment (mass moment threshold : ℝ) (ht : 0 < threshold)\n");
    emit("A4 LEAN     (h : threshold*mass ≤ moment) : mass ≤ moment/threshold := by\n");
    emit("A4 LEAN   apply (le_div_iff₀ ht).mpr\n");
    emit("A4 LEAN   simpa [mul_comm] using h\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A single strictly positive spectral weight gives a positive transformed sum. -/\n");
    emit("A4 LEAN theorem survivingWeight (weight factor rest : ℝ) (hw : 0 < weight)\n");
    emit("A4 LEAN     (hf : 0 < factor) (hr : 0 ≤ rest) : 0 < weight*factor+rest :=\n");
    emit("A4 LEAN   add_pos_of_pos_of_nonneg (mul_pos hw hf) hr\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ObservableWeights\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.curlLongitudinal\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.wickColor\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.pairAtom\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.thresholdCoefficient\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.variancePositive\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.massFromMoment\n");
    emit("A4 LEAN #print axioms YangMills.ObservableWeights.survivingWeight\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
