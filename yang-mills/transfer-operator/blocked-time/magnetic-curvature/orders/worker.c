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

typedef struct { int x[3]; int normal; } Face;
typedef struct { int x[3]; int axis; } Edge;

static Edge face_edge(Face f, int side) {
    int along = (f.normal + 1 + side / 2) % 3;
    int across = 3 - along - f.normal;
    Edge e = {{f.x[0],f.x[1],f.x[2]}, along};
    e.x[across] += side % 2;
    return e;
}

static int same(Edge a, Edge b, int period) {
    if (a.axis != b.axis) return 0;
    for (int d=0; d<3; ++d)
        if ((a.x[d]-b.x[d]) % period != 0) return 0;
    return 1;
}

/* Attach a new face along an edge, allowing repetitions at other positions. */
static int paths, short_wrap;
static void grow(Face *faces, int count) {
    if (count == 4) { ++paths; return; }
    for (int old=0; old<count; ++old) for (int j=0; j<4; ++j) {
        Edge target = face_edge(faces[old],j);
        for (int axis=0; axis<3; ++axis) {
            if (axis == target.axis) continue;
            for (int side=0; side<2; ++side) {
                Face next={{target.x[0],target.x[1],target.x[2]},axis};
                next.x[3-axis-target.axis] -= side;
                faces[count]=next;
                for (int a=0; a<4; ++a) for (int b=0; b<4; ++b)
                    for (int q=0; q<count; ++q) {
                        Edge e=face_edge(next,a), f=face_edge(faces[q],b);
                        int exact=same(e,f,100);
                        require(exact == same(e,f,8));
                        short_wrap |= exact != same(e,f,4);
                    }
                grow(faces,count+1);
            }
        }
    }
}

/* Under independent symmetric binary edge signs, a product of faces has
   mean one exactly when its mod-two boundary is empty. */
static int mean_mask(const int *faces, int size, int selected) {
    int boundary=0;
    for (int i=0; i<size; ++i) if (selected & (1<<i)) boundary ^= faces[i];
    return boundary == 0;
}
static int cumulant(const int *faces, int n, int selected) {
    int total=mean_mask(faces,n,selected);
    int first=selected & -selected;
    for (int s=(selected-1)&selected; s; s=(s-1)&selected)
        if (s & first)
            total -= cumulant(faces,n,s)*mean_mask(faces,n,selected^s);
    return total;
}

__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    Face faces[4]={{{0,0,0},2}};
    grow(faces,1);
    require(paths==16*32*48 && short_wrap);
    emit("A4 CHILD spectrum\nA4 LEAN rooted four-face edge identifications on the cover and two tori\n");
#elif ROLE==1
    int masks[6]={0};
    for (int d=0; d<3; ++d) for (int side=0; side<2; ++side) {
        Face face={{0,0,0},d};
        face.x[d]=side;
        for (int j=0; j<4; ++j) {
            Edge e=face_edge(face,j);
            int i=(e.axis+1)%3, k=(e.axis+2)%3;
            masks[2*d+side] |= 1 << (4*e.axis+2*e.x[i]+e.x[k]);
        }
    }
    require(cumulant(masks,6,63)==1);
    int split[]={masks[0],masks[0],masks[1],masks[1]};
    require(cumulant(split,4,15)==0);
    require(mean_mask(split,4,15)==1);
    emit("A4 CHILD limit\nA4 LEAN cube cumulant and disconnected repeated-face control\n");
#else
    /* Two-state chain with transition [[3,1],[2,2]]/4, stationary
       weights (2,1)/3. For the indicator of the second state the
       connected correlation is (2/9)(1/4)^n. */
    long a=0,b=1,den=1;
    for (int n=0;n<=12;++n) {
        require(3*b-den==2);
        if (n>0) require(3*b!=2);
        long next_a=3*a+b, next_b=2*a+2*b;
        a=next_a; b=next_b; den*=4;
    }
    emit("A4 LEAN vacuum subtraction retains the exact exponential in a biased chain\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
