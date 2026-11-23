/* Schwartz weights, ordered chambers and independent axial spin chains. */
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
    unsigned n=0;
    for (unsigned a=0;a<=8;++a) for (unsigned b=a;b<=8;++b)
        for (unsigned c=b;c<=8;++c) {
            if (!(0<a+1 && a+1<b+2 && b+2<c+3)) stop(7);
            ++n;
        }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace WeakOS\n");
    emit("theorem chamberCount : (");number(n);emit(" : ℕ) = 165 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned n=0;
    for(unsigned a=0;a<81;++a) for(unsigned b=0;b<81;++b) {
        unsigned i=a,j=b,hamming=0;
        for(unsigned axis=0;axis<4;++axis){hamming+=(i%3!=j%3);i/=3;j/=3;}
        if(hamming<=1) ++n;
    }
    emit("LEAN-BEGIN\ntheorem supportedPairs : (");number(n);emit(" : ℕ) = 729 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if(x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem weightDifference (r : ℝ) : 2*(1+r^2)-(1+r)^2=(r-1)^2 := by ring\n");
    emit("theorem chainMode (p : ℝ) : (1+p)/2-(1-p)/2=p := by ring\n");
    emit("#print axioms chamberCount\n#print axioms supportedPairs\n#print axioms weightDifference\n#print axioms chainMode\nend WeakOS\nLEAN-END\n");
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
