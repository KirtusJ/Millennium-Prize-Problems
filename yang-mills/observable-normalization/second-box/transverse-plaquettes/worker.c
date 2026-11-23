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
    int mult[4]={0,0,0,0};
    for(int mask=1;mask<8;++mask){
        int bits=(mask&1)+((mask>>1)&1)+((mask>>2)&1);
        mult[bits]+=6;
    }
    if(mult[1]!=18||mult[2]!=18||mult[3]!=6)return 0;
#elif ROLE == 1
    /* Third powers of every linear projection cancel between opposite points. */
    for(int a=-3;a<=3;++a)for(int b=-3;b<=3;++b){
        int sum=0;
        for(int x=-2;x<=2;++x)for(int y=-2;y<=2;++y){
            int u=a*x+b*y; sum+=u*u*u;
        }
        if(sum)return 0;
    }
#else
    for(int d=1;d<=8;++d)for(int b=-6;b<=6;++b)for(int t=-8;t<=8;++t)
        if(d*(2*b*t-d*t*t)>b*b)return 0;
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
    emit("A4 LEAN namespace YangMills.HardVacuum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Nonconstant Fourier modes of the three-component curl. -/\n");
    emit("A4 LEAN theorem curlSymbol (p q r x y z : ℝ) :\n");
    emit("A4 LEAN     (p*y-q*x)^2+(p*z-r*x)^2+(q*z-r*y)^2 =\n");
    emit("A4 LEAN     (p^2+q^2+r^2)*(x^2+y^2+z^2)-(p*x+q*y+r*z)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem hardCount : 3*2*(3+3+1) = 42 := by decide\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Inversion annihilates a first-order diagonal matrix element. -/\n");
    emit("A4 LEAN theorem parityCancellation (m : ℝ) (odd : m = -m) : m=0 := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- All linear color-invariant covectors vanish, tested against two half turns. -/\n");
    emit("A4 LEAN theorem invariantLinear (a b c : ℝ) (h1 : b = -b ∧ c = -c) (h2 : a = -a) :\n");
    emit("A4 LEAN     a = 0 ∧ b = 0 ∧ c = 0 := by\n");
    emit("A4 LEAN   obtain ⟨hb,hc⟩ := h1\n");
    emit("A4 LEAN   exact ⟨by linarith, by linarith, by linarith⟩\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A complementary spectral gap absorbs first-order off-diagonal coupling. -/\n");
    emit("A4 LEAN theorem rayleighCost (t d b e : ℝ) (hd : 0 < d)\n");
    emit("A4 LEAN     (h : e ≤ 2*b*t-d*t^2) : d*e ≤ b^2 := by\n");
    emit("A4 LEAN   have hmul := mul_le_mul_of_nonneg_left h hd.le\n");
    emit("A4 LEAN   nlinarith only [hmul, sq_nonneg (d*t-b)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem softScale (h : ℝ) (hh : h ≠ 0) : h^3 * (1/h)^2 = h := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Numerator of the moving-plane diagonal coefficient after multiplying by √3. -/\n");
    emit("A4 LEAN theorem positiveCurvature (u v : ℝ) (hu : 0 < u) (hv : 0 < v)\n");
    emit("A4 LEAN     (two : u^2 = 2) (six : v^2 = 6) : 0 < v-u-1 := by\n");
    emit("A4 LEAN   have small : u < 3/2 := by\n");
    emit("A4 LEAN     by_contra! bad\n");
    emit("A4 LEAN     nlinarith only [two, mul_nonneg (sub_nonneg.mpr bad) (show 0 ≤ u+3/2 by linarith)]\n");
    emit("A4 LEAN   by_contra! bad\n");
    emit("A4 LEAN   have q := mul_nonneg (show 0 ≤ u+1-v by linarith) (show 0 ≤ u+1+v by linarith)\n");
    emit("A4 LEAN   nlinarith only [q, small, two, six]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Scalar color component of the fixed-plane quadratic form. -/\n");
    emit("A4 LEAN theorem fixedCurvature (x y z : ℝ) :\n");
    emit("A4 LEAN     -4*(x^2+y^2+z^2) + x*y+x*z+y*z ≤ -3*(x^2+y^2+z^2) := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (x-y), sq_nonneg (x-z), sq_nonneg (y-z)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.HardVacuum\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.curlSymbol\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.hardCount\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.parityCancellation\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.invariantLinear\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.rayleighCost\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.softScale\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.positiveCurvature\n");
    emit("A4 LEAN #print axioms YangMills.HardVacuum.fixedCurvature\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
