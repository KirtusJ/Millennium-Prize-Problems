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

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    /* A reversible test kernel with positive eigenvector. T times (1,2,3)
       equals 12 times (1,2,3); use integer units throughout. */
    int kernel[3][3]={{4,1,2},{1,10,1},{2,1,0}};
    /* Third diagonal makes the last row sum to 36 after weighting.
       Use three times this kernel to keep that entry integral. */
    for(int i=0;i<3;++i) for(int j=0;j<3;++j) kernel[i][j]*=3;
    kernel[2][2]=32;
    for(int code=0;code<125;++code) {
        int v=code, w[3];
        for(int i=0;i<3;++i) { w[i]=v%5-2; v/=5; }
        int lhs=0, rhs=0;
        for(int i=0;i<3;++i) {
            int f=i+1;
            lhs+=36*f*f*w[i]*w[i];
            for(int j=0;j<3;++j) {
                int edge=kernel[i][j]*f*(j+1);
                lhs-=edge*w[i]*w[j];
                rhs+=edge*(w[i]-w[j])*(w[i]-w[j]);
            }
        }
        require(2*lhs==rhs);
    }
    emit("A4 CHILD spectrum\nA4 LEAN Weighted ground-state identity for signed and positive trial factors\n");
#elif ROLE == 1
    /* Circle section in units of pi/24. Centers at 0 and 24. */
    for(int i=0;i<48;++i) for(int j=0;j<48;++j) {
        int si=(i<12 || i>=36), sj=(j<12 || j>=36);
        int jump=i>j ? i-j : j-i;
        if(jump>24) jump=48-jump;
        if(si!=sj && jump<=4) {
            int ti=i%24, tj=j%24;
            if(ti>12) ti=24-ti;
            if(tj>12) tj=24-tj;
            require(ti>=8 && tj>=8);
        }
    }
    emit("A4 CHILD limit\nA4 LEAN Short jumps that change a center sign meet the exterior band\n");
#else
    int multiplicity[4]={0};
    for(int p=1;p<8;++p) {
        int v[3]={2*(p&1),2*((p>>1)&1),2*((p>>2)&1)};
        int s=0;
        for(int i=0;i<3;++i) s+=v[i]*v[i];
        int trace=0, mat[3][3];
        for(int i=0;i<3;++i) for(int j=0;j<3;++j)
            mat[i][j]=(i==j ? s : 0)-v[i]*v[j];
        for(int i=0;i<3;++i) {
            trace+=mat[i][i];
            for(int j=0;j<3;++j) {
                int x=0;
                for(int l=0;l<3;++l) x+=mat[i][l]*mat[l][j];
                require(x==s*mat[i][j]);
            }
        }
        require(trace==2*s);
        multiplicity[s/4]+=3*trace/s;
    }
    require(multiplicity[1]==18 && multiplicity[2]==18 && multiplicity[3]==6);
    emit("A4 LEAN Two-site-per-axis curl spectrum has 42 transverse color modes\n");
#endif
    emit("A4 FINISHED\n"); finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
