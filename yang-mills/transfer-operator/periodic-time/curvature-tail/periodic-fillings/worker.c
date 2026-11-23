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

/* Permutations provide a finite noncommutative control on based square swaps. */
typedef struct { int p[3]; } Perm;
static const Perm group[6]={{{0,1,2}},{{0,2,1}},{{1,0,2}},{{1,2,0}},{{2,0,1}},{{2,1,0}}};
static Perm prod(Perm a,Perm b) {
    Perm c;
    for(int i=0;i<3;++i)c.p[i]=a.p[b.p[i]];
    return c;
}
static Perm inverse(Perm a) {
    Perm b;
    for(int i=0;i<3;++i)b.p[a.p[i]]=i;
    return b;
}
static int equal(Perm a,Perm b) {
    return a.p[0]==b.p[0] && a.p[1]==b.p[1];
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for(int L=1;L<=8;++L) {
        int counts=0, v=L*L*L*L;
        for(int site=0;site<v;++site) {
            int q=site, x[4];
            for(int i=0;i<4;++i){ x[i]=q%L; q/=L; }
            for(int i=0;i<4;++i) for(int j=0;j<4;++j) {
                if(j>i) counts+=x[j];
                if(j<i && x[i]==L-1) counts+=L*x[j];
            }
        }
        require(counts==6*v*(L-1));
    }
    emit("A4 CHILD spectrum\nA4 LEAN total chord filling area for all sites through side eight\n");
#elif ROLE == 1
    int wrong_order=0;
    for(int k=0;k<6;++k) for(int p=0;p<6;++p)
    for(int q=0;q<6;++q) for(int s=0;s<6;++s) {
        Perm a=group[p], b=group[q], prefix=group[k], suffix=group[s];
        Perm old=prod(prod(prefix,a),suffix), next=prod(prod(prefix,b),suffix);
        Perm face=prod(a,inverse(b));
        Perm ratio=prod(old,inverse(next));
        require(equal(ratio,prod(prod(prefix,face),inverse(prefix))));
        if(!equal(ratio,face)) ++wrong_order;
    }
    require(wrong_order>0);
    emit("A4 CHILD limit\nA4 LEAN based square transport on 1296 permutation assignments\n");
#else
    for(int L=1;L<=16;++L) {
        int double_wrap=0, off_axis_wrap=0, spine_faces=0;
        int v=L*L*L*L;
        for(int site=0;site<v;++site) {
            int x[4],q=site;
            for(int i=0;i<4;++i){x[i]=q%L;q/=L;}
            if(x[0]==L-1 && x[1]==L-1) ++double_wrap;
            if(x[3]==L-1 && (x[0]||x[1]||x[2])) ++off_axis_wrap;
            for(int j=0;j<3;++j) {
                int here=(x[0]==0 && x[1]==0 && x[2]==0);
                int next=1;
                for(int i=0;i<3;++i) if((x[i]+(i==j))%L) next=0;
                if(here!=next) ++spine_faces;
            }
        }
        require(double_wrap==L*L && off_axis_wrap==L*L*L-1);
        require(spine_faces==(L==1 ? 0 : 6*L));
    }
    emit("A4 LEAN double-wrap multiplicities and isolated-cycle action counts\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
