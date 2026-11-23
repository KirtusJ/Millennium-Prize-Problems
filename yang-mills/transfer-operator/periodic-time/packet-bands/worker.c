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

static int absolute(int value) { return value < 0 ? -value : value; }

#if ROLE == 0
static void box_control(int r) {
    int avg[64] = {0}, factored[64] = {0}, out[64] = {0};
    for (int a = 0; a < r; ++a)
        for (int b = 0; b < r; ++b)
            for (int c = 0; c < r; ++c)
                for (int d = 0; d < r; ++d) ++avg[a+b+c+d];
    int mass = 0;
    for (int x = 0; x < 64; ++x) {
        require(avg[x] <= r*r*r);
        mass += avg[x];
    }
    require(mass == r*r*r*r);
    int coeff[4] = {1,-3,3,-1};
    for (int x = 0; x <= 4*(r-1); ++x) {
        for (int j = 0; j < 4; ++j) {
            out[x+j*r] += coeff[j]*avg[x];
            for (int a = 0; a < r; ++a)
                for (int b = 0; b < r; ++b)
                    for (int c = 0; c < r; ++c)
                        factored[x+a+b+c+j] += coeff[j]*avg[x];
        }
    }
    int variation = 0, moments[3] = {0};
    for (int x = 0; x < 64; ++x) {
        require(factored[x] == out[x]);
        variation += absolute(out[x]);
        moments[0] += out[x]; moments[1] += x*out[x]; moments[2] += x*x*out[x];
    }
    require(variation <= 8*mass);
    for (int j = 0; j < 3; ++j) require(moments[j] == 0);
}
#elif ROLE == 1
/* The oriented boundary of a 12-face has zero temporal and 3-components. */
static int profile(int t, int x, int y, int z) {
    return (13*t + 47*x - 7*y + 19*z) % 31;
}
static int primitive(int axis, int t, int x, int y, int z) {
    if (axis == 1) return profile(t,x,y,z)-profile(t,x,y-1,z);
    if (axis == 2) return profile(t,x-1,y,z)-profile(t,x,y,z);
    return 0;
}
static void path_control(int t, int x, int y, int z) {
    int goal[4] = {t,x,y,z}, cur[4] = {0}, sum = 0;
    for (int axis = 0; axis < 4; ++axis) {
        int direction = goal[axis] < 0 ? -1 : 1;
        while (cur[axis] != goal[axis]) {
            if (direction < 0) --cur[axis];
            sum += absolute(primitive(axis,cur[0],cur[1],cur[2],cur[3]));
            if (direction > 0) ++cur[axis];
        }
        if (axis == 0) require(sum == 0);
    }
    require(sum <= 60*(absolute(x)+absolute(y)));
}
#else
/* Four discrete total momenta on the unit circle, with independent weights.
   Removing the strictly positive energy interior removes the whole lower bound. */
static int band_form(const int v[4], int repeat, int select) {
    const int cosine[4] = {1,0,-1,0}, sine[4] = {0,1,0,-1};
    int total = 0;
    for (int k = 0; k < 4; ++k) {
        int energy = 3+k, re = 0, im = 0;
        if (!(energy > select && energy < 7)) continue;
        for (int j = 0; j < 4; ++j) {
            int phase = (repeat && j == 3 ? 2 : j)*k % 4;
            re += v[j]*cosine[phase]; im += v[j]*sine[phase];
        }
        total += (1+k)*(re*re+im*im);
    }
    return total;
}
#endif

__attribute__((used,noreturn)) static void run(void) {
#if ROLE == 0
    for (int r = 1; r <= 8; ++r) box_control(r);
    emit("A4 CHILD spectrum\nA4 LEAN eight box scales: convolution mass, cap, cancellations and telescope\n");
#elif ROLE == 1
    for (int t = -24; t <= 24; ++t)
        for (int x = -2; x <= 2; ++x)
            for (int y = -2; y <= 2; ++y)
                for (int z = -2; z <= 2; ++z) path_control(t,x,y,z);
    emit("A4 CHILD limit\nA4 LEAN 6125 signed root paths: magnetic primitive ignores the time trunk\n");
#else
    for (int code = 0; code < 625; ++code) {
        int v[4], norm = 0, digits = code;
        for (int j = 0; j < 4; ++j) {
            v[j] = digits%5-2; digits /= 5; norm += v[j]*v[j];
        }
        require(band_form(v,0,2) >= 4*norm);
        require(band_form(v,0,6) == 0);
    }
    int null_vector[4] = {0,0,1,-1};
    require(band_form(null_vector,1,2) == 0 && band_form(null_vector,0,2) > 0);
    emit("A4 LEAN 625 spectral Gram controls; duplicate and empty band lose rank\n");
#endif
    emit("A4 FINISHED\n");
    finish(0);
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall run\nud2");
