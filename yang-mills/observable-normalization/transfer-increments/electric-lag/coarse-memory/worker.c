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
    /* Variance numerator under a fine fiber with integer weights. */
    for(int W=1;W<=20;++W) for(int w=0;w<=W;++w)
    for(int x=-8;x<=8;++x)for(int y=-8;y<=8;++y){
        int first=w*x+(W-w)*y, second=w*x*x+(W-w)*y*y;
        if(W*second-first*first!=w*(W-w)*(x-y)*(x-y))return 0;
    }
#elif ROLE == 1
    /* Binary endpoints conditionally independent at each hidden state.
       Counts are unnormalized and the hidden state's mass is uniform. */
    for(int d=2;d<=12;++d)for(int a=0;a<=d;++a)for(int b=0;b<=d;++b){
        int n[2][2]={{0,0},{0,0}};
        for(int h=0;h<2;++h){
            int p=h?a:b,w[2]={d-p,p};
            for(int i=0;i<2;++i)for(int j=0;j<2;++j)n[i][j]+=w[i]*w[j];
        }
        int mean[2]={2*d-a-b,a+b};
        for(int i=0;i<2;++i)for(int j=0;j<2;++j){
            int diff=2*n[i][j]-mean[i]*mean[j];
            if(diff!=(i==j?1:-1)*(a-b)*(a-b))return 0;
        }
    }
#else
    /* Compute the trace memory directly and via the squared residual
       in a reversible four-state integer-weight chain. */
    for(int a=1;a<=4;++a)for(int b=1;b<=4;++b){
        int M[4][4]={{5,2,a,b},{2,5,b,a},{a,b,5,2},{b,a,2,5}};
        /* Observing {0,2} versus {1,3} would lump this example.
           Use {0,1,2} and {3} to exercise nonzero residuals. */
        int f[4]={1,1,1,-1},u[4]={0},twice[4]={0};
        for(int i=0;i<4;++i)for(int j=0;j<4;++j)u[i]+=M[i][j]*f[j];
        for(int i=0;i<4;++i)for(int j=0;j<4;++j)twice[i]+=M[i][j]*u[j];
        int sum=u[0]+u[1]+u[2],diff=0,res=0;
        for(int i=0;i<4;++i){
            int bar=i==3?3*u[3]:sum;
            diff+=9*f[i]*twice[i]-bar*bar;
            res+=(3*u[i]-bar)*(3*u[i]-bar);
        }
        if(diff!=res || res<0)return 0;
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.CoarseMemory\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Fiber variance of a two-point fine law at a fixed coarse value. -/\n");
    emit("A4 LEAN theorem fiberVariance (w x y : ℝ) :\n");
    emit("A4 LEAN     w*x^2+(1-w)*y^2-(w*x+(1-w)*y)^2=w*(1-w)*(x-y)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem variancePositive (w x y : ℝ) (hw : 0 < w) (hw' : w < 1)\n");
    emit("A4 LEAN     (hxy : x ≠ y) : 0 < w*(1-w)*(x-y)^2 := by\n");
    emit("A4 LEAN   exact mul_pos (mul_pos hw (sub_pos.mpr hw')) (sq_pos_of_ne_zero (sub_ne_zero.mpr hxy))\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Covariances kill the common constant in the electric endpoint law. -/\n");
    emit("A4 LEAN theorem covarianceProduct (a b x y t : ℝ) :\n");
    emit("A4 LEAN     (a+t*x)*(b+t*y)-a*b-t*(a*y+b*x)=t^2*x*y := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem traceResponse (a b : ℝ) :\n");
    emit("A4 LEAN     (a/4)^2+3*(b/4)^2=(a^2+3*b^2)/16 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- For binary endpoints the four deviations from the independent law\n");
    emit("A4 LEAN have equal magnitudes and sum to zero. -/\n");
    emit("A4 LEAN theorem binaryResidual (x y m v : ℝ) :\n");
    emit("A4 LEAN     (1+m*x+m*y+(m^2+v)*x*y)/4-((1+m*x)/2)*((1+m*y)/2)=v*x*y/4 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.CoarseMemory\n");
    emit("A4 LEAN #print axioms YangMills.CoarseMemory.fiberVariance\n");
    emit("A4 LEAN #print axioms YangMills.CoarseMemory.variancePositive\n");
    emit("A4 LEAN #print axioms YangMills.CoarseMemory.covarianceProduct\n");
    emit("A4 LEAN #print axioms YangMills.CoarseMemory.traceResponse\n");
    emit("A4 LEAN #print axioms YangMills.CoarseMemory.binaryResidual\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
