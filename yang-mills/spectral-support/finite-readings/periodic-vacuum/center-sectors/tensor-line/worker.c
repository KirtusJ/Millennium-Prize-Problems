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
    for(int n=1; n<=50; ++n)
        if(4*n*n-n*n<=0)return 0;
#elif ROLE == 1
    for(int a=-4;a<=4;a++)for(int m=-4;m<=4;m++)for(int l=-4;l<=4;l++)
        if((m-a)*(m-l)!=m*m-(a+l)*m+a*l)return 0;
#else
    for(int w=1;w<=10;w++)for(int d=0;d<=10;d++)for(int r=0;r<=d*w;r++)
        if(w+r>w*(1+d))return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Analysis.InnerProductSpace.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.TensorLine\n");
    emit("A4 LEAN open scoped RealInnerProductSpace\n");
    emit("A4 LEAN variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Three cyclically related differences sum to zero and have equal lengths. -/\n");
    emit("A4 LEAN theorem contrastGram (u v : H) (equal : ‖v‖ = ‖u‖) (third : ‖u+v‖ = ‖u‖) :\n");
    emit("A4 LEAN     2*⟪u,v⟫ = -‖u‖^2 := by\n");
    emit("A4 LEAN   have base := norm_add_sq_real u v\n");
    emit("A4 LEAN   rw [third, equal] at base\n");
    emit("A4 LEAN   linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The two projected differences have positive Gram determinant whenever one is nonzero. -/\n");
    emit("A4 LEAN theorem contrastRank (s k : ℝ) (hs : 0 < s) (off : 2*k = -s) :\n");
    emit("A4 LEAN     0 < s*s-k*k := by\n");
    emit("A4 LEAN   have h : k = -s/2 := by linarith\n");
    emit("A4 LEAN   rw [h]\n");
    emit("A4 LEAN   nlinarith [mul_pos hs hs]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The two weighted polynomial inequalities used for an isolated spectral point. -/\n");
    emit("A4 LEAN theorem templeFactors (a b μ root variance : ℝ) :\n");
    emit("A4 LEAN     variance+(μ-a)*(μ-root) = variance+μ^2-(a+root)*μ+a*root ∧\n");
    emit("A4 LEAN     variance+(μ-b)*(μ-root) = variance+μ^2-(b+root)*μ+b*root := by\n");
    emit("A4 LEAN   constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem templeUpper (a μ root variance : ℝ) (gap : 0 < μ-a)\n");
    emit("A4 LEAN     (moment : 0 ≤ variance + (μ-a)*(μ-root)) :\n");
    emit("A4 LEAN     root ≤ μ+variance/(μ-a) := by\n");
    emit("A4 LEAN   have h : root-μ ≤ variance/(μ-a) := (le_div_iff₀ gap).2 (by nlinarith)\n");
    emit("A4 LEAN   linarith\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A ratio of positive spectral weights gives a lower fraction after reweighting. -/\n");
    emit("A4 LEAN theorem fractionFromOdds (w tail d : ℝ) (hw : 0 < w) (hr : 0 ≤ tail)\n");
    emit("A4 LEAN     (hd : 0 ≤ d) (bound : tail ≤ d*w) : 1/(1+d) ≤ w/(w+tail) := by\n");
    emit("A4 LEAN   apply (div_le_div_iff₀ (by linarith : 0 < 1+d) (by linarith : 0 < w+tail)).2\n");
    emit("A4 LEAN   nlinarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem varianceDegree : 2*6+2*25 ≤ 2*32-1 := by decide\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Both orientations of the four-lag filter have the same spectral crossing. -/\n");
    emit("A4 LEAN theorem contrastKernel (x reversed : ℝ) :\n");
    emit("A4 LEAN     x*(-1+x*(13/3+x*(-13/3+x)))+reversed*(1+x*(-13/3+x*(13/3-x))) =\n");
    emit("A4 LEAN       (x-reversed)*(1-x)*(3-x)*(x-1/3) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.TensorLine\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.contrastGram\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.contrastRank\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.templeFactors\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.templeUpper\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.fractionFromOdds\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.varianceDegree\n");
    emit("A4 LEAN #print axioms YangMills.TensorLine.contrastKernel\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
