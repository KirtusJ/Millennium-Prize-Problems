/* Three native checks for the two-site flat-holonomy frequency sum. */
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

static int sign_at(unsigned mask, unsigned axis) {
    return (mask & (1u << axis)) ? -1 : 1;
}

static void parent(void) {
    /* At the origin and face midpoint, tabulate twice the sin-squared sum. */
    unsigned center[7] = {0}, face[7] = {0};
    const unsigned center_expected[] = {1,0,3,0,3,0,1};
    const unsigned face_expected[] = {0,2,0,4,0,2,0};
    for (unsigned mask = 0; mask < 8; ++mask) {
        int yz = sign_at(mask, 1) + sign_at(mask, 2);
        center[3 - sign_at(mask, 0) - yz]++;
        face[3 - yz]++;
    }
    for (unsigned k = 0; k < 7; ++k)
        if (center[k] != center_expected[k] || face[k] != face_expected[k]) stop(6);
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace SecondBoxHolonomy\n");
    emit("theorem midMultiplicity : ("); number(face[3]); emit(" : ℕ) = 4 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    unsigned checks = 0;
    /* Scale S by 32. The two unpaired cosines range over signed multiples
       of 1/16. Compare the squared denominators of f' in every pair. */
    for (int u = -16; u <= 16; ++u) for (int v = -16; v <= 16; ++v) {
        int a = 48 - u - v;
        for (int s = 1; s <= 16; ++s) {
            int lo = a-s, hi = a+s;
            if (lo < 0 || hi*(32+hi)-lo*(32+lo) != 2*s*(32+2*a)) stop(7);
            if (hi*(32+hi) <= lo*(32+lo)) stop(7);
            ++checks;
        }
    }
    emit("LEAN-BEGIN\ntheorem comparisonCount : ("); number(checks);
    emit(" : ℕ) = 17424 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x, unsigned y) {
    if (x != 4 || y != 3) stop(5);
    for (unsigned shift = 0; shift < 8; ++shift) for (unsigned mask = 0; mask < 8; ++mask)
        for (unsigned j = 0; j < 3; ++j)
            if (sign_at(mask^shift,j) != sign_at(mask,j)*sign_at(shift,j)) stop(8);
    emit("LEAN-BEGIN\ntheorem derivativeDifference (a s : ℝ) : (a+s)*(1+a+s)-(a-s)*(1+a-s)=2*s*(1+2*a) := by ring\n");
    emit("#print axioms midMultiplicity\n#print axioms comparisonCount\n#print axioms derivativeDifference\nend SecondBoxHolonomy\nLEAN-END\n");
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
