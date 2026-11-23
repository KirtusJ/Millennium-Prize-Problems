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
    for(int n=2;n<=12;++n){
        int edges=3*n*n*(n-1), tree=n*n*n-1;
        int cycles=edges-tree;
        if(cycles!=2*n*n*n-3*n*n+1 || cycles<1)return 0;
    }
#elif ROLE == 1
    /* For signed mass a over cell mass p, |a|<=M*p implies a²<=M*|a|*p. */
    for(int p=1;p<=9;++p)for(int m=0;m<=4;++m)
    for(int a=-m*p;a<=m*p;++a)if(a*a>m*p*(a<0?-a:a))return 0;
#else
    for(int x=-8;x<=8;++x)for(int y=-8;y<=8;++y)for(int s=-1;s<=1;s+=2)
        if((s*x)*(s*y)!=x*y)return 0;
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
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.SupportCriterion\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The private chords form an identity minor in the cycle Gram bound. -/\n");
    emit("A4 LEAN theorem privateChords (a b t u : ℝ) :\n");
    emit("A4 LEAN     a^2+b^2 ≤ a^2+b^2+(a*t+b*u)^2 := by nlinarith [sq_nonneg (a*t+b*u)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem gaussianFloor (m : ℝ) (hm : 0 ≤ m) (hc : m ≤ 12) :\n");
    emit("A4 LEAN     m+m^2/4 ≤ 48 := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg (sub_nonneg.mpr hc) (show 0 ≤ 12+m by linarith)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Pointwise L²-versus-L¹ bound for a bounded conditional mean. -/\n");
    emit("A4 LEAN theorem conditionalSquare (u M : ℝ) (ht : |u| ≤ M) : u^2 ≤ M*|u| := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     u^2 = |u| * |u| := by rw [← sq, sq_abs]\n");
    emit("A4 LEAN     _ ≤ _ := mul_le_mul_of_nonneg_right ht (abs_nonneg u)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem centeredPair (joint marginal mean : ℝ) :\n");
    emit("A4 LEAN     joint - mean*marginal = 0 ↔ joint = mean*marginal := sub_eq_zero\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem neutralSign (s x y : ℝ) (hs : s^2=1) : (s*x)*(s*y)=x*y := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _=s^2*(x*y) := by ring\n");
    emit("A4 LEAN     _=_ := by rw [hs,one_mul]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem covarianceTail (near far bound t : ℝ) (hk : far ≤ bound)\n");
    emit("A4 LEAN     (ht : 0 ≤ t) : near+t*far ≤ near+t*bound := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg ht (sub_nonneg.mpr hk)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.SupportCriterion\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.privateChords\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.gaussianFloor\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.conditionalSquare\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.centeredPair\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.neutralSign\n");
    emit("A4 LEAN #print axioms YangMills.SupportCriterion.covarianceTail\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
