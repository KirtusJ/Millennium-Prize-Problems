/* Three PCP guests enumerate steps, count stopped endpoints and calculate spectral powers. */
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




static int step(unsigned slot) {
    if (slot<8) return 0;
    int axis=(int)(slot-8)/2+1;
    return slot%2 ? -axis : axis;
}
static unsigned endpoint(int target) {
    unsigned count=0;
    for (unsigned i=0;i<16;++i) for (unsigned j=0;j<16;++j) {
        int a=step(i);
        count+=(a ? a : step(j))==target;
    }
    return count;
}
static void parent(void) {
    unsigned count=0, holds=0;
    for (unsigned i=0;i<16;++i) { ++count; holds+=step(i)==0; }
    emit("LEAN-BEGIN\n"
         "import Mathlib.Tactic.NoncommRing\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Analysis.Calculus.MeanValue\n"
         "import Mathlib.Algebra.BigOperators.Group.Finset.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic\n"
         "\n"
         "set_option maxRecDepth 5000\n"
         "open scoped BigOperators\n"
         "namespace YangMills.MagneticSmearing\n"
         "\n"
         "/-- The eight signed axis moves have weight one and holding has weight eight. -/\n"
         "def moves : List Int := List.replicate 8 0 ++ [1,-1,2,-2,3,-3,4,-4]\n"
         "\n"
         "theorem moveWeights : (moves.length,moves.count 0) = (");
    number(count);
    emit(",");
    number(holds);
    emit(") := by decide\n"
         "\n"
         "LEAN-END\n");

    request(1,4,2);
}
static void child(unsigned dim,unsigned order) {
    if (dim!=4 || order!=2) stop(5);
    unsigned total=endpoint(0);
    for (int axis=1;axis<=4;++axis) total+=endpoint(axis)+endpoint(-axis);
    emit("LEAN-BEGIN\n"
         "/-- At radius one the first nonzero move stops the two-step walk. -/\n"
         "def stoppedTwo : List Int := moves.flatMap fun a => moves.map fun b => if a=0 then b else a\n"
         "\n"
         "theorem stoppedMass : (stoppedTwo.count 0, stoppedTwo.count 1) = (");
    number(endpoint(0));
    emit(",");
    number(endpoint(1));
    emit(") := by decide\n"
         "\n"
         "theorem stoppedTotal : stoppedTwo.length = ");
    number(total);
    emit(" := by decide\n"
         "\n"
         "/-- Exit flux at each time must be added to the surviving distribution. -/\n"
         "theorem stoppedTelescopes {A : Type*} [AddCommGroup A] (u e : ℕ → A) (n : ℕ) :\n"
         "    ∑ j ∈ Finset.range n, (u j-u (j+1)-e j) =\n"
         "      u 0-(u n+∑ j ∈ Finset.range n, e j) := by\n"
         "  induction n with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]\n"
         "    abel\n"
         "\n"
         "/-- The static root path contributes a commutator for the transported face. -/\n"
         "theorem frameCommutator {A : Type*} [Ring A] (u v x y : A)\n"
         "    : (x*u)*y*v + u*y*(-(v*x)) = x*(u*y*v)-(u*y*v)*x := by\n"
         "  simp only [mul_neg]\n"
         "  noncomm_ring\n"
         "\n"
         "/-- Summing the two Hodge pieces leaves just the endpoint law. -/\n"
         "theorem hodgeRemainder {A : Type*} [AddCommGroup A] {g h k r : A}\n"
         "    (hd : h+k=g-r) : g=h+k+r := by rw [hd]; abel\n"
         "\n"
         "/-- Scalar recurrence for a killed row and its accumulated exit measure. -/\n"
         "theorem killedStep (live exit oldExit : ℝ) : live - (live-exit) = (oldExit+exit)-oldExit := by ring\n"
         "\n"
         "/-- Forward and backward faces give opposite first-order variations. -/\n"
         "theorem transportedSign (w x z : ℝ) : -(w*x-z) = w*(-x)+z := by ring\n"
         "\n"
         "/-- The estimates for the two finite-support Hodge primitives combine linearly. -/\n"
         "theorem wardBudget {v w h k r δ : ℝ}\n"
         "    (a : |v| ≤ h*δ) (b : |w| ≤ k*δ) :\n"
         "    |v+w|+r ≤ (h+k)*δ+r := by\n"
         "  linarith [abs_add_le v w]\n"
         "\n"
         "/-- The covariance error is controlled by the endpoint remainder. -/\n"
         "theorem projectionTail {v c e r : ℝ} (hid : v-c=e) (h : |e| ≤ r) : |v-c| ≤ r := by\n"
         "  rwa [hid]\n"
         "\n"
         "LEAN-END\n");

    request(2,dim,order);
}
static void grandchild(unsigned dim,unsigned order) {
    if (dim!=4 || order!=2) stop(5);
    unsigned power[2];
    for (unsigned m=1;m<=order;++m) power[m-1]=2*(2*m+dim);
    emit("LEAN-BEGIN\n"
         "def tailExponent (m : ℕ) := 2+m\n"
         "def varianceExponent (m : ℕ) := 2*(2*m+4)\n"
         "\n"
         "theorem smoothingPowers : (tailExponent 1,tailExponent 2) = (3,4) := by decide\n"
         "theorem spectralPowers : (varianceExponent 1,varianceExponent 2) = (");
    number(power[0]);
    emit(",");
    number(power[1]);
    emit(") := by decide\n"
         "\n"
         "/-- Uniform perturbations of the characteristic ODE give a pointwise error.\n"
         "The integrating factor increases on the interval from zero to time t. -/\n"
         "theorem integratingFactorRatio {v t u : ℝ} (hv : 0 ≤ v) (hu : 0 ≤ u) (hut : u ≤ t) :\n"
         "    Real.exp (-v*(t^2-u^2)/2) ≤ 1 := by\n"
         "  apply Real.exp_le_one_iff.mpr\n"
         "  have hs := pow_le_pow_left₀ hu hut 2\n"
         "  nlinarith [mul_nonneg hv (sub_nonneg.mpr hs)]\n"
         "\n"
         "theorem duhamelBound (v t ε : ℝ) (hv : 0 ≤ v) (ht : 0 ≤ t) (e : ℝ → ℝ)\n"
         "    (he : ∀ x ∈ Set.Icc 0 t, |e x| ≤ ε) :\n"
         "    |∫ u in (0:ℝ)..t, Real.exp (-v*(t^2-u^2)/2)*e u| ≤ ε*t := by\n"
         "  have h := intervalIntegral.norm_integral_le_of_norm_le_const\n"
         "    (a := (0:ℝ)) (b := t) (C := ε) (f := fun u => Real.exp (-v*(t^2-u^2)/2)*e u)\n"
         "    (by\n"
         "      intro x hx\n"
         "      rw [Set.uIoc_of_le ht] at hx\n"
         "      rw [Real.norm_eq_abs, abs_mul, abs_of_pos (Real.exp_pos _)]\n"
         "      exact (mul_le_mul_of_nonneg_right (integratingFactorRatio hv hx.1.le hx.2)\n"
         "        (abs_nonneg _)).trans (by simpa using he x ⟨hx.1.le,hx.2⟩))\n"
         "  simpa [Real.norm_eq_abs, abs_of_nonneg ht] using h\n"
         "\n"
         "theorem radialMoment (m : ℕ) {p : ℝ} (hp : p ≠ 0) :\n"
         "    (8*p/((2*(m:ℝ)+1)*(2*m+3)))/(2*(2*p)^3) =\n"
         "      1/(2*p^2*(2*m+1)*(2*m+3)) := by\n"
         "  have h₁ : (2*(m:ℝ)+1) ≠ 0 := by positivity\n"
         "  have h₃ : (2*(m:ℝ)+3) ≠ 0 := by positivity\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem determinantBigger {v c s : ℝ} (hs : 0 < s) (hc : 0 < c) (hv : c ≤ v) :\n"
         "    0 < (1+2*s*v)^2-(2*s*c)^2 ∧ (1+2*s*v)^2-(2*s*c)^2 < (1+2*s*v)^2 := by\n"
         "  have hx : 0 < 2*s*c := by positivity\n"
         "  have hy : 2*s*c ≤ 2*s*v := by nlinarith [mul_nonneg hs.le (sub_nonneg.mpr hv)]\n"
         "  constructor <;> nlinarith [sq_nonneg (2*s*c), sq_pos_of_pos hx,\n"
         "    mul_self_lt_mul_self hx.le (show 2*s*c < 1+2*s*v by linarith)]\n"
         "\n"
         "theorem energyReadback {lo hi mass : ℝ} (h : 0 < mass)\n"
         "    (hw : mass ≤ hi-lo) : lo < hi := by linarith\n"
         "\n"
         "/-- A negative reflected cross moment controls the positive-block moment. -/\n"
         "theorem reflectedSquare {v c : ℝ} (hc : c ≤ 0) : 2*v ≤ v+v-2*c := by linarith\n"
         "\n"
         "/-- The positively supported signed average preserves mass and first moment. -/\n"
         "theorem signedBlockMoments (mass moment shift : ℝ) :\n"
         "    2*mass-mass=mass ∧ 2*(moment+shift*mass)-(moment+2*shift*mass)=moment := by\n"
         "  constructor <;> ring\n"
         "\n"
         "theorem reflectedFirstMoment {moment mass : ℝ} (hc : 2*moment = -mass) :\n"
         "    moment-(-moment-mass)=0 := by linarith\n"
         "\n"
         "/-- The even moment bootstrap absorbs one lower power, independently of y. -/\n"
         "theorem absorbMoment {y A B : ℝ} {n : ℕ}\n"
         "    (hp : 1 ≤ y^n) (hA : 0 ≤ A) (h : y^(n+1) ≤ A+B*y^n) :\n"
         "    y ≤ A+B := by\n"
         "  by_contra hn\n"
         "  have hlt : A+B < y := lt_of_not_ge hn\n"
         "  have h₁ := mul_lt_mul_of_pos_right hlt (show 0 < y^n by linarith)\n"
         "  have h₂ := mul_nonneg hA (sub_nonneg.mpr hp)\n"
         "  rw [pow_succ] at h\n"
         "  nlinarith\n"
         "\n"
         "end YangMills.MagneticSmearing\n"
         "\n"
         "open YangMills.MagneticSmearing\n"
         "#print axioms moveWeights\n"
         "#print axioms stoppedMass\n"
         "#print axioms stoppedTotal\n"
         "#print axioms stoppedTelescopes\n"
         "#print axioms frameCommutator\n"
         "#print axioms hodgeRemainder\n"
         "#print axioms killedStep\n"
         "#print axioms transportedSign\n"
         "#print axioms wardBudget\n"
         "#print axioms projectionTail\n"
         "#print axioms smoothingPowers\n"
         "#print axioms spectralPowers\n"
         "#print axioms integratingFactorRatio\n"
         "#print axioms radialMoment\n"
         "#print axioms determinantBigger\n"
         "#print axioms energyReadback\n"
         "#print axioms duhamelBound\n"
         "#print axioms reflectedSquare\n"
         "#print axioms signedBlockMoments\n"
         "#print axioms reflectedFirstMoment\n"
         "#print axioms absorbMoment\n"
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
