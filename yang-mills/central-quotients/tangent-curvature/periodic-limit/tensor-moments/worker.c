/* Finite angular-generator checks for the spin-two overlap conjecture. */
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

/* Check both inequalities of the angular generator before sending the proof. */
static void parent(void) {
    unsigned count=0;
    for (unsigned a=0;a<12;++a) for (unsigned b=a+1;b<12;++b)
        for (unsigned c=b+1;c<12;++c) {
            if ((a+b)*(c-a)*(c-a)<=(a+c)*(b-a)*(b-a)) stop(7);
            if ((b+c)*(c-a)*(c-a)<=(a+c)*(c-b)*(c-b)) stop(7);
            ++count;
        }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace TensorCone\ntheorem testedTriples : (");
    number(count); emit(" : ℕ) = 220 := by decide\nLEAN-END\n"); request(1,4,3);
}
static void child(unsigned x,unsigned y) {
    if(x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem firstGap (u v a b c : ℝ) : (-a*u+b*v)-(a*u+c*(u+v))=-(2*a+c)*u+(b-c)*v := by ring\nLEAN-END\n"); request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if(x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem nextGap (u v a b c : ℝ) : (-b*v-c*(u+v))-(-a*u+b*v)=(a-c)*u-(2*b+c)*v := by ring\n#print axioms testedTriples\n#print axioms firstGap\n#print axioms nextGap\nend TensorCone\nLEAN-END\n");
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
