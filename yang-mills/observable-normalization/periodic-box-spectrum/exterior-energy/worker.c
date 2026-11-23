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
    for(int a=0;a<=20;++a)for(int b=0;b<=a;++b)for(int c=0;c<=b;++c)
        for(int r=a+1;r<=36;++r)
            if(r*r==a*a+b*b+c*c && r>2*b*b)return 0;
#elif ROLE == 1
    for(int x=-3;x<=3;++x)for(int z=-3;z<=3;++z)
        if((x-z)*(x-z)+(x+z)*(x+z)!=2*(x*x+z*z))return 0;
#else
    for(int r=1;r<40;++r)for(int c=0;c<=3;++c)
        if(2*r*r+2*(r+c)*(r+c)!=4*r*r+4*c*r+2*c*c)return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ExteriorEnergy\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem minorSum (a b c : ℝ) :\n");
    emit("A4 LEAN     2*(a^2*b^2+a^2*c^2+b^2*c^2) ≥ 2*a^2*(b^2+c^2) := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (b*c)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem secondDirection (r a b c : ℝ) (ha : 0 ≤ a) (hc : 0 ≤ c) (hcb : c ≤ b)\n");
    emit("A4 LEAN     (h : r^2=a^2+b^2+c^2) (hr : 1 ≤ r-a) :\n");
    emit("A4 LEAN     r ≤ 2*b^2 := by\n");
    emit("A4 LEAN   have hx : 0 ≤ r+a := by linarith\n");
    emit("A4 LEAN   nlinarith only [h,mul_nonneg (show 0 ≤ r-a-1 by linarith) hx,\n");
    emit("A4 LEAN     mul_nonneg (sub_nonneg.mpr hcb) (show 0 ≤ b+c by linarith),ha]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem fiberSquare (r t : ℝ) :\n");
    emit("A4 LEAN     (2*r*t)^2/2=2*r^2*t^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem planeAverage (l wx wy z v w : ℝ) :\n");
    emit("A4 LEAN     ((wx*w-wy*v)^2+(wy*z-l*w)^2+(l*v-wx*z)^2+\n");
    emit("A4 LEAN      (wx*w-wy*v)^2+(wy*z+l*w)^2+(l*v+wx*z)^2)/2 =\n");
    emit("A4 LEAN     (wx*w-wy*v)^2+z^2*(wx^2+wy^2)+l^2*(v^2+w^2) := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem gaussianEnergy (r c : ℝ) (hr : 0 < r) :\n");
    emit("A4 LEAN     2*r + 2*(r+c)^2/r = 4*r + 4*c + 2*c^2/r := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ExteriorEnergy\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorEnergy.minorSum\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorEnergy.secondDirection\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorEnergy.fiberSquare\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorEnergy.planeAverage\n");
    emit("A4 LEAN #print axioms YangMills.ExteriorEnergy.gaussianEnergy\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
