/* Midpoint reflection, independent-stream determinant and rounded witness. */
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
    const unsigned meshes[] = {5, 6, 7, 8, 10};
    for (unsigned i = 0; i < sizeof meshes / sizeof *meshes; ++i) {
        unsigned n = meshes[i], first = 5*n/2, last = (5*n+1)/2;
        /* Averaging both reflected ends puts mean separation at exactly N. */
        if (6*n - first - last != n || last > 3*n) stop(7);
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace ReflectedProbes\n");
    emit("theorem reflectedGram (x y u v : ℝ) : (x^2+y^2)*(u^2+v^2)-(x*u+y*v)^2=(x*v-y*u)^2 := by ring\nLEAN-END\n");
    request(1, 3, 2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem splitCross (a b c d e f : ℝ) : (a+d)*(c+f)-(b+e)^2-(a*c-b^2)-(d*f-e^2)=a*f+d*c-2*b*e := by ring\nLEAN-END\n");
    request(2, dimension, extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    emit("LEAN-BEGIN\ntheorem rectangle : (2287 : Nat)^2 > 29865 * 175 := by decide\n");
    emit("#print axioms reflectedGram\n#print axioms splitCross\n#print axioms rectangle\nend ReflectedProbes\nLEAN-END\n");
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
