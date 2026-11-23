/* Principal-angle branches and the orthogonal frame of a weighted circle. */
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
    /* Count principal pairs in Z/32 and retain their exact winding. */
    unsigned total=0;
    for(int k=1;k<=32;++k) for(int x=-16;x<16;++x) {
        int y=(k*x+16)%32;
        if(y<0) y+=32;
        y-=16;
        int shift=k*x-y;
        if(shift%32 || y < -16 || y >= 16) stop(7);
        ++total;
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace WindingCircle\n");
    emit("theorem branchCases : (");number(total);emit(" : ℕ) = 1024 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static void child(unsigned a,unsigned b) {
    if(a!=4 || b!=3) stop(5);
    unsigned total=0;
    for(int k=1;k<=8;++k) for(int x=-6;x<=6;++x) for(int y=-6;y<=6;++y) {
        int q=x+k*y, z=k*x-y;
        if(q*q+z*z != (1+k*k)*(x*x+y*y)) stop(8);
        ++total;
    }
    emit("LEAN-BEGIN\ntheorem frameCases : (");number(total);emit(" : ℕ) = 1352 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned a,unsigned b) {
    if(a!=4 || b!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem orthogonalFrame (x y k : ℝ) : (x+k*y)^2+(k*x-y)^2=(1+k^2)*(x^2+y^2) := by ring\n");
    emit("theorem inverseFirst (x y k : ℝ) : (x+k*y)+k*(k*x-y)=(1+k^2)*x := by ring\n");
    emit("#print axioms branchCases\n#print axioms frameCases\n#print axioms orthogonalFrame\n#print axioms inverseFirst\nend WindingCircle\nLEAN-END\n");
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
