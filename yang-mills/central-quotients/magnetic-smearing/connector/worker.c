/* Measured native guests check marked time rows, axial Haar moments and spectral powers. */
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


static unsigned shared(unsigned lag) {
    unsigned n = 0;
    for (unsigned t = 0; t < 5; ++t) {
        unsigned next = (t + 1) % 5;
        if ((t == 0 || t == lag) && (next == 0 || next == lag)) ++n;
    }
    return n;
}

static void parent(void) {
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.Calculus.Deriv.Inv\n"
         "import Mathlib.Tactic.Group\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Analysis.SpecialFunctions.Sqrt\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "open MeasureTheory Set\n"
         "open scoped BigOperators\n"
         "namespace YangMills.MagneticConnector\n"
         "\n"
         "/-- Temporal faces at the location of one selected spatial edge, on a five-slice circle. -/\n"
         "def doubleFaces (lag : ℕ) : ℕ :=\n"
         "  ((List.range 5).filter fun t =>\n"
         "    (t=0 ∨ t=lag) ∧ ((t+1)%5=0 ∨ (t+1)%5=lag)).length\n"
         "\n"
         "theorem markedRows : (doubleFaces 1,doubleFaces 2,doubleFaces 4) = (");
    number(shared(1));
    emit(",");
    number(shared(2));
    emit(",");
    number(shared(4));
    emit(") := by decide\n"
         "\n"
         "/-- Different collinear positive bonds cannot be the two parallel edges of a square. -/\n"
         "theorem straightPrivate {x y x' y' : ℤ} (row : y=y') :\n"
         "    ¬ (x=x' ∧ (y'=y+1 ∨ y=y'+1)) := by omega\n"
         "\n"
         "theorem rebaseConnector {G : Type*} [Group G] (p w a b : G) :\n"
         "    (p⁻¹*a*p)⁻¹*(w*b*w⁻¹)=p⁻¹*(a⁻¹*(p*w)*b*(p*w)⁻¹)*p := by group\n"
         "\n"
         "theorem orthogonalDeficit (x y z : ℝ) :\n"
         "    (x-y)^2 ≤ 2*((x-z)^2+(y-z)^2) := by nlinarith [sq_nonneg (x+y-2*z)]\n"
         "\n"
         "/-- Centering changes the measured second moment by a squared mean. -/\n"
         "theorem secondMomentError {s m v δ : ℝ} (hs : |s-v| ≤ δ) (hm : |m| ≤ δ) :\n"
         "    |(s-m^2)-v| ≤ δ+δ^2 := by\n"
         "  have hsq : m^2 ≤ δ^2 := by\n"
         "    nlinarith [sq_abs m, mul_nonneg (sub_nonneg.mpr hm) (add_nonneg\n"
         "      (le_trans (abs_nonneg m) hm) (abs_nonneg m))]\n"
         "  rw [abs_le] at hs ⊢\n"
         "  constructor <;> nlinarith [sq_nonneg m, sq_nonneg δ]\n"
         "\n"
         "/-- The two-slice transfer moment is an ordinary exponential-moment bound. -/\n"
         "theorem twoStepWindow (μ : Measure ℝ) [IsFiniteMeasure μ] (u : ℝ)\n"
         "    (hi : Integrable (fun x : ℝ => Real.exp (-2*x)) μ) :\n"
         "    Real.exp (-2*u) * μ.real (Iic u) ≤ ∫ x, Real.exp (-2*x) ∂μ := by\n"
         "  have hs : MeasurableSet (Iic u) := measurableSet_Iic\n"
         "  have h := integral_mono_ae ((integrable_const (μ := μ) (Real.exp (-2*u))).indicator hs) hi\n"
         "    (Filter.Eventually.of_forall (fun x =>\n"
         "      show (Iic u).indicator (fun _ => Real.exp (-2*u)) x ≤ Real.exp (-2*x) by\n"
         "        by_cases hx : x ∈ Iic u\n"
         "        · rw [indicator_of_mem hx]\n"
         "          exact Real.exp_le_exp.mpr (by change x ≤ u at hx; linarith)\n"
         "        · rw [indicator_of_not_mem hx]\n"
         "          exact (Real.exp_pos _).le))\n"
         "  rw [integral_indicator hs] at h\n"
         "  simpa [mul_comm] using h\n"
         "\n"
         "LEAN-END\n");

    request(1,4,2);
}

static void child(unsigned power, unsigned degree) {
    if (power != 4 || degree != 2) stop(5);
    unsigned count=0, squares=0;
    int sum=0;
    for (unsigned axis=0; axis<3; ++axis) {
        for (int sign=-1; sign<=1; sign+=2) {
            int dot=axis==0 ? sign : 0;
            ++count;
            sum+=dot;
            squares+=(unsigned)(dot*dot);
        }
    }
    if (sum != 0) stop(5);
    emit("LEAN-BEGIN\n"
         "/-- Squared entry and linear entry sums from the six axial images of a unit vector. -/\n"
         "def axialSample : List ℤ := [1,-1,0,0,0,0]\n"
         "\n"
         "theorem axialMoments : (axialSample.length,axialSample.sum,\n"
         "    (axialSample.map (fun x => x*x)).sum) = (");
    number(count);
    emit(",");
    number((unsigned)sum);
    emit(",");
    number(squares);
    emit(") := by decide\n"
         "\n"
         "theorem twoStepExponent (s θ : ℝ) :\n"
         "    Real.exp (-2*s) / Real.exp (-2*((1-θ)*s))=Real.exp (-2*θ*s) := by\n"
         "  rw [← Real.exp_sub]\n"
         "  congr 1\n"
         "  ring\n"
         "\n"
         "theorem varianceBudget {a b v δ : ℝ} (ha : |a-v| ≤ δ) (hb : b^2 ≤ δ^2) :\n"
         "    |a-b^2-v| ≤ δ+δ^2 := by\n"
         "  rw [abs_le] at ha ⊢\n"
         "  constructor <;> nlinarith [sq_nonneg b,sq_nonneg δ]\n"
         "\n"
         "theorem driftPartialBudget {n : ℕ} {e : ℕ → ℝ} {δ : ℝ} (he : ∀ i < n, |e i| ≤ δ) :\n"
         "    |∑ i ∈ Finset.range n, e i| ≤ n*δ := by\n"
         "  calc\n"
         "    _ ≤ ∑ i ∈ Finset.range n, |e i| := Finset.abs_sum_le_sum_abs _ _\n"
         "    _ ≤ ∑ _i ∈ Finset.range n, δ :=\n"
         "      Finset.sum_le_sum fun i hi => he i (Finset.mem_range.mp hi)\n"
         "    _ = _ := by simp\n"
         "\n"
         "theorem innovationIdentity {α : Type*} [MeasurableSpace α] (μ : Measure α)\n"
         "    [IsProbabilityMeasure μ] (f : α → ℝ) (hi : Integrable f μ)\n"
         "    (hi2 : Integrable (fun x => f x ^ 2) μ) :\n"
         "    ∫ x, (f x - ∫ y, f y ∂μ)^2 ∂μ = (∫ x, f x^2 ∂μ) - (∫ x, f x ∂μ)^2 := by\n"
         "  let m := ∫ y, f y ∂μ\n"
         "  change ∫ x, (f x-m)^2 ∂μ = _ - m^2\n"
         "  have hp : ∀ x, (f x-m)^2 = (f x^2-(2*m)*f x)+m^2 := by intro x; ring\n"
         "  simp_rw [hp]\n"
         "  have his : Integrable (fun x => f x^2 - (2*m)*f x) μ := hi2.sub (hi.const_mul _)\n"
         "  rw [integral_add his (integrable_const (m^2)),\n"
         "      integral_sub hi2 (hi.const_mul _), integral_const_mul, integral_const]\n"
         "  simp [m]\n"
         "  ring\n"
         "\n"
         "/-- The family may overlap arbitrarily. Only the individual one-step norms enter. -/\n"
         "theorem sumPrediction {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]\n"
         "    (s : Finset ℕ) (c δ : ℕ → ℝ) (u : ℕ → E) (hu : ∀ i ∈ s, ‖u i‖ ≤ δ i) :\n"
         "    ‖∑ i ∈ s, c i • u i‖ ≤ ∑ i ∈ s, |c i| * δ i := by\n"
         "  calc\n"
         "    _ ≤ ∑ i ∈ s, ‖c i • u i‖ := norm_sum_le _ _\n"
         "    _ ≤ _ := Finset.sum_le_sum fun i hi => by\n"
         "      rw [norm_smul, Real.norm_eq_abs]\n"
         "      exact mul_le_mul_of_nonneg_left (hu i hi) (abs_nonneg _)\n"
         "\n"
         "theorem dressingCost {q w ε : ℝ} (he : 0<ε) (h : q ≤ (w*ε)^2) :\n"
         "    q/ε^2 ≤ w^2 := by\n"
         "  apply (div_le_iff₀ (sq_pos_of_pos he)).mpr\n"
         "  nlinarith [mul_pow w ε 2]\n"
         "\n"
         "LEAN-END\n");

    request(2,power,degree);
}

static void grandchild(unsigned power, unsigned degree) {
    if (power != 4 || degree != 2) stop(5);
    emit("LEAN-BEGIN\n"
         "def disc (z h k : ℝ) := (z+h)^2-4*z*h*k\n"
         "\n"
         "theorem angularDiscriminant {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :\n"
         "    0 < disc z h k := by\n"
         "  unfold disc\n"
         "  nlinarith [sq_nonneg (z-h),mul_pos (mul_pos hz hh) (sub_pos.mpr hk)]\n"
         "\n"
         "theorem angularNumerator (z h k : ℝ) :\n"
         "    2*disc z h k-(z-h)*(2*(z+h)-4*h*k)=4*h*(z+h)*(1-k) := by unfold disc; ring\n"
         "\n"
         "theorem angularDerivative {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :\n"
         "    HasDerivAt (fun x => (x-h)/Real.sqrt (disc x h k))\n"
         "      (2*h*(z+h)*(1-k)/(Real.sqrt (disc z h k))^3) z := by\n"
         "  have hd := angularDiscriminant hz hh hk\n"
         "  have hs := (Real.sqrt_pos.2 hd).ne'\n"
         "  have da : HasDerivAt (fun x : ℝ => disc x h k) (2*(z+h)-4*h*k) z := by\n"
         "    unfold disc\n"
         "    convert ((((hasDerivAt_id z).add_const h).pow 2).sub\n"
         "      (((hasDerivAt_id z).const_mul 4).mul_const h |>.mul_const k)) using 1; simp\n"
         "  convert (((hasDerivAt_id z).sub_const h).div (da.sqrt hd.ne') hs) using 1\n"
         "  field_simp\n"
         "  set u := Real.sqrt (disc z h k)\n"
         "  have hu : u^2=disc z h k := Real.sq_sqrt hd.le\n"
         "  rw [show u*(2*u)=2*disc z h k by nlinarith [hu],angularNumerator,← hu]\n"
         "  ring\n"
         "\n"
         "theorem radialSlopePositive {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :\n"
         "    0 < 2*h*(z+h)*(1-k)/(Real.sqrt (disc z h k))^3 := by\n"
         "  exact div_pos (mul_pos (mul_pos (mul_pos (by norm_num) hh) (add_pos hz hh)) (sub_pos.mpr hk))\n"
         "    (pow_pos (Real.sqrt_pos.2 (angularDiscriminant hz hh hk)) _)\n"
         "\n"
         "theorem commonRadialCancellation {a b : ℝ} (h : a+b=0) : b = -a := by linarith\n"
         "\n"
         "theorem radialCovariancePair (x y fx fy : ℝ) :\n"
         "    (x-y)*(fx-fy)=x*fx+y*fy-x*fy-y*fx := by ring\n"
         "\n"
         "theorem strictRadialPair {x y fx fy : ℝ} (hx : x<y) (hf : fx<fy) :\n"
         "    0 < (x-y)*(fx-fy) := mul_pos_of_neg_of_neg (sub_neg.mpr hx) (sub_neg.mpr hf)\n"
         "\n"
         "theorem normalizedLaplacianCoefficients (v w t u : ℝ) :\n"
         "    (v+w)*(t+u)+(v-w)*(t-u) = 2*(v*t+w*u) := by ring\n"
         "\n"
         "def firstPowers : List Nat := [4+4,6+6,4+4+4+4]\n"
         "theorem windowPowers : firstPowers = [");
    number(degree*power);
    emit(",");
    number(degree*(power+2));
    emit(",");
    number(2*degree*power);
    emit("] := by decide\n"
         "\n"
         "theorem densitySimplex : (6:ℚ)^2/40320=1/1120 := by norm_num\n"
         "\n"
         "theorem positiveReading {h a rest : ℝ} (hh : 0<h) (ha : 0<a) (hr : 0≤rest) :\n"
         "    0<h*a^2+rest := add_pos_of_pos_of_nonneg (mul_pos hh (sq_pos_of_pos ha)) hr\n"
         "\n"
         "end YangMills.MagneticConnector\n"
         "open YangMills.MagneticConnector\n"
         "#print axioms markedRows\n"
         "#print axioms straightPrivate\n"
         "#print axioms rebaseConnector\n"
         "#print axioms orthogonalDeficit\n"
         "#print axioms secondMomentError\n"
         "#print axioms twoStepWindow\n"
         "#print axioms axialMoments\n"
         "#print axioms twoStepExponent\n"
         "#print axioms varianceBudget\n"
         "#print axioms driftPartialBudget\n"
         "#print axioms innovationIdentity\n"
         "#print axioms angularDiscriminant\n"
         "#print axioms angularNumerator\n"
         "#print axioms angularDerivative\n"
         "#print axioms radialSlopePositive\n"
         "#print axioms commonRadialCancellation\n"
         "#print axioms radialCovariancePair\n"
         "#print axioms strictRadialPair\n"
         "#print axioms normalizedLaplacianCoefficients\n"
         "#print axioms windowPowers\n"
         "#print axioms densitySimplex\n"
         "#print axioms positiveReading\n"
         "#print axioms sumPrediction\n"
         "#print axioms dressingCost\n"
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
