/* Native finite checks for the resolution cost at moving momentum. */
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
    unsigned block = 8;
    while (block*block*81 < 160*160*6) block += 8;
    emit("LEAN-BEGIN\n"
         "import Mathlib.Data.Real.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.NormNum\n"
         "import Mathlib.Tactic.Ring\n"
         "\n"
         "namespace MovingThreshold\n"
         "\n"
         "theorem excess (k d : ℝ) : (k+d)^2-k^2 = d*(2*k+d) := by ring\n"
         "\n"
         "theorem fiberWidth {x d z lo : ℝ} (hz : z^2=x) (hl : lo^2=x-d)\n"
         "    (hn : 0≤lo) (ho : lo≤z) : (z-lo)*z ≤ d := by\n"
         "  nlinarith [mul_nonneg (sub_nonneg.mpr ho) hn]\n"
         "\n"
         "theorem sparseFiber {inside outside fraction η : ℝ}\n"
         "    (hi : inside ≤ fraction) (ho : outside ≤ η/2)\n"
         "    (ht : η ≤ inside+outside) : η/2 ≤ fraction := by linarith\n"
         "\n"
         "theorem conditionalConstant :\n"
         "    (40:ℕ)^2*81 < 160^2*6 ∧ 160^2*6 ≤ ");
    number(block);
    emit("^2*81 := by decide\n"
         "LEAN-END\n");
    request(1, 4, 2);
}

static void child(unsigned order, unsigned power) {
    if (order != 4 || power != 2) stop(5);
    /* Fejer at order four is x(2x-1)^2. Square by convolution. */
    const int coefficients[] = {0, 1, -4, 4};
    int product[7] = {0};
    for (unsigned i = 0; i < order; ++i)
        for (unsigned j = 0; j < order; ++j)
            product[i+j] += coefficients[i]*coefficients[j];
    unsigned norm = 0;
    for (unsigned i = 0; i < 7; ++i)
        norm += (unsigned)(product[i] < 0 ? -product[i] : product[i]);
    emit("LEAN-BEGIN\n"
         "\n"
         "theorem mixedMass {a b m : ℝ} (h : m ≤ a+b) : m/2 ≤ a ∨ m/2 ≤ b := by\n"
         "  by_contra! hn\n"
         "  linarith\n"
         "\n"
         "theorem spinWeight {z : ℝ} (h : z^2 ≤ 1/4) : 9/16 ≤ (1-z^2)^2 := by\n"
         "  nlinarith [sq_nonneg (1/4-z^2)]\n"
         "\n"
         "theorem fejerFour (x : ℝ) :\n"
         "    (x*(2*x-1)^2)^2 = x^2-8*x^3+24*x^4-32*x^5+16*x^6 := by ring\n"
         "\n"
         "theorem fourClockNorm : (1+8+24+32+16 : ℕ) = ");
    number(norm);
    emit(" := by decide\n"
         "LEAN-END\n");
    request(2, order, power);
}

static void grandchild(unsigned order, unsigned power) {
    if (order != 4 || power != 2) stop(5);
    /* Nonconstant Fourier coefficients of 128 sin^8 from Pascal's row. */
    int total = 0, binomial = 1;
    for (unsigned j = 0; j < order; ++j) {
        int harmonic = (int)(order*power-2*j);
        int fifth = harmonic*harmonic*harmonic*harmonic*harmonic;
        total += (j % 2 ? 1 : -1) * binomial * fifth;
        binomial = binomial*(int)(order*power-j)/(int)(j+1);
    }
    if (total <= 0) stop(6);
    emit("LEAN-BEGIN\n"
         "\n"
         "theorem harmonicFive :\n"
         "    (56:ℤ)*2^5-28*4^5+8*6^5-8^5 = ");
    number((unsigned)total);
    emit(" := by decide\n"
         "\n"
         "theorem movingMean : (2/3:ℚ)*(1/12)/(20/240)*4 = 8/3 := by norm_num\n"
         "\n"
         "#print axioms excess\n"
         "#print axioms fiberWidth\n"
         "#print axioms sparseFiber\n"
         "#print axioms conditionalConstant\n"
         "#print axioms mixedMass\n"
         "#print axioms spinWeight\n"
         "#print axioms fejerFour\n"
         "#print axioms fourClockNorm\n"
         "#print axioms harmonicFive\n"
         "#print axioms movingMean\n"
         "end MovingThreshold\n"
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
