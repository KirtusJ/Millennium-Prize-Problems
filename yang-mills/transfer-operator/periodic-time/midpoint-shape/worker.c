/* Finite checks for midpoint subtraction and the two-projection argument using the wire format of the repository guest replay. */
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

/* Numerator of the geometric sum at p/q with denominator q^(k-1). */
static long geometric(long p, long q, unsigned k) {
    long result = 0;
    for (unsigned i = 0; i < k; ++i) result += power(p,i)*power(q,k-1-i);
    return result;
}

static void require(int predicate) {
    if (!predicate) {
        sys(60,1,0,0);
        __builtin_unreachable();
    }
}

static long square_sum_coeff(int k, int degree) {
    int count = 0;
    for (int i = 0; i < k; ++i) count += degree-i >= 0 && degree-i < k;
    return count;
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int n = 3; n <= 6; ++n) {
        for (int t = 0; t < n; ++t) {
            long products = 0, losses = 0;
            long x[12];
            for (int i = 0; i < 2*n; ++i) x[i] = (i*i+3*i)%7 - 3;
            for (int i = 0; i < 2*n; ++i) {
                long mid = x[(i+n)%(2*n)], lag = x[(i+t)%(2*n)];
                products += x[i]*(lag-mid);
                losses += (x[i]-mid)*(x[i]-mid) - (x[i]-lag)*(x[i]-lag);
            }
            require(2*products == losses);
        }
    }
    /* Check the two gap-scaled examples after removing exp(1/2).
       For xi=r^2 the first ratio is (1+r^3)/(1+r^2).
       For xi=4 log r the second ratio is (r^3+r^2)/(r^3+1). */
    for (long r = 2; r <= 1024; r *= 2) {
        long rr = r*r, cube = r*rr;
        require(2*(1+cube) >= r*(1+rr));
        require(r*(cube+rr) <= (r+1)*(cube+1));
    }
    emit("A4 CHILD spectrum\nA4 LEAN cyclic row contrast equals the difference of squared increments\nA4 LEAN rising and bounded correlation-time ratio controls\n");
#elif ROLE == 1
    /* Low-factor side of the separator: K3(3/8) < 6/125. */
    long s3 = geometric(3,8,3), s6 = geometric(3,8,6);
    require(125*power(3*8,3)*s3*s3 < 6*s6*s6);
    emit("A4 CHILD limit\nA4 LEAN the third normalized lag at 3/8 is below 6/125\n");
#else
    /* On [3/8,1] put z=(3+8u)/(8+8u). Clear the degree-ten denominator.
       The largest intermediate absolute value stays below 10^16. */
    long coefficients[11] = {0};
    for (int i = 0; i <= 10; ++i) {
        long factor = 100*(square_sum_coeff(5,i-1)-square_sum_coeff(4,i-2))
                      - 23*square_sum_coeff(6,i);
        long term[11] = {1};
        for (int k = 0; k < 10; ++k) {
            int constant = k < i ? 3 : 8;
            for (int j = k+1; j > 0; --j) term[j] = constant*term[j] + 8*term[j-1];
            term[0] *= constant;
        }
        for (int j = 0; j <= 10; ++j) coefficients[j] += factor*term[j];
    }
    for (int j = 0; j <= 10; ++j) require(coefficients[j] > 0);
    require(coefficients[0] == 1544283553L);
    require(coefficients[10] == 77309411328L);
    emit("A4 LEAN eleven positive coefficients certify the upper-factor exclusion\n");
#endif
    emit("A4 FINISHED\n");
    sys(60,0,0,0);
    __builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
