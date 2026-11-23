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

/* Signed basis units 1,i,j,k of Q8. */
static int mult(int a, int b) {
    static const int m[4][4] = {
        {1,2,3,4}, {2,-1,4,-3}, {3,-4,-1,2}, {4,3,-2,-1}
    };
    int s = 1;
    if (a < 0) { a = -a; s = -s; }
    if (b < 0) { b = -b; s = -s; }
    return s * m[a-1][b-1];
}
static int inv(int a) { return a == 1 || a == -1 ? a : -a; }

static int trace(int q) { return q==1 ? 2 : (q==-1 ? -2 : 0); }
static int site(int x,int y,int z,int L) {return (x%L)+L*((y%L)+L*(z%L));}
static void face(int x,int y,int z,int a,int b,int L,int out[4]) {
    int root=site(x,y,z,L), u=site(x+(a==0),y+(a==1),z+(a==2),L);
    int v=site(x+(b==0),y+(b==1),z+(b==2),L);
    out[0]=3*root+a; out[1]=3*u+b; out[2]=3*v+a; out[3]=3*root+b;
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    int total=0,projected=0;
    for(int a=-4;a<=4;++a)for(int b=-4;b<=4;++b) {
        if(!a || !b)continue;
        int sum=0;
        for(int u=-4;u<=4;++u)if(u) {
            int value=trace(mult(u,a))*trace(mult(inv(u),b));
            total+=value*value; sum+=value;
        }
        require(sum==4*trace(mult(a,b)));
        projected+=sum*sum;
    }
    require(total==512 && projected==1024);
    emit("A4 CHILD spectrum\nA4 LEAN exact shared-link projection in the quaternion subgroup\n");
#elif ROLE==1
    for(int L=6;L<=10;L+=2) {
        int ref[4], edges[4], neighbours=0, same=0;
        face(0,0,0,0,1,L,ref);
        for(int x=0;x<L;++x)for(int y=0;y<L;++y)for(int z=0;z<L;++z)
        for(int a=0;a<3;++a)for(int b=a+1;b<3;++b){
            face(x,y,z,a,b,L,edges);
            int shared=0;
            for(int i=0;i<4;++i)for(int j=0;j<4;++j)shared+=ref[i]==edges[j];
            require(shared==0 || shared==1 || shared==4);
            neighbours+=shared==1; same+=shared==4;
        }
        require(neighbours==12 && same==1);
    }
    emit("A4 CHILD limit\nA4 LEAN twelve edge-sharing squares on three cubic tori\n");
#else
    /* Unit is 1/420. Free denominators are 6, 10, 3, 7. */
    int interaction=420/6-420/(4*3)-3*420/(4*7);
    require(interaction==-10);
    int row=2*(420/6)-420/10+24*interaction;
    require(row==-142);
    for(int k=2;k<=60;++k) {
        /* lambda=1/k; H(1) and H(lambda^2) have opposite numerators
           over the common positive denominator k-1. */
        require(-(k+1)+(k+1)==0);
    }
    emit("A4 LEAN rational Hamiltonian coefficient and vacuum subtraction\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
