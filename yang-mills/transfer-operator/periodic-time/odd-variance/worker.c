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
/* A ternary location per axis denotes the left boundary, interior, or right
   boundary. The sign uses parity of all four corner bits. */
static int weight(int pattern,int corner) {
    int inside=1, shifted=1;
    for(int axis=0;axis<4;++axis) {
        int region=pattern%3, bit=(corner>>axis)&1;
        pattern/=3;
        inside &= region!=0;
        shifted &= region==1 || (region==0 && bit==1) || (region==2 && bit==0);
    }
    return shifted-inside;
}
#elif ROLE == 2
static int tent(int h,int i) {
    if(i<0 || i>=h) return 0;
    return i+1<h-i ? i+1 : h-i;
}
#endif
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    int allowed=0, rejected=0;
    for(int pattern=0;pattern<81;++pattern) for(int corner=0;corner<16;++corner) {
        int regions=pattern;
        for(int i=0;i<4;++i) {
            int same=weight(pattern,corner)==weight(pattern,corner^(1<<i));
            if(regions%3==1) {require(same); ++allowed;}
            else if(!same) ++rejected;
            regions/=3;
        }
    }
    require(allowed==1728 && rejected>0);
    emit("A4 CHILD spectrum\nA4 LEAN every interior-axis corner toggle preserves its boundary coefficient\n");
#elif ROLE == 1
    for(int k=1;k<=128;++k) {
        int plane=k+1;
        require(2*plane-2==2*k && 2*plane==2*k+2);
        require(2<=plane && plane<=2*k);
        for(int c=0;c<=1;++c) for(int y=0;y<=1;++y)
            require(2*plane-(y+c)==(2*plane-y-1)+(1-c));
    }
    emit("A4 CHILD limit\nA4 LEAN separated side-two slabs and adjacent shared site planes\n");
#else
    /* Integer taper permits exact autocorrelation and translation-norm checks. */
    for(int h=2;h<=40;++h) {
        long norm=0, next=0;
        for(int i=0;i<h;++i) {
            norm+=tent(h,i)*tent(h,i);
            next+=tent(h,i)*tent(h,i+1);
        }
        long box=h*norm;
        for(int k=1;k<=h;++k) {
            long ac=0;
            for(int i=0;i<h;++i) ac+=tent(h,i)*tent(h,i+k);
            require(norm-ac<=k*k*(norm-next));
            require((box-k)*norm>=box*ac);
        }
    }
    emit("A4 LEAN exact taper translation costs and dominating box correlations\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
