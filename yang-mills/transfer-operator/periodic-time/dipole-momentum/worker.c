/* Finite independent arithmetic controls using the repository guest wire format. */
#ifndef ROLE
#error ROLE required
#endif
__attribute__((used)) static volatile int worker_role = ROLE + 1;
static long sys(long n,long a,long b,long c) {
    long result;
    __asm__ volatile("syscall":"=a"(result):"a"(n),"D"(a),"S"(b),"d"(c):"rcx","r11","memory");
    return result;
}
static void emit(const char *s) {
    unsigned len=0;
    while(s[len]) ++len;
    while(len){
        long k=sys(1,1,(long)s,len);
        if(k<=0 || (unsigned long)k>len){sys(60,1,0,0);__builtin_unreachable();}
        len-=(unsigned)k;s+=k;
    }
}
static long power(long base, unsigned exponent) {
    long result = 1;
    while (exponent--) result *= base;
    return result;
}

static void require(int predicate) {
    if (!predicate) {
        sys(60,1,0,0);
        __builtin_unreachable();
    }
}

/* 2 sin^2(q/2) at the four cyclic momenta. */
static int sine_index(int index) {
    static const int table[] = {0,1,2,1};
    return table[index%4];
}

static int norm_index(int point) {
    return sine_index(point)+sine_index(point/4)+sine_index(point/16);
}

static int sum_index(int p, int q) {
    return sine_index(p%4+q%4)+sine_index((p/4)%4+(q/4)%4)
           +sine_index(p/16+q/16);
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    int equal = 0;
    for (int p=0; p<64; ++p) {
        for (int q=0; q<64; ++q) {
            long a=norm_index(p), b=norm_index(q), c=sum_index(p,q);
            /* Compare sqrt(2c) with sqrt(a(2+b))+sqrt(b(2+a)). */
            long x=a*(2+b), y=b*(2+a), delta=2*c-x-y;
            if (a && b) {
                require(delta < 0 || delta*delta < 4*x*y);
            } else {
                require(delta == 0 && x*y == 0);
                ++equal;
            }
        }
    }
    require(equal == 127);
    emit("A4 CHILD spectrum\nA4 LEAN 4096 exact dispersion comparisons; equality only at a zero leg\n");
#elif ROLE == 1
    /* At k_i=pi or 0, sin^2((k_i-r)/2) has numerator 1 or x^2,
       x=tan(r/2), over 1+x^2. Count the first power on diagonal rays. */
    for (int corners=0; corners<8; ++corners) {
        int ex=(corners&1) ? 0:2, ey=(corners&2) ? 0:2, ez=(corners&4) ? 0:2;
        int numerator=ez+(ex<ey ? ex:ey);
        int hard=numerator-(corners==0);
        int expected= corners==0 ? 9 : ((corners&4)&&(corners&3) ? 6:8);
        require(3+3+hard == expected);
    }
    /* Average theta_3^4 (1-theta_3^2)^2 / 4 over the unit sphere. */
    require(63-90+35 == 8 && 8*315 == 2*(4*315));
    require(241920L*6 == 9*512*315);
    emit("A4 CHILD limit\nA4 LEAN eight corner orders and the rest angular coefficient\n");
#else
    /* Positive power-series bounds behind soft-energy localization.
       sum x_i^j <= (sum x_i)^j and <= (max x_i)^(j-1) sum x_i. */
    for (int code=1; code<4096; ++code) {
        int energies[6], total=0, maximum=0, digits=code;
        for (int i=0; i<6; ++i) {
            energies[i]=digits%4; digits/=4;
            total+=energies[i];
            if (maximum<energies[i]) maximum=energies[i];
        }
        for (int j=1; j<=7; j+=2) {
            long sum=0;
            for (int i=0; i<6; ++i) sum+=power(energies[i],j);
            require(sum<=power(total,j) && sum<=power(maximum,j-1)*total);
        }
    }
    emit("A4 LEAN 4095 six-leg controls for soft-energy localization\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);
    __builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
