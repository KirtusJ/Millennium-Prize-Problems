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

/* Opposite faces are (0,1), (2,3) and (4,5). */
static int crossing_edges(int mask) {
    int count=0;
    for (int a=0;a<6;++a) for(int b=0;b<a;++b)
        if(a/2!=b/2) count+=((mask>>a)^(mask>>b))&1;
    return count;
}
static int bitcount(int mask) {
    int count=0;
    for (;mask;mask>>=1) count+=mask&1;
    return count;
}
static int partitions;
/* At q=1/2 the two internal waiting weights are 1/3 and 1/15.
   15^3 clears every ordered-partition denominator. */
static int summed_weights(int visited,int absent,int scale) {
    if(!absent) { ++partitions; return scale; }
    int sum=0;
    for(int next=absent;next;next=(next-1)&absent) {
        int new_set=visited|next, rest=absent^next;
        int denom=1;
        if(rest) {
            int cut=crossing_edges(new_set);
            require(cut==6 || cut==8);
            denom=(1<<(cut-4))-1;
        }
        require(scale%denom==0);
        sum+=summed_weights(new_set,rest,scale/denom);
    }
    return sum;
}
__attribute__((used,noreturn)) static void run(void) {
#if ROLE==0
    int four=0,six=0,eight=0;
    for(int mask=1;mask<63;++mask) {
        int k=crossing_edges(mask), size=bitcount(mask);
        require((k==4)==(size==1 || size==5));
        four+=k==4; six+=k==6; eight+=k==8;
    }
    require(four==12 && four+six+eight==62);
    emit("A4 CHILD spectrum\nA4 LEAN minimum cuts of the face adjacency graph of the cube\n");
#elif ROLE==1
    long total=0;
    for(int sink=1;sink<=2;++sink) {
        partitions=0;
        int value=summed_weights(1,63^(1|(1<<sink)),3375);
        require(partitions==75);
        total+=(sink==1?2:8)*value;
    }
    require(total*432000L==117413L*3375*256);
    emit("A4 CHILD limit\nA4 LEAN exact finite rational four-layer sum at fundamental multiplier one half\n");
#else
    int leading_cut_weight=0;
    for(int sink=1;sink<=2;++sink) {
        int weight=0;
        for(int i=1;i<6;++i)for(int j=1;j<6;++j)for(int k=1;k<6;++k) {
            int three=(1<<i)|(1<<j)|(1<<k);
            if((three&(1<<sink)) || bitcount(three)!=3) continue;
            int a=1|(1<<i), b=a|(1<<j), c=b|(1<<k);
            int prod=(crossing_edges(a)-4)*(crossing_edges(b)-4)*(crossing_edges(c)-4);
            require(64%prod==0);
            weight+=64/prod;
        }
        leading_cut_weight+=(sink==1?2:8)*weight;
    }
    require(leading_cut_weight*1024==73*64*256);
    emit("A4 LEAN scaled continuous-time limit from strictly ordered layers\n");
#endif
    emit("A4 FINISHED\n");finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
