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
    for(int x=-4;x<=4;++x)for(int y=-4;y<=4;++y)for(int t=0;t<=4;++t)
    for(int f=-1;f<=1;++f)
        if((x*x+t*t)*(y*y+t*t)-(f*t*t+x*y)*(f*t*t+x*y)!=
           (1-f*f)*t*t*(y*y+t*t)+t*t*(f*y-x)*(f*y-x))return 0;
#elif ROLE == 1
    for(int u=-5;u<=5;++u)for(int z=-4;z<=4;++z)
        if(1+2*u*z+z*z-(1+u*z)*(1+u*z)!=(1-u*u)*z*z)return 0;
#else
    for(int u=-9;u<=9;++u){
        int u2=u*u,u4=u2*u2;
        if(11*u4-(16*u4-12*u2-3*u2+6*u4+4*u4)!=15*(u2-u4))return 0;
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
    emit("A4 LEAN namespace YangMills.PlaneOverlap\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem horizontalLoss (x y t f : ℝ) :\n");
    emit("A4 LEAN     (x^2+t^2)*(y^2+t^2)-(f*t^2+x*y)^2 =\n");
    emit("A4 LEAN     (1-f^2)*t^2*(y^2+t^2)+t^2*(f*y-x)^2 := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem continuumLoss (u z : ℝ) :\n");
    emit("A4 LEAN     1+2*u*z+z^2-(1+u*z)^2=(1-u^2)*z^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem productSquare (u v : ℝ) :\n");
    emit("A4 LEAN     (v-u)^2-u^2=v*(v-2*u) := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Quartic coefficient in [log(1+uz)^2 - 2 log(1+uz) log(l)/2]/2,\n");
    emit("A4 LEAN where l is the shifted momentum norm. -/\n");
    emit("A4 LEAN theorem quartic (u : ℝ) :\n");
    emit("A4 LEAN     ((u^4/4+2*u^4/3)-\n");
    emit("A4 LEAN     (u*(4*u^3/3-u)+(-u^2/2)*(1/2-u^2)+(u^3/3)*u))/2\n");
    emit("A4 LEAN     =5*u^2*(1-u^2)/8 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.PlaneOverlap\n");
    emit("A4 LEAN #print axioms YangMills.PlaneOverlap.horizontalLoss\n");
    emit("A4 LEAN #print axioms YangMills.PlaneOverlap.continuumLoss\n");
    emit("A4 LEAN #print axioms YangMills.PlaneOverlap.productSquare\n");
    emit("A4 LEAN #print axioms YangMills.PlaneOverlap.quartic\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
