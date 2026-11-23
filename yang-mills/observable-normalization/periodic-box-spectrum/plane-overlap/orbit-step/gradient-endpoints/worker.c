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
    for(int a=-3;a<=3;a++)for(int b=-3;b<=3;b++)
    for(int c=-3;c<=3;c++)for(int d=-3;d<=3;d++)
        if(a*(d-b)-b*(c-a)+c*(-d)-d*(-c)!=a*d-b*c)return 0;
#elif ROLE == 1
    for(int a=-8;a<=8;a++)for(int b=-8;b<=8;b++)
        if(8*a*b!=2*a*b+2*a*b-(-2*a*b)-(-2*a*b))return 0;
#else
    for(int a=-8;a<=8;a++)for(int b=-8;b<=8;b++)
        if(4*(2*a*b)*(2*a*b)+(8*a*b)*(8*a*b)!=80*a*a*b*b)return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN namespace YangMills.GradientEndpoints\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- One coordinate of the second-order imaginary quaternion term. -/\n");
    emit("A4 LEAN theorem productArea (a b c d : ℝ) :\n");
    emit("A4 LEAN     a*(d-b)-b*(c-a) + (a+c-a)*(-d)-(b+d-b)*(-c) = a*d-b*c := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem originShift (a b c d u v : ℝ) :\n");
    emit("A4 LEAN     (a+u)*(d+v)-(b+v)*(c+u) = a*d-b*c+u*(d-b)-v*(c-a) := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem squareCurl (a b : ℝ) :\n");
    emit("A4 LEAN     2*a*b+2*a*b-(-2*a*b)-(-2*a*b)=8*a*b := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem linkAndFace (a b : ℝ) :\n");
    emit("A4 LEAN     ((2*a*b)^2+(-2*a*b)^2)/2 + (8*a*b)^2/4=20*a^2*b^2 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem gaussianCancellation (x y : ℝ) :\n");
    emit("A4 LEAN     -(x+y)/2-(-x-y)/2=0 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.GradientEndpoints\n");
    emit("A4 LEAN #print axioms YangMills.GradientEndpoints.productArea\n");
    emit("A4 LEAN #print axioms YangMills.GradientEndpoints.originShift\n");
    emit("A4 LEAN #print axioms YangMills.GradientEndpoints.squareCurl\n");
    emit("A4 LEAN #print axioms YangMills.GradientEndpoints.linkAndFace\n");
    emit("A4 LEAN #print axioms YangMills.GradientEndpoints.gaussianCancellation\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
