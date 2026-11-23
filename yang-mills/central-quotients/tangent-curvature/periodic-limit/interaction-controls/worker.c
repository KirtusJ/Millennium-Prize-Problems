/* Cubic shell, Wick cycles and gap normalization controls. */
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
    unsigned n = 0;
    for (int x=-1;x<=1;++x) for (int y=-1;y<=1;++y) for (int z=-1;z<=1;++z) {
        int energy=x*x+y*y+z*z;
        if (energy==0 && (x*x-y*y)!=0) stop(7);
        if (energy==1) n+=(unsigned)((x*x-y*y)*(x*x-y*y));
    }
    emit("LEAN-BEGIN\n");
    emit("import Mathlib.Data.Real.Basic\nimport Mathlib.Tactic.Ring\nnamespace InteractionControls\n");
    emit("theorem shellDifference : (");
    number(n);
    emit(" : ℕ) = 4 := by decide\n");
    emit("LEAN-END\n");
    request(1, 4, 3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    unsigned n=0;
    for (unsigned a=1;a<4;++a) for (unsigned b=1;b<4;++b) for (unsigned c=1;c<4;++c)
        if (a!=b && b!=c && c!=a) ++n;
    emit("LEAN-BEGIN\n");
    emit("theorem ringCount : (");
    number(n);
    emit(" : ℕ) = 6 := by decide\n");
    emit("LEAN-END\n");
    request(2, 4, 3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    unsigned n = 12u*8u*8u*12u*12u/96u;
    emit("LEAN-BEGIN\n");
    emit("theorem secondMomentConstant : (");
    number(n);
    emit(" : ℕ) = 1152 := by decide\n");
    emit("theorem pairEnergy (e m : ℝ) : 2*e-2*m=2*(e-m) := by ring\n#print axioms shellDifference\n#print axioms ringCount\n#print axioms secondMomentConstant\n#print axioms pairEnergy\nend InteractionControls\n");
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
