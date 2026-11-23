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
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    emit("A4 CHILD spectrum\n");
    emit("A4 LEAN import Mathlib.MeasureTheory.Integral.Bochner.Set\n");
    emit("A4 LEAN import Mathlib.Tactic.Linarith\n");
    emit("A4 LEAN import Mathlib.Tactic.Ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN namespace YangMills.PlaquetteResponse\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- On one excited face each of its four links contributes equally. -/\n");
    emit("A4 LEAN theorem onePlaquette (a b c d face : ℝ) :\n");
    emit("A4 LEAN     (3/4*(a+b+c+d))/3-face = (a+b+c+d)/4-face := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Six outer fundamental links and a shared link of Casimir j.\n");
    emit("A4 LEAN The two input faces each contribute its balanced mean weight. -/\n");
    emit("A4 LEAN theorem sharedCoefficient {j outer common av : ℝ} (positive : 0 < 9/2+j)\n");
    emit("A4 LEAN     (balance : 8*av=outer+2*common) :\n");
    emit("A4 LEAN     2*((3/4*outer+j*common)/(9/2+j)-av) =\n");
    emit("A4 LEAN       2*(j-3/2)*(common-av)/(9/2+j) := by\n");
    emit("A4 LEAN   generalize hd : (9/2:ℝ)+j = den at positive ⊢\n");
    emit("A4 LEAN   field_simp [positive.ne']\n");
    emit("A4 LEAN   rw [← hd, show outer=8*av-2*common by linarith]\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem channelFactors (d : ℝ) :\n");
    emit("A4 LEAN     2*((0:ℝ)-3/2)*d/(9/2+0) = -2*d/3 ∧\n");
    emit("A4 LEAN     2*((2:ℝ)-3/2)*d/(9/2+2) = 2*d/13 := by constructor <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Haar projection on the common link: the retained trace is a quarter\n");
    emit("A4 LEAN of the normalized outer trace, with squared norm one quarter. -/\n");
    emit("A4 LEAN theorem haarWeights :\n");
    emit("A4 LEAN     (1/4:ℝ)^2*(1/4)=1/64 ∧ (1/4:ℝ)^2-1/64=3/64 := by norm_num\n");
    emit("A4 LEAN \n");
#elif ROLE == 1
    emit("A4 CHILD limit\n");
    emit("A4 LEAN theorem channelWeights {h : ℝ} (hh : 0 < h) (d : ℝ) :\n");
    emit("A4 LEAN     (-2*d/(3*h))^2*(1/64)=d^2/(144*h^2) ∧\n");
    emit("A4 LEAN     (2*d/(13*h))^2*(3/64)=3*d^2/(2704*h^2) := by\n");
    emit("A4 LEAN   constructor <;> field_simp <;> ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem firstMoment {k : ℝ} (hk : 0 < k) (S : ℝ) :\n");
    emit("A4 LEAN     (9*k/2)*S/(144*(3*k)^2)+(13*k/2)*(3*S)/(2704*(3*k)^2)=S/(234*k) := by\n");
    emit("A4 LEAN   field_simp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem zeroPairSum {ι : Type*} (pairs : Finset ι) (d : ι → ℝ)\n");
    emit("A4 LEAN     (h : (∑ i ∈ pairs, (d i)^2) = 0) :\n");
    emit("A4 LEAN     ∀ i ∈ pairs, d i = 0 := by\n");
    emit("A4 LEAN   intro i hi\n");
    emit("A4 LEAN   have hp := Finset.single_le_sum (f := fun j => (d j)^2)\n");
    emit("A4 LEAN     (fun j _ => sq_nonneg (d j)) hi\n");
    emit("A4 LEAN   rw [h] at hp\n");
    emit("A4 LEAN   exact sq_eq_zero_iff.mp (le_antisymm hp (sq_nonneg _))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Three distinct incident faces are sufficient to identify their common weight. -/\n");
    emit("A4 LEAN theorem recoverIncident {w a b c : ℝ} (h₁ : 2*w=a+b)\n");
    emit("A4 LEAN     (h₂ : 2*w=a+c) (h₃ : 2*w=b+c) : a=w ∧ b=w ∧ c=w := by\n");
    emit("A4 LEAN   exact ⟨by linarith, by linarith, by linarith⟩\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem constantOnConnectedLinks {ι : Type*} (edge : ι → ι → Prop) (w : ι → ℝ)\n");
    emit("A4 LEAN     (connected : ∀ i j, Relation.ReflTransGen edge i j)\n");
    emit("A4 LEAN     (locallyEqual : ∀ i j, edge i j → w i = w j) (i j : ι) : w i = w j := by\n");
    emit("A4 LEAN   induction connected i j with\n");
    emit("A4 LEAN   | refl => rfl\n");
    emit("A4 LEAN   | tail _ step prev => exact prev.trans (locallyEqual _ _ step)\n");
    emit("A4 LEAN \n");
#elif ROLE == 2
    emit("A4 LEAN /-- Contributions at a lattice edge from four perpendicular pairs of faces\n");
    emit("A4 LEAN for an affine spatial test, using mesh spacing b. -/\n");
    emit("A4 LEAN theorem affineEdge (b g h : ℝ) :\n");
    emit("A4 LEAN     (b*(g+h)/4)^2+(b*(g-h)/4)^2+(b*(-g+h)/4)^2+(b*(-g-h)/4)^2 =\n");
    emit("A4 LEAN       b^2*(g^2+h^2)/4 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem affineCell (b x y z : ℝ) :\n");
    emit("A4 LEAN     b^2*(y^2+z^2)/4+b^2*(x^2+z^2)/4+b^2*(x^2+y^2)/4 =\n");
    emit("A4 LEAN       b^2*(x^2+y^2+z^2)/2 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- The six unordered pairs among four incident faces give the incidence\n");
    emit("A4 LEAN energy and the square of its residual, with exact coefficients. -/\n");
    emit("A4 LEAN theorem incidentSquare (a b c d : ℝ) :\n");
    emit("A4 LEAN     ((a+b)/2)^2+((a+c)/2)^2+((a+d)/2)^2+\n");
    emit("A4 LEAN     ((b+c)/2)^2+((b+d)/2)^2+((c+d)/2)^2 =\n");
    emit("A4 LEAN     (a^2+b^2+c^2+d^2)/2+(a+b+c+d)^2/4 := by ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- An averaged face contributes its deviation about the link mean. -/\n");
    emit("A4 LEAN theorem faceVariance (a b c d : ℝ) :\n");
    emit("A4 LEAN     let m := (a+b+c+d)/4\n");
    emit("A4 LEAN     (a-m)^2+(b-m)^2+(c-m)^2+(d-m)^2 = a^2+b^2+c^2+d^2-4*m^2 := by\n");
    emit("A4 LEAN   dsimp\n");
    emit("A4 LEAN   ring\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN theorem quadraticIncreasing {x y : ℝ} (h₀ : 0 ≤ x) (h : x ≤ y) :\n");
    emit("A4 LEAN     x/2+x^2/4 ≤ y/2+y^2/4 := by\n");
    emit("A4 LEAN   nlinarith [sq_nonneg (y-x), mul_nonneg h₀ (sub_nonneg.mpr h)]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Characteristic polynomial of the symmetric sector on an axial mode. -/\n");
    emit("A4 LEAN theorem axialRoot {s r : ℝ} (hr : r^2=s^2+8) :\n");
    emit("A4 LEAN     let m := 2+(s^2+s*r)/2\n");
    emit("A4 LEAN     (m-2)*(m-(2+s^2))=2*s^2 := by\n");
    emit("A4 LEAN   dsimp\n");
    emit("A4 LEAN   nlinarith only [show s^2*r^2=s^2*(s^2+8) by rw [hr]]\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN /-- Positivity on the two orthogonal output ranges gives a uniform lower\n");
    emit("A4 LEAN bound for a nearby map, after scaling the input columns. -/\n");
    emit("A4 LEAN theorem stableIndependent {V H : Type*} [NormedAddCommGroup V] [NormedAddCommGroup H]\n");
    emit("A4 LEAN     (T T₀ : V → H) {c err : ℝ} (he : err < c)\n");
    emit("A4 LEAN     (lower : ∀ v, c*‖v‖ ≤ ‖T₀ v‖)\n");
    emit("A4 LEAN     (close : ∀ v, ‖T₀ v-T v‖ ≤ err*‖v‖) {v : V} (hv : T v=0) : v=0 := by\n");
    emit("A4 LEAN   have h := close v\n");
    emit("A4 LEAN   rw [hv,sub_zero] at h\n");
    emit("A4 LEAN   have hb := (lower v).trans h\n");
    emit("A4 LEAN   by_contra hn\n");
    emit("A4 LEAN   exact (not_lt_of_ge hb) (mul_lt_mul_of_pos_right he (norm_pos_iff.mpr hn))\n");
    emit("A4 LEAN \n");
    emit("A4 LEAN end YangMills.PlaquetteResponse\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.onePlaquette\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.sharedCoefficient\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.channelFactors\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.haarWeights\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.channelWeights\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.firstMoment\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.zeroPairSum\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.recoverIncident\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.constantOnConnectedLinks\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.affineEdge\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.affineCell\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.stableIndependent\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.incidentSquare\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.faceVariance\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.quadraticIncreasing\n");
    emit("A4 LEAN #print axioms YangMills.PlaquetteResponse.axialRoot\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
