/* Exact finite controls. Each guest issues the next role through the shared runner. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;

static long syscall3(long nr, long a, long b, long c) {
    long out;
    __asm__ volatile("syscall" : "=a"(out) : "a"(nr), "D"(a), "S"(b), "d"(c)
                     : "rcx", "r11", "memory");
    return out;
}

static __attribute__((noreturn)) void finish(int result) {
    syscall3(60, result, 0, 0);
    __builtin_unreachable();
}

static void require(int condition) {
    if (!condition) finish(1);
}

static void emit(const char *str) {
    int len = 0;
    while (str[len]) ++len;
    while (len > 0) {
        long wrote = syscall3(1, 1, (long)str, len);
        require(wrote > 0 && wrote <= len);
        str += wrote;
        len -= wrote;
    }
}

#if ROLE == 0
/* Six affine permutations of Z/3, with the negative sign encoded by 3..5. */
static int mul(int a, int b) {
    return ((a%3 + (a<3 ? b%3 : 3-b%3))%3) + 3*((a/3)^(b/3));
}
static int inverse(int a) { return a<3 ? (3-a)%3 : a; }
static int conjugate(int a, int b) { return mul(mul(a,b),inverse(a)); }
static void check_orbit(int bridge, int p, int q) {
    int shell[36]={0}, rooted[36]={0}, pairs[216]={0};
    for (int gb=0; gb<6; ++gb) {
        int end_p=conjugate(gb,p), end_q=conjugate(gb,q);
        for (int go=0; go<6; ++go) {
            int v=mul(mul(go,bridge),inverse(gb));
            int a=conjugate(v,end_p), b=conjugate(v,end_q);
            ++shell[6*end_p+end_q]; ++rooted[6*a+b];
            ++pairs[36*v+6*end_p+end_q];
        }
    }
    for (int word=0; word<36; ++word) {
        require(shell[word] == rooted[word]);
        for (int v=0; v<6; ++v) require(6*pairs[36*v+word] == shell[word]);
    }
}
#elif ROLE == 1
/* Radius-one curl Gram on the eight signed axes. Off-diagonal entries connect
   different axes. For each face test, solve the dual equation with denominator 48. */
static void check_diagonal(int a, int b) {
    int u[8]={0}, x[8]={0};
    u[a]=1; u[b]=-1;
    for (int j=0; j<8; ++j) x[j]=3*(u[j]+u[j^1])+4*(u[j]-u[j^1]);
    for (int j=0; j<8; ++j) {
        int laplacian=0;
        for (int k=0; k<8; ++k) if ((k/2)!=(j/2)) laplacian+=x[j]-x[k];
        require(laplacian==48*u[j]);
    }
    require(x[a]-x[b]==14);
}
#else
/* Three-point quadrature with weights 1,4,1 has the Gaussian second and
   fourth moments at variance 1/3. S = (aZ + bY)^2, before the action factor 1/2. */
static void check_conditional(int a, int b) {
    int ws[3]={1,4,1};
    long first=0, second=0;
    for (int i=0; i<3; ++i) {
        long conditional_times_six=0;
        for (int j=0; j<3; ++j) {
            int total=a*(i-1)+b*(j-1);
            conditional_times_six+=ws[j]*total*total;
        }
        first+=ws[i]*conditional_times_six;
        second+=ws[i]*conditional_times_six*conditional_times_six;
    }
    /* Var(E[S|Z]) = 2 (a^2/3)^2, with common denominator 6^4. */
    require(6*second-first*first == 288L*a*a*a*a);
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int v=0; v<6; ++v) for (int p=0; p<6; ++p)
        for (int q=0; q<6; ++q) check_orbit(v,p,q);
    require(mul(1,3)!=mul(3,1));
    emit("A4 CHILD spectrum\nA4 LEAN 216 two-lasso orbits preserve joint law and open-bridge independence\n");
#elif ROLE == 1
    int count=0;
    for (int a=0; a<8; ++a) for (int b=0; b<8; ++b)
        if (a/2!=b/2) { check_diagonal(a,b); ++count; }
    require(count==48);
    emit("A4 CHILD limit\nA4 LEAN 48 oriented central faces give the radius-one diagonal 7/24\n");
#else
    for (int a=0; a<=6; ++a) for (int b=0; b<=6; ++b) check_conditional(a,b);
    emit("A4 LEAN 49 exact conditional fourth-moment controls for the quadratic action\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
