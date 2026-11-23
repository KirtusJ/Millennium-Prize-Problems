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

/* Arithmetic on F4=F2[w]/(w^2+w+1), with w encoded as 2. */
static unsigned field(unsigned a,unsigned b) {
    unsigned w=a<<1;
    if(w&4)w^=7;
    return ((b&1)?a:0)^((b&2)?w:0);
}
static unsigned group(unsigned x,unsigned y) {
    return x^y^(field(x&3,(y>>2)&3)<<4);
}
static unsigned twist(unsigned x) {
    return x^(field(x&3,x&3)<<4);
}
static unsigned conjugate(unsigned x,unsigned g) {
    unsigned inverse=g^(field(g&3,(g>>2)&3)<<4);
    return group(group(g,x),inverse);
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    /* Two-dimensional side-two torus: enumerate all 8 binary links. */
    int counts[16]={0};
    for(unsigned u=0;u<256;++u) {
        unsigned f=0;
        for(unsigned v=0;v<4;++v) {
            unsigned edges=(1u<<(2*v))^(1u<<(2*(v^1)+1))^
                (1u<<(2*(v^2)))^(1u<<(2*v+1));
            unsigned bits=u&edges,parity=0;
            while(bits){parity^=1;bits&=bits-1;}
            f|=parity<<v;
        }
        ++counts[f];
    }
    for(unsigned f=0;f<16;++f) {
        unsigned bits=f,parity=0;
        while(bits){parity^=1;bits&=bits-1;}
        require(counts[f]==(parity ? 0 : 32));
    }
    emit("A4 CHILD spectrum\nA4 LEAN equal curl fibres and exact zero period on the binary two-torus\n");
#elif ROLE==1
    for(unsigned x=0;x<64;++x) {
        int found=0;
        require(twist(twist(x))==x);
        for(unsigned y=0;y<64;++y) {
            require(twist(group(x,y))==group(twist(x),twist(y)));
            if(conjugate(x,y)==twist(x))found=1;
        }
        require(found);
    }
    emit("A4 CHILD limit\nA4 LEAN central twist preserves multiplication and the conjugacy class of each of 64 elements\n");
#else
    for(unsigned g=0;g<64;++g)
        require(conjugate(1,g)!=twist(1) || conjugate(2,g)!=twist(2));
    emit("A4 LEAN two based holonomies admit no common conjugator to their twisted pair\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
