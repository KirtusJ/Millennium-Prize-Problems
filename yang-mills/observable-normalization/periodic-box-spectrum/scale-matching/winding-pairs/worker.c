/* Finite-volume winding-pair tests in the cubic E channel. */
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
    /* Units of 10^-4. The SU(2) row is followed by the five SU(3) rows. */
    const unsigned lower[] = {12200, 5190, 5830, 6700, 8830, 9100};
    const unsigned flux[] =  { 5804, 2107, 2526, 3057, 3485, 4035};
    const unsigned costs[] = {  592,  976,  778,  586, 1860, 1030};
    for (unsigned i = 0; i < sizeof lower / sizeof *lower; ++i)
        if (lower[i] != 2 * flux[i] + costs[i]) stop(7);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Linarith\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace WindingPairs\n");
    emit("theorem diagonalFloor (l u w : ℝ) (hl : l ≤ u) (hw : 0 ≤ w) : l ≤ (1-w)*l+w*u := by nlinarith [mul_nonneg hw (sub_nonneg.mpr hl)]\nLEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem energyWeight (m w e : ℝ) (h : (1-w)*e ≤ m) : e-m ≤ e*w := by nlinarith only [h]\n");
    emit("theorem transferWeight (r w q : ℝ) (h : r ≤ w+(1-w)*q) : r-q ≤ (1-q)*w := by nlinarith only [h]\nLEAN-END\n");
    request(2, dimension, extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem commonMix (g a b c d : ℝ) : (g-a)*(b-g)-(g-c)*(d-g)=(a+b-c-d)*g+c*d-a*b := by ring\n");
    emit("#print axioms diagonalFloor\n#print axioms energyWeight\n#print axioms transferWeight\n#print axioms commonMix\nend WindingPairs\nLEAN-END\n");
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
