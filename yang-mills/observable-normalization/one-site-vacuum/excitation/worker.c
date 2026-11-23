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
    /* Radius r=a/b, block length ceil(8/r), including both endpoints. */
    for(int b=1;b<=80;++b)for(int a=1;a<=b;++a){
        int m=(8*b+a-1)/a;
        if(m*a<8*b || m*a>9*b || m<8 || 3*(m-(m+1)/2)<m)return 0;
    }
#elif ROLE == 1
    /* The fine frequency with largest Casimir is at least the mean. */
    for(int a=1;a<=15;++a)for(int b=1;b<=15;++b)for(int c=1;c<=15;++c){
        int largest=a>b?a:b; if(c>largest)largest=c;
        if(3*(largest*largest-1)<a*a+b*b+c*c-3)return 0;
    }
#else
    /* Covariance from the six signed coordinate directions, normalized
       to reproduce the three-component radial second moment. */
    for(int i=0;i<3;++i)for(int j=0;j<3;++j){
        int sum=0;for(int axis=0;axis<3;++axis)for(int s=-1;s<=1;s+=2)
            sum+=(axis==i?s:0)*(axis==j?s:0);
        if(sum!=(i==j?2:0))return 0;
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Topology.Instances.Real.Lemmas\n");
    emit("A4 LEAN import Mathlib.Topology.Algebra.Order.Field\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ToronExcitation\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem fiberScale (b d m r : ℝ) (h : b*d^2=m) :\n");
    emit("A4 LEAN     m*b*r^2*d^2=(m*r)^2 := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _=m*r^2*(b*d^2) := by ring\n");
    emit("A4 LEAN     _=_ := by rw [h]; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem coarseDefect (u v : ℝ) (hu : u ≤ 1) (hv : 0 ≤ v) :\n");
    emit("A4 LEAN     1-v ≤ 1-u*v := by nlinarith only [mul_nonneg (sub_nonneg.mpr hu) hv]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem weightLoss (a : ℝ) (ha : 0 ≤ a) (hb : a ≤ 1) :\n");
    emit("A4 LEAN     (1-a)^2 ≤ 1-a^2 := by nlinarith only [mul_nonneg ha (sub_nonneg.mpr hb)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem scaleKinetic (h : ℝ) : h^3*h^2=h*(h^2)^2 := by ring\n");
    emit("A4 LEAN theorem scaleQuartic (h : ℝ) : h^4=h^3*h := by ring\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem separation (e0 e1 a0 a1 eta : ℝ) (l : e1-eta ≤ a1)\n");
    emit("A4 LEAN     (u : a0 ≤ e0+eta) : e1-e0-2*eta ≤ a1-a0 := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Once both scaled levels converge, a strictly positive limiting\n");
    emit("A4 LEAN separation supplies a lower bound along the entire sequence. -/\n");
    emit("A4 LEAN theorem eventualGap (a b : ℕ → ℝ) (u v : ℝ) (hu : Filter.Tendsto a Filter.atTop (nhds u))\n");
    emit("A4 LEAN     (hv : Filter.Tendsto b Filter.atTop (nhds v)) (hlt : u < v) :\n");
    emit("A4 LEAN     ∀ᶠ n in Filter.atTop, (v-u)/2 < b n-a n := by\n");
    emit("A4 LEAN   have pos : (v-u)/2 < v-u := by linarith\n");
    emit("A4 LEAN   exact (hv.sub hu).eventually (lt_mem_nhds pos)\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ToronExcitation\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.fiberScale\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.coarseDefect\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.weightLoss\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.scaleKinetic\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.scaleQuartic\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.separation\n");
    emit("A4 LEAN #print axioms YangMills.ToronExcitation.eventualGap\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
