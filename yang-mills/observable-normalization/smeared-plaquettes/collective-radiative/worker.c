/* Algebraic controls for the Gaussian pair and radial probability bound. */
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
    for (int x=-8; x<=8; ++x)
        for (int y=-8; y<=8; ++y)
            if ((x+y)*(x-y) != x*x-y*y) stop(7);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace Collective\ntheorem exponent (s p : ℝ) : (s+p/2)^2+(p/2-s)^2=2*s^2+p^2/2 := by ring\nLEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem gram (s p d : ℝ) : (s+p+d)*(s+p-d)-(p-s)^2=4*s*p-d^2 := by ring\nLEAN-END\n");
    request(2, dimension, extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem filledBall (k a : ℝ) : 2*k^2*a^6/6=(5*a/3)*(k^2*a^5/5) := by ring\n");
    emit("#print axioms exponent\n#print axioms gram\n#print axioms filledBall\nend Collective\nLEAN-END\n");
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
