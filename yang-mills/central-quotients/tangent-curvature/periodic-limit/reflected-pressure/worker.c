/* Native checks of reflected Wilson blocks and independent seam noise. */
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
    unsigned cases = 0;
    for (unsigned l = 2; l <= 4; ++l) {
        unsigned side = 2*l, volume = side*side*side*side, seam = 0;
        for (unsigned site = 0; site < volume; ++site) {
            unsigned z = site, x[4];
            for (unsigned i = 0; i < 4; ++i) { x[i] = z%side; z /= side; }
            for (unsigned a = 0; a < 4; ++a) {
                unsigned on_face = 0;
                for (unsigned i = 0; i < 4; ++i)
                    if (i != a && x[i]%l == 0) on_face = 1;
                seam += on_face;
                for (unsigned b = a+1; b < 4; ++b) {
                    unsigned quarters = 0;
                    for (unsigned tile = 0; tile < 16; ++tile) {
                        unsigned share = 4;
                        for (unsigned i = 0; i < 4; ++i) {
                            unsigned t = (x[i]+side-((tile>>i)&1)*l)%side;
                            if (i == a || i == b) {
                                if (t >= l) share = 0;
                            } else if (t > l) share = 0;
                            else if (t == 0 || t == l) share /= 2;
                        }
                        quarters += share;
                    }
                    if (quarters != 4) stop(7);
                    ++cases;
                }
            }
        }
        if (seam != 4*volume-16*4*l*(l-1)*(l-1)*(l-1)) stop(7);
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nnamespace ReflectedPressure\n");
    emit("theorem faceChecks : ("); number(cases); emit(" : ℕ) = 33888 := by decide\nLEAN-END\n");
    request(1,4,3);
}

/* Quaternion units 1,i,j,k, followed by their negatives. */
static unsigned mul(unsigned a, unsigned b) {
    static const unsigned table[4][4] = {
        {0,1,2,3}, {1,4,3,6}, {2,7,4,1}, {3,2,5,4}
    };
    return table[a%4][b%4] ^ ((a^b)&4);
}
static unsigned inv(unsigned a) { return a%4 ? a^4 : a; }
static int scalar(unsigned a) { return a==0 ? 1 : (a==4 ? -1 : 0); }
static int face(const unsigned e[4]) {
    return scalar(mul(mul(e[0],e[1]),mul(inv(e[2]),inv(e[3]))));
}
static unsigned label(const unsigned x[4], unsigned dir) {
    unsigned h = 3+dir;
    for (unsigned j = 0; j < 4; ++j) h = 37*h+(j+2)*x[j]+(h>>3);
    return (h^(h>>5))%8;
}
static unsigned fold(unsigned x) { x %= 6; return x<=3 ? x : 6-x; }
static unsigned link(const unsigned x[4], unsigned dir, int folded) {
    if (!folded) return label(x,dir);
    unsigned v[4];
    for (unsigned j = 0; j < 4; ++j) v[j] = fold(x[j]);
    if (fold(x[dir]+1) > v[dir]) return label(v,dir);
    --v[dir];
    return inv(label(v,dir));
}
static int square(unsigned x[4], unsigned a, unsigned b, int folded) {
    unsigned e[4];
    e[0] = link(x,a,folded); e[3] = link(x,b,folded);
    ++x[a]; e[1] = link(x,b,folded); --x[a];
    ++x[b]; e[2] = link(x,a,folded); --x[b];
    return face(e);
}
static void child(unsigned xarg,unsigned yarg) {
    if (xarg!=4 || yarg!=3) stop(5);
    unsigned counts[3]={0};
    for (unsigned s=0; s<1296; ++s) {
        unsigned x[4], z=s;
        for (unsigned i=0; i<4; ++i) { x[i]=z%6; z/=6; }
        for (unsigned a=0; a<4; ++a) for (unsigned b=a+1; b<4; ++b) {
            unsigned v[4];
            for (unsigned i=0; i<4; ++i) {
                v[i]=fold(x[i]);
                if ((i==a || i==b) && fold(x[i]+1)<v[i]) --v[i];
            }
            int value=square(x,a,b,1);
            if (value!=square(v,a,b,0)) stop(8);
            ++counts[1+value];
        }
    }
    if (!counts[0] || !counts[1] || !counts[2]) stop(8);
    emit("LEAN-BEGIN\ntheorem foldedSquares : (");
    number(counts[0]+counts[1]+counts[2]); emit(" : ℕ) = 7776 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned xarg,unsigned yarg) {
    if (xarg!=4 || yarg!=3) stop(5);
    const unsigned noise[7]={0,1,5,2,6,3,7};
    const unsigned refs[3][4]={{1,2,1,2},{1,2,5,2},{1,2,3,2}};
    for (unsigned t=0;t<3;++t) for (unsigned mask=0;mask<16;++mask) {
        int total=0, expected=face(refs[t]);
        unsigned cases=1;
        for (unsigned j=0;j<4;++j) if (mask&(1U<<j)) { cases*=7; expected*=4; }
        for (unsigned s=0;s<cases;++s) {
            unsigned z=s, e[4]; int weight=1;
            for (unsigned j=0;j<4;++j) {
                e[j]=refs[t][j];
                if (mask&(1U<<j)) {
                    unsigned n=z%7; z/=7;
                    if (!n) weight*=4;
                    e[j]=mul(e[j],noise[n]);
                }
            }
            total += weight*face(e);
        }
        if (total!=expected) stop(9);
    }
    emit("LEAN-BEGIN\ntheorem seamPolynomial (l : ℤ) : 4*(l^3-(l-1)^3)=12*l^2-12*l+4 := by ring\n");
    emit("theorem squareLoss (a : ℤ) : 1-a^4=(1-a)*(1+a+a^2+a^3) := by ring\n");
    emit("#print axioms faceChecks\n#print axioms foldedSquares\n#print axioms seamPolynomial\n#print axioms squareLoss\nend ReflectedPressure\nLEAN-END\n");
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
