/* Binomial truncation, strided indices and a lifted polynomial identity. */
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
    unsigned counts[9] = {1};
    for (unsigned toss=0; toss<8; ++toss)
        for (unsigned heads=toss+1; heads>0; --heads)
            counts[heads]+=counts[heads-1];
    unsigned tail=counts[0]+counts[1]+counts[7]+counts[8];
    emit("LEAN-BEGIN\nimport Mathlib.Data.Real.Basic\nimport Mathlib.Tactic.Ring\nnamespace ClockPrecision\n");
    emit("theorem omittedCount : ("); number(tail);
    emit(" : ℕ) = 18 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned count=0;
    for (unsigned j=1; j<=64; ++j)
        for (unsigned limit=1; limit<=j; ++limit)
            for (unsigned stride=1; stride<=limit+1; ++stride) {
                unsigned q=j/stride, r=j%stride, d=(limit-r)/stride;
                if (r>limit || r+q*stride!=j || d>q || r+d*stride>limit) stop(7);
                ++count;
            }
    emit("LEAN-BEGIN\ntheorem stridedCases : ("); number(count);
    emit(" : ℕ) = 47840 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem lifted (u : ℝ) : 16*u^8=u^2*(-2+16*u^3)+2*u^2*(8*u^6-8*u^3+1) := by ring\n");
    emit("theorem residue (r s k : ℕ) : r+s*(k+1)=r+s*k+s := by ring\n");
    emit("#print axioms omittedCount\n#print axioms stridedCases\n#print axioms lifted\n#print axioms residue\nend ClockPrecision\nLEAN-END\n");
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
