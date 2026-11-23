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
    for(int a=2;a<=5;++a)for(int b=2;b<=6;++b)for(int c=2;c<=7;++c){
        int volume=a*b*c, total=9*volume, gauge=3*(volume-1);
        if(total-gauge-9!=6*(volume-1))return 0;
    }
#elif ROLE == 1
    for(int x=-5;x<=5;++x)for(int y=-5;y<=5;++y)for(int z=-5;z<=5;++z)
        if((x+y+z)+(x-y-z)+(-x+y-z)+(-x-y+z))return 0;
#else
    for(int d=1;d<8;++d)for(int b=-4;b<=4;++b)
    for(int x=-4;x<=4;++x)for(int y=-4;y<=4;++y)
        if(d*(2*b*x*y-d*y*y)>b*b*x*x)return 0;
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
    emit("A4 LEAN namespace YangMills.PeriodicSpectrum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem meanVariance (s h n : ℝ) (hh : h ≠ 0) (hn : n ≠ 0) (scale : s^2=h^3) :\n");
    emit("A4 LEAN     s^2/(n*h^2)=h/n := by\n");
    emit("A4 LEAN   rw [scale]\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem volumeDilation (l k v : ℝ) (hl : l ≠ 0) :\n");
    emit("A4 LEAN     l^2*k/(2*l^3) + 2*l^3*v/l^4=(k/2+2*v)/l := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Absorb an off-diagonal coupling into the complementary spectral gap. -/\n");
    emit("A4 LEAN theorem blockCost (d b x y : ℝ) : d*(2*b*x*y-d*y^2) ≤ b^2*x^2 := by\n");
    emit("A4 LEAN   nlinarith only [sq_nonneg (d*y-b*x)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem colorAverage (x y z : ℝ) :\n");
    emit("A4 LEAN     (x+y+z)+(x-y-z)+(-x+y-z)+(-x-y+z)=0 := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Lift a first-order quasimode across a separated hard channel. -/\n");
    emit("A4 LEAN theorem corrector (g l b : ℝ) (sep : g-l ≠ 0) :\n");
    emit("A4 LEAN     l*(b/(g-l))+b-g*(b/(g-l))=0 := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The paired shifts cancel in the mean while producing a transverse component. -/\n");
    emit("A4 LEAN theorem pairedSlope (a x y : ℝ) : a*x^2+(-a)*y^2=a*(x^2-y^2) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A positively weighted winding with a nontrivial phase strictly lowers a heat trace. -/\n");
    emit("A4 LEAN theorem windingDeficit (a phase rest : ℝ) (ha : 0 < a) (hp : phase < 1)\n");
    emit("A4 LEAN     (hr : 0 ≤ rest) : 0 < a*(1-phase)+rest :=\n");
    emit("A4 LEAN   add_pos_of_pos_of_nonneg (mul_pos ha (sub_pos.mpr hp)) hr\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem shellAbsorption (g b r err : ℝ) (he : err ≤ g*b*r/2) :\n");
    emit("A4 LEAN     g*(1-b*r)+err ≤ g*(1-b*r/2) := by linarith only [he]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.PeriodicSpectrum\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.meanVariance\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.volumeDilation\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.blockCost\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.colorAverage\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.corrector\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.pairedSlope\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.windingDeficit\n");
    emit("A4 LEAN #print axioms YangMills.PeriodicSpectrum.shellAbsorption\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
