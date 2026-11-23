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
    for(int axis=0;axis<3;++axis)for(int mask=1;mask<8;++mask){
        int average=0;
        for(int site=0;site<8;++site){
            int m=site&mask;
            int parity=(m&1)+((m>>1)&1)+((m>>2)&1);
            average+=(parity&1)?-1:1;
        }
        if(average!=0)return 0;
    }
#elif ROLE == 1
    for(int d=1;d<=7;++d)for(int x=-4;x<=4;++x)for(int y=-4;y<=4;++y)
    for(int b=-4;b<=4;++b)if(d*(2*b*x*y-d*y*y)>b*b*x*x)return 0;
#else
    /* The neutral combination on the eight distinct center images. */
    for(int mask=0;mask<8;++mask){
        int counts[8]={0};
        for(int corner=0;corner<8;++corner)counts[corner^mask]++;
        for(int i=0;i<8;++i)if(counts[i]!=1)return 0;
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
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.JointSpectrum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem meanVariance (s h : ℝ) (hh : h ≠ 0) (scale : s^2=h^3) :\n");
    emit("A4 LEAN     s^2/(8*h^2)=h/8 := by\n");
    emit("A4 LEAN   rw [scale]\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem matrixDilation (k v : ℝ) :\n");
    emit("A4 LEAN     4*k/16+16*v/16=(k/2+2*v)/2 := by ring\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- An orbit tilt linear in the background enters the transverse curl squared\n");
    emit("A4 LEAN only quadratically on this two-site lattice. -/\n");
    emit("A4 LEAN theorem transverseCurl (s q t a b w : ℝ) :\n");
    emit("A4 LEAN     (s+t^2*a)*(q+t^2*b)-(t*w)^2-s*q =\n");
    emit("A4 LEAN     t^2*(a*q+s*b+t^2*a*b-w^2) := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem sumDifference (u v k l : ℝ) :\n");
    emit("A4 LEAN     (u+k)^2+(v+l)^2-(u^2+v^2)=2*(u*k+v*l)+(k^2+l^2) := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Separate ordered energy bounds do not give a lower bound for a difference. -/\n");
    emit("A4 LEAN theorem trialOrdering : ∃ (a₀ a₁ u₀ u₁ : ℝ), a₀ < a₁ ∧ a₀ ≤ u₀ ∧ a₁ ≤ u₁ ∧\n");
    emit("A4 LEAN     a₁-a₀ < u₁-u₀ := by\n");
    emit("A4 LEAN   exact ⟨0,1,1,3,by norm_num,by norm_num,by norm_num,by norm_num⟩\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Equal cross terms among eight image vectors, each normalized by 1/√8. -/\n");
    emit("A4 LEAN theorem centerAverage (diagonal off : ℝ) :\n");
    emit("A4 LEAN     (8*diagonal+56*off)/8=diagonal+7*off := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.JointSpectrum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.meanVariance\n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.matrixDilation\n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.transverseCurl\n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.sumDifference\n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.trialOrdering\n");
    emit("A4 LEAN #print axioms YangMills.JointSpectrum.centerAverage\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
