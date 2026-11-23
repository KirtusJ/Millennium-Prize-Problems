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

/* Enumerate rooted, oriented, simple six-step loops on the cubic cover.
   A bounding box with side 2 detects a rectangle. In the unit cube
   distinguish adjacent from antipodal omitted vertices. */
static int vertices[7][3], rectangles, chairs, skew;
static void walk(int n) {
    if (n==6) {
        int lo[3]={0},hi[3]={0};
        for (int j=0;j<6;++j) for(int d=0;d<3;++d) {
            int v=vertices[j][d];
            if(v<lo[d])lo[d]=v;
            if(v>hi[d])hi[d]=v;
        }
        for(int d=0;d<3;++d) if(hi[d]-lo[d]==2) {++rectangles;return;}
        int mask=0;
        for(int j=0;j<6;++j) {
            int k=0;
            for(int d=0;d<3;++d) k+= (vertices[j][d]-lo[d])<<d;
            mask|=1<<k;
        }
        int missing[2],m=0;
        for(int k=0;k<8;++k)if(!(mask&(1<<k))) {require(m<2);missing[m++]=k;}
        require(m==2);
        int delta=missing[0]^missing[1];
        if(delta==7)++skew;
        else {require(delta==1||delta==2||delta==4);++chairs;}
        return;
    }
    for(int axis=0;axis<3;++axis) for(int dir=-1;dir<=1;dir+=2) {
        for(int d=0;d<3;++d) vertices[n+1][d]=vertices[n][d]+(d==axis?dir:0);
        int repeat=-1;
        for(int j=0;j<=n;++j) {
            int match=1;
            for(int d=0;d<3;++d) match &= vertices[n+1][d]==vertices[j][d];
            if(match) repeat=j;
        }
        if(n==5 ? repeat==0 : repeat<0) walk(n+1);
    }
}
static int mult(int a,int b) {
    static const int m[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
    int sign=(a<0 ? -1:1)*(b<0 ? -1:1);
    return sign*m[(a<0?-a:a)-1][(b<0?-b:b)-1];
}
static int trace(int a){return a==1 ? 2 : (a==-1 ? -2 : 0);}
static long disk(int left,int word,int product) {
    if(!left)return product*trace(word);
    long sum=0;
    for(int j=-4;j<=4;++j)if(j)sum+=disk(left-1,mult(word,j),product*trace(j));
    return sum;
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    walk(0);
    require(rectangles==12*6 && chairs==12*12 && skew==12*4);
    emit("A4 CHILD spectrum\nA4 LEAN six-edge rectangles, chairs and skew loops on the cubic cover\n");
#elif ROLE==1
    long size=1;
    for(int j=1;j<=5;++j) {
        size*=8;
        require(disk(j,1,1)*(1L<<(j-1))==size);
    }
    emit("A4 CHILD limit\nA4 LEAN disk character contractions through the six-face sphere in Q8\n");
#else
    /* Susceptibility v = 1 - b^2/8 + 5 b^4/96 - 7 b^6/360.
       Recursion -v' = v*(-log v)' using common denominator 23040. */
    long c2=2880,c4=-1020,c6=313;
    require(2*c2==23040/4);
    require(4*c4-2*c2/8==-23040*20/96);
    require(6*c6-4*c4/8+2*c2*5/96==23040*42/360);
    /* S_4 = 4[-6/48 + 4/64 + (4/3)*9/256] = -1/16. */
    require(4*(-6*16+4*12+36)==-48);
    emit("A4 LEAN logarithmic susceptibility coefficients and the six-loop correction\n");
#endif
    emit("A4 FINISHED\n");finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
