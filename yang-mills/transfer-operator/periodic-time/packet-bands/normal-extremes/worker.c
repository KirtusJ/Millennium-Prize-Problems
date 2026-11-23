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

static int choose(int n,int k) {
    int v=1;
    for(int i=1;i<=k;++i) v=v*(n-i+1)/i;
    return v;
}
#if ROLE == 0
/* Numerator of S^(d)(x/2) with denominator 2^(7-d) (7-d)! for d=0,2. */
static long spline(int x,int d) {
    long sum=0;
    for(int j=0;j<=8;++j) {
        int base=8-x-2*j;
        if(base<=0) continue;
        long p=1;
        for(int i=0;i<7-d;++i) p*=base;
        sum+=(j%2?-1:1)*choose(8,j)*p;
    }
    return sum;
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    require(spline(0,0)*315==151L*128*5040 && spline(0,2)*3==-2L*32*120);
    require(spline(1,0)==259723 && spline(1,2)*768==-289L*32*120);
    require(spline(2,0)*1680==397L*128*5040 && spline(2,2)*8==32*120);
    require(spline(9,0)==0 && spline(9,2)==0);
    long numerator=spline(2,2)*spline(1,0)+spline(2,0)*spline(1,2);
    long denominator=2*spline(0,2)*spline(0,0);
    require(numerator*9895936L==denominator*597627L);
    emit("A4 CHILD spectrum\nA4 LEAN exact transverse characteristic mark 597627/9895936 and exterior zero\n");
#elif ROLE == 1
    /* Soft states have matched unit transverse and normal signs. A hard state
       has normal momentum +/-25 and independent transverse mark 0 or 2. */
    for(int n=2;n<=6;n+=2) {
        int hist[2][25]={{0}};
        for(int at=0;at<n;++at) for(int code=0;code<(1<<(n-1));++code)
            for(int sign=0;sign<2;++sign) for(int mark=0;mark<2;++mark) {
                int p=0,z=0,bits=code;
                for(int i=0;i<n;++i) {
                    if(i==at){p+=2*mark; z+=sign?25:-25;}
                    else {int s=(bits&1)?1:-1;bits>>=1;p+=s;z+=s;}
                }
                require(z>12 || z< -12);
                ++hist[z>0][p+10];
            }
        for(int k=0;k<25;++k) {
            int total=0;
            for(int j=0;j<n;++j) for(int mark=0;mark<2;++mark)
                if(2*j-(n-1)+2*mark+10==k) total+=n*choose(n-1,j);
            require(hist[0][k]==total && hist[1][k]==total);
        }
    }
    emit("A4 CHILD limit\nA4 LEAN signed exceptional leg and unscaled spectator convolution at orders 2 4 6\n");
#else
    /* w_j apart from its common factor and z^j is (2j+1) C(2j,j)/4^j.
       Marking a leg gives the shifted negative-binomial recurrence. */
    for(int j=1;j<=10;++j) {
        long a=j*(2*j+1)*choose(2*j,j);
        long b=(j+1)*(2*j+3)*choose(2*j+2,j+1);
        require(2*j*b==4*(2*j+3)*a);
    }
    emit("A4 LEAN ten exact size-biased order ratios for the spectator count\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
