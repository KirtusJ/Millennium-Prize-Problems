/* One-cube controls for weak convergence of conditional curvature laws. */
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





typedef struct {int s,x,y,z;} Pauli;

/* In the basis I, i sigma_1, i sigma_2, i sigma_3 the vector term
   in a product uses minus the ordinary cross product. */
static Pauli product(Pauli a, Pauli b) {
    return (Pauli){a.s*b.s-a.x*b.x-a.y*b.y-a.z*b.z,
        a.s*b.x+b.s*a.x-a.y*b.z+a.z*b.y,
        a.s*b.y+b.s*a.y-a.z*b.x+a.x*b.z,
        a.s*b.z+b.s*a.z-a.x*b.y+a.y*b.x};
}
static Pauli add(Pauli a, int w, Pauli b) {
    return (Pauli){a.s+w*b.s,a.x+w*b.x,a.y+w*b.y,a.z+w*b.z};
}

static const Pauli axes[6]={
    {0,1,0,0},{0,-1,0,0},{0,0,1,0},{0,0,-1,0},{0,0,0,1},{0,0,0,-1}};
static const Pauli one={1,0,0,0}, zero={0,0,0,0};
static Pauli inverse(Pauli a) { return (Pauli){a.s,-a.x,-a.y,-a.z}; }
static int same(Pauli a, Pauli b) {
    return a.s==b.s && a.x==b.x && a.y==b.y && a.z==b.z;
}
/* (23,13,12) bottom faces followed by corresponding opposite faces.
   Axes are bits 1,2,4, vertices their bitsets. */
static const unsigned first[3]={1,0,0}, second[3]={2,2,1};
static const unsigned shift[3]={1,2,4};
static const int sign[6]={-1,1,-1,1,-1,1};
static Pauli cube_sum(Pauli links[8][3],int linear) {
    Pauli sum=zero;
    for (unsigned f=0; f<6; ++f) {
        unsigned j=f%3, v=f<3?0:shift[j], a=first[j], b=second[j];
        Pauli m=links[v][a], n=links[v|(1U<<a)][b];
        Pauli p=links[v|(1U<<b)][a], q=links[v][b];
        Pauli face;
        if (linear) face=add(add(add(m,1,n),-1,p),-1,q);
        else {
            Pauli u=product(product(product(m,n),inverse(p)),inverse(q));
            if (u.s<0) stop(9); /* principal log is only used at I or a quarter turn */
            face=(Pauli){0,u.x,u.y,u.z};
        }
        sum=add(sum,sign[f],face);
    }
    return sum;
}
static void parent(void) {
    unsigned tested=0;
    for (unsigned i=0; i<6; ++i) for (unsigned j=0; j<6; ++j) {
        if (i/2==j/2) continue;
        Pauli links[8][3];
        for (unsigned v=0;v<8;++v) for (unsigned a=0;a<3;++a) links[v][a]=one;
        links[0][0]=axes[i]; links[0][1]=axes[j];
        Pauli actual=cube_sum(links,0);
        Pauli expected=add(add(axes[i],-1,axes[j]),-1,product(axes[i],inverse(axes[j])));
        if (!same(actual,expected) || actual.x*actual.x+actual.y*actual.y+actual.z*actual.z!=3) stop(7);
        ++tested;
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace CurvatureKernel\n");
    emit("theorem noncommutingWitnesses : ("); number(tested); emit(" : ℕ) = 24 := by decide\nLEAN-END\n");
    request(1,4,3);
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned tested=0;
    for (unsigned v=0;v<8;++v) for (unsigned a=0;a<3;++a) {
        if (v&(1U<<a)) continue;
        for (unsigned j=0;j<6;++j) {
            Pauli linear[8][3]={0};
            linear[v][a]=axes[j];
            if (!same(cube_sum(linear,1),zero)) stop(8);
            ++tested;
        }
    }
    emit("LEAN-BEGIN\ntheorem linearCoboundaries : ("); number(tested); emit(" : ℕ) = 72 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem twoEdgeDefect (u v c h : ℝ) : -v+u-(u-v+h*c)= -h*c := by ring\n");
    emit("theorem resampling (p : ℝ) : p-p*p=p*(1-p) := by ring\n");
    emit("#print axioms noncommutingWitnesses\n#print axioms linearCoboundaries\n#print axioms twoEdgeDefect\n#print axioms resampling\nend CurvatureKernel\nLEAN-END\n");
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
