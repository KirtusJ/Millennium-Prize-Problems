/* Independent-scale scalar products and extrapolation controls. */
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
    const unsigned masses[] = {5001, 3652};  /* 10^4 aM */
    const unsigned flow[] = {3522, 6628};    /* 10^3 t0/a^2 */
    const unsigned lows[] = {2654, 2659};    /* 10^3 M sqrt(8t0), rounded down */
    for (unsigned i = 0; i < 2; ++i) {
        unsigned long squared = 8UL * flow[i] * masses[i] * masses[i];
        unsigned long low = lows[i];
        if (squared <= 100000UL * low * low ||
            squared >= 100000UL * (low + 1) * (low + 1)) stop(7);
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace PhysicalScalar\n");
    emit("theorem affineIntercept (a b c f : ℝ) : c*(a+b*f)-f*(a+b*c)=(c-f)*a := by ring\nLEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem quadraticError (k c f : ℝ) : c*(k*f^2)-f*(k*c^2)= -(c-f)*k*c*f := by ring\nLEAN-END\n");
    request(2, dimension, extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem inverseSideResidual : (20 : Nat)*847-12*840 = 6860 := by decide\n");
    emit("#print axioms affineIntercept\n#print axioms quadraticError\n#print axioms inverseSideResidual\nend PhysicalScalar\nLEAN-END\n");
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
