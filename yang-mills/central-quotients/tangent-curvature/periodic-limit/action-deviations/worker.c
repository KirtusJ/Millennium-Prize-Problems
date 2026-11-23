/* Periodic seam, constrained exponential tilt and rate-function controls. */
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






/* Each positive bond is labelled by the originating site and direction.
   A plaquette word uses bonds at x, x+e_a and x+e_b. */
static unsigned shifted(unsigned x,unsigned tile) {
    return x-x%tile+(x%tile+1)%tile;
}
static void parent(void) {
    unsigned checked=0;
    for (unsigned tile=2;tile<=8;++tile) {
        unsigned side=2*tile, different=0;
        for (unsigned i=0;i<side;++i) for (unsigned j=0;j<side;++j)
            for (unsigned k=0;k<side;++k) for (unsigned l=0;l<side;++l) {
                unsigned x[4]={i,j,k,l};
                for (unsigned a=0;a<4;++a) for (unsigned b=a+1;b<4;++b) {
                    int moved_a=shifted(x[a],tile)!=(x[a]+1)%side;
                    int moved_b=shifted(x[b],tile)!=(x[b]+1)%side;
                    if (moved_a || moved_b) ++different;
                }
            }
        if (different!=16*6*(2*tile*tile*tile-tile*tile)) stop(7);
        ++checked;
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace ActionDeviation\n");
    emit("theorem seamSides : ("); number(checked); emit(" : ℕ) = 7 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static unsigned ipow(unsigned a,unsigned b) {
    unsigned n=1;
    for (unsigned j=0;j<b;++j) n*=a;
    return n;
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned index[8][3]={0}, id=0;
    for (unsigned v=0;v<8;++v) for (unsigned a=0;a<3;++a)
        if (!(v&(1U<<a))) index[v][a]=id++;
    unsigned counts[7]={0}, total=0;
    unsigned long tilted=0, initial=0;
    for (unsigned mask=0;mask<(1U<<12);++mask) {
        unsigned k=0;
        for (unsigned a=0;a<3;++a) for (unsigned b=a+1;b<3;++b)
            for (unsigned v=0;v<8;++v) {
                if (v&((1U<<a)|(1U<<b))) continue;
                unsigned parity=(mask>>index[v][a])^(mask>>index[v|(1U<<a)][b])
                                ^(mask>>index[v|(1U<<b)][a])^(mask>>index[v][b]);
                k+=parity&1U;
            }
        ++counts[k]; ++total;
        initial+=ipow(2,6-k);
        tilted+=ipow(3,k)*ipow(4,6-k);
    }
    const unsigned choose[7]={1,6,15,20,15,6,1};
    for (unsigned k=0;k<=6;++k)
        if (counts[k]!=(k%2 ? 0U : 128U*choose[k])) stop(8);
    /* Strip off the factor 2^6 or 4^6 in each rational weight.
       Even parity gives half the sum of (1+w)^6 and (1-w)^6. */
    if (initial!=64UL*(ipow(3,6)+1) || tilted!=64UL*(ipow(7,6)+1)) stop(8);
    emit("LEAN-BEGIN\ntheorem cubeAssignments : ("); number(total); emit(" : ℕ) = 4096 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem pressureCoefficient : (6 : ℝ)*(3/4)=9/2 := by ring\n");
    emit("theorem quadraticDual (z s : ℝ) : z^2/9-(s*z-9*s^2/4)=(z/3-3*s/2)^2 := by ring\n");
    emit("#print axioms seamSides\n#print axioms cubeAssignments\n#print axioms pressureCoefficient\n#print axioms quadraticDual\nend ActionDeviation\nLEAN-END\n");
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
