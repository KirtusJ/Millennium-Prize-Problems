/* Native PCP commission on spatial-flow bases and energy concentration. */
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
    unsigned power = 1;
    for (unsigned i=0; i<4; ++i) power *= 3;
    unsigned speed = 6*3*power, lipschitz = 6*5*power;
    emit("LEAN-BEGIN\n"
         "import Mathlib.Analysis.SpecialFunctions.ExpDeriv\n"
         "import Mathlib.Algebra.Order.BigOperators.Group.Finset\n"
         "import Mathlib.Data.Real.Sqrt\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "namespace YangMills.FlowBasis\n"
         "\n"
         "theorem mixedClock (s u E : ℝ) :\n"
         "    Real.exp (-s*E^2/2)*Real.exp (-u*E^2/2)=Real.exp (-((s+u)/2)*E^2) := by\n"
         "  rw [← Real.exp_add]\n"
         "  congr 1\n"
         "  ring\n"
         "\n"
         "theorem gramScale {s u : ℝ} (hs : 0<s) (hu : 0<u) :\n"
         "    (2*Real.sqrt s*Real.sqrt u/(s+u))^2 + ((s-u)/(s+u))^2 = 1 := by\n"
         "  have h := Real.sq_sqrt hs.le\n"
         "  have h' := Real.sq_sqrt hu.le\n"
         "  field_simp [show s+u ≠ 0 by linarith]\n"
         "  nlinarith [congrArg₂ (fun x y : ℝ => x*y) h h']\n"
         "\n"
         "theorem entrywiseError {ι : Type*} (I : Finset ι) (c : ι → ℝ) (D : ι → ι → ℝ)\n"
         "    (e : ℝ) (hb : ∀ i ∈ I, ∀ j ∈ I, |D i j| ≤ e) :\n"
         "    |∑ i ∈ I, ∑ j ∈ I, c i*c j*(D i j)| ≤ e*(∑ i ∈ I, |c i|)^2 := by\n"
         "  calc\n"
         "    _ ≤ ∑ i ∈ I, |∑ j ∈ I, c i*c j*(D i j)| := Finset.abs_sum_le_sum_abs _ _\n"
         "    _ ≤ ∑ i ∈ I, ∑ j ∈ I, |c i*c j*(D i j)| := by\n"
         "      apply Finset.sum_le_sum\n"
         "      intro i _\n"
         "      exact Finset.abs_sum_le_sum_abs _ _\n"
         "    _ ≤ ∑ i ∈ I, ∑ j ∈ I, |c i| * |c j| * e := by\n"
         "      apply Finset.sum_le_sum\n"
         "      intro i hi\n"
         "      apply Finset.sum_le_sum\n"
         "      intro j hj\n"
         "      rw [abs_mul,abs_mul]\n"
         "      exact mul_le_mul_of_nonneg_left (hb i hi j hj) (by positivity)\n"
         "    _ = _ := by\n"
         "      simp only [sq, Finset.mul_sum, Finset.sum_mul]\n"
         "      apply Finset.sum_congr rfl\n"
         "      intro i _\n"
         "      apply Finset.sum_congr rfl\n"
         "      intro j _\n"
         "      ring\n"
         "\n"
         "noncomputable def sg (x : ℝ) : ℝ := if x<0 then -1 else 1\n"
         "\n"
         "theorem signProduct (x : ℝ) : x*sg x=|x| := by\n"
         "  by_cases hx : x<0\n"
         "  · simp [sg,hx,abs_of_neg hx]\n"
         "  · simp [sg,hx,abs_of_nonneg (le_of_not_gt hx)]\n"
         "\n"
         "theorem sharpLine {ι : Type*} (I : Finset ι) (c : ι → ℝ) (e : ℝ) :\n"
         "    (∑ i ∈ I, ∑ j ∈ I, c i*c j*(e*sg (c i)*sg (c j))) = e*(∑ i ∈ I, |c i|)^2 := by\n"
         "  simp only [sq,Finset.sum_mul,Finset.mul_sum]\n"
         "  apply Finset.sum_congr rfl\n"
         "  intro i _\n"
         "  apply Finset.sum_congr rfl\n"
         "  intro j _\n"
         "  rw [← signProduct (c i),← signProduct (c j)]\n"
         "  ring\n"
         "\n"
         "theorem amplificationBound {h ell chi A qN : ℝ} (hq : 0<qN) (hA : 0<A)\n"
         "    (hh : h ≤ ell+chi*A*qN) : (h-ell)/(A*qN) ≤ chi := by\n"
         "  apply (div_le_iff₀ (mul_pos hA hq)).2\n"
         "  linarith only [hh, mul_assoc chi A qN]\n"
         "\n"
         "theorem monotoneWeights {l h w₁ w₂ : ℝ} (hl : 0≤l) (hh : 0≤h) (hw : w₁≤w₂) :\n"
         "    (l*w₁)*h ≤ l*(h*w₂) := by\n"
         "  nlinarith [mul_nonneg (mul_nonneg hl hh) (sub_nonneg.mpr hw)]\n"
         "\n"
         "\n"
         "theorem localQuaternionBounds : ((6*3^5,6*5*3^4) : ℕ × ℕ) = (");
    number(speed);
    emit(",");
    number(lipschitz);
    emit(") := by decide\n"
         "\n"
         "theorem recoverBand {X V M A r : ℝ} (hA : 0<A) (h : V ≤ A*X+M*r) :\n"
         "    (V-M*r)/A ≤ X := by\n"
         "  apply (div_le_iff₀ hA).2\n"
         "  linarith only [h, mul_comm A X]\n"
         "LEAN-END\n");

    request(1,4,2);
}
static void child(unsigned dim,unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    int c[5] = {1,-16,96,-256,256};
    unsigned total = 0;
    for (unsigned j=0; j<5; ++j) total += (unsigned)(c[j]<0 ? -c[j] : c[j]);
    emit("LEAN-BEGIN\n"
         "theorem fejerThree (x : ℝ) :\n"
         "    1-(4*(2*x-1)^3-3*(2*x-1)) = 2*(1-x)*(1-4*x)^2 := by ring\n"
         "\n"
         "theorem fiveWeights (x : ℝ) :\n"
         "    (1-4*x)^4=1-16*x+96*x^2-256*x^3+256*x^4 := by ring\n"
         "\n"
         "theorem signedSum : (1-16+96-256+256 : ℤ)=81 := by decide\n"
         "theorem absoluteSum : (1+16+96+256+256 : ℕ)=");
    number(total);
    emit(" := by decide\n"
         "\n"
         "theorem eighthHarmonics : ((-56*2^3+28*4^3-8*6^3+8^3 : ℚ)/128)=1 ∧\n"
         "    ((56*2-28*4+8*6-8 : ℚ)/128)=5/16 := by norm_num\n"
         "\n"
         "theorem limitMomentRatio {g : ℝ} (hg : 0<g) :\n"
         "    ((5/32:ℝ)/g^7)/((1/12:ℝ)/g^5)=15/(8*g^2) := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "theorem halfBand {p : ℝ} (h : p≤15/32) : 1/2 < 1-p := by linarith\n"
         "LEAN-END\n");

    request(2,dim,pair);
}
static void grandchild(unsigned dim,unsigned pair) {
    if (dim!=4 || pair!=2) stop(5);
    int c[5] = {1,-16,96,-256,256};
    int sixth = 0;
    for (unsigned i=2; i<5; ++i) sixth += c[i]*c[6-i];
    emit("LEAN-BEGIN\n"
         "noncomputable def term (r : ℝ) := (5*r-1)*r^2*Real.sqrt r\n"
         "\n"
         "theorem sqrtBounds (u lo hi : ℝ) (hl : lo^2 ≤ u) (hh : u ≤ hi^2) (hp : 0 ≤ hi) :\n"
         "    lo ≤ Real.sqrt u ∧ Real.sqrt u ≤ hi :=\n"
         "  ⟨Real.le_sqrt_of_sq_le hl, Real.sqrt_le_iff.mpr ⟨hp,hh⟩⟩\n"
         "\n"
         "noncomputable def comp (f : ℝ → ℝ) :=\n"
         "    1*f (8/8) -32*f (8/11) +448*f (8/14) -3584*f (8/17) +17920*f (8/20) -57344*f (8/23) +");
    number((unsigned)sixth);
    emit("*f (8/26) -131072*f (8/29) +65536*f (8/32)\n"
         "\n"
         "theorem fiveRayleigh : comp term < 0 := by\n"
         "  have h0 := sqrtBounds (8/8) (10000000000/10000000000) (10000000001/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h1 := sqrtBounds (8/11) (8528028654/10000000000) (8528028655/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h2 := sqrtBounds (8/14) (7559289460/10000000000) (7559289461/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h3 := sqrtBounds (8/17) (6859943405/10000000000) (6859943406/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h4 := sqrtBounds (8/20) (6324555320/10000000000) (6324555321/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h5 := sqrtBounds (8/23) (5897678246/10000000000) (5897678247/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h6 := sqrtBounds (8/26) (5547001962/10000000000) (5547001963/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h7 := sqrtBounds (8/29) (5252257314/10000000000) (5252257315/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  have h8 := sqrtBounds (8/32) (5000000000/10000000000) (5000000001/10000000000) (by norm_num) (by norm_num) (by norm_num)\n"
         "  unfold comp term\n"
         "  linarith only [h0.2, h1.1, h2.2, h3.1, h4.2, h5.1, h6.2, h7.1, h8.2]\n"
         "\n"
         "\n"
         "/-- At fixed flow variable, the moving-momentum energy window has square-root width. -/\n"
         "theorem windowWidth {lo hi D : ℝ} (hlo : 0 ≤ lo) (hhi : lo ≤ hi)\n"
         "    (h : hi^2-lo^2 ≤ D) : hi-lo ≤ Real.sqrt D := by\n"
         "  apply Real.le_sqrt_of_sq_le\n"
         "  nlinarith [mul_nonneg hlo (sub_nonneg.mpr hhi)]\n"
         "\n"
         "theorem energyWindow (E δ : ℝ) : (E+δ)^2-E^2=δ*(2*E+δ) := by ring\n"
         "\n"
         "theorem intervalAverage {num den cap : ℝ} (hd : 0 < den) (hb : num ≤ cap*den) :\n"
         "    num/den ≤ cap := (div_le_iff₀ hd).2 hb\n"
         "\n"
         "end YangMills.FlowBasis\n"
         "open YangMills.FlowBasis\n"
         "#print axioms mixedClock\n"
         "#print axioms gramScale\n"
         "#print axioms entrywiseError\n"
         "#print axioms signProduct\n"
         "#print axioms sharpLine\n"
         "#print axioms amplificationBound\n"
         "#print axioms monotoneWeights\n"
         "#print axioms fejerThree\n"
         "#print axioms fiveWeights\n"
         "#print axioms signedSum\n"
         "#print axioms absoluteSum\n"
         "#print axioms eighthHarmonics\n"
         "#print axioms limitMomentRatio\n"
         "#print axioms halfBand\n"
         "#print axioms sqrtBounds\n"
         "#print axioms fiveRayleigh\n"
         "#print axioms localQuaternionBounds\n"
         "#print axioms recoverBand\n"
         "#print axioms windowWidth\n"
         "#print axioms energyWindow\n"
         "#print axioms intervalAverage\n"
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
