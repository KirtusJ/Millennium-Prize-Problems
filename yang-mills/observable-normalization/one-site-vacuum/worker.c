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
    for(int n=8;n<=2048;++n){
        int count=0;
        for(int k=n-1;2*k>=n;k-=2) ++count;
        if(8*count<n)return 0;
    }
#elif ROLE == 1
    for(int m=6;m<=20;++m){
        int first=(m+1)/2;
        if(3*(m-first)<m)return 0;
        for(int pattern=0;pattern<256;++pattern){
            int total=0,late=0;
            for(int j=0;j<m;++j)if((pattern>>(j%8))&1){
                ++total;if(j>=first)++late;
            }
            if(total<late)return 0;
        }
    }
#else
    /* A killed three-state walk, integer transition weights with common
       denominator 6. Sum its first five iterates and test telescoping. */
    int W[3][3]={{1,2,1},{0,4,1},{1,0,5}};
    long v[3]={1,1,1},s[3]={0,0,0},den=1;
    for(int j=0;j<5;++j){
        long w[3]={0};
        for(int i=0;i<3;++i){
            s[i]=6*s[i]+6*v[i];
            for(int k=0;k<3;++k)w[i]+=W[i][k]*v[k];
        }
        for(int i=0;i<3;++i)v[i]=w[i];
        den*=6;
    }
    for(int i=0;i<3;++i){
        long ws=0;for(int k=0;k<3;++k)ws+=W[i][k]*s[k];
        if(6*s[i]-ws!=6*(den-v[i]) || v[i]>=den)return 0;
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
    emit("A4 LEAN import Mathlib.Tactic.Abel\n");
    emit("A4 LEAN import Mathlib.Algebra.BigOperators.Group.Finset.Basic\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.ToronVacuum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem twoStep (lo mid hi x : ℝ) (rec : lo-hi=x*mid)\n");
    emit("A4 LEAN     (h : hi ≤ mid) (hx : 0 ≤ x) : (1+x)*hi ≤ lo := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg hx (sub_nonneg.mpr h), rec]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem fundamental (q z b : ℝ) (h : z ≤ q) (hb : 0 < b)\n");
    emit("A4 LEAN     (rec : b*(1-z)=4*q) (hq : q ≤ 1) : b*(1-q) ≤ 4 := by\n");
    emit("A4 LEAN   nlinarith only [rec, mul_nonneg hb.le (sub_nonneg.mpr h), hq]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem productScale (m b d : ℝ) (h : b*d^2=m) :\n");
    emit("A4 LEAN     m*b^2*d^4=m^3 := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     m*b^2*d^4=m*(b*d^2)^2 := by ring\n");
    emit("A4 LEAN     _=m^3 := by rw [h]; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem occupation (survival cost fraction : ℝ) (h : survival ≤ 1-cost*fraction)\n");
    emit("A4 LEAN     (hc : 0 ≤ cost) (hf : 1/6 ≤ fraction) : survival ≤ 1-cost/6 := by\n");
    emit("A4 LEAN   nlinarith only [h, mul_nonneg hc (sub_nonneg.mpr hf)]\n");
#elif ROLE == 2
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem superSolution (phi Kphi V e m : ℝ) (hm : 0 < m)\n");
    emit("A4 LEAN     (bound : phi ≤ m) (he : 0 ≤ e) (hV : 0 ≤ V)\n");
    emit("A4 LEAN     (tel : e*(1+V) ≤ (1+V)*phi-Kphi) :\n");
    emit("A4 LEAN     e*phi ≤ m*((1+V)*phi-Kphi) := by\n");
    emit("A4 LEAN   nlinarith only [mul_nonneg he (sub_nonneg.mpr bound),\n");
    emit("A4 LEAN     mul_nonneg hm.le (sub_nonneg.mpr tel), mul_nonneg (mul_nonneg hm.le he) hV]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Summing survival iterates produces a supersolution when a whole\n");
    emit("A4 LEAN block loses mass. No independence between times is used. -/\n");
    emit("A4 LEAN theorem finiteSurvival {G : Type*} [AddCommGroup G] (B : G →+ G)\n");
    emit("A4 LEAN     (u : ℕ → G) (step : ∀ i, B (u i) = u (i+1)) (m : ℕ) :\n");
    emit("A4 LEAN     (∑ i ∈ Finset.range m, u i) - B (∑ i ∈ Finset.range m, u i) =\n");
    emit("A4 LEAN     u 0 - u m := by\n");
    emit("A4 LEAN   induction m with\n");
    emit("A4 LEAN   | zero => simp\n");
    emit("A4 LEAN   | succ m ih =>\n");
    emit("A4 LEAN     rw [Finset.sum_range_succ, map_add, step]\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       _ = ((∑ i ∈ Finset.range m, u i) - B (∑ i ∈ Finset.range m, u i)) +\n");
    emit("A4 LEAN           u m - u (m+1) := by abel\n");
    emit("A4 LEAN       _ = _ := by rw [ih]; abel\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.ToronVacuum\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.twoStep\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.fundamental\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.productScale\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.occupation\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.superSolution\n");
    emit("A4 LEAN #print axioms YangMills.ToronVacuum.finiteSurvival\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
