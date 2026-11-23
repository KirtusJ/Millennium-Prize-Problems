/* Radial integral and time-window controls for G4 PR 10. */
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
    unsigned fact = 1;
    for (unsigned j = 1; j <= 9; ++j) fact *= j;
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Tactic.NormNum\nnamespace FourierDecay\n");
    emit("theorem radialConstant : (");
    number(fact/126);
    emit(" : \u2115) = 2880 := by decide\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned a, unsigned b) {
    if (a != 4 || b != 3) stop(5);
    unsigned acc = 1;
    for (unsigned j = 10; j <= 11; ++j) acc *= j;
    emit("LEAN-BEGIN\n");
    emit("theorem relativeMoment : (");
    number(acc);
    emit(" : \u2115) = 110 := by decide\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned a, unsigned b) {
    if (a != 4 || b != 3) stop(5);
    unsigned count = 0;
    for (unsigned k = 1; k <= 50; ++k) {
        unsigned gamma = 20*k+8, beta = 2*gamma+2;
        if (gamma*2 < beta && 20*k > 4) ++count;
    }
    emit("LEAN-BEGIN\n");
    emit("theorem separatedWindows : (");
    number(count);
    emit(" : \u2115) = 50 := by decide\n");
    emit("#print axioms radialConstant\n#print axioms relativeMoment\n#print axioms separatedWindows\nend FourierDecay\n");
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
