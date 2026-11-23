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

/* Vertices are 3-bit coordinates; each positive directed edge is a letter. */
static int edge(int vertex, int axis) { return 1+3*vertex+axis; }
static int stack[48], depth;
static void letter(int q) {
    if (depth && stack[depth-1]==-q) --depth;
    else stack[depth++]=q;
}
static void face(int normal, int upper, int sign) {
    int v=upper ? 1<<normal : 0, a=normal==0 ? 1 : 0, b=normal==2 ? 1 : 2;
    int word[4]={edge(v,a),edge(v+(1<<a),b),-edge(v+(1<<b),a),-edge(v,b)};
    if (upper) letter(edge(0,normal));
    for(int j=0;j<4;++j) letter(sign>0 ? word[j] : -word[3-j]);
    if (upper) letter(-edge(0,normal));
}
static int skew(int i,int j) { return (i<j)-(i>j); }

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    face(0,0,-1); face(1,1,-1); face(2,0,-1);
    face(0,1,1); face(1,0,1); face(2,1,1);
    require(depth==0);
    emit("A4 CHILD spectrum\nA4 LEAN twelve-edge cube word freely cancels\n");
#elif ROLE == 1
    int form[5][5];
    for(int i=0;i<5;++i) for(int j=0;j<5;++j) {
        form[i][j]=skew(i,j)-skew(i,5)-skew(5,j);
        require(form[i][j]==skew(i,j));
    }
    int pf=form[0][1]*form[2][3]-form[0][2]*form[1][3]+form[0][3]*form[1][2];
    require(pf==1);
    emit("A4 CHILD limit\nA4 LEAN closed-face skew form has a four-dimensional nonsingular minor\n");
#else
    /* Nodes -sqrt(3),0,sqrt(3) with integer weights 1,4,1 over 6. */
    int second=0,fourth=0;
    for(int a=-1;a<=1;++a) for(int b=-1;b<=1;++b)
    for(int c=-1;c<=1;++c) for(int d=-1;d<=1;++d) {
        int w=(a?1:4)*(b?1:4)*(c?1:4)*(d?1:4);
        int v=3*(a*d-b*c);
        second+=w*v*v;
        fourth+=w*v*v*v*v;
    }
    require(second==1296*2 && fourth==1296*24);
    emit("A4 LEAN one skew Gaussian block has variance two and fourth moment twenty-four\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
