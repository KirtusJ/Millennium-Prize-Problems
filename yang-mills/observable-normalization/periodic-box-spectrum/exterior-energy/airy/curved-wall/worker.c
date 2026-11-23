/* Polynomial controls for the sheared Gaussian trial on the exterior domain. */
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
    /* Scaled lower edge x=R-u/(2R) at z=R. */
    for (int r=2; r<=10; ++r)
        for (int u=0; u<=4; ++u) {
            int lower=2*r*r-u;
            if (lower*lower+4*r*r*u != 4*r*r*r*r+u*u) stop(7);
        }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace CurvedWall\ntheorem edge (v u l : ℝ) : (2*v-l*u)^2+4*v*u=4*v^2+4*v*u*(1-l)+l^2*u^2 := by ring\nLEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem potential (z b u : ℝ) : 2*(z-b*u)^2*u-2*z^2*u= -4*z*b*u^2+2*b^2*u^3 := by ring\nLEAN-END\n");
    request(2, dimension, extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem correction (l : ℝ) : 1/4+1/4-1+l-3*l= -1/2-2*l := by ring\n");
    emit("#print axioms edge\n#print axioms potential\n#print axioms correction\nend CurvedWall\nLEAN-END\n");
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
