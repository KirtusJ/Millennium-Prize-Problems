/* Finite spatial-block, path and energy-band calculations. */
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
    int row[22] = {1}, next[22];
    unsigned length = 1;
    for (unsigned layer = 0; layer < 6; ++layer) {
        for (unsigned i = 0; i < 22; ++i) next[i] = 0;
        for (unsigned i = 0; i < length; ++i)
            for (unsigned j = 0; j < 4; ++j) next[i+j] += row[i];
        length += 3;
        for (unsigned i = 0; i < length; ++i) row[i] = next[i];
    }
    for (unsigned layer = 0; layer < 3; ++layer) {
        for (unsigned i = length; i > 0; --i) row[i] -= row[i-1];
        ++length;
    }
    unsigned total = 0;
    int third = 0;
    for (unsigned i = 0; i < length; ++i) {
        total += (unsigned)(row[i]<0 ? -row[i] : row[i]);
        third += (int)(i*i*i)*row[i];
    }
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.MeasureTheory.Integral.Bochner.Basic\n"
         "import Mathlib.Analysis.SpecialFunctions.Log.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Ring\n"
         "import Mathlib.Tactic.NormNum\n"
         "\n"
         "open MeasureTheory\n"
         "namespace WilsonBlock\n"
         "\n"
         "theorem thirdDifference (x : ℝ) :\n"
         "    (1-x)^3=1-3*x+3*x^2-x^3 := by ring\n"
         "\n");
    emit("theorem boxMoment : ((");
    number(total);
    emit(", ");
    number((unsigned)(-third));
    emit(") : ℕ × ℕ) = (264,24576) := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned width, unsigned shifts) {
    if (width != 4 || shifts != 3) stop(5);
    unsigned spatial_visits = 0;
    int radius = (int)width/2;
    for (int t = -1; t <= 1; t += 2)
        for (int x = -radius; x <= radius; ++x)
            for (int y = -radius; y <= radius; ++y)
                for (int z = -radius; z <= radius; ++z) {
                    int p[3] = {x,y,z};
                    for (unsigned axis = 0; axis < shifts; ++axis)
                        for (int j = 0; j != p[axis]; j += p[axis] > 0 ? 1 : -1)
                            ++spatial_visits;
                }
    emit("LEAN-BEGIN\n");
    emit("theorem pathBound {ι κ : Type*} (s : Finset κ) (p : κ → Finset ι)\n"
         "    (h : ι → ℝ) (v : κ → ℝ) (H : ℝ) (hh : ∀ e, |h e| ≤ H) :\n"
         "    (∑ i ∈ s, |v i| * ∑ e ∈ p i, |h e|) ≤\n"
         "       H * ∑ i ∈ s, |v i| * ((p i).card : ℝ) := by\n"
         "  rw [Finset.mul_sum]\n"
         "  apply Finset.sum_le_sum\n"
         "  intro i _\n"
         "  have he : (∑ e ∈ p i, |h e|) ≤ ∑ _e ∈ p i, H :=\n"
         "    Finset.sum_le_sum fun e _ => hh e\n"
         "  simp only [Finset.sum_const, nsmul_eq_mul] at he\n"
         "  calc\n"
         "    _ ≤ |v i| * (((p i).card : ℝ)*H) := mul_le_mul_of_nonneg_left he (abs_nonneg _)\n"
         "    _ = _ := by ring\n"
         "\n"
         "theorem summedError {ι : Type*} (s : Finset ι) (a x y : ι → ℝ)\n"
         "    (d : ℝ) (h : ∀ i ∈ s, |x i-y i| ≤ d) :\n"
         "    |(∑ i ∈ s, a i*x i)-(∑ i ∈ s, a i*y i)| ≤ (∑ i ∈ s, |a i|)*d := by\n"
         "  rw [← Finset.sum_sub_distrib, Finset.sum_mul]\n"
         "  calc\n"
         "    _ ≤ ∑ i ∈ s, |a i*x i-a i*y i| := Finset.abs_sum_le_sum_abs _ _\n"
         "    _ ≤ _ := by\n"
         "      apply Finset.sum_le_sum\n"
         "      intro i hi\n"
         "      rw [← mul_sub, abs_mul]\n"
         "      exact mul_le_mul_of_nonneg_left (h i hi) (abs_nonneg _)\n"
         "\n");
    emit("theorem spatialVisits : (");
    number(spatial_visits);
    emit(" : ℕ) = 900 := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned width, unsigned shifts) {
    if (width != 4 || shifts != 3) stop(5);
    const int numerator[3] = {0,2,4}, counts[3] = {1,14,1};
    int sum = 0;
    for (unsigned i = 0; i < 3; ++i)
        sum += counts[i]*(numerator[i]-1)*(3-numerator[i]);
    emit("LEAN-BEGIN\n");
    emit("theorem bandWeight {X : Type*} [MeasurableSpace X] (μ : Measure X)\n"
         "    (J : Set X) (f : X → ℝ) (hf : Integrable f μ)\n"
         "    (hi : Integrable (J.indicator (fun _ : X => (1:ℝ))) μ)\n"
         "    (hin : ∀ x ∈ J, f x ≤ 1) (hout : ∀ x ∉ J, f x ≤ 0) :\n"
         "    (∫ x, f x ∂μ) ≤ ∫ x, J.indicator (fun _ : X => (1:ℝ)) x ∂μ := by\n"
         "  apply integral_mono hf hi\n"
         "  intro x\n"
         "  by_cases h : x ∈ J\n"
         "  · simpa [Set.indicator_of_mem h] using hin x h\n"
         "  · simpa [Set.indicator, h] using hout x h\n"
         "\n"
         "theorem timeWitness {n m v c B : ℝ} (hn : 0 < n) (hc : 0 < c) (hv : v ≤ 1)\n"
         "    (hl : c ≤ B) (ht : B ≤ Real.exp (-m*n)*v) : m ≤ -Real.log c/n := by\n"
         "  have h : c ≤ Real.exp (-m*n) := calc\n"
         "    c ≤ B := hl\n"
         "    _ ≤ Real.exp (-m*n)*v := ht\n"
         "    _ ≤ Real.exp (-m*n)*1 := mul_le_mul_of_nonneg_left hv (Real.exp_pos _).le\n"
         "    _ = _ := mul_one _\n"
         "  have hlog := Real.log_le_log hc h\n"
         "  rw [Real.log_exp] at hlog\n"
         "  exact (le_div_iff₀ hn).2 (by linarith)\n"
         "\n");
    emit("theorem bandExample : (1*(-1)*3+14*1*1+1*3*(-1) : ℤ) = ");
    number((unsigned)sum);
    emit(" := by decide\n"
         "\n");
    emit("#print axioms thirdDifference\n"
         "#print axioms boxMoment\n"
         "#print axioms pathBound\n"
         "#print axioms summedError\n"
         "#print axioms spatialVisits\n"
         "#print axioms bandWeight\n"
         "#print axioms timeWitness\n"
         "#print axioms bandExample\n"
         "end WilsonBlock\n");
    emit("LEAN-END\n");
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
