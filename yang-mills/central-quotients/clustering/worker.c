/* Native PCP supervisor chain. Task bytes: depth, spectral threshold, Laurent weight. */
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




/* Weighted Laurent walk on a line. At degree six the extreme powers are ±6. */
static unsigned constant_term(unsigned degree, unsigned up, unsigned down) {
    unsigned row[13]={0};
    if (degree>6) stop(6);
    row[6]=1;
    for (unsigned n=0;n<degree;++n) {
        unsigned next[13]={0};
        for (unsigned i=6-n;i<=6+n;++i) {
            next[i+1]+=up*row[i];
            next[i-1]+=down*row[i];
        }
        for (unsigned i=0;i<13;++i) row[i]=next[i];
    }
    return row[6];
}
static void parent(void) {
    unsigned up=4;
    emit("LEAN-BEGIN\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv\n"
         "import Mathlib.Analysis.SpecialFunctions.Exp\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "\n"
         "open MeasureTheory Set Filter\n"
         "namespace YangMills.Clustering\n"
         "\n"
         "/-- Real part of the rectangular contour phase on its upper side. -/\n"
         "theorem topPhase {m x u y : ℝ} (hm : 0 ≤ m) (hx : m ≤ x) (hu : 0 ≤ u)\n"
         "    (hu' : u ≤ 1) (hy : 0 ≤ y) :\n"
         "    u*(m*Real.cosh y-x*Real.sinh y) ≤ m*Real.exp (-y) := by\n"
         "  have hs := Real.sinh_nonneg_iff.mpr hy\n"
         "  have h : m*Real.cosh y - x*Real.sinh y ≤ m*(Real.cosh y-Real.sinh y) := by\n"
         "    nlinarith [mul_nonneg (sub_nonneg.mpr hx) hs]\n"
         "  rw [Real.cosh_sub_sinh] at h\n"
         "  calc\n"
         "    _ ≤ u*(m*Real.exp (-y)) := mul_le_mul_of_nonneg_left h hu\n"
         "    _ ≤ _ := by nlinarith [mul_nonneg (sub_nonneg.mpr hu') (mul_nonneg hm (Real.exp_pos (-y)).le)]\n"
         "\n"
         "/-- Zeroth cyclic coefficient of (a*z+b/z)^n, computed as a Laurent walk. -/\n"
         "private def coeff (a b : ℕ) : ℕ → ℤ → ℕ\n"
         "  | 0, j => if j = 0 then 1 else 0\n"
         "  | n+1, j => a*coeff a b n (j-1) + b*coeff a b n (j+1)\n"
         "\n"
         "theorem circleFixture : (coeff 4 2 5 0, coeff 4 2 6 0) = (");
    number(constant_term(5,up,2));
    emit(",");
    number(constant_term(6,up,2));
    emit(") := by decide\n"
         "\n"
         "/-- The low branch is increasing and its value at the threshold has tail error at most q. -/\n"
         "theorem lowResidual {f : ℝ → ℝ} {m x q : ℝ} (h : MonotoneOn f (Icc 0 m))\n"
         "    (h0 : f 0 = 0) (hx : 0 ≤ x) (hm : x ≤ m)\n"
         "    (hq : q ≤ 1) (hend : |1-f m| ≤ q) : |1-f x| ≤ 1 := by\n"
         "  have hfirst := h (show 0 ∈ Icc 0 m from ⟨le_rfl,hx.trans hm⟩) ⟨hx,hm⟩ hx\n"
         "  have hlast := h (show x ∈ Icc 0 m from ⟨hx,hm⟩) ⟨hx.trans hm,le_rfl⟩ hm\n"
         "  rw [h0] at hfirst\n"
         "  rw [abs_le] at hend ⊢\n"
         "  constructor <;> linarith\n"
         "LEAN-END\n");

    request(1,3,up);
}
static void child(unsigned threshold, unsigned up) {
    if (threshold!=3 || up!=4) stop(5);
    const unsigned energies[]={0,1,2,3,7}, masses[]={81,6,10,7,4};
    unsigned low=0,high=0;
    for (unsigned i=0;i<5;++i) {
        if (!energies[i]) continue;
        if (energies[i]<threshold) low+=masses[i]; else high+=masses[i];
    }
    emit("LEAN-BEGIN\n"
         "\n"
         "/-- The absolute residual on a signed cross spectrum, integrated against a\n"
         "positive dominating measure, costs one below the threshold and q above. -/\n"
         "theorem residualIntegral (μ : Measure ℝ) [IsFiniteMeasure μ]\n"
         "    (f s : ℝ → ℝ) (m q : ℝ)\n"
         "    (hs : ∀ x, |s x| ≤ 1) (hl : ∀ x < m, |1-f x| ≤ 1)\n"
         "    (hh : ∀ x, m ≤ x → |1-f x| ≤ q) :\n"
         "    |∫ x, (1-f x)*s x ∂μ| ≤ μ.real (Iio m) + q * μ.real (Ici m) := by\n"
         "  let g : ℝ → ℝ := fun x => (Iio m).indicator (fun _ => (1:ℝ)) x +\n"
         "                             (Ici m).indicator (fun _ => q) x\n"
         "  have hg : Integrable g μ :=\n"
         "    ((integrable_const _).indicator measurableSet_Iio).add\n"
         "      ((integrable_const _).indicator measurableSet_Ici)\n"
         "  have bound : ∀ x, ‖(1-f x)*s x‖ ≤ g x := by\n"
         "    intro x\n"
         "    simp only [Real.norm_eq_abs, abs_mul]\n"
         "    have hs' := mul_le_mul_of_nonneg_left (hs x) (abs_nonneg (1-f x))\n"
         "    by_cases hm : x < m\n"
         "    · simpa [g, hm, not_le.mpr hm, Set.indicator, mul_one] using (hs'.trans (by simpa using hl x hm))\n"
         "    · have hm' := le_of_not_gt hm\n"
         "      simpa [g, hm, hm', Set.indicator, mul_one] using (hs'.trans (by simpa using hh x hm'))\n"
         "  have H := norm_integral_le_of_norm_le hg (Filter.Eventually.of_forall bound)\n"
         "  rw [Real.norm_eq_abs] at H\n"
         "  calc\n"
         "    _ ≤ _ := H\n"
         "    _ = _ := by\n"
         "      rw [show g = _ from rfl, integral_add ((integrable_const _).indicator measurableSet_Iio)\n"
         "        ((integrable_const _).indicator measurableSet_Ici),\n"
         "        integral_indicator measurableSet_Iio, integral_indicator measurableSet_Ici]\n"
         "      simp [mul_comm]\n"
         "\n"
         "theorem translatedBudget {c v w d q : ℝ} (hq : q < 1)\n"
         "    (h : c ≤ d + w + q*(v-w)) : (c-d-q*v)/(1-q) ≤ w := by\n"
         "  apply (div_le_iff₀ (by linarith)).mpr\n"
         "  linarith\n"
         "\n"
         "theorem guardedBand {mass low band u ell v : ℝ}\n"
         "    (h : mass ≤ low+band) (hg : low ≤ ell^2*u^2*v) :\n"
         "    mass-ell^2*u^2*v ≤ band := by linarith\n"
         "\n"
         "private def atoms : List (ℕ × ℕ) := [(0,81),(1,6),(2,10),(3,7),(7,4)]\n"
         "private def mass (p : ℕ → Bool) := ((atoms.filter fun em => p em.1).map Prod.snd).sum\n"
         "theorem thresholdFixture : (mass (fun e => 0 < e && e < 3), mass (fun e => 3 ≤ e)) = (");
    number(low);
    emit(",");
    number(high);
    emit(") := by decide\n"
         "LEAN-END\n");

    request(2,threshold,up);
}
static void grandchild(unsigned threshold, unsigned up) {
    if (threshold!=3 || up!=4) stop(5);
    unsigned h=up*up, mass=2*threshold;
    emit("LEAN-BEGIN\n"
         "\n"
         "/-- Keeping the filter damping yields the Euclidean norm of (h,m) in the exponent. -/\n"
         "theorem angularBalance {h m t a c s : ℝ} (ht : 0 ≤ t) (ha : 0 ≤ a)\n"
         "    (hunit : c^2+s^2=1) (ha2 : a^2=h^2+m^2) :\n"
         "    t*(h*s-m*(1-c)) ≤ t*(a-m) := by\n"
         "  have hs : (h*s+m*c)^2 ≤ a^2 := by\n"
         "    have id : (h*s+m*c)^2+(h*c-m*s)^2=(h^2+m^2)*(c^2+s^2) := by ring\n"
         "    rw [hunit, mul_one, ← ha2] at id\n"
         "    nlinarith [sq_nonneg (h*c-m*s)]\n"
         "  have hle : h*s+m*c ≤ a := by nlinarith [sq_nonneg (h*s+m*c-a)]\n"
         "  apply mul_le_mul_of_nonneg_left _ ht\n"
         "  linarith\n"
         "\n"
         "theorem balancedTime {t a m d : ℝ} (h : t*a=d) :\n"
         "    -d+t*(a-m) = -m*t := by linarith\n"
         "\n"
         "theorem strongExponent {a : ℝ} (ha : 0 < a) (h : a^2 ≤ 292) :\n"
         "    (7:ℝ)/10 < 12/a := by\n"
         "  apply (lt_div_iff₀ ha).mpr\n"
         "  nlinarith [sq_nonneg (a-120/7)]\n"
         "\n"
         "theorem optimizedRate {w : ℝ} (hw : 0 < w) :\n"
         "    ((w+2)^2)/(1+2/w) = w*(w+2) := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem translatedExample {w : ℝ} (h : 3/4 ≤ 1/16+w+(1/4)*(1-w)) :\n"
         "    7/12 ≤ w := by linarith\n"
         "\n"
         "private def squaredNorm (h m : ℕ) := h*h+m*m\n"
         "theorem clockFixture : squaredNorm 16 6 = ");
    number(h*h+mass*mass);
    emit(" := by decide\n"
         "\n"
         "/-- The imaginary-time contour kernel is dominated by the static kernel. -/\n"
         "theorem lagKernel {b a u : ℝ} (hb : 1 ≤ b) (hba : b^2=1+a^2)\n"
         "    (hu : u^2 ≤ 1) : b*u^2 ≤ u^2+a^2 := by\n"
         "  have := mul_nonneg (sub_nonneg.mpr hb) (sub_nonneg.mpr hu)\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ b by linarith)]\n"
         "\n"
         "theorem poleResidue {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :\n"
         "    b*a/(2*a*b)=1/2 := by field_simp; ring\n"
         "\n"
         "/-- One nonzero reading can force mass bounded away from zero and infinity. -/\n"
         "theorem threeReadingBand {read err v small upper multiplier mass : ℝ}\n"
         "    (h : read ≤ err+small*v+upper*v+multiplier*mass) (hm : 0 < multiplier) :\n"
         "    (read-err-(small+upper)*v)/multiplier ≤ mass := by\n"
         "  apply (div_le_iff₀ hm).mpr\n"
         "  linarith\n"
         "\n"
         "#print axioms lagKernel\n"
         "#print axioms poleResidue\n"
         "#print axioms threeReadingBand\n"
         "#print axioms topPhase\n"
         "#print axioms circleFixture\n"
         "#print axioms lowResidual\n"
         "#print axioms residualIntegral\n"
         "#print axioms translatedBudget\n"
         "#print axioms guardedBand\n"
         "#print axioms thresholdFixture\n"
         "#print axioms angularBalance\n"
         "#print axioms balancedTime\n"
         "#print axioms strongExponent\n"
         "#print axioms optimizedRate\n"
         "#print axioms translatedExample\n"
         "#print axioms clockFixture\n"
         "end YangMills.Clustering\n"
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
