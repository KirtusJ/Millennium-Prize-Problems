/* One-site frozen-link Wilson form and transverse walk moments. */
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






typedef long long integer;
struct quat { int w,x,y,z; };
static void average(struct quat g, int a, int b, int c, unsigned weight,
                    integer *linear, integer *quadratic) {
    /* Multiply g by the unnormalized quaternion (9,4a,4b,4c). */
    integer den=g.w*g.w+g.x*g.x+g.y*g.y+g.z*g.z;
    integer y=9*g.y+4*(g.w*b+g.z*a-g.x*c);
    integer z=9*g.z+4*(g.w*c+g.x*b-g.y*a);
    integer t=y*y+z*z, norm=225*den;
    *linear+=weight*(2*t-norm);
    *quadratic+=weight*(6*t*t-6*t*norm+norm*norm);
}
static void parent(void) {
    const struct quat inputs[]={{1,0,0,0},{0,0,1,0},{1,1,1,1},{3,4,0,0},
                               {0,3,0,4},{1,-2,3,-1},{-2,1,-3,2}};
    unsigned checks=0;
    for (unsigned i=0;i<sizeof(inputs)/sizeof(inputs[0]);++i) {
        struct quat g=inputs[i];
        integer linear=0,quadratic=0;
        for (int k=0;k<3;++k) {
            for (int sign=-1;sign<=1;sign+=2) {
                int a[3]={0}; a[k]=3*sign;
                average(g,a[0],a[1],a[2],52,&linear,&quadratic);
            }
            for (int mask=0;mask<8;++mask) {
                int a[3];
                for (int j=0;j<3;++j) a[j]=(j==k?1:2)*((mask&(1<<j))?-1:1);
                average(g,a[0],a[1],a[2],27,&linear,&quadratic);
            }
        }
        integer norm=g.w*g.w+g.x*g.x+g.y*g.y+g.z*g.z;
        integer t=g.y*g.y+g.z*g.z;
        if (75*linear!=11*960*225*(2*t-norm)) stop(7);
        if (3125*quadratic!=-779LL*960*225*225*(6*t*t-6*t*norm+norm*norm)) stop(7);
        checks+=2;
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace OneSiteFiber\n");
    emit("theorem angularChecks : ("); number(checks); emit(" : ℕ) = 14 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    /* r=k/128. Check the two competing block lengths by cross multiplication. */
    unsigned checks=0;
    for (unsigned beta=16;beta<=128;++beta) for (unsigned k=1;k<=128;++k) {
        unsigned m=128/k;
        if (beta/8<m) m=beta/8;
        if (!m || 8*m>beta || m*k>128) stop(8);
        if (beta*k<=128) { if (16*m<beta) stop(8); }
        else if (16*m*k<128) stop(8);
        ++checks;
    }
    emit("LEAN-BEGIN\ntheorem blockChecks : ("); number(checks); emit(" : ℕ) = 14464 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem fourthIncrement (t a b : ℝ) : (1/3+a*(2*t-1)/2+b*(6*t^2-6*t+1)/6)=b*t^2+(a-b)*t+(2-3*a+b)/6 := by ring\n");
    emit("theorem fourthInduction (t s v : ℝ) : t^2+8*s*v*t+8*(s*v)^2+8*v*(t+2*s*v)+8*v^2=t^2+8*((s+1)*v)*t+8*((s+1)*v)^2 := by ring\n");
    emit("#print axioms angularChecks\n#print axioms blockChecks\n#print axioms fourthIncrement\n#print axioms fourthInduction\nend OneSiteFiber\nLEAN-END\n");
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
