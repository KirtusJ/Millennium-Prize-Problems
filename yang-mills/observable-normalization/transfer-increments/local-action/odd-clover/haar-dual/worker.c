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
#if ROLE != 2
/* One coordinate step fits in each of the four packed base-8 digits.
   The root digits are 3, leaving room for all incident plaquettes. */
static int stride(int axis) { return 1<<(3*axis); }
static int root_vertex(void) { return 3*(1+8+64+512); }
static void square_edges(int *edges, int i, int j, int s, int t) {
    int p=root_vertex(), dirs[4]={i,j,i,j}, signs[4]={s,t,-s,-t};
    for (int k=0;k<4;++k) {
        int dir=dirs[k], step=stride(dir)*signs[k];
        edges[k]=4*(p+(step<0?step:0))+dir;
        p+=step;
    }
}
static void pair_edges(int *edges, int index) {
    int axes[3][4]={{0,1,2,3},{0,2,1,3},{0,3,1,2}};
    const int *pair=axes[index/16];
    for (int t=0;t<2;++t) {
        int i=pair[2*t],j=pair[2*t+1];
        square_edges(edges+4*t,i,j,1-2*((index>>i)&1),1-2*((index>>j)&1));
    }
}
#endif
static int verify_count(void) {
#if ROLE == 0
    for (int k=0;k<48;++k) {
        int edges[8], ends[16], high=0;
        pair_edges(edges,k);
        for(int n=0;n<8;++n) {
            ends[2*n]=edges[n]/4;
            ends[2*n+1]=ends[2*n]+stride(edges[n]%4);
            for (int j=0;j<n;++j) if(edges[n]==edges[j]) return 0;
        }
        for(int m=0;m<16;++m) {
            int occ=0;
            for(int n=0;n<16;++n) occ+=ends[m]==ends[n];
            if (occ==4 && ends[m]==root_vertex()) ++high;
            else if (occ!=2) return 0;
        }
        if(high!=4) return 0;
        for(int j=0;j<k;++j) {
            int other[8],same=0; pair_edges(other,j);
            for(int m=0;m<8;++m) for(int n=0;n<8;++n) same+=edges[m]==other[n];
            if(same==8) return 0;
        }
    }
#elif ROLE == 1
    for (int k=0;k<48;++k) {
        int edges[8],seen[48],nseen=0;
        pair_edges(edges,k);
        for (int n=0;n<8;++n) {
            int i=edges[n]%4, x=edges[n]/4;
            for(int j=0;j<4;++j) if(j!=i) for(int off=0;off<=1;++off) {
                int face=16*(x-off*stride(j))+(1<<i)+(1<<j);
                int duplicate=0;
                for(int h=0;h<nseen;++h) duplicate|=seen[h]==face;
                if(!duplicate) seen[nseen++]=face;
            }
        }
        if(nseen!=38) return 0;
    }
#else
    /* An exterior-dependent nonuniform conditional law on four atoms.
       The product character has unit uniform overlap with itself
       and zero overlap with the lower-coordinate characters. */
    int weights[4]={1,2,3,6}, overlap=0, constant=0, first=0, second=0;
    for(int i=0;i<4;++i) {
        int x=(i&1)?1:-1, y=(i&2)?1:-1, h=x*y;
        int dual6=18*h/weights[i];
        overlap+=weights[i]*h*dual6; constant+=weights[i]*dual6;
        first+=weights[i]*x*dual6; second+=weights[i]*y*dual6;
    }
    if(overlap!=72 || constant || first || second) return 0;
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN import Mathlib.Tactic.NormNum\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.HaarDual\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The common site coefficient from three colors and 48 oriented pairs. -/\n");
    emit("A4 LEAN theorem haarContact : (48:ℝ) * ((1/16)^2 * (3*(1/4)^2)) = 9/256 := by norm_num\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A positive conditional density can be canceled in the dual\n");
    emit("A4 LEAN pairing, for every value of the conditioned exterior field. -/\n");
    emit("A4 LEAN theorem cancelWeight (f g ρ : ℝ) (h : 0 < ρ) :\n");
    emit("A4 LEAN     (f*(g/ρ))*ρ = f*g := by\n");
    emit("A4 LEAN   rw [mul_assoc, div_mul_cancel₀ _ (ne_of_gt h)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Pairing against a covariance kernel supported on the diagonal. -/\n");
    emit("A4 LEAN theorem diagonalPair {ι : Type*} [DecidableEq ι] (s : Finset ι) (f : ι → ℝ) (v : ℝ) :\n");
    emit("A4 LEAN     (∑ i ∈ s, ∑ j ∈ s, f i * (if i=j then v else 0) * f j)\n");
    emit("A4 LEAN       = v * ∑ i ∈ s, (f i)^2 := by\n");
    emit("A4 LEAN   classical\n");
    emit("A4 LEAN   rw [mul_sum]\n");
    emit("A4 LEAN   apply sum_congr rfl\n");
    emit("A4 LEAN   intro i hi\n");
    emit("A4 LEAN   rw [sum_eq_single i]\n");
    emit("A4 LEAN   · simp; ring\n");
    emit("A4 LEAN   · intro j _ hji\n");
    emit("A4 LEAN     simp [Ne.symm hji]\n");
    emit("A4 LEAN   · simp [hi]\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- Symmetric finite-range cross terms are bounded by the squared\n");
    emit("A4 LEAN coefficient budget of their two endpoints. -/\n");
    emit("A4 LEAN theorem edgePair (x y : ℝ) : 2 * |x*y| ≤ x^2 + y^2 := by\n");
    emit("A4 LEAN   rw [abs_mul]\n");
    emit("A4 LEAN   nlinarith [sq_nonneg (|x|-|y|), sq_abs x, sq_abs y]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The Gram bound on the local dual and its exact mixed overlap\n");
    emit("A4 LEAN give a variance floor for every real smearing. -/\n");
    emit("A4 LEAN theorem dualFloor (v n gram variance upper : ℝ)\n");
    emit("A4 LEAN     (hn : 0 < n) (hu : 0 < upper) (hv : 0 ≤ variance)\n");
    emit("A4 LEAN     (bound : gram ≤ upper*n) (cs : (v*n)^2 ≤ variance*gram) :\n");
    emit("A4 LEAN     v^2/upper*n ≤ variance := by\n");
    emit("A4 LEAN   have h : (v^2*n)*n ≤ (variance*upper)*n := by\n");
    emit("A4 LEAN     calc\n");
    emit("A4 LEAN       _ = (v*n)^2 := by ring\n");
    emit("A4 LEAN       _ ≤ variance*gram := cs\n");
    emit("A4 LEAN       _ ≤ variance*(upper*n) := mul_le_mul_of_nonneg_left bound hv\n");
    emit("A4 LEAN       _ = _ := by ring\n");
    emit("A4 LEAN   have h' := (le_of_mul_le_mul_right h hn)\n");
    emit("A4 LEAN   rwa [div_mul_eq_mul_div, div_le_iff₀ hu]\n");
#elif ROLE == 2
    emit("A4 LEAN /-- A first-order error in the dual norm costs at most the same\n");
    emit("A4 LEAN first-order error in the optimal lower variance bound. -/\n");
    emit("A4 LEAN theorem smallCouplingFloor (v e : ℝ) (hv : 0 < v) (he : 0 ≤ e) :\n");
    emit("A4 LEAN     v-e ≤ v^2/(v+e) := by\n");
    emit("A4 LEAN   apply (le_div_iff₀ (add_pos_of_pos_of_nonneg hv he)).2\n");
    emit("A4 LEAN   nlinarith [sq_nonneg e]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The error of a local weighted witness remains controlled after\n");
    emit("A4 LEAN summing over all possible roots, with a constant independent of the support. -/\n");
    emit("A4 LEAN theorem neighborhoodBudget {ι κ : Type*} (roots : Finset ι) (patch : Finset κ)\n");
    emit("A4 LEAN     (a : ι → κ → ℝ) (n : ℝ) (column : ∀ b ∈ patch, ∑ x ∈ roots, (a x b)^2 ≤ n) :\n");
    emit("A4 LEAN     (∑ x ∈ roots, (∑ b ∈ patch, a x b)^2) ≤ (patch.card:ℝ)^2 * n := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ∑ x ∈ roots, (patch.card:ℝ) * ∑ b ∈ patch, (a x b)^2 := by\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro x _\n");
    emit("A4 LEAN       simpa using sum_mul_sq_le_sq_mul_sq patch (fun _ ↦ (1:ℝ)) (a x)\n");
    emit("A4 LEAN     _ = (patch.card:ℝ) * ∑ b ∈ patch, ∑ x ∈ roots, (a x b)^2 := by\n");
    emit("A4 LEAN       rw [← mul_sum, sum_comm]\n");
    emit("A4 LEAN     _ ≤ (patch.card:ℝ) * ∑ _b ∈ patch, n := by\n");
    emit("A4 LEAN       exact mul_le_mul_of_nonneg_left (sum_le_sum column) (Nat.cast_nonneg _)\n");
    emit("A4 LEAN     _ = _ := by simp [nsmul_eq_mul]; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem mixedRemainder (a b : ℝ) : a^2/2-b^2 ≤ (a+b)^2 := by\n");
    emit("A4 LEAN   nlinarith [sq_nonneg (a+2*b)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.HaarDual\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.haarContact\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.cancelWeight\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.diagonalPair\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.edgePair\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.dualFloor\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.smallCouplingFloor\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.neighborhoodBudget\n");
    emit("A4 LEAN #print axioms YangMills.HaarDual.mixedRemainder\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
