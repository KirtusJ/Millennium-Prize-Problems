/* Native PCP commission on finite filters and spatial momentum sectors. */
#include <stddef.h>

static long syscall3(long number, long a, long b, long c) {
    long result;
    __asm__ volatile ("syscall" : "=a"(result)
                      : "a"(number), "D"(a), "S"(b), "d"(c)
                      : "rcx", "r11", "memory");
    return result;
}

_Noreturn static void stop(int status) {
    syscall3(60, status, 0, 0);
    __builtin_unreachable();
}

static void emit(const char *text) {
    size_t size = 0;
    while (text[size]) ++size;
    while (size) {
        long written = syscall3(1, 1, (long)text, size);
        if (written <= 0 || (size_t)written > size) stop(3);
        text += written;
        size -= written;
    }
}

static void number(unsigned n) {
    char text[12];
    unsigned pos = sizeof text - 1;
    text[pos] = 0;
    do { text[--pos] = '0' + n % 10; n /= 10; } while (n);
    emit(text + pos);
}

static void request(unsigned depth, unsigned a, unsigned b) {
    emit("NEXT "); number(depth); emit(" "); number(a); emit(" "); number(b); emit("\n");
}

static void parent(void) {
    int filter[3] = {-1,1,2};
    int middle = 0;
    for (unsigned i=0;i<3;++i) middle += filter[i]*filter[2-i];
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Algebra.Order.BigOperators.Group.Finset\n"
         "import Mathlib.Data.Finset.Max\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.Ring\n"
         "namespace YangMills.FlowMomentum\n"
         "\n"
         "/-- A nonnegative bounded sequence cannot have a doubling continuation from every index. -/\n"
         "theorem boundedDoubling (v : ℕ → ℝ) (K : ℝ) (h0 : ∀ n, 0 ≤ v n)\n"
         "    (hb : ∀ n, v n ≤ K) (hg : ∀ n, ∃ j, 2*v n ≤ v j) (n : ℕ) : v n = 0 := by\n"
         "  by_contra hn\n"
         "  have hp : 0 < v n := lt_of_le_of_ne (h0 n) (Ne.symm hn)\n"
         "  have hstep : ∀ m : ℕ, ∃ j, ((m:ℝ)+1)*v n ≤ v j := by\n"
         "    intro m\n"
         "    induction m with\n"
         "    | zero => exact ⟨n, by simp⟩\n"
         "    | succ m ih =>\n"
         "      obtain ⟨j,hj⟩ := ih\n"
         "      obtain ⟨k,hk⟩ := hg j\n"
         "      refine ⟨k,?_⟩\n"
         "      push_cast\n"
         "      nlinarith [mul_nonneg (Nat.cast_nonneg (α:=ℝ) m) hp.le]\n"
         "  obtain ⟨m,hm⟩ := exists_nat_gt (K/v n)\n"
         "  obtain ⟨j,hj⟩ := hstep m\n"
         "  nlinarith [(div_lt_iff₀ hp).mp hm,hb j]\n"
         "\n"
         "/-- After multiplying by a geometric weight, a finite recurrence gives a doubling step. -/\n"
         "theorem supergeometricZero (b : ℕ → ℝ) (A : ℝ) (hA : 0 ≤ A)\n"
         "    (hs : ∀ B : ℝ, 1 ≤ B → ∃ K : ℝ, ∀ n : ℕ, B^n*|b n| ≤ K)\n"
         "    (hg : ∀ n : ℕ, ∃ j : ℕ, 0 < j ∧ |b n| ≤ A*|b (n+j)|)\n"
         "    (n : ℕ) : b n = 0 := by\n"
         "  let B := 2*(A+1)\n"
         "  have hB : 1 ≤ B := by dsimp [B]; linarith\n"
         "  obtain ⟨K,hK⟩ := hs B hB\n"
         "  have grow : ∀ m : ℕ, ∃ k : ℕ, 2*(B^m*|b m|) ≤ B^k*|b k| := by\n"
         "    intro m\n"
         "    obtain ⟨j,hj,hh⟩ := hg m\n"
         "    have hj' : B ≤ B^j := by\n"
         "      simpa using pow_le_pow_right₀ hB (show 1 ≤ j from hj)\n"
         "    have hcomp : 2*A ≤ B^j := le_trans (by dsimp [B]; linarith) hj'\n"
         "    have hx : 2*|b m| ≤ B^j*|b (m+j)| := by\n"
         "      nlinarith [mul_le_mul_of_nonneg_right hcomp (abs_nonneg (b (m+j)))]\n"
         "    refine ⟨m+j,?_⟩\n"
         "    rw [pow_add]\n"
         "    nlinarith [mul_le_mul_of_nonneg_left hx (pow_nonneg (by linarith : 0 ≤ B) m)]\n"
         "  have h := boundedDoubling (fun m => B^m*|b m|) K\n"
         "    (fun m => mul_nonneg (pow_nonneg (by linarith : 0 ≤ B) m) (abs_nonneg _)) hK grow n\n"
         "  have hn : 0 < B^n := pow_pos (by linarith) n\n"
         "  exact abs_eq_zero.mp ((mul_eq_zero.mp h).resolve_left hn.ne')\n"
         "\n"
         "theorem recurrenceStep (b a : ℕ → ℝ) (c : ℝ) (hc : c ≠ 0) (S : Finset ℕ) (hS : S.Nonempty)\n"
         "    (n : ℕ) (eqn : c*b n + ∑ j ∈ S, a j*b (n+j) = 0) :\n"
         "    ∃ j ∈ S, |b n| ≤ ((∑ i ∈ S, |a i|)/|c|)*|b (n+j)| := by\n"
         "  obtain ⟨j,hj,hmax⟩ := S.exists_max_image (fun i => |b (n+i)|) hS\n"
         "  refine ⟨j,hj,?_⟩\n"
         "  have h : |b n| * |c| ≤ (∑ i ∈ S, |a i|)*|b (n+j)| := by\n"
         "    calc\n"
         "      _ = |-(∑ i ∈ S, a i*b (n+i))| := by\n"
         "        rw [← abs_mul, mul_comm (b n) c, show c*b n = -(∑ i ∈ S, a i*b (n+i)) by linarith]\n"
         "      _ ≤ ∑ i ∈ S, |a i*b (n+i)| := by rw [abs_neg]; exact Finset.abs_sum_le_sum_abs _ _\n"
         "      _ ≤ _ := by\n"
         "        rw [Finset.sum_mul]\n"
         "        apply Finset.sum_le_sum\n"
         "        intro i hi\n"
         "        rw [abs_mul]\n"
         "        exact mul_le_mul_of_nonneg_left (hmax i hi) (abs_nonneg _)\n"
         "  rw [div_mul_eq_mul_div]\n"
         "  exact (le_div_iff₀ (abs_pos.mpr hc)).2 h\n"
         "\n"
         "theorem recurrentSupergeometric (b a : ℕ → ℝ) (c : ℝ) (hc : c ≠ 0)\n"
         "    (S : Finset ℕ) (hS : S.Nonempty) (hpos : ∀ j ∈ S, 0 < j)\n"
         "    (hs : ∀ B : ℝ, 1 ≤ B → ∃ K : ℝ, ∀ n : ℕ, B^n*|b n| ≤ K)\n"
         "    (heq : ∀ n, c*b n+∑ j ∈ S, a j*b (n+j)=0) (n : ℕ) : b n=0 := by\n"
         "  apply supergeometricZero b ((∑ j ∈ S, |a j|)/|c|) (by positivity) hs _ n\n"
         "  intro m\n"
         "  obtain ⟨j,hj,hh⟩ := recurrenceStep b a c hc S hS m (heq m)\n"
         "  exact ⟨j,hpos j hj,hh⟩\n"
         "\n"
         "theorem filterFixture (x : ℝ) : (-1+x+2*x^2)^2=1-2*x-");
    number((unsigned)(-middle));
    emit("*x^2+4*x^3+4*x^4 := by ring\n"
         "LEAN-END\n");

    request(1,4,2);
}
static void child(unsigned dim,unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    unsigned den = 120*pair*pair;
    emit("LEAN-BEGIN\n"
         "theorem phaseFactor (E k z : ℝ) :\n"
         "    (E^2-z^2)^2+(2*k^2-E^2-z^2)^2 =\n"
         "    2*((E^2-k^2)^2+(k^2-z^2)^2) := by ring\n"
         "\n"
         "theorem polarizationWeight (c : ℝ) : 0 < 1+c^2 := by positivity\n"
         "\n"
         "theorem thresholdAngle {k z : ℝ} (_hk : 0<k) (hz : |z|<k) : 0<(k^2-z^2)^2 := by\n"
         "  have h := abs_lt.mp hz\n"
         "  have hp := mul_pos (by linarith : 0<k-z) (by linarith : 0<k+z)\n"
         "  exact sq_pos_of_pos (by nlinarith)\n"
         "\n"
         "theorem spatialHeatFactor (s E z : ℝ) :\n"
         "    Real.exp (-2*s*(((E+z)/2)^2+((E-z)/2)^2)) =\n"
         "      Real.exp (-s*E^2)*Real.exp (-s*z^2) := by\n"
         "  rw [← Real.exp_add]\n"
         "  congr 1\n"
         "  ring\n"
         "\n"
         "theorem freeSplit (E k : ℝ) :\n"
         "    ((E^2-k^2)^2/64+k^4/120)/4 =\n"
         "    (E^4-2*k^2*E^2+(23/15)*k^4)/256 := by ring\n"
         "\n"
         "theorem thresholdCoefficient : ((1:ℚ)/120)/4=1/");
    number(den);
    emit(" := by norm_num\n"
         "\n"
         "theorem restDensity (E : ℝ) : ((E^2-(0:ℝ)^2)^2/64+(0:ℝ)^4/120)/4=E^4/256 := by ring\n"
         "LEAN-END\n");

    request(2,dim,pair);
}
static void grandchild(unsigned dim,unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    unsigned deficit = pair*832895-918686-737430;
    emit("LEAN-BEGIN\n"
         "theorem propagatorDeficit (a b x y : ℝ) :\n"
         "    a*b-x*y = (a-x)*b+x*(b-y) := by ring\n"
         "\n"
         "theorem gaussianTail {a s t : ℝ} (ha : 0<a) (h : a≤2*s) :\n"
         "    Real.exp (-(t^2)/(4*a)) ≤ Real.exp (-(t^2)/(16*s))*Real.exp (-(t^2)/(8*a)) := by\n"
         "  have hs : 0<s := by linarith\n"
         "  rw [← Real.exp_add,Real.exp_le_exp]\n"
         "  have H : t^2/(16*s) ≤ t^2/(8*a) := div_le_div_of_nonneg_left (sq_nonneg _) (by positivity) (by linarith)\n"
         "  rw [show -(t^2)/(4*a) = -(t^2)/(8*a) + -(t^2)/(8*a) by ring]\n"
         "  simp only [neg_div]\n"
         "  linarith only [H]\n"
         "\n"
         "theorem temporalFilter (a b x : ℝ) : a^2 + 2*a*b*x + b^2*x^2=(a+b*x)^2 := by ring\n"
         "\n"
         "theorem coneDensityPositive {s E k z : ℝ} (hk : 0<k) (hz : |z|<k) :\n"
         "    0<Real.exp (-s*(E^2+z^2))*((E^2-k^2)^2+(k^2-z^2)^2) :=\n"
         "  mul_pos (Real.exp_pos _) (add_pos_of_nonneg_of_pos (sq_nonneg _) (thresholdAngle hk hz))\n"
         "\n"
         "theorem torusBound {a b c : ℝ} (ha : a≤918686/1000000)\n"
         "    (hb : 832895/1000000≤b) (hc : c≤737430/1000000) :\n"
         "    a-2*b+c ≤ -");
    number(deficit);
    emit("/1000000 := by linarith\n"
         "\n"
         "end YangMills.FlowMomentum\n"
         "open YangMills.FlowMomentum\n"
         "#print axioms boundedDoubling\n"
         "#print axioms supergeometricZero\n"
         "#print axioms recurrenceStep\n"
         "#print axioms recurrentSupergeometric\n"
         "#print axioms phaseFactor\n"
         "#print axioms polarizationWeight\n"
         "#print axioms thresholdAngle\n"
         "#print axioms spatialHeatFactor\n"
         "#print axioms freeSplit\n"
         "#print axioms thresholdCoefficient\n"
         "#print axioms restDensity\n"
         "#print axioms propagatorDeficit\n"
         "#print axioms gaussianTail\n"
         "#print axioms temporalFilter\n"
         "#print axioms coneDensityPositive\n"
         "#print axioms filterFixture\n"
         "#print axioms torusBound\n"
         "LEAN-END\n");
}

__attribute__((used,noreturn)) static void run(void) {
    static unsigned char input[4];
    long fd = syscall3(2, (long)"task.bin", 0, 0);
    if (fd < 0 || syscall3(0, fd, (long)input, sizeof input) != 3 ||
        syscall3(0, fd, (long)(input+3), 1) != 0 || syscall3(3, fd, 0, 0) != 0) stop(2);
    if (!input[0] && !input[1] && !input[2]) parent();
    else if (input[0] == 1) child(input[1],input[2]);
    else if (input[0] == 2) grandchild(input[1],input[2]);
    else stop(2);
    stop(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
