/* PCP native shell count, torus sign bound, and free spectral powers. */
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
    unsigned single=0, mixed=0;
    for (unsigned spatial=0; spatial<2; ++spatial) {
        for (unsigned spatialSign=0; spatialSign<2; ++spatialSign) {
            ++single;
            for (unsigned temporalSign=0; temporalSign<2; ++temporalSign) ++mixed;
        }
    }
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.Calculus.Deriv.Pow\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "open MeasureTheory\n"
         "namespace YangMills.SpatialFlow\n"
         "\n"
         "/-- Count the lowest visible axis modes and the first modes which also move in time. -/\n"
         "def modes : List (ℕ × ℕ) := (List.range 4).flatMap fun i =>\n"
         "  (List.range 2).map fun sign => (i,sign)\n"
         "def leading := modes.filter (fun p => p.1 < 2)\n"
         "def temporal := leading.flatMap fun p => (modes.filter (fun v => v.1=3)).map fun v => (p,v)\n"
         "theorem firstShells : (leading.length,temporal.length) = (");
    number(single);
    emit(",");
    number(mixed);
    emit(") := by decide\n"
         "\n"
         "theorem singleExponential (E t h : ℝ) :\n"
         "    Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h))\n"
         "    = Real.exp (-E*t)*(1-Real.exp (-E*h))^2 := by\n"
         "  rw [show -E*(t+h)= -E*t+(-E*h) by ring,\n"
         "      show -E*(t+2*h)=(-E*t+(-E*h))+(-E*h) by ring]\n"
         "  simp only [Real.exp_add]\n"
         "  ring\n"
         "\n"
         "/-- This necessary positive-time test also permits a measure with infinite total mass. -/\n"
         "theorem spectralSecondDifference (μ : Measure ℝ) (t h : ℝ)\n"
         "    (i0 : Integrable (fun E : ℝ => Real.exp (-E*t)) μ)\n"
         "    (i1 : Integrable (fun E : ℝ => Real.exp (-E*(t+h))) μ)\n"
         "    (i2 : Integrable (fun E : ℝ => Real.exp (-E*(t+2*h))) μ) :\n"
         "    0 ≤ (∫ E, Real.exp (-E*t) ∂μ)-2*(∫ E, Real.exp (-E*(t+h)) ∂μ)+\n"
         "      (∫ E, Real.exp (-E*(t+2*h)) ∂μ) := by\n"
         "  have isub : Integrable (fun E : ℝ => Real.exp (-E*t)-2*Real.exp (-E*(t+h))) μ :=\n"
         "    i0.sub (i1.const_mul 2)\n"
         "  have hp : ∀ E : ℝ, 0 ≤ Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h)) := by\n"
         "    intro E\n"
         "    rw [singleExponential]\n"
         "    positivity\n"
         "  have hh : 0 ≤ ∫ E : ℝ, Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h)) ∂μ := integral_nonneg hp\n"
         "  rw [integral_add isub i2,integral_sub i0 (i1.const_mul 2),integral_const_mul] at hh\n"
         "  exact hh\n"
         "\n"
         "theorem negativeAgainstSpectrum {a b c : ℝ} (h : a-2*b+c<0) : ¬ 0≤a-2*b+c := not_le.mpr h\n"
         "\n"
         "theorem subtractMean (a b c m : ℝ) :\n"
         "    (a-m^2)-2*(b-m^2)+(c-m^2)=a-2*b+c := by ring\n"
         "\n"
         "LEAN-END\n");

    request(1,4,2);
}
static void child(unsigned dim, unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    unsigned deficit=pair*822440-913459-721559;
    emit("LEAN-BEGIN\n"
         "/-- Three outward-rounded upper/lower endpoints for normalized squared torus covariances. -/\n"
         "def upperWitness : ℤ := 913459-2*822440+721559\n"
         "theorem torusWitness : upperWitness = -");
    number(deficit);
    emit(" := by decide\n"
         "\n"
         "theorem torusUpper {a b c : ℝ} (ha : a≤913459/1000000)\n"
         "    (hb : 822440/1000000≤b) (hc : c≤721559/1000000) :\n"
         "    a-2*b+c ≤ -9862/1000000 := by linarith\n"
         "\n"
         "theorem midpointObstruction {a b c : ℝ} (ha : 0 ≤ a) (hc : 0 ≤ c) (h : a+c<2*b) :\n"
         "    a*c<b^2 := by\n"
         "  have hb : 0 ≤ b := by linarith\n"
         "  nlinarith [mul_pos (show 0<2*b-(a+c) by linarith) (show 0<2*b+(a+c) by linarith),\n"
         "    sq_nonneg (a-c)]\n"
         "\n"
         "theorem secondShellSign {c u : ℝ} (hc : 0<c) (hu : u<1) :\n"
         "    2*c*(u-1)<0 := mul_neg_of_pos_of_neg (by positivity) (sub_neg.mpr hu)\n"
         "\n"
         "theorem smoothingCurvature {a u : ℝ} (ha : 0<a) (ha2 : a<2)\n"
         "    (h : u≤1/4) : a*(2*a*u-1)<0 := by\n"
         "  apply mul_neg_of_pos_of_neg ha\n"
         "  nlinarith [mul_nonneg ha.le (sub_nonneg.mpr h)]\n"
         "\n"
         "theorem gaussianSecondDerivative (c : ℝ) (x : ℝ) :\n"
         "    HasDerivAt (fun t : ℝ => -2*c*t*Real.exp (-c*t^2))\n"
         "      (2*c*(2*c*x^2-1)*Real.exp (-c*x^2)) x := by\n"
         "  have h1 := ((hasDerivAt_id x).pow 2).const_mul (-c)\n"
         "  have h2 := (((hasDerivAt_id x).const_mul (-2*c)).mul h1.exp)\n"
         "  convert h2 using 1; simp; ring\n"
         "\n"
         "LEAN-END\n");

    request(2,dim,pair);
}
static void grandchild(unsigned dim, unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    emit("LEAN-BEGIN\n"
         "def densityPower (base : ℕ) : ℕ := base+1\n"
         "theorem thresholdPowers : (densityPower 4,4+4) = (");
    number(dim+1);
    emit(",");
    number(dim*pair);
    emit(") := by decide\n"
         "\n"
         "theorem positiveCutoff {s e : ℝ} (he : 0<e) : 0<e^4*Real.exp (-s*e^2) := by positivity\n"
         "\n"
         "theorem projectedTrace (a b c : ℝ) (h : a^2+b^2+c^2=1) :\n"
         "    (1-a^2)^2+(1-b^2)^2+(1-c^2)^2+2*((a*b)^2+(a*c)^2+(b*c)^2)=2 := by\n"
         "  nlinarith [congrArg (fun x : ℝ => x^2) h]\n"
         "\n"
         "theorem energyRatio : ((1/32:ℚ)/(3/128))=4/3 := by norm_num\n"
         "\n"
         "theorem continuumWitness {a b c : ℝ} (ha : a≤960/1000) (hb : 910/1000≤b)\n"
         "    (hc : c≤848/1000) : a-2*b+c ≤ -12/1000 := by linarith\n"
         "\n"
         "theorem heatDifference {k : ℝ} (h : 0<k) : 0<k/4 := by positivity\n"
         "\n"
         "/-- One summable initial defect permits a persistent discrepancy even with common initial data. -/\n"
         "def mismatch (n : ℕ) : ℝ := if n=0 then 0 else 1\n"
         "def defect (n : ℕ) : ℝ := if n=0 then 1 else 0\n"
         "theorem persistentDiscrepancy (n : ℕ) :\n"
         "    mismatch 0=0 ∧ mismatch (n+1)=1 ∧ mismatch (n+1)≤mismatch n+defect n := by\n"
         "  cases n <;> simp [mismatch,defect]\n"
         "\n"
         "/-- A positive rank-one remainder annihilates the first basis vector but can be measured\n"
         "    between two equal swap insertions on that vector. -/\n"
         "def swap (v : ℝ × ℝ) := (v.2,v.1)\n"
         "def remOp (v : ℝ × ℝ) : ℝ × ℝ := (0,v.2)\n"
         "def vacuum : ℝ × ℝ := (1,0)\n"
         "theorem insertionSeesRemainder : remOp vacuum=(0,0) ∧\n"
         "    (swap (remOp (swap vacuum))).1=1 ∧ (∀ v : ℝ × ℝ, 0≤v.1*(remOp v).1+v.2*(remOp v).2) := by\n"
         "  refine ⟨rfl,rfl,?_⟩\n"
         "  intro v\n"
         "  simp [remOp,mul_self_nonneg]\n"
         "\n"
         "end YangMills.SpatialFlow\n"
         "open YangMills.SpatialFlow\n"
         "#print axioms firstShells\n"
         "#print axioms singleExponential\n"
         "#print axioms spectralSecondDifference\n"
         "#print axioms negativeAgainstSpectrum\n"
         "#print axioms subtractMean\n"
         "#print axioms torusWitness\n"
         "#print axioms torusUpper\n"
         "#print axioms midpointObstruction\n"
         "#print axioms secondShellSign\n"
         "#print axioms smoothingCurvature\n"
         "#print axioms gaussianSecondDerivative\n"
         "#print axioms thresholdPowers\n"
         "#print axioms positiveCutoff\n"
         "#print axioms projectedTrace\n"
         "#print axioms energyRatio\n"
         "#print axioms continuumWitness\n"
         "#print axioms heatDifference\n"
         "#print axioms persistentDiscrepancy\n"
         "#print axioms insertionSeesRemainder\n"
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
