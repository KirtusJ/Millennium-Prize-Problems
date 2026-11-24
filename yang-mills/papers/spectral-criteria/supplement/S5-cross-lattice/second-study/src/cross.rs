// e2-cross instrument (worker under T231). Built on G4's sampler primitives (g4/wilson_mc.rs, included verbatim).
// Usage: cross BETA SEED HOT(0/1) N(5|10) T BURN NMEAS GAP OUTFILE
// Heat-bath sweeps only (as G4's winding.rs). Measurement every GAP sweeps after BURN sweeps.
// All observables are functions of the COMMON COARSE LINKS of one time slice:
//   N=5: the links themselves; N=10: U(x,mu)U(x+mu,mu) at even x (stride 2, origin 0), spatial mu.
// Coarse slice side is always 5. Observables (K=16), slice averages:
//  0-2  W_mu   = mean over 25 transverse bases of (1/2 Tr prod_{5 coarse links along mu})^2   (G4 convention)
//  3-5  P_i    = mean over 125 coarse sites of coarse plaquette half-trace in plane orthogonal to i (planes (1,2),(0,2),(0,1))
//  6-8  Rc_i   = mean over 125 sites and both orientations of the 2x1 coarse rectangle half-trace in that plane
//  9  Pa1^2, 10 Wa1^2, 11 Wa1*Pa1, 12 Ra1^2, 13 sum_i (P_i-Pa1)^2, 14 sum_i (W_i-Wa1)^2, 15 sum_i W_i*P_i
//  (Pa1, Wa1, Ra1 = means over i.)
// Lag: 1 slice for N=5, 2 slices for N=10 (= l/5); all time origins, periodic wrap.
// Output (file opened create_new; never overwritten):
//   '#' header; 'B,sweep,plaq' burn-in diagnostics every 8 sweeps; 'M,k,plaq,x0..x15' per measurement
//   (x = slice values averaged over all T slices); final 'S1', 'S00', 'SL' rows with raw sums over
//   all measurements and all time origins, 'NS' = number of (measurement,origin) terms.
mod g4 {
    #![allow(dead_code)]
    include!("../g4/wilson_mc.rs");

    const K: usize = 16;

    fn coarse_slice(lat: &Lattice, t: usize) -> Vec<[Q; 3]> {
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
    fn step(i: usize, mu: usize) -> usize {
        let mut c = [i % 5, (i / 5) % 5, i / 25];
        c[mu] = (c[mu] + 1) % 5;
        c[0] + 5 * (c[1] + 5 * c[2])
    }
    fn obs(c: &Vec<[Q; 3]>) -> [f64; K] {
        let mut x = [0.0; K];
        // windings
        for dir in 0..3 {
            let mut acc = 0.0;
            for i in 0..125 {
                let cc = [i % 5, (i / 5) % 5, i / 25];
                if cc[dir] != 0 { continue; }
                let mut y = i; let mut p = ONE;
                for _ in 0..5 { p = mul(p, c[y][dir]); y = step(y, dir); }
                assert_eq!(y, i);
                acc += p[0] * p[0];
            }
            x[dir] = acc / 25.0;
        }
        let planes = [(1usize, 2usize), (0, 2), (0, 1)];
        for (k, &(mu, nu)) in planes.iter().enumerate() {
            let (mut ps, mut rs) = (0.0, 0.0);
            for i in 0..125 {
                let (im, inu) = (step(i, mu), step(i, nu));
                ps += dot(mul(c[i][mu], c[im][nu]), mul(c[i][nu], c[inu][mu]));
                // 2 along mu, 1 along nu
                let imm = step(im, mu);
                let inm = step(inu, mu);
                rs += dot(mul(mul(c[i][mu], c[im][mu]), c[imm][nu]), mul(c[i][nu], mul(c[inu][mu], c[inm][mu])));
                // 2 along nu, 1 along mu
                let inn = step(inu, nu);
                let imn = step(im, nu);
                rs += dot(mul(mul(c[i][nu], c[inu][nu]), c[inn][mu]), mul(c[i][mu], mul(c[im][nu], c[imn][nu])));
            }
            x[3 + k] = ps / 125.0;
            x[6 + k] = rs / 250.0;
        }
        let wa = (x[0] + x[1] + x[2]) / 3.0;
        let pa = (x[3] + x[4] + x[5]) / 3.0;
        let ra = (x[6] + x[7] + x[8]) / 3.0;
        x[9] = pa * pa; x[10] = wa * wa; x[11] = wa * pa; x[12] = ra * ra;
        x[13] = (0..3).map(|i| (x[3 + i] - pa).powi(2)).sum();
        x[14] = (0..3).map(|i| (x[i] - wa).powi(2)).sum();
        x[15] = (0..3).map(|i| x[i] * x[3 + i]).sum();
        x
    }
    fn mean_plaq(lat: &Lattice) -> f64 { lat.action() / (6 * lat.links.len()) as f64 }

    pub fn run() {
        use std::io::Write;
        let a: Vec<String> = env::args().collect();
        assert!(a.len() == 10, "BETA SEED HOT N T BURN NMEAS GAP OUT");
        let beta: f64 = a[1].parse().unwrap();
        let seed: u64 = a[2].parse().unwrap();
        let hot = a[3] == "1";
        let n: usize = a[4].parse().unwrap();
        assert!(n == 5 || n == 10);
        let tt: usize = a[5].parse().unwrap();
        let (burn, nmeas, gap): (usize, usize, usize) = (a[6].parse().unwrap(), a[7].parse().unwrap(), a[8].parse().unwrap());
        let lag = n / 5;
        let mut f = std::fs::OpenOptions::new().write(true).create_new(true).open(&a[9]).expect("result file exists: never overwritten");
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tt, false, hot, &mut rng);
        writeln!(f, "# cross beta={beta} seed={seed} hot={hot} N={n} T={tt} burn={burn} nmeas={nmeas} gap={gap} lag={lag} K={K}").unwrap();
        for s in 0..burn {
            lat.sweep(beta, &mut rng, false);
            if s % 8 == 7 { writeln!(f, "B,{},{:.10}", s + 1, mean_plaq(&lat)).unwrap(); }
        }
        let mut s1 = [0.0f64; K];
        let mut s00 = [[0.0f64; K]; K];
        let mut sl = [[0.0f64; K]; K];
        let mut ns: u64 = 0;
        for m in 0..nmeas {
            for _ in 0..gap { lat.sweep(beta, &mut rng, false); }
            let xs: Vec<[f64; K]> = (0..tt).map(|t| obs(&coarse_slice(&lat, t))).collect();
            let mut avg = [0.0; K];
            for t in 0..tt {
                let (u, v) = (&xs[t], &xs[(t + lag) % tt]);
                for i in 0..K {
                    avg[i] += u[i] / tt as f64;
                    s1[i] += u[i];
                    for j in 0..K { s00[i][j] += u[i] * u[j]; sl[i][j] += u[i] * v[j]; }
                }
                ns += 1;
            }
            write!(f, "M,{},{:.10}", m, mean_plaq(&lat)).unwrap();
            for v in avg { write!(f, ",{:.12e}", v).unwrap(); }
            writeln!(f).unwrap();
        }
        writeln!(f, "NS,{ns}").unwrap();
        write!(f, "S1").unwrap(); for v in s1 { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap();
        for i in 0..K { write!(f, "S00,{i}").unwrap(); for v in s00[i] { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap(); }
        for i in 0..K { write!(f, "SL,{i}").unwrap(); for v in sl[i] { write!(f, ",{:.17e}", v).unwrap(); } writeln!(f).unwrap(); }
        writeln!(f, "END").unwrap();
    }
}
fn main() { g4::run() }
