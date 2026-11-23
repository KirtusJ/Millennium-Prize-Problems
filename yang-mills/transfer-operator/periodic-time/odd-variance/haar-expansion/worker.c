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
static void quaternion(int n, int q[4]) {
    for(int j=0;j<4;++j)
        q[j]=n<8 ? (j==n/2 ? (n%2?2:-2) : 0) : (((n-8)>>j)&1 ? 1 : -1);
}
#elif ROLE == 1
static int point(int i) { return 1<<(2*i); }
static int make_face(int base,int i,int j) {
    return 16*base+4*(i<j?i:j)+(i<j?j:i);
}
#endif
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    int norm=0, mixed=0, trace2=0, trace4=0;
    for(int i=0;i<24;++i) {
        int u[4]; quaternion(i,u);
        trace2+=u[0]*u[0]; trace4+=u[0]*u[0]*u[0]*u[0];
        for(int j=0;j<24;++j) {
            int v[4]; quaternion(j,v);
            int dot=u[1]*v[1]+u[2]*v[2]+u[3]*v[3];
            norm+=dot*dot; mixed+=dot*dot*u[0]*u[0];
        }
    }
    require(trace2==24 && trace4==48);
    require(norm==576*3 && mixed==576*2);
    require(mixed-norm*trace2/24==-576);
    emit("A4 CHILD spectrum\nA4 LEAN spherical Haar moments and the negative connected face insertion\n");
#elif ROLE == 1
    int faces[48], count=0;
    int origin=85; /* coordinates (1,1,1,1) in base four */
    for(int i=0;i<4;++i) {
        int pair=i^1;
        for(int offset=0;offset<2;++offset) for(int j=0;j<4;++j) {
            if(j==i) continue;
            for(int sign=0;sign<2;++sign) {
                int face=make_face(origin+offset*point(pair)-sign*point(j),i,j);
                int found=0;
                for(int k=0;k<count;++k) found|=faces[k]==face;
                if(!found) faces[count++]=face;
            }
        }
    }
    require(count==38);
    emit("A4 CHILD limit\nA4 LEAN exact conditional neighborhood of the eight selected links\n");
#else
    /* On a cycle, no walk of length below four reaches a site at graph
       distance four or more; all length-n walks have total count 2^n. */
    int old[18]={1};
    for(int n=0;n<=12;++n) {
        int next[18], total=0;
        for(int j=0;j<18;++j) {
            if(n<4 && j>=4 && j<=14) require(old[j]==0);
            total+=old[j];
            next[j]=old[(j+1)%18]+old[(j+17)%18];
        }
        require(total==(1<<n));
        for(int j=0;j<18;++j) old[j]=next[j];
    }
    emit("A4 LEAN influence-path distance and total row mass on a periodic graph\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
