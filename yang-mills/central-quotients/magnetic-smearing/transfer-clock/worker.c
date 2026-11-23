/* Native PCP commission on transfer clocks, stationary flux and character weight. */
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
    unsigned cap = 1;
    while (cap*7*9 <= 48*64) cap *= 2;
    emit("LEAN-BEGIN\n"
         "import Mathlib.Data.Real.Sqrt\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "open MeasureTheory\n"
         "namespace YangMills.TransferClock\n"
         "\n"
         "noncomputable def walkRoot (v : ℝ) := (2+v-Real.sqrt (v*(v+4)))/2\n"
         "\n"
         "theorem walkEquation {v : ℝ} (hv : 0≤v) :\n"
         "    (2+v)*walkRoot v = 1+(walkRoot v)^2 := by\n"
         "  unfold walkRoot\n"
         "  nlinarith [Real.sq_sqrt (show 0≤v*(v+4) by positivity)]\n"
         "\n"
         "theorem boundedClockPoint {y l : ℝ} (hl : l≤y) (hy : y≤1) :\n"
         "    (1+l)*(1-y)≤1-y^2 := by nlinarith [mul_nonneg (sub_nonneg.mpr hl) (sub_nonneg.mpr hy)]\n"
         "\n"
         "theorem boundedClockLaw {X : Type*} [MeasurableSpace X] (μ : Measure X)\n"
         "    (f : X → ℝ) (l : ℝ) (hr : ∀ x, l≤f x ∧ f x≤1)\n"
         "    (h1 : Integrable (fun x => 1-f x) μ) (h2 : Integrable (fun x => 1-(f x)^2) μ) :\n"
         "    (1+l)*(∫ x, 1-f x ∂μ) ≤ ∫ x, 1-(f x)^2 ∂μ := by\n"
         "  rw [← integral_const_mul]\n"
         "  exact integral_mono (h1.const_mul _) h2 (fun x => boundedClockPoint (hr x).1 (hr x).2)\n"
         "\n"
         "theorem clockError {a r d₁ d₂ u₁ u₂ e : ℝ} (ha : 0≤a)\n"
         "    (hf : a*u₁ ≤ u₂) (hg : d₂ ≤ r*d₁) (h1 : d₁-e ≤ u₁) (h2 : u₂ ≤ d₂+e) :\n"
         "    (a-r)*d₁ ≤ (1+a)*e := by\n"
         "  nlinarith [mul_le_mul_of_nonneg_left h1 ha]\n"
         "\n"
         "theorem capConstant : ((7:ℚ)/48)*(9/64)>1/");
    number(cap);
    emit(" := by norm_num\n"
         "\n"
         "theorem sharedClockDifference (E z : ℝ) :\n"
         "    ((E+z)/2)^2+((E-z)/2)^2=(E^2+z^2)/2 := by ring\n"
         "\n"
         "theorem independentSymmetry (a b c d : ℝ) : (a*b+c*d)/2=(d*c+b*a)/2 := by ring\n"
         "LEAN-END\n");

    request(1,4,2);
}
static int seam(unsigned side,unsigned x,unsigned y) {
    return x+1 == side ? -(int)(side*y) : 0;
}
static void child(unsigned dimension,unsigned legs) {
    if (dimension!=4 || legs!=2) stop(5);
    const unsigned side = dimension+legs;
    unsigned count = 0;
    for (unsigned x=0; x<side; ++x) for (unsigned y=0; y<side; ++y) {
        int face = seam(side,x,y) + (int)((x+1)%side) - seam(side,x,(y+1)%side) - (int)x;
        if (((face%4)+4)%4==1) ++count;
    }
    emit("LEAN-BEGIN\n"
         "def ux (L x y : ℕ) : ℤ := if x+1=L then -(L:ℤ)*y else 0\n"
         "\n"
         "def flux (L x y : ℕ) : ℤ :=\n"
         "  (ux L x y+((x+1)%L:ℕ)-ux L x ((y+1)%L)-(x:ℤ))%4\n"
         "\n"
         "def faces (L : ℕ) : List ℤ := (List.range L).flatMap fun x => (List.range L).map (flux L x)\n"
         "\n"
         "theorem sixTorus : ((faces 6).filter (·=1)).length = ");
    number(count);
    emit(" := by decide\n"
         "\n"
         "theorem evenCorner (k : ℤ) : (1-(2*k)^2)%4=1 := by\n"
         "  rw [show 1-(2*k)^2= -k^2*4+1 by ring]\n"
         "  omega\n"
         "\n"
         "theorem conditionalRange (κ h : ℝ) (h₁ : (3/8)*κ ≤ h) (h₂ : (1/8)*κ ≤ 1/2-h) :\n"
         "    (3/8)*κ ≤ h ∧ h ≤ 1/2-κ/8 := by constructor <;> linarith\n"
         "\n"
         "/-- A lower bound for a squared discrepancy on one measurable set. -/\n"
         "theorem eventIntegral {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]\n"
         "    (D : X → ℝ) (m v p : ℝ) {S : Set X} (hm : MeasurableSet S)\n"
         "    (hp : p ≤ μ.real S) (hv : 0≤v)\n"
         "    (hs : ∀ x ∈ S, v≤(D x-m)^2) (hi : Integrable (fun x => (D x-m)^2) μ) :\n"
         "    v*p ≤ ∫ x, (D x-m)^2 ∂μ := by\n"
         "  apply (mul_le_mul_of_nonneg_left hp hv).trans\n"
         "  exact (setIntegral_ge_of_const_le hm (measure_ne_top _ _) hs hi.integrableOn).trans\n"
         "    (setIntegral_le_integral hi (Filter.Eventually.of_forall (fun x => sq_nonneg _)))\n"
         "\n"
         "theorem separatedReadings {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]\n"
         "    (D : X → ℝ) (m a b p : ℝ) (hab : a≤b) (A B : Set X)\n"
         "    (hA : MeasurableSet A) (hB : MeasurableSet B) (pA : p ≤ μ.real A) (pB : p ≤ μ.real B)\n"
         "    (lo : ∀ x ∈ A, D x≤a) (hi : ∀ x ∈ B, b≤D x) (integ : Integrable (fun x => (D x-m)^2) μ) :\n"
         "    ((b-a)/2)^2*p ≤ ∫ x, (D x-m)^2 ∂μ := by\n"
         "  by_cases hh : (a+b)/2≤m\n"
         "  · apply eventIntegral μ D m _ p hA pA (sq_nonneg _) _ integ\n"
         "    intro x hx\n"
         "    have d := lo x hx\n"
         "    have h := mul_nonneg (show 0≤(m-D x)-(b-a)/2 by linarith)\n"
         "      (show 0≤(m-D x)+(b-a)/2 by linarith)\n"
         "    nlinarith\n"
         "  · apply eventIntegral μ D m _ p hB pB (sq_nonneg _) _ integ\n"
         "    intro x hx\n"
         "    have d := hi x hx\n"
         "    have h := mul_nonneg (show 0≤(D x-m)-(b-a)/2 by linarith)\n"
         "      (show 0≤(D x-m)+(b-a)/2 by linarith)\n"
         "    nlinarith\n"
         "LEAN-END\n");

    request(2,dimension,legs);
}
static void grandchild(unsigned dimension,unsigned legs) {
    if (dimension!=4 || legs!=2) stop(5);
    /* E[x^2]=1/d and E[x^4]=3/(d(d+2)) for the Haar sphere. */
    unsigned denominator = dimension*(dimension+2)*legs;
    unsigned numerator = 4*(dimension+2-3);
    if (denominator%numerator) stop(6);
    emit("LEAN-BEGIN\n"
         "theorem squareMagnetic (x : ℝ) : (1-x^2)/2 = (3-(4*x^2-1))/8 := by ring\n"
         "\n"
         "theorem centerOrder {y t : ℝ} (hy : 0<y) (hy' : y<1) (ht : 0<t) (ht' : t<1) :\n"
         "    2*y*t/(1+y^2*t^2) < 2*y*t/(t^2+y^2) := by\n"
         "  have h : 0<(1-y^2)*(1-t^2) := by\n"
         "    apply mul_pos\n"
         "    · nlinarith [mul_pos (sub_pos.mpr hy') (by linarith : 0<1+y)]\n"
         "    · nlinarith [mul_pos (sub_pos.mpr ht') (by linarith : 0<1+t)]\n"
         "  apply div_lt_div_of_pos_left (by positivity) (by positivity)\n"
         "  nlinarith\n"
         "\n"
         "theorem oddWeight {l h x a b : ℝ} (hx : 0≤x) (ha : 0≤a) (hb : 0≤b)\n"
         "    (hd : 2*x*b ≤ h-l) (hs : 2*a ≤ h+l) : 4*x*a*b ≤ h^2-l^2 := by\n"
         "  have hh := mul_le_mul hd hs (by positivity : 0 ≤ 2*a) (by linarith [mul_nonneg hx hb] : 0 ≤ h-l)\n"
         "  nlinarith only [hh]\n"
         "\n"
         "theorem haarCoefficient : (4:ℚ)/2*(1/4-1/8)=1/");
    number(denominator/numerator);
    emit(" := by norm_num\n"
         "\n"
         "theorem atomFloor {v a b : ℝ} (ha : 0≤a) (hb : b≤a) (h : a*(a-b)/8≤-v) :\n"
         "    (a*(a-b)/8)^2 ≤ v^2 := by\n"
         "  have hd : 0 ≤ a-b := sub_nonneg.mpr hb\n"
         "  have hp : 0≤a*(a-b)/8 := by positivity\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr h) (by linarith : 0 ≤ -v+a*(a-b)/8)]\n"
         "\n"
         "theorem characterLimit (x : ℝ) (hx : x ≠ -1) : 2*(1-x)/(1+x)=4/(1+x)-2 := by\n"
         "  field_simp [show 1+x ≠ 0 by intro h; apply hx; linarith]\n"
         "  ring\n"
         "\n"
         "end YangMills.TransferClock\n"
         "open YangMills.TransferClock\n"
         "#print axioms walkEquation\n"
         "#print axioms boundedClockPoint\n"
         "#print axioms boundedClockLaw\n"
         "#print axioms clockError\n"
         "#print axioms capConstant\n"
         "#print axioms sharedClockDifference\n"
         "#print axioms independentSymmetry\n"
         "#print axioms sixTorus\n"
         "#print axioms evenCorner\n"
         "#print axioms conditionalRange\n"
         "#print axioms eventIntegral\n"
         "#print axioms separatedReadings\n"
         "#print axioms squareMagnetic\n"
         "#print axioms centerOrder\n"
         "#print axioms oddWeight\n"
         "#print axioms haarCoefficient\n"
         "#print axioms atomFloor\n"
         "#print axioms characterLimit\n"
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
