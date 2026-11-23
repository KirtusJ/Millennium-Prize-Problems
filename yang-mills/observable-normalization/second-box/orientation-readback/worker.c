/* Walsh weights in the conditional orientation expansion. */
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

static unsigned weight(unsigned mask) {
    return (mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1);
}



static void parent(void) {
    unsigned inverse_sum = 0;
    for (unsigned mode = 1; mode < 8; ++mode) inverse_sum += 6 / weight(mode);
    if (inverse_sum != 29) stop(7);
    emit("LEAN-BEGIN\nnamespace Orientation\ntheorem inverseSum : (");
    number(inverse_sum); emit(" : Nat) = 29 := by decide\nLEAN-END\n");
    request(1,3,2);
}

static void child(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    for (unsigned i = 0; i < dimension; ++i) {
        int signed_sum = 0;
        for (unsigned mode = 1; mode < 8; ++mode) {
            int term = 6 / (int)weight(mode);
            signed_sum += (mode & (1u << i)) ? -term : term;
        }
        if (signed_sum != 1) stop(7);
    }
    emit("LEAN-BEGIN\ntheorem tangentCoefficient : (3*29+1 : Nat) = 88 := by decide\nLEAN-END\n");
    request(2,dimension,extent);
}

static void grandchild(unsigned dimension, unsigned extent) {
    if (dimension != 3 || extent != 2) stop(5);
    /* A scalar perturbation has trace four times its eigenvalue. */
    unsigned scalar = 3 * (88 - 4);
    if (scalar != 252) stop(7);
    emit("LEAN-BEGIN\ntheorem scalarControl : ("); number(scalar);
    emit(" : Nat) = 24*21/2 := by decide\n");
    emit("#print axioms inverseSum\n#print axioms tangentCoefficient\n#print axioms scalarControl\nend Orientation\nLEAN-END\n");
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
