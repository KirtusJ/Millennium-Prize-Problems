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
#if ROLE == 0
/* Unit quaternions encoded as signed 1, i, j, k. */
static int qmul(int a,int b) {
    int i=__builtin_abs(a)-1, j=__builtin_abs(b)-1, s=a*b<0?-1:1;
    if (!i || !j) return s*(1+i+j);
    if (i==j) return -s;
    return s*(7-i-j)*(i%3+1==j?1:-1);
}
static int inv(int a) {return __builtin_abs(a)==1?a:-a;}
#endif
static int verify_count(void) {
#if ROLE == 0
    int wrong=0;
    for(int g=-4;g<=4;++g) if(g) for(int u=-4;u<=4;++u) if(u) {
        int child=qmul(g,u);
        if(qmul(qmul(g,u),inv(child))!=1) return 0;
        if(qmul(qmul(g,u),inv(qmul(u,g)))!=1) ++wrong;
    }
    /* Center multiplication negates the real coordinate, whose squared
       sum over the eight unit quaternions is two. */
    int real_square_sum=0;
    for(int u=-4;u<=4;++u) if(u) {
        int real=(__builtin_abs(u)==1?u:0), v=qmul(-1,u);
        if((__builtin_abs(v)==1?v:0)!=-real) return 0;
        real_square_sum+=real*real;
    }
    if(real_square_sum!=2) return 0;
    if(wrong!=24 || qmul(qmul(2,3),inv(qmul(3,2)))!=-1) return 0;
#elif ROLE == 1
    /* Discrete ramp Green column scaled by L solves T y = L e_1. */
    for(int L=2;L<=96;++L) {
        int norm=0;
        for(int t=1;t<L;++t) {
            int y=L-t, prev=(t==1?0:y+1), next=y-1;
            if(2*y-prev-next!=(t==1?L:0)) return 0;
            norm+=y*y;
        }
        if(6*norm!=(L-1)*L*(2*L-1)) return 0;
    }
#else
    /* Fix the two transverse coordinates. The translated strips from
       all bottom columns use the rectangle [0,x) times [0,L). */
    for(int L=2;L<=24;++L) {
        int faces[24][24]={0},boundary[24]={0};
        for(int x=1;x<L;++x) {
            int length=L;
            for(int j=0;j<x;++j) {
                length+=2;
                for(int t=0;t<L;++t) {++faces[j][t];++length;}
            }
            for(int t=0;t<L;++t) ++boundary[t];
            if(length>L*L+3*L) return 0;
        }
        for(int t=0;t<L;++t) {
            if(boundary[t]!=L-1) return 0;
            for(int j=0;j<L;++j) if(faces[j][t]!=L-1-j) return 0;
        }
    }
#endif
    return 1;
}
__attribute__((used,noreturn)) static void run(void) {
    if(!verify_count()){sys(60,2,0,0);__builtin_unreachable();}
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.Analysis.InnerProductSpace.Basic\n");
    emit("A4 LEAN import Mathlib.Data.Real.Basic\n");
    emit("A4 LEAN import Mathlib.Algebra.Order.BigOperators.Ring.Finset\n");
    emit("A4 LEAN import Mathlib.Tactic.FieldSimp\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN open Finset\n");
    emit("A4 LEAN namespace YangMills.DirichletBox\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The orientation convention in the paper fixes each forward tree edge. -/\n");
    emit("A4 LEAN theorem gaugeForward {G : Type*} [Group G] (parent edge : G) :\n");
    emit("A4 LEAN     parent * edge * (parent * edge)⁻¹ = 1 := mul_inv_cancel _\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Cauchy-Schwarz with path length and edge congestion bounded separately.\n");
    emit("A4 LEAN No commutativity of the original parallel transports is needed here. -/\n");
    emit("A4 LEAN theorem congestion {α ι : Type*} [DecidableEq ι] (roots : Finset α)\n");
    emit("A4 LEAN     (edges : Finset ι) (path : α → Finset ι) (a : ι → ℝ) (len mult : ℝ)\n");
    emit("A4 LEAN     (hlen : ∀ x ∈ roots, ((path x).card:ℝ) ≤ len)\n");
    emit("A4 LEAN     (hl : 0 ≤ len)\n");
    emit("A4 LEAN     (cover : ∀ x ∈ roots, path x ⊆ edges)\n");
    emit("A4 LEAN     (hcount : ∀ i ∈ edges, (((roots.filter (fun x ↦ i ∈ path x)).card):ℝ) ≤ mult) :\n");
    emit("A4 LEAN     (∑ x ∈ roots, (∑ i ∈ path x, a i)^2) ≤ len*mult*∑ i ∈ edges, (a i)^2 := by\n");
    emit("A4 LEAN   classical\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ∑ x ∈ roots, len * ∑ i ∈ path x, (a i)^2 := by\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro x hx\n");
    emit("A4 LEAN       have h : (∑ i ∈ path x, a i)^2 ≤ ((path x).card:ℝ)*∑ i ∈ path x, (a i)^2 := by\n");
    emit("A4 LEAN         simpa using sum_mul_sq_le_sq_mul_sq (path x) (fun _ ↦ (1:ℝ)) a\n");
    emit("A4 LEAN       exact h.trans (mul_le_mul_of_nonneg_right (hlen x hx) (sum_nonneg fun i _ ↦ sq_nonneg (a i)))\n");
    emit("A4 LEAN     _ = len * ∑ i ∈ edges, ∑ x ∈ roots, if i ∈ path x then (a i)^2 else 0 := by\n");
    emit("A4 LEAN       rw [← mul_sum, sum_comm]\n");
    emit("A4 LEAN       congr 1\n");
    emit("A4 LEAN       apply sum_congr rfl\n");
    emit("A4 LEAN       intro x hx\n");
    emit("A4 LEAN       rw [← sum_filter]\n");
    emit("A4 LEAN       congr 1\n");
    emit("A4 LEAN       ext i\n");
    emit("A4 LEAN       simp only [mem_filter]\n");
    emit("A4 LEAN       exact ⟨fun h ↦ ⟨cover x hx h,h⟩, fun h ↦ h.2⟩\n");
    emit("A4 LEAN     _ ≤ len * ∑ i ∈ edges, mult*(a i)^2 := by\n");
    emit("A4 LEAN       apply mul_le_mul_of_nonneg_left _ hl\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       rw [← sum_filter]\n");
    emit("A4 LEAN       simp only [sum_const, nsmul_eq_mul]\n");
    emit("A4 LEAN       exact mul_le_mul_of_nonneg_right (hcount i hi) (sq_nonneg _)\n");
    emit("A4 LEAN     _ = _ := by rw [← mul_sum, mul_assoc]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A central gauge flip on one time slice forces a transfer zero\n");
    emit("A4 LEAN mode whenever it negates every pairing with a nonzero vector. -/\n");
    emit("A4 LEAN theorem transferKernel {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]\n");
    emit("A4 LEAN     (T : H → H) (v : H) (nz : v ≠ 0) (hT : T 0 = 0)\n");
    emit("A4 LEAN     (flip : ∀ w, (@inner ℝ H _) w (T v) = -((@inner ℝ H _) w (T v))) :\n");
    emit("A4 LEAN     T v = 0 ∧ ¬ Function.Injective T := by\n");
    emit("A4 LEAN   have h : (@inner ℝ H _) (T v) (T v) = 0 := by linarith [flip (T v)]\n");
    emit("A4 LEAN   have hz : T v = 0 := inner_self_eq_zero.mp h\n");
    emit("A4 LEAN   exact ⟨hz, fun inj ↦ nz (inj (hz.trans hT.symm))⟩\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A self-adjoint transfer whose range is physical also kills the\n");
    emit("A4 LEAN orthogonal complement of the physical projection. -/\n");
    emit("A4 LEAN theorem boundaryProjection {M : Type*} [Monoid M] [StarMul M] (P T : M)\n");
    emit("A4 LEAN     (hp : star P = P) (ht : star T = T) (rangeIn : P*T=T) : T*P=T := by\n");
    emit("A4 LEAN   simpa only [star_mul, hp, ht] using congrArg star rangeIn\n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN /-- A Schur root is a zero of the bordered matrix's scalar equation. -/\n");
    emit("A4 LEAN theorem rootIdentity (lam r g : ℝ) (h : lam-r-lam*g=0) :\n");
    emit("A4 LEAN     r = lam*(1-g) := by linarith\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Resolvent control traps the bottom mode between explicit quantities. -/\n");
    emit("A4 LEAN theorem rootBounds (a L r delta K : ℝ) (ha : 0 ≤ a)\n");
    emit("A4 LEAN     (hr : r = a*(1/L-delta)) (hd : 0 ≤ delta) (hu : delta ≤ r*K)\n");
    emit("A4 LEAN     (hk : 0 ≤ K) :\n");
    emit("A4 LEAN     (a/L)/(1+a*K) ≤ r ∧ r ≤ a/L := by\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · apply (div_le_iff₀ (by positivity : 0 < 1+a*K)).2\n");
    emit("A4 LEAN     have eq : a/L = r + a*delta := by rw [hr]; ring\n");
    emit("A4 LEAN     rw [eq]\n");
    emit("A4 LEAN     nlinarith [mul_le_mul_of_nonneg_left hu ha]\n");
    emit("A4 LEAN   · rw [hr]\n");
    emit("A4 LEAN     have eq : a*(1/L-delta)=a/L-a*delta := by ring\n");
    emit("A4 LEAN     rw [eq]\n");
    emit("A4 LEAN     linarith [mul_nonneg ha hd]\n");
#elif ROLE == 2
    emit("A4 LEAN /-- If two unnormalised densities have bounded relative distortion,\n");
    emit("A4 LEAN their normalized integrals inherit the same two factors. -/\n");
    emit("A4 LEAN theorem normalizedDistortion (a b m n u : ℝ) (hm : 0 < m) (hn : 0 < n)\n");
    emit("A4 LEAN     (hu : 0 ≤ u) (hb : 0 ≤ b) (hw : a ≤ u*b) (hz : n ≤ u*m) :\n");
    emit("A4 LEAN     a/m ≤ u^2*(b/n) := by\n");
    emit("A4 LEAN   apply (div_le_iff₀ hm).2\n");
    emit("A4 LEAN   apply (mul_le_mul_iff_of_pos_right hn).mp\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     a*n ≤ (u*b)*n := mul_le_mul_of_nonneg_right hw hn.le\n");
    emit("A4 LEAN     _ ≤ (u*b)*(u*m) := mul_le_mul_of_nonneg_left hz (mul_nonneg hu hb)\n");
    emit("A4 LEAN     _ = (u^2*(b/n)*m)*n := by field_simp; ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Cubic error and the threshold for the random and identity shells. -/\n");
    emit("A4 LEAN theorem scaleExponents (L : ℝ) :\n");
    emit("A4 LEAN     (L^5)^3 = L^15 ∧ (L^7)^3 = L^21 ∧ (L^15)^2 = L^30 := by\n");
    emit("A4 LEAN   constructor\n");
    emit("A4 LEAN   · ring\n");
    emit("A4 LEAN   constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- A uniform link bound and summed energy bound control the cubic Taylor cost. -/\n");
    emit("A4 LEAN theorem cubicBudget {ι : Type*} (edges : Finset ι) (a : ι → ℝ) (L E : ℝ)\n");
    emit("A4 LEAN     (hL : 0 ≤ L) (hE : 0 ≤ E)\n");
    emit("A4 LEAN     (point : ∀ i ∈ edges, a i ≤ L*E)\n");
    emit("A4 LEAN     (energy : ∑ i ∈ edges, (a i)^2 ≤ 32*L^3*E^2) :\n");
    emit("A4 LEAN     (∑ i ∈ edges, (a i)^3) ≤ 32*L^4*E^3 := by\n");
    emit("A4 LEAN   calc\n");
    emit("A4 LEAN     _ ≤ ∑ i ∈ edges, L*E*(a i)^2 := by\n");
    emit("A4 LEAN       apply sum_le_sum\n");
    emit("A4 LEAN       intro i hi\n");
    emit("A4 LEAN       calc\n");
    emit("A4 LEAN         _ = a i*(a i)^2 := by ring\n");
    emit("A4 LEAN         _ ≤ _ := mul_le_mul_of_nonneg_right (point i hi) (sq_nonneg _)\n");
    emit("A4 LEAN     _ ≤ (L*E)*(32*L^3*E^2) := by\n");
    emit("A4 LEAN       rw [← mul_sum]\n");
    emit("A4 LEAN       exact mul_le_mul_of_nonneg_left energy (mul_nonneg hL hE)\n");
    emit("A4 LEAN     _ = _ := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.DirichletBox\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.gaugeForward\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.congestion\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.rootIdentity\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.rootBounds\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.normalizedDistortion\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.scaleExponents\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.transferKernel\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.cubicBudget\n");
    emit("A4 LEAN #print axioms YangMills.DirichletBox.boundaryProjection\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
