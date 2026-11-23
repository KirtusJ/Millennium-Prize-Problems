/* Exact finite checks for mesoscopic Wilson estimates. */
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
    /* Each adjacent swap on a three-edge cube path crosses one face.
       The untouched prefix selects that face's lower or upper side. */
    const unsigned swaps[6] = {0,1,0,1,0,1};
    unsigned axes[3] = {0,1,2}, mask = 0, positives = 0;
    for (unsigned j = 0; j < 6; ++j) {
        unsigned at = swaps[j], i = axes[at], k = axes[at+1];
        unsigned normal = 3-i-k;
        mask |= 1u << (2*normal+at);
        positives += i < k;
        axes[at] = k;
        axes[at+1] = i;
    }
    if (axes[0] || axes[1] != 1 || axes[2] != 2) stop(6);
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Analysis.SpecialFunctions.Log.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Ring\n"
         "import Mathlib.Tactic.NormNum\n"
         "\n"
         "namespace WilsonRate\n"
         "\n"
         "theorem braidLinear (a b c a' b' c' : ℝ) :\n"
         "    a + b' + c - a' - b - c' = -((c'-c)-(b'-b)+(a'-a)) := by ring\n"
         "\n");
    emit("theorem cubeCensus : ((");
    number(mask);
    emit(", ");
    number(positives);
    emit(") : ℕ × ℕ) = (63, 3) := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned shift) {
    if (dimension != 3 || shift != 2) stop(5);
    const unsigned steps = dimension+1;
    unsigned row[9] = {1};
    for (unsigned j = 1; j <= 2*steps; ++j)
        for (unsigned k = j; k > 0; --k) row[k] += row[k-1];
    unsigned previous = 0, variation = 0;
    for (unsigned i = 0; i < 9; ++i) {
        variation += row[i] >= previous ? row[i]-previous : previous-row[i];
        previous = row[i];
    }
    variation += previous;
    emit("LEAN-BEGIN\n");
    emit("theorem telescope (k : ℝ) (M : ℕ) :\n"
         "    (1-k)*(∑ j ∈ Finset.range M, k^j) = 1-k^M := by\n"
         "  induction M with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [Finset.sum_range_succ, mul_add, ih, pow_succ]\n"
         "    ring\n"
         "\n"
         "theorem weightedDifferences (p : ℕ → ℝ) (N : ℕ) :\n"
         "    (∑ i ∈ Finset.range N, ((i:ℝ)+1)*(p i-p (i+1))) =\n"
         "      (∑ i ∈ Finset.range N, p i) - (N:ℝ)*p N := by\n"
         "  induction N with\n"
         "  | zero => simp\n"
         "  | succ n ih =>\n"
         "    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]\n"
         "    push_cast\n"
         "    ring\n"
         "\n");
    emit("theorem binomialVariation : 2 * Nat.choose 8 4 = ");
    number(variation);
    emit(" := by decide\n"
         "\n");
    emit("LEAN-END\n");
    request(2, 3, 2);
}

static void grandchild(unsigned dimension, unsigned shift) {
    if (dimension != 3 || shift != 2) stop(5);
    unsigned power = 2*(dimension+1+2*shift);
    unsigned doubling = 1;
    for (unsigned i = 0; i < power; ++i) doubling *= 2;
    emit("LEAN-BEGIN\n");
    emit("theorem lagRatio {a b e A B q : ℝ}\n"
         "    (hA : |A-a| ≤ e) (hB : |B-b| ≤ e) (hq : 0 ≤ q)\n"
         "    (hsep : q*(a+e) ≤ b-e) : q*A ≤ B := by\n"
         "  rw [abs_le] at hA hB\n"
         "  calc\n"
         "    q*A ≤ q*(a+e) := mul_le_mul_of_nonneg_left (by linarith) hq\n"
         "    _ ≤ b-e := hsep\n"
         "    _ ≤ B := by linarith\n"
         "\n"
         "theorem gapAtLag {m n A B q : ℝ} (hA : 0 < A) (hn : 0 < n)\n"
         "    (hq : 0 < q) (hr : q*A ≤ B) (hs : B ≤ Real.exp (-m*n)*A) :\n"
         "    m ≤ -Real.log q/n := by\n"
         "  have hqe : q ≤ Real.exp (-m*n) := (le_of_mul_le_mul_right (hr.trans hs) hA)\n"
         "  have hlog := Real.log_le_log hq hqe\n"
         "  rw [Real.log_exp] at hlog\n"
         "  exact (le_div_iff₀ hn).2 (by linarith)\n"
         "\n"
         "theorem rankTwoScale : (2:ℕ)*(8+4*2)=32 := by decide\n"
         "\n");
    emit("theorem doubleLag : 2^(8+4*2) = (");
    number(doubling);
    emit(" : ℕ) := by decide\n"
         "\n");
    emit("#print axioms braidLinear\n"
         "#print axioms cubeCensus\n"
         "#print axioms telescope\n"
         "#print axioms weightedDifferences\n"
         "#print axioms binomialVariation\n"
         "#print axioms lagRatio\n"
         "#print axioms gapAtLag\n"
         "#print axioms rankTwoScale\n"
         "#print axioms doubleLag\n"
         "end WilsonRate\n");
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
