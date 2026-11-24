//! SU(2) Wilson 4D, N=6, T=12, frozen skeleton on t=0. Own implementation.
//! Predicates (fixed before first run):
//!  P0 control.txt == 0.250000.
//!  P1 independence check: for every colour, no link of one pair lies in a plaquette (other than the shared one) of another pair [exact-joint-law condition]; expected: all 24 colours pass (my expectation, from the stated design).
//!  P2 frozen links never change; |U|=1 within 1e-9 at end.
//!  P3 beta=0 run: J1/Var(f1) = 1/24 within 4 standard errors (Haar prediction), Var(f1)=1/4 within 4 se.
//!  P4 beta=3.276133577: compare J/Var with reference 0.0464+-0.0055 (f4), 0.0639+-0.0023 (f1); agreement = |diff| <= 2*sqrt(se_mine^2+se_ref^2).
//! usage: mc beta nstreams burn nmeas every seed outfile
use std::io::Write;
const N: i32 = 6; const T: i32 = 12;
type Q = [f64; 4];
fn mul(a: &Q, b: &Q) -> Q { [a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3], a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2], a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1], a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]] }
fn conj(a: &Q) -> Q { [a[0], -a[1], -a[2], -a[3]] }
fn norm(a: &Q) -> f64 { (a[0]*a[0]+a[1]*a[1]+a[2]*a[2]+a[3]*a[3]).sqrt() }
struct Rng { s: [u64; 4] }
impl Rng {
    fn new(seed: u64) -> Rng { let mut z = seed; let mut s = [0u64; 4];
        for i in 0..4 { z = z.wrapping_add(0x9E3779B97F4A7C15); let mut x = z; x = (x ^ (x >> 30)).wrapping_mul(0xBF58476D1CE4E5B9); x = (x ^ (x >> 27)).wrapping_mul(0x94D049BB133111EB); s[i] = x ^ (x >> 31); } Rng { s } }
    fn next(&mut self) -> u64 { let r = self.s[1].wrapping_mul(5).rotate_left(7).wrapping_mul(9); let t = self.s[1] << 17;
        self.s[2] ^= self.s[0]; self.s[3] ^= self.s[1]; self.s[1] ^= self.s[2]; self.s[0] ^= self.s[3]; self.s[2] ^= t; self.s[3] = self.s[3].rotate_left(45); r }
    fn u(&mut self) -> f64 { ((self.next() >> 11) as f64 + 0.5) / 9007199254740992.0 }
    fn gauss(&mut self) -> f64 { (-2.0*self.u().ln()).sqrt() * (6.283185307179586*self.u()).cos() }
    fn haar(&mut self) -> Q { loop { let q = [self.gauss(), self.gauss(), self.gauss(), self.gauss()]; let n = norm(&q); if n > 1e-8 { return [q[0]/n, q[1]/n, q[2]/n, q[3]/n]; } } }
    // W with density ~ sqrt(1-a0^2) exp(alpha a0), uniform direction
    fn wdraw(&mut self, alpha: f64) -> Q {
        if alpha < 1e-9 { return self.haar(); }
        let a0 = loop { let (x1, x2, x3, x4) = (self.u(), self.u(), self.u(), self.u());
            let c = (6.283185307179586*x2).cos();
            let d = -(x1.ln() + c*c*x3.ln())/alpha;
            if x4*x4 <= 1.0 - d/2.0 { break 1.0 - d; } };
        let r = (1.0 - a0*a0).max(0.0).sqrt();
        let v = [self.gauss(), self.gauss(), self.gauss()]; let n = (v[0]*v[0]+v[1]*v[1]+v[2]*v[2]).sqrt();
        [a0, r*v[0]/n, r*v[1]/n, r*v[2]/n] }
}
fn site(c: [i32; 4]) -> usize { let w = |v: i32, m: i32| ((v % m) + m) % m;
    ((((w(c[3], T)*N + w(c[2], N))*N + w(c[1], N))*N + w(c[0], N)) as usize) }
fn lk(c: [i32; 4], mu: usize) -> usize { site(c)*4 + mu }
fn sh(c: [i32; 4], mu: usize, d: i32) -> [i32; 4] { let mut r = c; r[mu] += d; r }
// staple links for link (c,mu), plaquette direction nu, sign
fn staple_links(c: [i32; 4], mu: usize, nu: usize, sg: i32) -> [(usize, bool); 3] {
    if sg > 0 { [(lk(sh(c, mu, 1), nu), false), (lk(sh(c, nu, 1), mu), true), (lk(c, nu), true)] }
    else { let cm = sh(c, nu, -1); [(lk(sh(cm, mu, 1), nu), true), (lk(cm, mu), true), (lk(cm, nu), false)] } }
fn staple(u: &Vec<Q>, c: [i32; 4], mu: usize, nu: usize, sg: i32) -> Q {
    let l = staple_links(c, mu, nu, sg); let mut p = [1.0, 0.0, 0.0, 0.0];
    for &(i, d) in l.iter() { let q = if d { conj(&u[i]) } else { u[i] }; p = mul(&p, &q); } p }
fn csum(u: &Vec<Q>, c: [i32; 4], mu: usize, skip: Option<(usize, i32)>) -> Q {
    let mut s = [0.0; 4];
    for nu in 0..4 { if nu == mu { continue; } for &sg in [1, -1].iter() {
        if let Some((n2, s2)) = skip { if n2 == nu && s2 == sg { continue; } }
        let q = staple(u, c, mu, nu, sg); for k in 0..4 { s[k] += q[k]; } } } s }
fn draw_link(rng: &mut Rng, cs: &Q, beta: f64) -> Q {
    let k = norm(cs); if k < 1e-12 { return rng.haar(); }
    let v = [cs[0]/k, cs[1]/k, cs[2]/k, cs[3]/k]; let w = rng.wdraw(beta*k); mul(&w, &conj(&v)) }
fn plaq_re(u: &Vec<Q>, c: [i32; 4], i: usize, j: usize) -> f64 {
    let a = mul(&u[lk(c, i)], &u[lk(sh(c, i, 1), j)]); let b = mul(&conj(&u[lk(sh(c, j, 1), i)]), &conj(&u[lk(c, j)])); mul(&a, &b)[0] }
struct Pair { su: [i32; 4], i: usize, j: usize, lu: usize, lv: usize, cu: [i32; 4], cv: [i32; 4], ku: (usize, i32), kv: (usize, i32), s: [i32; 4] }
fn refresh(u: &mut Vec<Q>, p: &Pair, beta: f64, rng: &mut Rng) {
    let cu = csum(u, p.cu, p.i, Some(p.ku)); let cv = csum(u, p.cv, p.j, Some(p.kv));
    loop { u[p.lu] = draw_link(rng, &cu, beta); u[p.lv] = draw_link(rng, &cv, beta);
        let r = plaq_re(u, p.s, p.i, p.j); if rng.u() < (beta*(r - 1.0)).exp() { break; } } }
fn eval(u: &Vec<Q>) -> (f64, f64, f64) {
    let b: Q = [0.0, 1.0, 0.0, 0.0]; let mut gs = vec![]; let mut g1 = [0.0; 4];
    for a in 0..2 { for bb in 0..2 {
        let s = [a, bb, 0, 0];
        let p = { let x = mul(&u[lk(s, 0)], &u[lk(sh(s, 0, 1), 1)]); let y = mul(&conj(&u[lk(sh(s, 1, 1), 0)]), &conj(&u[lk(s, 1)])); mul(&x, &y) };
        let mut l = [1.0, 0.0, 0.0, 0.0];
        for c in 0..a { l = mul(&l, &u[lk([c, 0, 0, 0], 0)]); }
        for r in 0..bb { l = mul(&l, &u[lk([a, r, 0, 0], 1)]); }
        let g = mul(&mul(&l, &p), &conj(&l)); if a == 0 && bb == 0 { g1 = g; } gs.push(g); } }
    let mut gb = [0.0; 4]; for g in gs.iter() { for k in 0..4 { gb[k] += g[k]/4.0; } }
    (mul(&b, &g1)[0], mul(&b, &gb)[0], 1.0 - norm(&gb).powi(2)) }
fn main() {
    let a: Vec<String> = std::env::args().collect();
    let beta: f64 = a[1].parse().unwrap(); let ns: usize = a[2].parse().unwrap(); let burn: usize = a[3].parse().unwrap();
    let nm: usize = a[4].parse().unwrap(); let every: usize = a[5].parse().unwrap(); let seed: u64 = a[6].parse().unwrap();
    let mut out = std::fs::OpenOptions::new().write(true).create_new(true).open(&a[7]).unwrap();
    let nsite = (N*N*N*T) as usize;
    // frozen
    let mut frozen = vec![false; nsite*4]; let mut u0 = vec![[1.0, 0.0, 0.0, 0.0]; nsite*4];
    for x in 0..N { for y in 0..N { for z in 0..N { let c = [x, y, z, 0]; for i in 0..3 {
        let o: Vec<usize> = (0..3).filter(|&k| k != i).collect();
        if c[o[0]] % 2 == 0 && c[o[1]] % 2 == 0 { frozen[lk(c, i)] = true; } } } } }
    u0[lk([2, 0, 0, 0], 1)] = [-1.0, 0.0, 0.0, 0.0]; u0[lk([2, 0, 0, 0], 2)] = [0.0, 1.0, 0.0, 0.0];
    let nfrozen = frozen.iter().filter(|&&b| b).count();
    // colours
    let planes = [(0usize, 1usize), (0, 2), (1, 2)]; let mut cols: Vec<Vec<Pair>> = vec![];
    for &(i, j) in planes.iter() { for pv in 0..8 { let par = [pv & 1, (pv >> 1) & 1, (pv >> 2) & 1]; let mut v = vec![];
        for x in 0..N { for y in 0..N { for z in 0..N { let s = [x, y, z, 0];
            if (0..3).any(|k| (s[k] % 2) as usize != par[k]) { continue; }
            let (cu, ku) = if s[j] % 2 == 0 { (sh(s, j, 1), (j, -1)) } else { (s, (j, 1)) };
            let (cv, kv) = if s[i] % 2 == 0 { (sh(s, i, 1), (i, -1)) } else { (s, (i, 1)) };
            v.push(Pair { su: s, i, j, lu: lk(cu, i), lv: lk(cv, j), cu, cv, ku, kv, s }); } } } cols.push(v); } }
    // P1 independence check
    let mut npass = 0;
    for col in cols.iter() { let mut ok = true; let all: std::collections::HashSet<usize> = col.iter().flat_map(|p| vec![p.lu, p.lv]).collect();
        for p in col.iter() { for &(c, mu, sk) in [(p.cu, p.i, p.ku), (p.cv, p.j, p.kv)].iter() {
            for nu in 0..4 { if nu == mu { continue; } for &sg in [1, -1].iter() { if sk == (nu, sg) { continue; }
                for &(l, _) in staple_links(c, mu, nu, sg).iter() { if all.contains(&l) { ok = false; } } } }
            // frozen? pair links must be free
            if frozen[p.lu] || frozen[p.lv] { ok = false; } } }
        if ok { npass += 1; } }
    eprintln!("P1 colours passing independence+free check: {}/24; frozen links {}", npass, nfrozen);
    writeln!(out, "# beta={} ns={} burn={} nm={} every={} seed={} P1pass={}/24", beta, ns, burn, nm, every, seed, npass).unwrap();
    let free: Vec<usize> = (0..nsite*4).filter(|&l| !frozen[l]).collect();
    let mut colsum1 = vec![0.0; 24]; let mut colsum4 = vec![0.0; 24]; let mut cnt = 0.0;
    for st in 0..ns {
        let mut rng = Rng::new(seed + 1000*st as u64);
        let cold = st % 2 == 0;
        let mut u = u0.clone();
        if !cold { for l in 0..nsite*4 { if !frozen[l] { u[l] = rng.haar(); } } }
        let sweep = |u: &mut Vec<Q>, rng: &mut Rng| { for &l in free.iter() { let site_i = l/4; let mu = l%4;
            let w = site_i as i32; let x = w % N; let y = (w/N) % N; let z = (w/(N*N)) % N; let t = w/(N*N*N);
            let cs = csum(u, [x, y, z, t], mu, None); u[l] = draw_link(rng, &cs, beta); } };
        for _ in 0..burn { sweep(&mut u, &mut rng); }
        for m in 0..nm {
            for _ in 0..every { sweep(&mut u, &mut rng); }
            let (f1, f4, sp) = eval(&u); let (mut j1, mut j4) = (0.0, 0.0);
            for (ci, col) in cols.iter().enumerate() {
                let saved: Vec<(Q, Q)> = col.iter().map(|p| (u[p.lu], u[p.lv])).collect();
                for p in col.iter() { refresh(&mut u, p, beta, &mut rng); } let (a1, a4, _) = eval(&u);
                for p in col.iter() { refresh(&mut u, p, beta, &mut rng); } let (b1, b4, _) = eval(&u);
                for (p, s) in col.iter().zip(saved.iter()) { u[p.lu] = s.0; u[p.lv] = s.1; }
                let d1 = 0.5*(a1-b1)*(a1-b1); let d4 = 0.5*(a4-b4)*(a4-b4);
                j1 += d1/24.0; j4 += d4/24.0; colsum1[ci] += d1; colsum4[ci] += d4; }
            cnt += 1.0;
            writeln!(out, "{},{},{:.9},{:.9},{:.9},{:.9},{:.9}", st, m, f1, f4, sp, j1, j4).unwrap(); }
        // P2
        for l in 0..nsite*4 { assert!((norm(&u[l]) - 1.0).abs() < 1e-9); if frozen[l] { assert!(u[l] == u0[l]); } }
        out.flush().unwrap();
    }
    let s1: Vec<String> = colsum1.iter().map(|x| format!("{:.5}", x/cnt)).collect(); let s4: Vec<String> = colsum4.iter().map(|x| format!("{:.5}", x/cnt)).collect();
    writeln!(out, "# percolour_J1 {}", s1.join(" ")).unwrap(); writeln!(out, "# percolour_J4 {}", s4.join(" ")).unwrap();
}
