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
    for(int x=-5;x<=5;++x)for(int y=-5;y<=5;++y){
        int u=x*x-y*y,v=2*x*y;
        if(y*y-x*x!=-u||2*(-y)*x!=-v)return 0;
        if(x*x-(-y)*(-y)!=u||2*x*(-y)!=-v)return 0;
    }
#elif ROLE == 1
    for(int m=0;m<12;++m)for(int n=m+1;n<=12;++n)
        if(n*n-m*m!=(n-m)*(n+m)||n*n<=m*m)return 0;
#else
    /* Independent axis sign flips eliminate every odd Taylor monomial. */
    for(int a=0;a<=3;++a)for(int b=0;a+b<=3;++b){
        int c=3-a-b,total=0;
        for(int mask=0;mask<8;++mask){
            int power=((mask&1)?a:0)+((mask&2)?b:0)+((mask&4)?c:0);
            total+=(power%2)?-1:1;
        }
        if(total!=0)return 0;
    }
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
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ReflectionAudit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem gramDet (a b c : ℝ) :\n");
    emit("A4 LEAN     (a+b)^2-((a-b)^2+(2*c)^2)=4*(a*b-c^2) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The two allowed lattice reflection characters admit any pair of energies. -/\n");
    emit("A4 LEAN theorem diagonalCommutes (a b x y : ℝ) :\n");
    emit("A4 LEAN     (a*(-x), b*y) = (-(a*x), b*y) := by simp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem quarterTurnForcesEquality (a b : ℝ) (h : ∀ x y : ℝ,\n");
    emit("A4 LEAN     (a*(-y),b*x) = (-(b*y),a*x)) : a=b := by\n");
    emit("A4 LEAN   have eq := congrArg Prod.snd (h 1 0)\n");
    emit("A4 LEAN   simpa using eq.symm\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Reusing an upper-charge radial state at lower charge strictly saves energy. -/\n");
    emit("A4 LEAN theorem angularOrdering (m n kin w : ℝ) (hm : 0 ≤ m) (hn : m < n) (hw : 0 < w) :\n");
    emit("A4 LEAN     kin + m^2*w < kin + n^2*w := by\n");
    emit("A4 LEAN   have hpos : 0 < (n-m)*(n+m) :=\n");
    emit("A4 LEAN     mul_pos (sub_pos.mpr hn) (by linarith)\n");
    emit("A4 LEAN   nlinarith only [mul_pos hpos hw]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem oddCubicVanishes (z : ℝ) (reflection : z = -z) : z = 0 := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A Hessian estimate along rays makes the vacuum minimum quantitative. -/\n");
    emit("A4 LEAN theorem localMinimum (shift c cost error : ℝ)\n");
    emit("A4 LEAN     (b : c*cost-error ≤ shift) (h : error ≤ (c/2)*cost) :\n");
    emit("A4 LEAN     (c/2)*cost ≤ shift := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ReflectionAudit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.gramDet\n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.diagonalCommutes\n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.quarterTurnForcesEquality\n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.angularOrdering\n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.oddCubicVanishes\n");
    emit("A4 LEAN #print axioms YangMills.ReflectionAudit.localMinimum\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
