/* Tree-level trace normalization and free-field four-point controls. */
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
    unsigned coefficient = 0;
    for (unsigned a = 0; a < 4; ++a)
        for (unsigned b = a + 1; b < 4; ++b)
            coefficient += 2 * 2 * 2;
    emit("LEAN-BEGIN\nimport Mathlib.Data.Real.Basic\nimport Mathlib.Tactic.Ring\nnamespace ShortDistance\n");
    emit("theorem maxwellCoefficient : ("); number(coefficient);
    emit(" : ℕ) = 48 := by decide\nLEAN-END\n");
    request(1, 4, 3);
}

/* Every tetrahedral edge has squared length eight. Its unit-normal
   reflection interchanges two signed axes and fixes the other two. */
static const int vertices[4][4] = {
    {1,1,1,0},{1,-1,-1,0},{-1,1,-1,0},{-1,-1,1,0}
};

static int cycle_trace(const unsigned order[4]) {
    int matrix[4][4] = {{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};
    for (unsigned h=0; h<4; ++h) {
        int edge[4];
        for (unsigned a=0; a<4; ++a)
            edge[a]=vertices[order[h]][a]-vertices[order[(h+1)%4]][a];
        for (unsigned col=0; col<4; ++col) {
            int dot=0;
            for (unsigned a=0; a<4; ++a) dot+=edge[a]*matrix[a][col];
            for (unsigned a=0; a<4; ++a) matrix[a][col]-=edge[a]*dot/4;
        }
    }
    int trace=0;
    for (unsigned a=0; a<4; ++a)
        for (unsigned b=a+1; b<4; ++b)
            trace+=matrix[a][a]*matrix[b][b]-matrix[a][b]*matrix[b][a];
    return trace;
}

static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned count=0;
    for (unsigned a=1; a<4; ++a)
        for (unsigned b=1; b<4; ++b)
            for (unsigned c=1; c<4; ++c) {
                if (a==b || b==c || a==c) continue;
                unsigned order[4]={0,a,b,c};
                if (cycle_trace(order)!=0) stop(8);
                ++count;
            }
    emit("LEAN-BEGIN\ntheorem vanishingCyclesCount : ("); number(count);
    emit(" : ℕ) = 6 := by decide\nLEAN-END\n");
    request(2,4,3);
}

static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem triangleCorrection (g h : ℝ) : (g+h)^3-g^3=3*g^2*h+3*g*h^2+h^3 := by ring\n");
    emit("theorem twoSpecies (a b : ℝ) : 2*(a^4+b^4)-(a^2+b^2)^2=(a^2-b^2)^2 := by ring\n");
    emit("#print axioms maxwellCoefficient\n#print axioms vanishingCyclesCount\n#print axioms triangleCorrection\n#print axioms twoSpecies\nend ShortDistance\nLEAN-END\n");
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
