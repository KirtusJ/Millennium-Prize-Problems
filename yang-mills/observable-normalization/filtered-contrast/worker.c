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
static int oddfactor(int power){
    int product=1;
    for(int j=1;j<power;j+=2) product*=j;
    return product;
}
static int verify_count(void){
#if ROLE == 0
    /* Clear the thirds in the exact difference of two orientation multipliers. */
    for(long a=3;a<=11;++a) for(long x=0;x<=4;++x) for(long y=0;y<=4;++y){
        long nx=(3+2*x)*(1-x), ny=(3+2*y)*(1-y);
        if(nx*(a-y)-ny*(a-x)!=(x-y)*(3-a-2*a*(x+y)+2*x*y)) return 0;
    }
    return 1;
#else
#if ROLE == 1
    const int count=2, degree=2, norm=2*108;
    const int terms[][4]={{1,2,0,0},{-1,0,2,0}};
    const int num=1, den=1890;
#else
    const int count=4, degree=4, norm=2*3*216*216;
    const int terms[][4]={{-8,4,0,0},{8,0,4,0},{1,2,0,2},{-1,0,2,2}};
    const int num=331, den=26943840;
#endif
    long sum=0;
    for(int i=0;i<count;++i) for(int j=0;j<count;++j){
        long v=terms[i][0]*terms[j][0];
        for(int axis=1;axis<=3;++axis)
            v*=oddfactor(terms[i][axis]+terms[j][axis]);
        sum+=v;
    }
    return 3L*sum*den==(long)num*norm*(2*degree+3)*oddfactor(2*degree+2);
#endif
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.FilteredContrast\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem orientationDifference (a x y : ℝ) :\n");
    emit("A4 LEAN     (3+2*x)*(1-x)*(a-y)-(3+2*y)*(1-y)*(a-x) =\n");
    emit("A4 LEAN     (x-y)*(3-a-2*a*(x+y)+2*x*y) := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem cubicAverage : ((3-1)/(35*108) : ℝ) = 1/1890 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem quarticShape (x y z : ℝ) :\n");
    emit("A4 LEAN     (x^2+y^2+z^2)*(x^2-y^2)-9*(x^4-y^4) =\n");
    emit("A4 LEAN     -8*x^4+8*y^4+x^2*z^2-y^2*z^2 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem quarticAverage :\n");
    emit("A4 LEAN     (3*(128*105-128*9+2*9-2*3-32*15+32*3)/(11*945*2*3*216^2) : ℝ)\n");
    emit("A4 LEAN     = 331/26943840 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.FilteredContrast\n");
    emit("A4 LEAN #print axioms YangMills.FilteredContrast.orientationDifference\n");
    emit("A4 LEAN #print axioms YangMills.FilteredContrast.cubicAverage\n");
    emit("A4 LEAN #print axioms YangMills.FilteredContrast.quarticShape\n");
    emit("A4 LEAN #print axioms YangMills.FilteredContrast.quarticAverage\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
