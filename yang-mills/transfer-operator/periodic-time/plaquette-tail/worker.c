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
    for(int L=4;L<=64;L*=2) {
        int row[64]={0}; row[0]=1;
        for(int span=1;span<L;span*=2) {
            int r=1-span;
            for(int t=r;t<=0;++t) {
                int old=(t+L)%L, image=(2*r-1-t+2*L)%L;
                require(row[old]==1 && row[image]==0);
                row[image]=1;
            }
        }
        for(int t=0;t<L;++t) require(row[t]==1);
        int hits[64]={0};
        for(int t=0;t<L;++t) ++hits[(t+(t%2))%L];
        for(int t=0;t<L;++t) require(hits[t]==(t%2 ? 0 : 2));
    }
    emit("A4 CHILD spectrum\nA4 LEAN dyadic slab doubling and two copies per transverse even site\n");
#elif ROLE == 1
    for(int L=4;L<=16;L*=2) {
        int counts[16][16][16][3]={0};
        for(int x=0;x<L;++x)for(int y=0;y<L;++y)for(int z=0;z<L;z+=2)
            for(int sign=-1;sign<=1;sign+=2) {
                int slab=(z+(sign<0 ? -1 : 0)+L)%L;
                ++counts[x][y][(z+sign+L)%L][0];
                ++counts[x][y][slab][1]; ++counts[x][(y+1)%L][slab][1];
                ++counts[x][y][slab][2]; ++counts[(x+1)%L][y][slab][2];
            }
        for(int x=0;x<L;++x)for(int y=0;y<L;++y)for(int z=0;z<L;++z)
            for(int j=0;j<3;++j)require(counts[x][y][z][j]==(!j && !(z%2) ? 0 : 2));
    }
    emit("A4 CHILD limit\nA4 LEAN both spatial cube shells cover each unused face in the slice twice\n");
#else
    for(long d=1;d<=10;++d)for(long b=0;b<=d;++b) {
        long num=1,den=1;
        for(int m=1;m<=4;++m) {
            num*=b; den*=d;
            require(d*(den-num)<=m*(d-b)*den);
        }
    }
    for(int L=4;L<=128;L*=2) {
        long vol=(long)L*L*L*L, seam=vol/L;
        require((4*vol-(vol-seam))-(3*vol-3*seam)==4*seam);
    }
    emit("A4 LEAN plaquette product-mean inequality and residual seam exponent\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
