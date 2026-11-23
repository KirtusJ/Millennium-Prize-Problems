/* PCP proof producer for central link shifts. Tasks carry dimension and face count. */
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



static unsigned shift(unsigned n, unsigned site, unsigned axis) {
    unsigned stride = axis == 0 ? 1 : (axis == 1 ? n : n*n);
    unsigned digit = (site/stride)%n;
    return site - stride*digit + stride*((digit+1)%n);
}

static void boundary(unsigned n, unsigned face, unsigned edge[4]) {
    unsigned site = face/3, i = (face%3+1)%3, j = (face%3+2)%3;
    edge[0] = 3*site+i;
    edge[1] = 3*shift(n,site,i)+j;
    edge[2] = 3*shift(n,site,j)+i;
    edge[3] = 3*site+j;
}


static unsigned mask(unsigned size, unsigned edge, unsigned p) {
    unsigned edges[4]; boundary(size,p,edges);
    for (unsigned j=0; j<4; ++j) if (edges[j]==edge) return 1;
    return 0;
}
static unsigned common(unsigned size, unsigned a, unsigned b) {
    unsigned out=0;
    for (unsigned p=0; p<3*size*size*size; ++p) out+=mask(size,a,p)*mask(size,b,p);
    return out;
}
static unsigned census(unsigned size) {
    unsigned count=0;
    for (unsigned a=0;a<3*size*size*size;++a)
        count += common(size,a,a)==4;
    return count;
}
static void parent(void) {
    unsigned faces=common(3,0,0);
    emit("LEAN-BEGIN\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Set\n"
         "import Mathlib.Tactic.NoncommRing\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Positivity\n"
         "import Mathlib.Tactic.FieldSimp\n"
         "\n"
         "open MeasureTheory Set\n"
         "open scoped BigOperators\n"
         "namespace YangMills.ElectricDisorder\n"
         "\n"
         "theorem twistConjugation {R : Type*} [Ring R] {d v h w : R}\n"
         "    (hinv : d*v=1) (hw : v*h*d=h+w) : h*d-d*h=d*w := by\n"
         "  have t := congrArg (d*·) hw\n"
         "  change d*(v*h*d)=d*(h+w) at t\n"
         "  rw [← mul_assoc, ← mul_assoc, hinv, one_mul, mul_add] at t\n"
         "  rw [t]\n"
         "  abel\n"
         "\n"
         "/-- Unit-disk trace deficit controls squared distance from one. -/\n"
         "theorem diskDefect {x y : ℝ} (hd : x^2+y^2 ≤ 1) :\n"
         "    (1-x)^2+y^2 ≤ 2*(1-x) := by nlinarith\n"
         "\n"
         "/-- A normalized nonnegative average of bounded SU(2) plaquette defects. -/\n"
         "theorem meanSquare (s : Finset ℕ) (p d : ℕ → ℝ)\n"
         "    (hp : ∀ i ∈ s, 0 ≤ p i) (hn : ∑ i ∈ s, p i = 1)\n"
         "    (hd : ∀ i ∈ s, 0 ≤ d i ∧ d i ≤ 2) :\n"
         "    (∑ i ∈ s, p i*d i)^2 ≤ 2*(∑ i ∈ s, p i*d i) := by\n"
         "  have lo : 0 ≤ ∑ i ∈ s, p i*d i :=\n"
         "    Finset.sum_nonneg fun i hi => mul_nonneg (hp i hi) (hd i hi).1\n"
         "  have hi : (∑ i ∈ s, p i*d i) ≤ 2 := calc\n"
         "    _ ≤ ∑ i ∈ s, p i*2 := Finset.sum_le_sum fun i hi =>\n"
         "      mul_le_mul_of_nonneg_left (hd i hi).2 (hp i hi)\n"
         "    _ = 2 := by rw [← Finset.sum_mul, hn, one_mul]\n"
         "  nlinarith [mul_nonneg lo (sub_nonneg.mpr hi)]\n"
         "\n"
         "private def shiftSite (n site axis : ℕ) : ℕ :=\n"
         "  let stride := n^axis\n"
         "  let digit := site / stride % n\n"
         "  site - stride*digit + stride*((digit+1)%n)\n"
         "\n"
         "private def corners (n p : ℕ) : List ℕ :=\n"
         "  let s := p/3\n"
         "  let i := (p%3+1)%3\n"
         "  let j := (p%3+2)%3\n"
         "  [3*s+i,3*shiftSite n s i+j,3*shiftSite n s j+i,3*s+j]\n"
         "\n"
         "private def flipped (n e : ℕ) := (List.range (3*n^3)).filter fun p => (corners n p).contains e\n"
         "\n"
         "theorem sideThreeFixture : (flipped 3 0).length = ");
    number(faces);
    emit(" ∧\n"
         "    ((flipped 3 0).filter fun p => (flipped 3 1).contains p).length = ");
    number(common(3,0,1));
    emit(" := by decide +kernel\n"
         "LEAN-END\n");

    request(1,3,faces);
}
static void child(unsigned dimension, unsigned faces) {
    if (dimension!=3 || faces!=common(3,0,0)) stop(5);
    emit("LEAN-BEGIN\n"
         "\n"
         "theorem residualTail (μ : Measure ℝ) [IsFiniteMeasure μ] (δ : ℝ) (hδ : 0 < δ)\n"
         "    (hi : Integrable (fun x : ℝ => (x-1)^2) μ) :\n"
         "    δ^2 * μ.real {x : ℝ | δ ≤ |x-1|} ≤ ∫ x, (x-1)^2 ∂μ := by\n"
         "  let S := {x : ℝ | δ ≤ |x-1|}\n"
         "  have hs : MeasurableSet S := measurableSet_le measurable_const\n"
         "    ((continuous_id.sub continuous_const).abs.measurable)\n"
         "  have h := integral_mono_ae ((integrable_const (μ := μ) (δ^2)).indicator hs) hi\n"
         "    (Filter.Eventually.of_forall (fun x => show S.indicator (fun _ => δ^2) x ≤ (x-1)^2 by\n"
         "      by_cases hx : x ∈ S\n"
         "      · rw [indicator_of_mem hx]\n"
         "        have hh : δ ≤ |x-1| := hx\n"
         "        nlinarith [sq_abs (x-1), mul_nonneg (sub_nonneg.mpr hh)\n"
         "          (add_nonneg (abs_nonneg (x-1)) hδ.le)]\n"
         "      · rw [indicator_of_not_mem hx]\n"
         "        positivity))\n"
         "  rw [integral_indicator hs] at h\n"
         "  simpa [S, mul_comm] using h\n"
         "\n"
         "theorem vacuumBound (μ : Measure ℝ) [IsFiniteMeasure μ]\n"
         "    (hi : Integrable (fun x : ℝ => (x-1)^2) μ) :\n"
         "    μ.real {0} ≤ ∫ x, (x-1)^2 ∂μ := by\n"
         "  have hset : ({0} : Set ℝ) ⊆ {x | 1 ≤ |x-1|} := by\n"
         "    intro x hx\n"
         "    simp only [mem_singleton_iff] at hx\n"
         "    subst x\n"
         "    norm_num\n"
         "  exact (measureReal_mono (μ := μ) hset).trans (by simpa using residualTail μ 1 (by norm_num) hi)\n"
         "\n"
         "theorem twoStepSquare {x c : ℝ} : (x-c)^2=x^2-2*c*x+c^2 := by ring\n"
         "\n"
         "theorem transferBudget {ham wilson normStep vacuum err : ℝ} (h1 : wilson ≤ ham+normStep+vacuum)\n"
         "    (hn : 0 ≤ wilson) (h : ham ≤ err) :\n"
         "    wilson^2 ≤ (err+normStep+vacuum)^2 := by\n"
         "  have hb : wilson ≤ err+normStep+vacuum := by linarith\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ err+normStep+vacuum+wilson by linarith)]\n"
         "\n"
         "private def shiftEnergy (n : ℕ) : ℕ := (flipped 3 n).length*2\n"
         "theorem fourFacesEnergy : shiftEnergy 0 = ");
    number(2*faces);
    emit(" := by decide +kernel\n"
         "LEAN-END\n");

    request(2,dimension,faces);
}
static void grandchild(unsigned dimension, unsigned faces) {
    if (dimension!=3 || faces!=common(3,0,0)) stop(5);
    emit("LEAN-BEGIN\n"
         "\n"
         "/-- Effective rank from a trace lower bound and a Hilbert-Schmidt budget. -/\n"
         "theorem rankBudget {k allowed rank tr hs : ℝ}\n"
         "    (hk : 0 ≤ k) (hr : 0 ≤ rank) (ha : 0 < allowed)\n"
         "    (htr : k ≤ tr) (hcs : tr^2 ≤ rank*hs) (hhs : hs ≤ allowed) :\n"
         "    k^2/allowed ≤ rank := by\n"
         "  apply (div_le_iff₀ ha).mpr\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr htr) (show 0 ≤ tr+k by linarith),\n"
         "    mul_nonneg hr (sub_nonneg.mpr hhs)]\n"
         "\n"
         "theorem exactBandFraction : 1 - 16*((2:ℚ)*(17*1024/8+3/16)/2^20) = 489469/524288 := by norm_num\n"
         "\n"
         "theorem sideFourRank : (93:ℚ) <\n"
         "    192*(489469/524288)^2/(1+191*(34819/8388608)) := by norm_num\n"
         "\n"
         "theorem threeRank : (52:ℚ) <\n"
         "    81*(489469/524288)^2/(1+80*(34819/8388608)) := by norm_num\n"
         "\n"
         "private def numLinks (n : ℕ) := 3*n^3\n"
         "theorem rankCount : (numLinks 3,numLinks 4)=(");
    number(census(3));
    emit(",");
    number(census(4));
    emit(") := by decide\n"
         "\n"
         "/-- Averaging all rotations/translations of a defect pattern uses each face\n"
         "with the same total weight. This identity permits arbitrary input states. -/\n"
         "theorem orbitAverage {ι κ : Type*} (s : Finset ι) (f : Finset κ)\n"
         "    (w : ι → κ → ℝ) (cost : κ → ℝ) (c : ℝ)\n"
         "    (uniform : ∀ p ∈ f, ∑ i ∈ s, w i p = c) :\n"
         "    (∑ i ∈ s, ∑ p ∈ f, w i p * cost p) = c * ∑ p ∈ f, cost p := by\n"
         "  rw [Finset.sum_comm, Finset.mul_sum]\n"
         "  apply Finset.sum_congr rfl\n"
         "  intro p hp\n"
         "  rw [← Finset.sum_mul, uniform p hp]\n"
         "\n"
         "theorem subspaceFraction {err : ℝ} (he : 0 ≤ err) (h : err ≤ 7/100) :\n"
         "    (92:ℝ)/100 ≤ 1-16*err^2 := by\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr h) (show 0 ≤ 7/100+err by linarith)]\n"
         "\n"
         "\n"
         "/-- Cancellation of the electric timeline and the spatial trial width. -/\n"
         "theorem trialClock (beta b a A : ℝ) (hbeta : 0 < beta) (hb : 0 < b) (ha : 0 < a) (hA : 0 < A) :\n"
         "    (1 / ((beta*b/a)*(A^2/beta))) / (a*beta/b) = 1/(A^2*beta) := by\n"
         "  field_simp\n"
         "  ring\n"
         "\n"
         "/-- Cost of the two potential factors in the one-step residual. -/\n"
         "theorem stepFactors {j step bound : ℝ} (hj : 0 < j) (h : step ≤ (j⁻¹+j)*bound) :\n"
         "    step*j ≤ (1+j^2)*bound := by\n"
         "  have hb := mul_le_mul_of_nonneg_right h hj.le\n"
         "  have eq : (j⁻¹+j)*bound*j = (1+j^2)*bound := calc\n"
         "    _ = (j⁻¹*j+j^2)*bound := by ring\n"
         "    _ = _ := by simp [ne_of_gt hj]\n"
         "  rwa [eq] at hb\n"
         "\n"
         "theorem projectedBadPart (μ : Measure ℝ) [IsFiniteMeasure μ] (eta : ℝ)\n"
         "    (hn : ∀ᵐ x ∂μ, 0 ≤ x) (hi : Integrable (fun x : ℝ => x) μ) :\n"
         "    eta * μ.real (Ici eta) ≤ ∫ x, x ∂μ := by\n"
         "  have hs := measurableSet_Ici (a := eta)\n"
         "  have H := integral_mono_ae ((integrable_const (μ := μ) eta).indicator hs) hi\n"
         "    (by\n"
         "      filter_upwards [hn] with x hx\n"
         "      by_cases hmem : x ∈ Ici eta\n"
         "      · rw [indicator_of_mem hmem]\n"
         "        exact hmem\n"
         "      · rwa [indicator_of_not_mem hmem])\n"
         "  rw [integral_indicator hs] at H\n"
         "  simpa [mul_comm] using H\n"
         "\n"
         "\n"
         "#print axioms trialClock\n"
         "#print axioms stepFactors\n"
         "#print axioms projectedBadPart\n"
         "#print axioms orbitAverage\n"
         "#print axioms subspaceFraction\n"
         "#print axioms twistConjugation\n"
         "#print axioms diskDefect\n"
         "#print axioms meanSquare\n"
         "#print axioms sideThreeFixture\n"
         "#print axioms residualTail\n"
         "#print axioms vacuumBound\n"
         "#print axioms twoStepSquare\n"
         "#print axioms transferBudget\n"
         "#print axioms fourFacesEnergy\n"
         "#print axioms rankBudget\n"
         "#print axioms exactBandFraction\n"
         "#print axioms sideFourRank\n"
         "#print axioms threeRank\n"
         "#print axioms rankCount\n"
         "end YangMills.ElectricDisorder\n"
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
