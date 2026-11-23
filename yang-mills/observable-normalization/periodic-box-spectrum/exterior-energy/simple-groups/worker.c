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
    for(int a=-9;a<=9;++a)for(int b=-9;b<=9;++b)for(int d=2;d<=9;++d)
        if(d*(a+b)*(a+b)<(d-1)*a*a-d*d*b*b)return 0;
#elif ROLE == 1
    for(int x=-2;x<=2;++x)for(int y=-2;y<=2;++y)for(int a=-3;a<=3;++a)for(int b=-3;b<=3;++b)
        if((x*b-y*a)*(x*b-y*a)!=(x*x+y*y)*(a*a+b*b)-(x*a+y*b)*(x*a+y*b))return 0;
#else
    for(int n=2;n<=50;++n)for(int k=1;k<n;++k)if(k*(n-k)<n-1)return 0;
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
    emit("A4 LEAN namespace YangMills.RootCost\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem remainder (a b e : ℝ) (he : 0 < e) :\n");
    emit("A4 LEAN     e*(a+b)^2 ≥ e*(1-e)*a^2 - b^2 := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (e*a+b), mul_nonneg (le_of_lt he) (sq_nonneg b)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem shift (a b t : ℝ) : a*t+b = a*(t+b/a) ∨ a=0 := by\n");
    emit("A4 LEAN   by_cases h : a=0\n");
    emit("A4 LEAN   · exact Or.inr h\n");
    emit("A4 LEAN   · left\n");
    emit("A4 LEAN     field_simp\n");
    emit("A4 LEAN     ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem transverse (x y z a b c : ℝ) :\n");
    emit("A4 LEAN     (x*b-y*a)^2+(x*c-z*a)^2+(y*c-z*b)^2 =\n");
    emit("A4 LEAN       (x^2+y^2+z^2)*(a^2+b^2+c^2)-(x*a+y*b+z*c)^2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem chamber (p q m x y : ℝ) (hp : 0 ≤ p) (hq : 0 ≤ q)\n");
    emit("A4 LEAN     (hx : m ≤ x) (hy : m ≤ y) : m*(p+q) ≤ p*x+q*y := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg hp (sub_nonneg.mpr hx),mul_nonneg hq (sub_nonneg.mpr hy)]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem cluster (n k : ℝ) (hk : 1 ≤ k) (hn : k ≤ n-1) :\n");
    emit("A4 LEAN     n-1 ≤ k*(n-k) := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr hn)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.RootCost\n");
    emit("A4 LEAN #print axioms YangMills.RootCost.remainder\n");
    emit("A4 LEAN #print axioms YangMills.RootCost.shift\n");
    emit("A4 LEAN #print axioms YangMills.RootCost.transverse\n");
    emit("A4 LEAN #print axioms YangMills.RootCost.chamber\n");
    emit("A4 LEAN #print axioms YangMills.RootCost.cluster\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
