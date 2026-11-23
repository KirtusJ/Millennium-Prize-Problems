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
    for(int x=-6;x<=6;x++)for(int y=-6;y<=6;y++)
        if(x*x+y*y-2*x*y!=(x-y)*(x-y))return 0;
#elif ROLE == 1
    for(int x=-8;x<=8;x++)for(int y=-8;y<=8;y++)
        if(-(x*x+y*y)+x*x+y*y!=0)return 0;
#else
    for(int t=-6;t<=6;t++)
        if(25-(9+16*t)!=16*(1-t))return 0;
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
    emit("A4 LEAN namespace YangMills.OrbitStep\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem constantAction (c d a b t : ℝ) :\n");
    emit("A4 LEAN     1-(c*d+t*a*b) = (1-c*d)-t*a*b := by ring\n");
    emit("A4 LEAN theorem diagonal (c s t : ℝ) (h : c^2+s^2=1) :\n");
    emit("A4 LEAN     1-(c*c+t*s*s)=(1-t)*s^2 := by nlinarith\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem normalHessian (a b : ℝ) :\n");
    emit("A4 LEAN     (a^2+b^2)/2-a*b=(a-b)^2/2 := by ring\n");
    emit("A4 LEAN theorem contrast (u v : ℝ) :\n");
    emit("A4 LEAN     -(u^2+v^2)/2-((-u^2)+(-v^2))/2=0 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem rotorQuartic (x y z : ℝ) :\n");
    emit("A4 LEAN     (x^2+y^2)/12-z^2/6=(x^2+y^2-2*z^2)/12 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.OrbitStep\n");
    emit("A4 LEAN #print axioms YangMills.OrbitStep.constantAction\n");
    emit("A4 LEAN #print axioms YangMills.OrbitStep.diagonal\n");
    emit("A4 LEAN #print axioms YangMills.OrbitStep.normalHessian\n");
    emit("A4 LEAN #print axioms YangMills.OrbitStep.contrast\n");
    emit("A4 LEAN #print axioms YangMills.OrbitStep.rotorQuartic\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
