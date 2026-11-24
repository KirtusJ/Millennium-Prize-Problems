// f2-cross2 instrument (worker T239, Director Z4). Built on G4's sampler (g4/wilson_mc.rs, included verbatim).
// Usage:  cross2 run BETA SEED HOT(0/1) N(5|10) T BURN NMEAS GAP OUTFILE
//         cross2 selftest BETA SEED N T OUTFILE
// Heat-bath sweeps only (as G4's winding.rs). Measurement every GAP sweeps after BURN sweeps.
// COMMON COARSE LINKS of a time slice: N=5 the links; N=10 U(x,mu)U(x+mu,mu), x on the stride-2 grid (origin 0), mu spatial.
// Coarse slice is 5^3 on both lattices. Lag = 1 slice (N=5), 2 slices (N=10) = l/5; all T time origins, periodic wrap.
// LOCAL FIELDS x_s (KL=54) anchored at coarse site s (all half-traces of closed coarse loops, squared windings, products):
//   0-2  w_mu(s) = (1/2 Tr W_mu(line through s))^2           3-5  p_k(s) plaquette, plane orthogonal to k: (1,2),(0,2),(0,1)
//   6-11 rect: plane k, 6+2k = 2 along first dir x 1 along second, 7+2k = 1 x 2
//   12-17 chair (mu,nu,rho) for the 6 permutations of (0,1,2): path mu, nu, -mu, rho, -nu, -rho
//   18-23 h_mu(s) h_mu(s+nu) (h = 1/2 Tr W, neighbouring parallel lines), (mu,nu) = (0,1),(0,2),(1,0),(1,2),(2,0),(2,1)
//   24-29 w_mu(s) w_mu(s+nu), same order          30-32 w_mu^2     33-35 p_k^2     36-38 w_mu p_mu
//   39-41 p0p1, p0p2, p1p2                        42-53 indicator[w_mu in bin b], index 42+4mu+b, bins [0,.25),[.25,.5),[.5,.75),[.75,1]
// CLASSES of time-slice functions, each with raw sums S1, S00, SL (SL[i][j] = sum x_i(t) x_j(t+lag)):
//   L  : local, sums over all 125 sites s (translation-averaged same-position correlator); NS_L = 125*T*NMEAS
//   Z  : slice averages X(t) = (1/125) sum_s x_s (zero momentum); NS = T*NMEAS
//   Pk : k=0,1,2: Xc = (1/125) sum_s cos(2 pi s_k/5) x_s, Xs likewise with sin; S00 += XcXc^T+XsXs^T, SL likewise
//        (translation average of the cos-projected function); S1 sums Xc only (expected 0). NS = T*NMEAS
//   J  : G4 joint histogram: 4x4 counts of (bin w(line,t), bin w(line,t+lag)) pooled over the 75 lines and all origins.
// Output file opened create_new (never overwritten).
mod g4 {
    #![allow(dead_code)]
    include!("../g4/wilson_mc.rs");

    pub const KL: usize = 54;

    pub fn coarse_slice(lat: &Lattice, t: usize) -> Vec<[Q; 3]> {
        let n = lat.l;
        let s = n / 5;
        let mut out = vec![[ONE; 3]; 125];
        for c2 in 0..5 { for c1 in 0..5 { for c0 in 0..5 {
            let x = s * c0 + n * (s * c1 + n * (s * c2)) + n * n * n * t;
            for mu in 0..3 {
                let mut y = x;
                let mut p = ONE;
                for _ in 0..s { p = mul(p, lat.links[y][mu]); y = lat.plus[y][mu]; }
                out[c0 + 5 * (c1 + 5 * c2)][mu] = p;
            }
        }}}
        out
    }
    pub fn step(i: usize, mu: usize) -> usize {
        let mut c = [i % 5, (i / 5) % 5, i / 25];
        c[mu] = (c[mu] + 1) % 5;
        c[0] + 5 * (c[1] + 5 * c[2])
    }
    pub fn coord(i: usize) -> [usize; 3] { [i % 5, (i / 5) % 5, i / 25] }
    pub fn bin(w: f64) -> usize { ((4.0 * w).floor() as i64).clamp(0, 3) as usize }

    /// half-traces of windings h[mu][s] (line through s, started at s)
    pub fn windings(c: &Vec<[Q; 3]>) -> [[f64; 125]; 3] {
        let mut h = [[0.0; 125]; 3];
        for mu in 0..3 { for i in 0..125 {
            let mut y = i; let mut p = ONE;
            for _ in 0..5 { p = mul(p, c[y][mu]); y = step(y, mu); }
            assert_eq!(y, i);
            h[mu][i] = p[0];
        }}
        h
    }

    pub fn local(c: &Vec<[Q; 3]>) -> Vec<[f64; KL]> {
        let h = windings(c);
        let planes = [(1usize, 2usize), (0, 2), (0, 1)];
        let pairs = [(0usize, 1usize), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)];
        let perms = [(0usize, 1usize, 2usize), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)];
        let mut out = vec![[0.0; KL]; 125];
        for i in 0..125 {
            let x = &mut out[i];
            for mu in 0..3 { x[mu] = h[mu][i] * h[mu][i]; }
            for (k, &(mu, nu)) in planes.iter().enumerate() {
                let (im, inu) = (step(i, mu), step(i, nu));
                x[3 + k] = dot(mul(c[i][mu], c[im][nu]), mul(c[i][nu], c[inu][mu]));
                let imm = step(im, mu); let inm = step(inu, mu);
                x[6 + 2 * k] = dot(mul(mul(c[i][mu], c[im][mu]), c[imm][nu]), mul(c[i][nu], mul(c[inu][mu], c[inm][mu])));
                let inn = step(inu, nu); let imn = step(im, nu);
                x[7 + 2 * k] = dot(mul(mul(c[i][nu], c[inu][nu]), c[inn][mu]), mul(c[i][mu], mul(c[im][nu], c[imn][nu])));
            }
            for (k, &(mu, nu, rho)) in perms.iter().enumerate() {
                let im = step(i, mu); let inu = step(i, nu); let inr = step(inu, rho); let ir = step(i, rho);
                // A = U_mu(i) U_nu(i+mu) U_mu(i+nu)^+ U_rho(i+nu) ; B = U_rho(i) U_nu(i+rho) ; 1/2 Tr A B^+
                let a = mul(mul(mul(c[i][mu], c[im][nu]), conj(c[inu][mu])), c[inu][rho]);
                let b = mul(c[i][rho], c[ir][nu]);
                let _ = inr;
                x[12 + k] = dot(a, b);
            }
            for (k, &(mu, nu)) in pairs.iter().enumerate() {
                let j = step(i, nu);
                x[18 + k] = h[mu][i] * h[mu][j];
                x[24 + k] = x[mu] * h[mu][j] * h[mu][j];
            }
            for mu in 0..3 { x[30 + mu] = x[mu] * x[mu]; x[33 + mu] = x[3 + mu] * x[3 + mu]; x[36 + mu] = x[mu] * x[3 + mu]; }
            x[39] = x[3] * x[4]; x[40] = x[3] * x[5]; x[41] = x[4] * x[5];
            for mu in 0..3 { x[42 + 4 * mu + bin(x[mu])] = 1.0; }
        }
        out
    }
    fn mean_plaq(lat: &Lattice) -> f64 { lat.action() / (6 * lat.links.len()) as f64 }

    struct Acc { s1: Vec<f64>, s00: Vec<f64>, sl: Vec<f64>, ns: u64 }
    impl Acc {
        fn new() -> Self { Acc { s1: vec![0.0; KL], s00: vec![0.0; KL * KL], sl: vec![0.0; KL * KL], ns: 0 } }
        fn add(&mut self, u: &[f64; KL], v: &[f64; KL], s1: bool) {
            if s1 { for i in 0..KL { self.s1[i] += u[i]; } }
            for i in 0..KL { let ui = u[i]; if ui == 0.0 { continue; }
                let r0 = &mut self.s00[i * KL..(i + 1) * KL]; for j in 0..KL { r0[j] += ui * u[j]; }
                let r1 = &mut self.sl[i * KL..(i + 1) * KL]; for j in 0..KL { r1[j] += ui * v[j]; } }
        }
        fn write(&self, f: &mut std::fs::File, tag: &str) {
            use std::io::Write;
            writeln!(f, "{tag}NS,{}", self.ns).unwrap();
            write!(f, "{tag}S1").unwrap(); for v in &self.s1 { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap();
            for i in 0..KL { write!(f, "{tag}S00,{i}").unwrap(); for v in &self.s00[i * KL..(i + 1) * KL] { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap(); }
            for i in 0..KL { write!(f, "{tag}SL,{i}").unwrap(); for v in &self.sl[i * KL..(i + 1) * KL] { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap(); }
        }
    }

    fn all_local(lat: &Lattice) -> Vec<Vec<[f64; KL]>> { (0..lat.time).map(|t| local(&coarse_slice(lat, t))).collect() }

    fn selftest(a: &Vec<String>) {
        use std::io::Write;
        let beta: f64 = a[2].parse().unwrap(); let seed: u64 = a[3].parse().unwrap();
        let n: usize = a[4].parse().unwrap(); let tt: usize = a[5].parse().unwrap();
        let mut f = std::fs::OpenOptions::new().write(true).create_new(true).open(&a[6]).expect("result file exists: never overwritten");
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tt, false, true, &mut rng);
        for _ in 0..20 { lat.sweep(beta, &mut rng, false); }
        let base = all_local(&lat);
        let ctrl = |l: &Lattice| { let c = coarse_slice(l, 0); (windings(&c)[0][0], c[0][0][1]) };
        let (h0, l0) = ctrl(&lat);
        let maxdiff = |x: &Vec<Vec<[f64; KL]>>| { let mut m: f64 = 0.0; for t in 0..x.len() { for s in 0..125 { for k in 0..KL { m = m.max((x[t][s][k] - base[t][s][k]).abs()); } } } m };
        writeln!(f, "# selftest beta={beta} seed={seed} N={n} T={tt} KL={KL}; tolerance 1e-12 on max |delta| over all fields, sites, slices").unwrap();
        // random gauge transformation on every fine site: U(x,mu) -> V(x) U(x,mu) V(x+mu)^+
        let mut g = Lattice::new(n, tt, false, false, &mut rng); g.links = lat.links.clone();
        let v: Vec<Q> = (0..lat.links.len()).map(|_| rng.haar()).collect();
        for x in 0..lat.links.len() { for mu in 0..4 { g.links[x][mu] = mul(mul(v[x], lat.links[x][mu]), conj(v[lat.plus[x][mu]])); } }
        let (gh, gl) = ctrl(&g);
        writeln!(f, "GAUGE maxdiff={:.3e} control_link_component_change={:.3e} control_winding_change={:.3e}", maxdiff(&all_local(&g)), (gl - l0).abs(), (gh - h0).abs()).unwrap();
        // center flips: links in direction mu with fine coordinate x_mu = cpos multiplied by -1
        for mu in 0..4 {
            let size = if mu < 3 { n } else { tt };
            let cpos = (rng.u() * size as f64) as usize % size;
            let mut z = Lattice::new(n, tt, false, false, &mut rng); z.links = lat.links.clone();
            let strides = [1, n, n * n, n * n * n];
            for x in 0..lat.links.len() { if (x / strides[mu]) % size == cpos { z.links[x][mu] = z.links[x][mu].map(|q| -q); } }
            let (zh, _) = ctrl(&z);
            writeln!(f, "CENTER mu={mu} pos={cpos} maxdiff={:.3e} control_h_x(line at s=0)_change={:.3e}", maxdiff(&all_local(&z)), (zh - h0).abs()).unwrap();
        }
        writeln!(f, "END").unwrap();
    }

    pub fn run() {
        use std::io::Write;
        let a: Vec<String> = env::args().collect();
        if a[1] == "selftest" { assert!(a.len() == 7); selftest(&a); return; }
        assert!(a.len() == 11 && a[1] == "run", "run BETA SEED HOT N T BURN NMEAS GAP OUT");
        let beta: f64 = a[2].parse().unwrap();
        let seed: u64 = a[3].parse().unwrap();
        let hot = a[4] == "1";
        let n: usize = a[5].parse().unwrap();
        assert!(n == 5 || n == 10);
        let tt: usize = a[6].parse().unwrap();
        let (burn, nmeas, gap): (usize, usize, usize) = (a[7].parse().unwrap(), a[8].parse().unwrap(), a[9].parse().unwrap());
        let lag = n / 5;
        let mut f = std::fs::OpenOptions::new().write(true).create_new(true).open(&a[10]).expect("result file exists: never overwritten");
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tt, false, hot, &mut rng);
        writeln!(f, "# cross2 beta={beta} seed={seed} hot={hot} N={n} T={tt} burn={burn} nmeas={nmeas} gap={gap} lag={lag} KL={KL}").unwrap();
        for s in 0..burn {
            lat.sweep(beta, &mut rng, false);
            if s % 8 == 7 { writeln!(f, "B,{},{:.10}", s + 1, mean_plaq(&lat)).unwrap(); }
        }
        let mut al = Acc::new(); let mut az = Acc::new();
        let mut ap = [Acc::new(), Acc::new(), Acc::new()];
        let mut jh = [[0u64; 4]; 4];
        let cs: Vec<[f64; 3]> = (0..125).map(|s| { let c = coord(s); [0, 1, 2].map(|k| (std::f64::consts::TAU * c[k] as f64 / 5.0).cos()) }).collect();
        let sn: Vec<[f64; 3]> = (0..125).map(|s| { let c = coord(s); [0, 1, 2].map(|k| (std::f64::consts::TAU * c[k] as f64 / 5.0).sin()) }).collect();
        for m in 0..nmeas {
            for _ in 0..gap { lat.sweep(beta, &mut rng, false); }
            let xs = all_local(&lat);
            let mut z = vec![[0.0; KL]; tt];
            let mut pc = vec![[[0.0; KL]; 3]; tt];
            let mut ps = vec![[[0.0; KL]; 3]; tt];
            for t in 0..tt { for s in 0..125 { for k in 0..KL {
                let v = xs[t][s][k] / 125.0;
                z[t][k] += v;
                for d in 0..3 { pc[t][d][k] += v * cs[s][d]; ps[t][d][k] += v * sn[s][d]; }
            }}}
            for t in 0..tt {
                let t2 = (t + lag) % tt;
                for s in 0..125 { al.add(&xs[t][s], &xs[t2][s], true); al.ns += 1; }
                for mu in 0..3 { for s in 0..125 { if coord(s)[mu] != 0 { continue; }
                    jh[bin(xs[t][s][mu])][bin(xs[t2][s][mu])] += 1; } }
                az.add(&z[t], &z[t2], true); az.ns += 1;
                for d in 0..3 { ap[d].add(&pc[t][d], &pc[t2][d], true); ap[d].add(&ps[t][d], &ps[t2][d], false); ap[d].ns += 1; }
            }
            let wa: f64 = (0..tt).map(|t| (z[t][0] + z[t][1] + z[t][2]) / 3.0).sum::<f64>() / tt as f64;
            let pa: f64 = (0..tt).map(|t| (z[t][3] + z[t][4] + z[t][5]) / 3.0).sum::<f64>() / tt as f64;
            writeln!(f, "M,{},{:.10},{:.12e},{:.12e}", m, mean_plaq(&lat), wa, pa).unwrap();
        }
        al.write(&mut f, "L"); az.write(&mut f, "Z");
        for d in 0..3 { ap[d].write(&mut f, &format!("P{d}")); }
        for i in 0..4 { writeln!(f, "J,{i},{},{},{},{}", jh[i][0], jh[i][1], jh[i][2], jh[i][3]).unwrap(); }
        writeln!(f, "END").unwrap();
    }
}
fn main() { g4::run() }
