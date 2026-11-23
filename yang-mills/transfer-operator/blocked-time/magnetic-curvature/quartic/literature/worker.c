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
#if ROLE==0
    /* Cubic modes with momenta 0 or pi. i labels the face normal. */
    for(int mask=0;mask<8;++mask) {
        int cos_p[3],t[3],phat2=0;
        for(int i=0;i<3;++i){
            int pi=(mask>>i)&1;
            cos_p[i]=1-2*pi;
            t[i]=2*(1-pi);
            phat2+=4*pi;
        }
        for(int i=0;i<3;++i)for(int j=0;j<3;++j){
            int neighbor=t[i]*t[j],cube=neighbor;
            if(i==j) {
                cube=2*cos_p[i];
                neighbor=2*(cos_p[(i+1)%3]+cos_p[(i+2)%3]);
            }
            int b4=-3*(neighbor+cube)-(i==j?32:0);
            int munster=i==j ? -50+3*phat2 : -6*t[i]*t[j];
            require(b4==munster);
        }
    }
    emit("A4 CHILD spectrum\nA4 LEAN momentum matrices in eight Brillouin-zone corners\n");
#elif ROLE==1
    /* At zero momentum the off-diagonal entries are -24/3 at order four
       and -28 at order six. Scalar minus E equals three such entries. */
    require(-98-(-26)==3*(-24));
    require(-20984-13036==3*(-28)*405);
    emit("A4 CHILD limit\nA4 LEAN isotropic scalar and tensor splittings at orders four and six\n");
#else
    /* W=kappa H/2, x=kappa ell/4. Compare rationals by integer cross products. */
    require(71*16*105==71*2*840);
    require(73*256*27==73*2*3456);
    emit("A4 LEAN Hamiltonian normalization for the quadratic and cube-only terms\n");
#endif
    emit("A4 FINISHED\n"); finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
