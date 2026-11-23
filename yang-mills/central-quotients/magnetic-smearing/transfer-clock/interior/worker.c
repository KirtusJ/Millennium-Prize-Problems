/* Finite checks for independent spatial clocks at an interior energy. */
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
    /* Width in E^2-k^2 for E0=5, half-width=1/5. Clear denominator 25. */
    unsigned upper = 26, lower = 24;
    unsigned width_times_five = (upper*upper-lower*lower)/5;
    emit("LEAN-BEGIN\n"
         "import Mathlib.MeasureTheory.Integral.Bochner.Basic\n"
         "import Mathlib.Data.Real.Basic\n"
         "import Mathlib.Tactic.Linarith\n"
         "import Mathlib.Tactic.Ring\n"
         "import Mathlib.Tactic.NormNum\n"
         "\n"
         "namespace InteriorClock\n"
         "\n"
         "theorem twoLegs (E z s t : ℝ) :\n"
         "    s*((E+z)/2)^2+t*((E-z)/2)^2 =\n"
         "    (s+t)*(E^2+z^2)/4+(s-t)*E*z/2 := by ring\n"
         "\n"
         "theorem centeredWindowWidth (E d : ℝ) :\n"
         "    (E+d)^2-(E-d)^2 = 4*E*d := by ring\n"
         "\n"
         "theorem geometricRatio (u v : ℝ) (hu : 0 < u) :\n"
         "    (u-1/2)^2+v^2 < (u+1/2)^2+v^2 := by linarith\n"
         "\n"
         "theorem windowExample : (5 : ℕ)*");
    number(width_times_five);
    emit(" = 100 := by decide\n"
         "LEAN-END\n");
    request(1, 4, 2);
}

static void child(unsigned order, unsigned power) {
    if (order != 4 || power != 2) stop(5);
    /* 8 times the translated even Fejer pair at cos(theta0)=1/2. */
    const int shifted[] = {1, -14, 80, -64};
    int squared[7] = {0};
    for (unsigned i = 0; i < order; ++i)
        for (unsigned j = 0; j < order; ++j)
            squared[i+j] += shifted[i]*shifted[j];
    unsigned norm = 0;
    for (unsigned i = 0; i < 7; ++i)
        norm += (unsigned)(squared[i] < 0 ? -squared[i] : squared[i]);
    emit("LEAN-BEGIN\n"
         "\n"
         "open MeasureTheory in\n"
         "theorem finiteWindowTrace {X ι : Type*} [MeasurableSpace X] (μ : Measure X)\n"
         "    (s : Finset ι) (a : ι → ℝ) (h : ι → X → ℝ)\n"
         "    (hi : ∀ i ∈ s, Integrable (fun x => (h i x)^2) μ)\n"
         "    (hf : Integrable (fun x => (∑ i ∈ s, a i * h i x)^2) μ) :\n"
         "    (∫ x, (∑ i ∈ s, a i * h i x)^2 ∂μ) ≤\n"
         "      (∑ i ∈ s, (a i)^2) * ∑ i ∈ s, ∫ x, (h i x)^2 ∂μ := by\n"
         "  have ht : Integrable (fun x => ∑ i ∈ s, (h i x)^2) μ :=\n"
         "    integrable_finset_sum s hi\n"
         "  calc\n"
         "    _ ≤ ∫ x, (∑ i ∈ s, (a i)^2) * ∑ i ∈ s, (h i x)^2 ∂μ :=\n"
         "      integral_mono hf (ht.const_mul _) (fun x =>\n"
         "        Finset.sum_mul_sq_le_sq_mul_sq s a (fun i => h i x))\n"
         "    _ = _ := by rw [integral_const_mul, integral_finset_sum s hi]\n"
         "\n"
         "theorem shiftedFour (x : ℝ) :\n"
         "    let y := 2*x-1\n"
         "    4+3*y-2*(2*y^2-1)-2*(4*y^3-3*y) = 1-14*x+80*x^2-64*x^3 := by\n"
         "  dsimp\n"
         "  ring\n"
         "\n"
         "theorem shiftedSquare (x : ℝ) :\n"
         "    (1-14*x+80*x^2-64*x^3)^2 =\n"
         "    1-28*x+356*x^2-2368*x^3+8192*x^4-10240*x^5+4096*x^6 := by ring\n"
         "\n"
         "theorem shiftedNorm : (1+28+356+2368+8192+10240+4096 : ℕ) = ");
    number(norm);
    emit(" := by decide\n"
         "\n"
         "theorem independentProduct (a b x y : ℝ) :\n"
         "    (a+b)*(x+y)=a*x+a*y+b*x+b*y := by ring\n"
         "LEAN-END\n");
    request(2, order, power);
}

static void grandchild(unsigned order, unsigned power) {
    if (order != 4 || power != 2) stop(5);
    int total = 0, choose = 1;
    for (unsigned j = 0; j < order; ++j) {
        int frequency = (int)(order*power-2*j);
        int seventh = 1;
        for (unsigned k = 0; k < 7; ++k) seventh *= frequency;
        total += (j % 2 ? -1 : 1)*choose*seventh;
        choose = choose*(int)(order*power-j)/(int)(j+1);
    }
    if (total <= 0) stop(6);
    emit("LEAN-BEGIN\n"
         "\n"
         "theorem harmonicSeven :\n"
         "    (8:ℤ)^7-8*6^7+28*4^7-56*2^7 = ");
    number((unsigned)total);
    emit(" := by decide\n"
         "\n"
         "theorem shiftedMeanSquare :\n"
         "    (4:ℚ)*(1/12)/(151/630)=210/151 := by norm_num\n"
         "\n"
         "#print axioms twoLegs\n"
         "#print axioms centeredWindowWidth\n"
         "#print axioms geometricRatio\n"
         "#print axioms windowExample\n"
         "#print axioms finiteWindowTrace\n"
         "#print axioms shiftedFour\n"
         "#print axioms shiftedSquare\n"
         "#print axioms shiftedNorm\n"
         "#print axioms independentProduct\n"
         "#print axioms harmonicSeven\n"
         "#print axioms shiftedMeanSquare\n"
         "end InteriorClock\n"
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
