// a2-mixb Q2 sampler: unconditioned Wilson measure (no frozen links), side n, period T, SU(2).
// Update cycle = one heat-bath sweep + one over-relaxation (reflection) sweep, G4's primitives from wilson_mc.rs
// (same cycle as the prior worker's `gen` mode). Sequential site-by-site update (valid Gibbs sampler).
//
// Marks, for each time slice t and each spatial root r with all three coordinates even (27 roots at n=6):
//   W_c   = coarse 2x2 xy loop at r (path +x,+x,+y,+y,-x,-x,-y,-y)
//   B_c   = coarse 2x2 xz loop at r;  B0_c = (0, b1, b2, b3)/|(b1,b2,b3)|
//   gbar_c = mean over a,b in {0,1} of P U_xy(r + a e_x + b e_y) P^-1, P = links from r along +x a times then +y b times
//   m1 = (B0_c gbar_c)[0]  (= 1/2 Tr, gauge invariant);  theta_c = arccos(-W_c[0])
// Gates g: 0 = all, 1 = theta<0.3, 2 = theta<0.6, 3 = theta<1.2, 4 = theta>1.2 (clear). m_g = m1 * 1[gate].
// Per configuration output line:  plaq, then for g in 0..5: count_g, S1_g = sum m_g, S2_g[t] = sum_{c,t0} m_g(c,t0) m_g(c,t0+t)
// for t = 0..6 (periodic in time), then for g in 1..5: I2_g[t] = sum_{c,t0} 1_g(c,t0) 1_g(c,t0+t), t = 0..6.
//
// Predicates fixed before the first run (asserted in this program; exit != 0 on failure):
//  Q2-P1 gauge invariance: at the first measured configuration, a Haar-random gauge transformation is applied
//        to a copy and all 324 marks m1 and angles theta are recomputed; max deviation <= 1e-10
//        (tolerance: double rounding over ~40 quaternion products, ~1e-14 each, with a wide margin).
//  Q2-P2 the mark at root 0, t=0 equals the prior worker's test `average_tl` formula (B from loop_hol(0,0,2,2),
//        gbar from loop_hol(s,0,1,1) transported) — reimplemented here independently via an explicit path, |diff| <= 1e-12.
mod m {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::Write;

    // product of links along a list of (direction, forward?) steps from x
    fn path(lat: &Lattice, x0: usize, steps: &[(usize, bool)]) -> (Q, usize) {
        let mut h = ONE; let mut x = x0;
        for &(d, fwd) in steps {
            if fwd { h = mul(h, lat.links[x][d]); x = lat.plus[x][d]; }
            else { x = lat.minus[x][d]; h = mul(h, conj(lat.links[x][d])); }
        }
        (h, x)
    }

    fn coarse(lat: &Lattice, r: usize, i: usize, j: usize) -> Q {
        let (h, x) = path(lat, r, &[(i, true), (i, true), (j, true), (j, true), (i, false), (i, false), (j, false), (j, false)]);
        assert_eq!(x, r);
        h
    }

    // returns (m1, theta)
    fn mark(lat: &Lattice, r: usize) -> (f64, f64) {
        let w = coarse(lat, r, 0, 1);
        let b = coarse(lat, r, 0, 2);
        let nim = (b[1] * b[1] + b[2] * b[2] + b[3] * b[3]).sqrt();
        let b0 = [0., b[1] / nim, b[2] / nim, b[3] / nim];
        let mut gbar = [0.; 4];
        for a in 0..2 { for bb in 0..2 {
            let mut steps = Vec::new();
            for _ in 0..a { steps.push((0usize, true)); }
            for _ in 0..bb { steps.push((1usize, true)); }
            let (p, s) = path(lat, r, &steps);
            let (pl, s2) = path(lat, s, &[(0, true), (1, true), (0, false), (1, false)]);
            assert_eq!(s2, s);
            let g = mul(mul(p, pl), conj(p));
            for k in 0..4 { gbar[k] += g[k] / 4.; }
        }}
        (mul(b0, gbar)[0], (-w[0]).clamp(-1., 1.).acos())
    }

    fn roots(n: usize, tp: usize) -> Vec<Vec<usize>> {
        // roots[t] = site indices (x + n y + n^2 z + n^3 t) with x,y,z even
        (0..tp).map(|t| {
            let mut v = Vec::new();
            for z in (0..n).step_by(2) { for y in (0..n).step_by(2) { for x in (0..n).step_by(2) {
                v.push(x + n * y + n * n * z + n * n * n * t);
            }}}
            v
        }).collect()
    }

    fn all_marks(lat: &Lattice, rs: &[Vec<usize>]) -> Vec<Vec<(f64, f64)>> {
        rs.iter().map(|v| v.iter().map(|&r| mark(lat, r)).collect()).collect()
    }

    const GATES: usize = 5;
    fn gate(g: usize, th: f64) -> bool {
        match g { 0 => true, 1 => th < 0.3, 2 => th < 0.6, 3 => th < 1.2, 4 => th > 1.2, _ => unreachable!() }
    }

    fn prior_formula(lat: &Lattice) -> f64 {
        // the prior worker's tests(): loop_hol(x,i,j,len) = len steps +i, len +j, len -i, len -j
        fn loop_hol(lat: &Lattice, x: usize, i: usize, j: usize, len: usize) -> Q {
            let mut h = ONE; let mut y = x;
            for _ in 0..len { h = mul(h, lat.links[y][i]); y = lat.plus[y][i]; }
            for _ in 0..len { h = mul(h, lat.links[y][j]); y = lat.plus[y][j]; }
            for _ in 0..len { y = lat.minus[y][i]; h = mul(h, conj(lat.links[y][i])); }
            for _ in 0..len { y = lat.minus[y][j]; h = mul(h, conj(lat.links[y][j])); }
            h
        }
        let b = loop_hol(lat, 0, 0, 2, 2);
        let im = [0., b[1], b[2], b[3]];
        let nim = dot(im, im).sqrt();
        let btl = im.map(|c| c / nim);
        let mut gbar = [0.; 4];
        for cx in 0..2 { for cy in 0..2 {
            let mut s = 0; let mut p = ONE;
            for _ in 0..cx { p = mul(p, lat.links[s][0]); s = lat.plus[s][0]; }
            for _ in 0..cy { p = mul(p, lat.links[s][1]); s = lat.plus[s][1]; }
            let g = mul(mul(p, loop_hol(lat, s, 0, 1, 1)), conj(p));
            for k in 0..4 { gbar[k] += g[k] / 4.; }
        }}
        mul(btl, gbar)[0]
    }

    pub fn run() {
        let a: Vec<String> = env::args().collect();
        assert_eq!(a.len(), 10, "q2 beta seed hot burn_cycles nconf gap_cycles n T out_prefix");
        let beta: f64 = a[1].parse().unwrap();
        let seed: u64 = a[2].parse().unwrap();
        let hot = a[3] == "1";
        let burn: usize = a[4].parse().unwrap();
        let nconf: usize = a[5].parse().unwrap();
        let gap: usize = a[6].parse().unwrap();
        let n: usize = a[7].parse().unwrap();
        let tp: usize = a[8].parse().unwrap();
        let pre = &a[9];
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, hot, &mut rng);
        let rs = roots(n, tp);
        let mut fo = std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}.txt")).unwrap();
        writeln!(fo, "# args {}", a[1..].join(" ")).unwrap();
        for _ in 0..burn { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
        let half = tp / 2;
        for c in 0..nconf {
            for _ in 0..gap { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
            let mk = all_marks(&lat, &rs);
            if c == 0 {
                // Q2-P1 gauge invariance
                let mut gr = Rng { state: seed ^ 0x5bd1e995 };
                let gt: Vec<Q> = (0..lat.links.len()).map(|_| gr.haar()).collect();
                let mut cp = Lattice::new(n, tp, false, false, &mut gr);
                for x in 0..lat.links.len() { for mu in 0..4 {
                    cp.links[x][mu] = mul(mul(gt[x], lat.links[x][mu]), conj(gt[lat.plus[x][mu]]));
                }}
                let mk2 = all_marks(&cp, &rs);
                let mut dev: f64 = 0.;
                for t in 0..tp { for k in 0..rs[t].len() {
                    dev = dev.max((mk[t][k].0 - mk2[t][k].0).abs()).max((mk[t][k].1 - mk2[t][k].1).abs());
                }}
                eprintln!("Q2-P1 max gauge deviation {dev:e}");
                assert!(dev <= 1e-10, "Q2-P1 gauge invariance failed");
                // Q2-P2 agreement with the prior formula at root 0, t = 0
                let d2 = (prior_formula(&lat) - mk[0][0].0).abs();
                eprintln!("Q2-P2 deviation from prior formula {d2:e}");
                assert!(d2 <= 1e-12, "Q2-P2 failed");
            }
            let mut pl = 0.;
            for x in 0..lat.links.len() { for mu in 0..4 { for nu in 0..mu { pl += lat.plaquette(x, mu, nu); } } }
            pl /= (6 * lat.links.len()) as f64;
            let mut line = format!("{pl:.9}");
            let nr = rs[0].len();
            for g in 0..GATES {
                let mut cnt = 0usize; let mut s1 = 0.; let mut s2 = [0.; 7];
                for t0 in 0..tp { for k in 0..nr {
                    let (m0, th0) = mk[t0][k];
                    if !gate(g, th0) { continue; }
                    cnt += 1; s1 += m0;
                    for dt in 0..=half {
                        let (m1, th1) = mk[(t0 + dt) % tp][k];
                        if gate(g, th1) { s2[dt] += m0 * m1; }
                    }
                }}
                line += &format!(" {cnt} {s1:.10e}");
                for v in s2 { line += &format!(" {v:.10e}"); }
            }
            for g in 1..GATES {
                let mut i2 = [0usize; 7];
                for t0 in 0..tp { for k in 0..nr {
                    if !gate(g, mk[t0][k].1) { continue; }
                    for dt in 0..=half { if gate(g, mk[(t0 + dt) % tp][k].1) { i2[dt] += 1; } }
                }}
                for v in i2 { line += &format!(" {v}"); }
            }
            writeln!(fo, "{line}").unwrap();
        }
    }
}
fn main() { m::run(); }
