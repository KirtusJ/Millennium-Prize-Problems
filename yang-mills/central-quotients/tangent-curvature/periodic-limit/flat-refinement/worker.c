/* Finite arithmetic checks for the flat holonomy refinement. */
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
    unsigned shell[4] = {0};
    for (unsigned i=0; i<3; ++i) for (unsigned j=0; j<3; ++j)
        for (unsigned k=0; k<3; ++k) ++shell[(i!=0)+(j!=0)+(k!=0)];
    if (shell[0]!=1 || shell[1]!=6 || shell[2]!=12 || shell[3]!=8) stop(7);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace FlatRefinement\n");
    emit("theorem hardShells : ([");
    number(shell[1]); emit(","); number(shell[2]); emit(","); number(shell[3]);
    emit("] : List ℕ) = [6,12,8] := by decide\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x!=4 || y!=3) stop(5);
    /* Fourth derivative of |m|^-2, summed over three coordinates:
       three constants of 24, and a radial contribution of -288. */
    unsigned deficit=288-3*24;
    if (deficit!=216) stop(8);
    emit("LEAN-BEGIN\ntheorem radialTrace : (288 - 3*24 : ℕ) = ");
    number(deficit); emit(" := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem symbolCoefficient (s : ℝ) : -(12+(-216+384*s)/2)=24*(4-8*s) := by ring\n");
    emit("#print axioms hardShells\n#print axioms radialTrace\n#print axioms symbolCoefficient\nend FlatRefinement\nLEAN-END\n");
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
