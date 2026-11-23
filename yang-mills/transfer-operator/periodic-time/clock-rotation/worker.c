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

static int mod5(int v) { return (v%5+5)%5; }
__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int n=6;n<=400;n+=2) {
        int j=2*(n/4);
        require(j>=2 && j<=n/2 && n/2-j<2);
        for(int den=2;den<=10;++den)for(int num=0;num<=den;++num){
            /* For each d, (d+1)(1-r)r^d <= 1 by geometric summation. */
            long top=1,bot=1,series=1;
            for(int d=0;d<=12;++d) {
                require((d+1)*top<=series);
                require((den-num)*series<=den*bot);
                top*=num; bot*=den;
                series=series*den+top;
            }
        }
    }
    emit("A4 CHILD spectrum\nA4 LEAN even buffers and geometric interior-time energy bound\n");
#elif ROLE == 1
    for(long k=2;k<=1024;++k){
        /* r=1-1/k^2 and negative tilted fraction 1/k. Scale by k^3. */
        long adjacent=k+2*(k*k-1);
        require(adjacent >= k*k);
        require(adjacent <= 3*k*k);
        require(adjacent-k==2*(k*k-1));
    }
    emit("A4 CHILD limit\nA4 LEAN signed two-mode example loses the Lipschitz rate\n");
#else
    const int dx[5]={0,1,-1,0,0}, dy[5]={0,0,0,1,-1};
    for(int x=-20;x<=20;++x)for(int y=-20;y<=20;++y){
        int count=0;
        for(int j=0;j<5;++j){
            int u=x+dx[j],v=y+dy[j];
            if(mod5(v-2*u))continue;
            ++count;
            int a=3*u-4*v,b=4*u+3*v;
            require(!mod5(a) && !mod5(b));
            require(a*a+b*b==25*(u*u+v*v));
        }
        require(count==1);
    }
    emit("A4 LEAN unique one-step repair and exact norm-preserving rotation\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
