/* Three finite arithmetic checks using the wire format of the repository guest replay. */
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
__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    /* Scaled roots 0,1,1+d. Lower point a is near one; bound its
       interpolation weight from the cubic residual irrespective of d. */
    int accepted=0, repeated=0;
    for(long d=0;d<=64;d++)for(long m=32;m<=160;m++){
        long lower=(m-64)*(m-64-d);
        long ab=lower<0?-lower:lower;
        /* |a(a-1)(a-1-d/64)| <= 1/64 */
        if(m*ab>64*64)continue;
        accepted++; repeated+=d==0;
        /* |(a-1)(a-1-d/64)/(1+d/64)| <= 2/64 */
        if(ab>2*(64+d))sys(60,1,0,0);
    }
    if(accepted<100||repeated<2)sys(60,1,0,0);
    emit("A4 CHILD spectrum\nA4 LEAN lower-pair product including repeated centers\n");
#elif ROLE==1
    for(int x=-2;x<=2;x++)for(int y=-2;y<=2;y++)for(int z=-2;z<=2;z++){
        int n[3]={x*x,y*y,z*z},s=n[0]+n[1]+n[2],v[3],sum=0;
        for(int i=0;i<3;i++){
            v[i]=-s;
            for(int j=0;j<3;j++)if(i!=j)v[i]-=n[i]+n[j];
            sum+=v[i];
        }
        for(int i=0;i<3;i++){
            long centered=3*v[i]-sum;
            if(centered!=s-3*n[i])sys(60,1,0,0);
            if(centered-9*n[i]!=s-12*n[i])sys(60,1,0,0);
        }
    }
    emit("A4 CHILD limit\nA4 LEAN 125 directional eigenvector and translation corrections\n");
#else
    /* Unit ball: by radial integration E[r^2]=3/5, E[r^4]=3/7;
       angular z^2 and z^4 have averages 1/3, 1/5. */
    long s4=3, s22=(15-3*s4)/6; /* angular denominator 15 */
    if(s22!=1 || 3*60!=5*3*12 || 3*(s4-s22)*1890!=7*15*108)sys(60,1,0,0);
    if(3*(s4-s22)*3360!=7*15*192)sys(60,1,0,0);
    emit("A4 LEAN based cube and frozen-eigenvector ball constants\n");
#endif


    emit("A4 FINISHED\n");
    sys(60,0,0,0);__builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
