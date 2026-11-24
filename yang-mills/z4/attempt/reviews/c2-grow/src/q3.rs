// c2-grow Q2 sampler (q3): unconditioned Wilson measure, side n, period T, SU(2); cycle = 1 heat-bath + 1 over-relaxation
// sweep (G4's primitives, same cycle as the prior q2). Composite mark from a weight file (name value per line; names as z1mx4:
// R.face.kind with R in {B, T}, face = plane + base digits, kind in {g00,g10,g01,g11,Rv,Rh,L_no11}).
// For every time slice t, every root r with even spatial coordinates (27 at n=6) and every one of the 48 orientations o
// (signed permutations of the spatial axes, applied to every step of every loop):
//   B_c = mapped coarse xz loop at r, B0 = normalised traceless part; X_i = Re(B0 L_i) (R=B) or Re(L_i) (R=T), L_i mapped loop.
//   gate angle th = max over the three gate faces (mapped coarse loops of xy000, xy200, yz204: the -I faces on the skeleton)
//   of arccos(-Re h). Gates: th < 0.6, th < 1.2.  comp = sum_i w_i X_i ; single = Re(B0 gbar) (four-face mark of the marked square).
// Gated marks m = mark * 1[gate] over all (r, o, t). Ungated marks: identity orientation only (27 roots x T slices), by the
// lattice symmetry of the measure every orientation has the same law (stated hypothesis; avoids 48x cost).
// Output per configuration (one line): plaq, then for g in {0.6, 1.2}: count, then for mark in {comp, single}: S1, S2[t] t=0..4
// (sum over (r,o,t0) of m(t0) m(t0+t), periodic), then I2[t] t=0..4 (gated pairs); then ungated: count, comp S1 S2[0..4], single S1 S2[0..4].
// Predicates fixed before the first run (asserted; exit != 0 on failure):
//  Q3-P1 gauge invariance at the first configuration: composite and gate angle of every (r, o) on slice 0 change by <= 1e-10
//        under a Haar-random gauge transformation (tolerance: rounding over ~50 products).
//  Q3-P2 the identity-orientation single mark at root 0, slice 0 equals the prior q2 formula (B0 from loop_hol(0,0,2,2), gbar
//        transported +x^a +y^b) to 1e-12.
//  Q3-P3 the 48 orientations are distinct and every mapped loop closes (assert in closed()).
//  Q3-P4 identity orientation, root 0: X_i with B0 replaced by the full B equals z1mx4's marks formula Re(B L_i) (same loops) to 1e-12.
mod m {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::Write;
    fn path(lat: &Lattice, x0: usize, steps: &[usize]) -> (Q, usize) {
        let mut h = ONE; let mut y = x0;
        for &s in steps {
            if s < 4 { h = mul(h, lat.links[y][s]); y = lat.plus[y][s]; }
            else { y = lat.minus[y][s - 4]; h = mul(h, conj(lat.links[y][s - 4])); }
        }
        (h, y)
    }
    fn closed(lat: &Lattice, r: usize, steps: &[usize]) -> Q { let (h, y) = path(lat, r, steps); assert_eq!(y, r, "loop not closed"); h }
    fn inv(steps: &[usize]) -> Vec<usize> { steps.iter().rev().map(|&s| (s + 4) % 8).collect() }
    fn tail(b: [usize; 3]) -> Vec<usize> {
        let mut t = Vec::new();
        for d in 0..3 { match b[d] { 0 => {}, 2 => { t.push(d); t.push(d); }, 4 => { t.push(d + 4); t.push(d + 4); }, _ => panic!() } }
        t
    }
    // same construction as z1mx4 face_loops
    fn loop_of(face: &str, kind: &str) -> Vec<usize> {
        let pl = match &face[0..2] { "xy" => (0usize, 1usize), "xz" => (0, 2), "yz" => (1, 2), _ => panic!("face") };
        let b: [usize; 3] = std::array::from_fn(|k| face[2 + k..3 + k].parse().unwrap());
        let (a, c) = pl; let t0 = tail(b);
        let inner = match kind {
            "Rv" => vec![a, c, c, a + 4, c + 4, c + 4],
            "Rh" => vec![a, a, c, a + 4, a + 4, c + 4],
            "L_no11" => vec![a, a, c, a + 4, c, a + 4, c + 4, c + 4],
            "coarse" => vec![a, a, c, c, a + 4, a + 4, c + 4, c + 4],
            g => { let ca: usize = g[1..2].parse().unwrap(); let cb: usize = g[2..3].parse().unwrap();
                   let mut tt = vec![a; ca]; tt.extend(vec![c; cb]); let mut s = tt.clone(); s.extend([a, c, a + 4, c + 4]); s.extend(inv(&tt)); s }
        };
        let mut s = t0.clone(); s.extend(inner); s.extend(inv(&t0)); s
    }
    fn orientations() -> Vec<([usize; 3], [bool; 3])> {
        let perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]];
        let mut v = Vec::new();
        for p in perms { for sg in 0..8 { v.push((p, [sg & 1 == 1, sg & 2 == 2, sg & 4 == 4])); } }
        v
    }
    fn map_steps(o: &([usize; 3], [bool; 3]), s: &[usize]) -> Vec<usize> {
        s.iter().map(|&st| { let d = st % 4; let fwd = st < 4; let nd = o.0[d]; let f2 = fwd ^ o.1[nd]; if f2 { nd } else { nd + 4 } }).collect()
    }
    struct Geo { marks: Vec<(usize, Vec<usize>)>, w: Vec<f64>, bl: Vec<usize>, gates: Vec<Vec<usize>>, plaq: Vec<Vec<usize>> }
    fn unit_im(b: Q) -> Q { let n = (b[1] * b[1] + b[2] * b[2] + b[3] * b[3]).sqrt(); [0., b[1] / n, b[2] / n, b[3] / n] }
    // returns (comp, single, gate angle)
    fn eval(lat: &Lattice, r: usize, g: &Geo, want_comp: bool) -> (f64, f64, f64) {
        let mut th: f64 = 0.;
        for gl in &g.gates { let h = closed(lat, r, gl); th = th.max((-h[0]).clamp(-1., 1.).acos()); }
        let b0 = unit_im(closed(lat, r, &g.bl));
        let mut gbar = [0.; 4];
        for pl in &g.plaq { let q = closed(lat, r, pl); for k in 0..4 { gbar[k] += q[k] / 4.; } }
        let single = mul(b0, gbar)[0];
        let mut comp = 0.;
        if want_comp { for (k, (rf, s)) in g.marks.iter().enumerate() { let l = closed(lat, r, s); comp += g.w[k] * if *rf == 0 { mul(b0, l)[0] } else { l[0] }; } }
        (comp, single, th)
    }
    pub fn run() {
        let a: Vec<String> = env::args().collect();
        assert_eq!(a.len(), 11, "q3 beta seed hot burn nconf gap n T wfile out");
        let beta: f64 = a[1].parse().unwrap(); let seed: u64 = a[2].parse().unwrap(); let hot = a[3] == "1";
        let burn: usize = a[4].parse().unwrap(); let nconf: usize = a[5].parse().unwrap(); let gap: usize = a[6].parse().unwrap();
        let n: usize = a[7].parse().unwrap(); let tp: usize = a[8].parse().unwrap(); let pre = &a[10];
        let mut names = Vec::new(); let mut w0 = Vec::new();
        for line in std::fs::read_to_string(&a[9]).unwrap().lines() {
            let f: Vec<&str> = line.split_whitespace().collect(); if f.len() != 2 { continue; }
            names.push(f[0].to_string()); w0.push(f[1].parse::<f64>().unwrap());
        }
        let ors = orientations();
        for i in 0..48 { for j in 0..i { assert!(ors[i] != ors[j], "Q3-P3 orientations"); } }
        let base: Vec<(usize, Vec<usize>)> = names.iter().map(|nm| { let p: Vec<&str> = nm.split('.').collect(); (if p[0] == "B" { 0 } else { 1 }, loop_of(p[1], p[2])) }).collect();
        let geos: Vec<Geo> = ors.iter().map(|o| Geo {
            marks: base.iter().map(|(rf, s)| (*rf, map_steps(o, s))).collect(), w: w0.clone(),
            bl: map_steps(o, &loop_of("xz000", "coarse")),
            gates: ["xy000", "xy200", "yz204"].iter().map(|f| map_steps(o, &loop_of(f, "coarse"))).collect(),
            plaq: ["g00", "g10", "g01", "g11"].iter().map(|k| map_steps(o, &loop_of("xy000", k))).collect() }).collect();
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, hot, &mut rng);
        let roots: Vec<Vec<usize>> = (0..tp).map(|t| { let mut v = Vec::new();
            for z in (0..n).step_by(2) { for y in (0..n).step_by(2) { for x in (0..n).step_by(2) { v.push(x + n * y + n * n * z + n * n * n * t); } } } v }).collect();
        let nr = roots[0].len(); let no = ors.len();
        let mut fo = std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}.txt")).unwrap();
        writeln!(fo, "# args {} ; marks {}", a[1..].join(" "), names.len()).unwrap();
        for _ in 0..burn { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
        let thetas = [0.6f64, 1.2];
        for c in 0..nconf {
            for _ in 0..gap { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
            // pass 1: gate angles and single marks for all (t, r, o); composite only where th < 1.2
            let mut ev = vec![(0f64, 0f64, 0f64); tp * nr * no];
            for t in 0..tp { for k in 0..nr { for o in 0..no {
                let (_, s, th) = eval(&lat, roots[t][k], &geos[o], false);
                let comp = if th < 1.2 { eval(&lat, roots[t][k], &geos[o], true).0 } else { 0. };
                ev[(t * nr + k) * no + o] = (comp, s, th);
            }}}
            if c == 0 {
                let mut gr = Rng { state: seed ^ 0x5bd1e995 };
                let gt: Vec<Q> = (0..lat.links.len()).map(|_| gr.haar()).collect();
                let mut cp = Lattice::new(n, tp, false, false, &mut gr);
                for x in 0..lat.links.len() { for mu in 0..4 { cp.links[x][mu] = mul(mul(gt[x], lat.links[x][mu]), conj(gt[lat.plus[x][mu]])); } }
                let mut dev: f64 = 0.;
                for k in 0..nr { for o in 0..no {
                    let e1 = eval(&lat, roots[0][k], &geos[o], true); let e2 = eval(&cp, roots[0][k], &geos[o], true);
                    dev = dev.max((e1.0 - e2.0).abs()).max((e1.1 - e2.1).abs()).max((e1.2 - e2.2).abs());
                }}
                eprintln!("Q3-P1 max gauge deviation {dev:e}"); assert!(dev <= 1e-10, "Q3-P1");
                // P2: prior q2 formula
                fn loop_hol(lat: &Lattice, x: usize, i: usize, j: usize, len: usize) -> Q {
                    let mut h = ONE; let mut y = x;
                    for _ in 0..len { h = mul(h, lat.links[y][i]); y = lat.plus[y][i]; }
                    for _ in 0..len { h = mul(h, lat.links[y][j]); y = lat.plus[y][j]; }
                    for _ in 0..len { y = lat.minus[y][i]; h = mul(h, conj(lat.links[y][i])); }
                    for _ in 0..len { y = lat.minus[y][j]; h = mul(h, conj(lat.links[y][j])); }
                    h
                }
                let b = loop_hol(&lat, 0, 0, 2, 2); let btl = unit_im(b);
                let mut gbar = [0.; 4];
                for cx in 0..2 { for cy in 0..2 { let mut s = 0; let mut p = ONE;
                    for _ in 0..cx { p = mul(p, lat.links[s][0]); s = lat.plus[s][0]; }
                    for _ in 0..cy { p = mul(p, lat.links[s][1]); s = lat.plus[s][1]; }
                    let g = mul(mul(p, loop_hol(&lat, s, 0, 1, 1)), conj(p)); for k in 0..4 { gbar[k] += g[k] / 4.; } } }
                let id = ors.iter().position(|o| o.0 == [0, 1, 2] && o.1 == [false, false, false]).unwrap();
                let d2 = (mul(btl, gbar)[0] - eval(&lat, 0, &geos[id], false).1).abs();
                eprintln!("Q3-P2 deviation {d2:e}"); assert!(d2 <= 1e-12, "Q3-P2");
                // P4: identity orientation marks with full B vs z1mx4 formula (independent path code: loop_hol for B)
                let mut d4: f64 = 0.;
                for (rf, s) in &base { let l = closed(&lat, 0, s); let v = if *rf == 0 { mul(b, l)[0] } else { l[0] };
                    let l2 = closed(&lat, 0, &geos[id].marks.iter().find(|m| &m.1 == s).unwrap().1); let v2 = if *rf == 0 { mul(closed(&lat, 0, &geos[id].bl), l2)[0] } else { l2[0] };
                    d4 = d4.max((v - v2).abs()); }
                eprintln!("Q3-P4 deviation {d4:e}"); assert!(d4 <= 1e-12, "Q3-P4");
            }
            let mut pl = 0.;
            for x in 0..lat.links.len() { for mu in 0..4 { for nu in 0..mu { pl += lat.plaquette(x, mu, nu); } } }
            pl /= (6 * lat.links.len()) as f64;
            let mut line = format!("{pl:.9}");
            let idx = |t: usize, k: usize, o: usize| ((t % tp) * nr + k) * no + o;
            for &th in &thetas {
                let mut cnt = 0usize; let mut s1 = [0f64; 2]; let mut s2 = [[0f64; 5]; 2]; let mut i2 = [0usize; 5];
                for t0 in 0..tp { for k in 0..nr { for o in 0..no {
                    let e0 = ev[idx(t0, k, o)]; if e0.2 >= th { continue; }
                    cnt += 1; s1[0] += e0.0; s1[1] += e0.1;
                    for dt in 0..5 { let e1 = ev[idx(t0 + dt, k, o)]; if e1.2 < th { i2[dt] += 1; s2[0][dt] += e0.0 * e1.0; s2[1][dt] += e0.1 * e1.1; } }
                }}}
                line += &format!(" {cnt}");
                for m in 0..2 { line += &format!(" {:.10e}", s1[m]); for v in s2[m] { line += &format!(" {v:.10e}"); } }
                for v in i2 { line += &format!(" {v}"); }
            }
            // ungated, identity orientation only: composite for all roots
            let id = ors.iter().position(|o| o.0 == [0, 1, 2] && o.1 == [false, false, false]).unwrap();
            let comp_u: Vec<f64> = (0..tp).flat_map(|t| (0..nr).map(move |k| (t, k))).map(|(t, k)| eval(&lat, roots[t][k], &geos[id], true).0).collect();
            let mut s1 = [0f64; 2]; let mut s2 = [[0f64; 5]; 2];
            for t0 in 0..tp { for k in 0..nr {
                let v0 = [comp_u[t0 * nr + k], ev[idx(t0, k, id)].1];
                s1[0] += v0[0]; s1[1] += v0[1];
                for dt in 0..5 { let t1 = (t0 + dt) % tp; let v1 = [comp_u[t1 * nr + k], ev[idx(t1, k, id)].1]; s2[0][dt] += v0[0] * v1[0]; s2[1][dt] += v0[1] * v1[1]; }
            }}
            line += &format!(" {}", tp * nr);
            for m in 0..2 { line += &format!(" {:.10e}", s1[m]); for v in s2[m] { line += &format!(" {v:.10e}"); } }
            writeln!(fo, "{line}").unwrap();
        }
    }
}
fn main() { m::run(); }
