/* Finite checks for the signed fixed-box SU(2) Laplace correction. */
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
static int determinant(Pauli a, Pauli b, Pauli c) {
    return a.x*(b.y*c.z-b.z*c.y)+a.y*(b.z*c.x-b.x*c.z)+a.z*(b.x*c.y-b.y*c.x);
}
static void parent(void) {
    const Pauli axes[7]={{0,0,0,0},{0,1,0,0},{0,-1,0,0},{0,0,1,0},
                         {0,0,-1,0},{0,0,0,1},{0,0,0,-1}};
    const Pauli unit={1,0,0,0};
    const int choose[4][4]={{1,0,0,0},{1,1,0,0},{1,2,1,0},{1,3,3,1}};
    unsigned tested=0;
    for (unsigned word=0; word<2401; ++word) {
        unsigned index=word;
        Pauli v[4], derivatives[4]={unit};
        for (unsigned i=0; i<4; ++i) {
            v[i]=axes[index%7]; index/=7;
            Pauli powers[4]={unit};
            for (int j=1; j<=3; ++j) powers[j]=product(powers[j-1],v[i]);
            for (int j=3; j>=0; --j) {
                Pauli value={0,0,0,0};
                for (int k=0; k<=j; ++k)
                    value=add(value,choose[j][k],product(derivatives[j-k],powers[k]));
                derivatives[j]=value;
            }
        }
        int cubic=0;
        for (unsigned i=0;i<4;++i) for (unsigned j=i+1;j<4;++j)
            for (unsigned k=j+1;k<4;++k) cubic+=determinant(v[i],v[j],v[k]);
        if (derivatives[3].s!=6*cubic) stop(7);
        ++tested;
    }
    emit("LEAN-BEGIN\nimport Mathlib.Tactic.Ring\nimport Mathlib.Data.Real.Basic\nnamespace BoxLaplace\n");
    emit("theorem signedWords : ("); number(tested); emit(" : ℕ) = 2401 := by decide\nLEAN-END\n");
    request(1,4,3);
}

static int interior(const int p[4],int n) {
    for (int i=0; i<4; ++i) if (p[i]<=-n || p[i]>=n) return 0;
    return 1;
}
static int free_edge(int p[4],int axis,int n) {
    int start=interior(p,n);
    ++p[axis]; int end=interior(p,n); --p[axis];
    return (start || end) && !(axis==0 && start);
}
/* Three positive-link coordinates of a single oriented spatial square.
   The sign of its third vector is reversed on the underlying positive link. */
static int marked(const int p[4],int axis) {
    if (p[0] || p[3]) return 0;
    return (axis==1 && !p[1] && (p[2]==0 || p[2]==1)) ||
           (axis==2 && p[1]==1 && !p[2]);
}
static void child(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    unsigned tested=0, witness=0;
    for (int n=1;n<=2;++n) for (int t=-n;t<=n;++t) for (int i=-n;i<=n;++i)
        for (int j=-n;j<=n;++j) for (int k=-n;k<=n;++k) {
            int p[4]={t,i,j,k};
            for (int a=0;a<4;++a) for (int b=a+1;b<4;++b) {
                if (p[a]==n || p[b]==n) continue;
                int free_count=free_edge(p,a,n)+free_edge(p,b,n);
                int hits=marked(p,a)+marked(p,b);
                ++p[a]; free_count+=free_edge(p,b,n); hits+=marked(p,b); --p[a];
                ++p[b]; free_count+=free_edge(p,a,n); hits+=marked(p,a); --p[b];
                if (n==1 && free_count>2) stop(8);
                if (n==2 && hits==3) {
                    if (free_count!=4) stop(8);
                    ++witness;
                }
                ++tested;
            }
        }
    if (witness!=1) stop(8);
    emit("LEAN-BEGIN\ntheorem geometryCases : ("); number(tested); emit(" : ℕ) = 2616 := by decide\nLEAN-END\n");
    request(2,4,3);
}
static void grandchild(unsigned x,unsigned y) {
    if (x!=4 || y!=3) stop(5);
    emit("LEAN-BEGIN\ntheorem normalization (h c m : ℝ) : (1-h*(c-m))*(1-h*m)-(1-h*c)=h^2*m*(c-m) := by ring\n");
    emit("theorem evenCancellation (c f : ℝ) : c*f+(-c)*f=0 := by ring\n");
    emit("#print axioms signedWords\n#print axioms geometryCases\n#print axioms normalization\n#print axioms evenCancellation\nend BoxLaplace\nLEAN-END\n");
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
