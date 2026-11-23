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
    for(int x=1;x<7;++x)for(int a=-2;a<=2;++a)for(int b=-2;b<=2;++b)
    for(int c=-2;c<=2;++c)for(int d=-2;d<=2;++d){
        int p=a*b+c*d, t=a*d-b*c, z=x*x;
        if((z-a*a-c*c)*(z-b*b-d*d)-p*p!=z*z-z*(a*a+b*b+c*c+d*d)+t*t)return 0;
    }
#elif ROLE == 1
    for(int r=1;r<50;++r)for(int x=0;x<=r;++x)
        if((r-x)*r>r*r-x*x)return 0;
#else
    for(int x=-4;x<5;++x)for(int z=-4;z<5;++z)
        if(-2*z*(2*x+z)+4*x*z!=-2*z*z)return 0;
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
    emit("A4 LEAN namespace YangMills.AiryWall\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem jacobianPolynomial (x a b c d : ℝ) :\n");
    emit("A4 LEAN     (x^2-a^2-c^2)*(x^2-b^2-d^2)-(a*b+c*d)^2 =\n");
    emit("A4 LEAN     x^4-x^2*(a^2+b^2+c^2+d^2)+(a*d-b*c)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem wallShift (R x s : ℝ) (hx : 0 ≤ x) (h : x ≤ R)\n");
    emit("A4 LEAN     (he : R^2 ≤ x^2+s) : (R-x)*R ≤ s := by\n");
    emit("A4 LEAN   nlinarith only [he,mul_nonneg hx (sub_nonneg.mpr h)]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem potentialSplit (x u v : ℝ) :\n");
    emit("A4 LEAN     2*(x^2*u^2+x^2*v^2+u^2*v^2)=\n");
    emit("A4 LEAN     2*x^2*(u^2+v^2)+2*(u*v)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem fourSquares (x a b c d : ℝ) :\n");
    emit("A4 LEAN     2*x^2*(a^2+b^2+c^2+d^2)=\n");
    emit("A4 LEAN     ((2*x*a)^2+(2*x*b)^2+(2*x*c)^2+(2*x*d)^2)/2 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem airyRescaling (x z f : ℝ) :\n");
    emit("A4 LEAN     -(4*f*(2*x+z))/2+4*x*f = -2*z*f := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem gaussianVariance (v : ℝ) :\n");
    emit("A4 LEAN     (4*3*v^2+12*v^2)-(4*v)^2=8*v^2 := by ring\n");
    emit("A4 LEAN end YangMills.AiryWall\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.jacobianPolynomial\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.wallShift\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.potentialSplit\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.fourSquares\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.airyRescaling\n");
    emit("A4 LEAN #print axioms YangMills.AiryWall.gaussianVariance\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
