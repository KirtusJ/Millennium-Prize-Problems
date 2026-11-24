// z1-mix6 own sampler. Reuses only the quaternion/Rng/Lattice/heat-bath primitives of
// wilson_mc.rs (G4's file, copied unchanged, validated by the control). Everything else
// (skeleton loading, colours, pair draw, tests, per-colour loss, clearance, generator) is written here.
//
// Predicates fixed before the first run (checked in this program by assert!, exit != 0 on failure):
//  P1 colours: 24 colours, each with N^3/8 * ... = 27 pairs at N=6 (all N^3*3/24); no pair link is frozen;
//     within one colour no link occurs twice and no plaquette of the 4D lattice contains links of two
//     different pairs of the same colour (so sequential pair draws = joint exact draw).
//  P2 the frozen links are unchanged after every measurement (bitwise).
//  P3 the pair-draw acceptance exponent beta*(ReU_p-1) <= 0 (tolerance 1e-12, float rounding).
//  P4 (checked outside, in run.py) at a skeleton equal to G4's (W=-I, B=i) and G4's seeds, the first
//     five output columns are byte-identical to build/g4_replicas on this machine.
mod m {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::Write;

    type Link = (usize, usize);
    #[derive(Clone, Copy)]
    struct Pair { x: usize, i: usize, j: usize, u: Link, v: Link }

    fn coords(n: usize, x: usize) -> [usize; 3] { [x % n, (x / n) % n, x / (n * n)] }

    fn is_frozen(n: usize, x: usize, i: usize) -> bool {
        if x >= n.pow(3) || i == 3 { return false; }
        let c = coords(n, x);
        (0..3).all(|k| k == i || c[k] % 2 == 0)
    }

    fn make_colours(lat: &Lattice) -> Vec<Vec<Pair>> {
        let n = lat.l;
        let mut g: Vec<Vec<Pair>> = (0..24).map(|_| Vec::new()).collect();
        for x in 0..n.pow(3) {
            let c = coords(n, x);
            let p = [c[0] % 2, c[1] % 2, c[2] % 2];
            let planes = [(0usize, 1usize), (0, 2), (1, 2)];
            for o in 0..3 {
                let (i, j) = planes[o];
                // the i-link of the fine plaquette with odd j-coordinate, and the j-link with odd i-coordinate
                let u = (if p[j] == 1 { x } else { lat.plus[x][j] }, i);
                let v = (if p[i] == 1 { x } else { lat.plus[x][i] }, j);
                g[8 * o + p[0] + 2 * p[1] + 4 * p[2]].push(Pair { x, i, j, u, v });
            }
        }
        g
    }

    fn plaq_links(lat: &Lattice, x: usize, a: usize, b: usize) -> [Link; 4] {
        [(x, a), (lat.plus[x][a], b), (lat.plus[x][b], a), (x, b)]
    }

    fn check_colours(lat: &Lattice, cols: &[Vec<Pair>]) {
        let n = lat.l;
        let rows = lat.links.len();
        assert_eq!(cols.len(), 24);
        // owner[link] = pair id within the colour
        for col in cols {
            assert_eq!(col.len(), 3 * n.pow(3) / 24);
            let mut owner = vec![[usize::MAX; 4]; rows];
            for (k, p) in col.iter().enumerate() {
                for &(s, d) in &[p.u, p.v] {
                    assert!(!is_frozen(n, s, d), "pair link frozen");
                    assert_eq!(owner[s][d], usize::MAX, "link twice in a colour");
                    owner[s][d] = k;
                }
                // the common plaquette is the fine plaquette at x in plane (i,j)
                let pl = plaq_links(lat, p.x, p.i, p.j);
                assert!(pl.contains(&p.u) && pl.contains(&p.v));
            }
            for x in 0..rows {
                for a in 0..4 { for b in (a + 1)..4 {
                    let mut seen = usize::MAX;
                    for &(s, d) in &plaq_links(lat, x, a, b) {
                        let o = owner[s][d];
                        if o != usize::MAX {
                            assert!(seen == usize::MAX || seen == o, "plaquette couples two pairs of one colour");
                            seen = o;
                        }
                    }
                }}
            }
        }
    }

    fn cond_sweep(lat: &mut Lattice, beta: f64, rng: &mut Rng) {
        let n = lat.l;
        for x in 0..lat.links.len() {
            for i in 0..4 {
                if !is_frozen(n, x, i) { lat.links[x][i] = rng.heat(lat.staple(x, i), beta); }
            }
        }
    }

    // exact draw of a pair from its joint conditional law; returns number of proposals
    fn pair_draw(lat: &mut Lattice, p: Pair, beta: f64, rng: &mut Rng) -> u64 {
        let (u, a) = p.u; let (v, b) = p.v;
        lat.links[u][a] = [0.; 4];
        lat.links[v][b] = [0.; 4];
        let hu = lat.staple(u, a);
        let hv = lat.staple(v, b);
        let mut tries = 0;
        loop {
            tries += 1;
            lat.links[u][a] = rng.heat(hu, beta);
            lat.links[v][b] = rng.heat(hv, beta);
            let y = lat.plaquette(p.x, p.i, p.j);
            assert!(y - 1. <= 1e-12);
            if rng.u().ln() <= beta * (y - 1.) { return tries; }
        }
    }

    fn loop_hol(lat: &Lattice, x: usize, i: usize, j: usize, len: usize) -> Q {
        let mut h = ONE; let mut y = x;
        for _ in 0..len { h = mul(h, lat.links[y][i]); y = lat.plus[y][i]; }
        for _ in 0..len { h = mul(h, lat.links[y][j]); y = lat.plus[y][j]; }
        for _ in 0..len { y = lat.minus[y][i]; h = mul(h, conj(lat.links[y][i])); }
        for _ in 0..len { y = lat.minus[y][j]; h = mul(h, conj(lat.links[y][j])); }
        h
    }

    // tests: [f1, f4, spread, f1_tl, f4_tl] with B = full xz holonomy and B_tl = normalised traceless part
    fn tests(lat: &Lattice) -> [f64; 5] {
        let b = loop_hol(lat, 0, 0, 2, 2);
        let im = [0., b[1], b[2], b[3]];
        let nim = dot(im, im).sqrt();
        let btl = if nim > 0. { im.map(|c| c / nim) } else { [0.; 4] };
        let g1 = loop_hol(lat, 0, 0, 1, 1);
        let mut gbar = [0.; 4];
        for cx in 0..2 { for cy in 0..2 {
            let mut s = 0; let mut path = ONE;
            for _ in 0..cx { path = mul(path, lat.links[s][0]); s = lat.plus[s][0]; }
            for _ in 0..cy { path = mul(path, lat.links[s][1]); s = lat.plus[s][1]; }
            let g = mul(mul(path, loop_hol(lat, s, 0, 1, 1)), conj(path));
            for k in 0..4 { gbar[k] += g[k] / 4.; }
        }}
        [mul(b, g1)[0], mul(b, gbar)[0], 1. - dot(gbar, gbar), mul(btl, g1)[0], mul(btl, gbar)[0]]
    }

    // angles from -I of all coarse spatial faces of slice 0 (81 at N=6), order: base x, planes xy,xz,yz
    fn coarse_angles(lat: &Lattice) -> Vec<f64> {
        let n = lat.l; let mut out = Vec::new();
        for x in 0..n.pow(3) {
            let c = coords(n, x);
            if c.iter().any(|v| v % 2 == 1) { continue; }
            for &(i, j) in &[(0usize, 1usize), (0, 2), (1, 2)] {
                let h = loop_hol(lat, x, i, j, 2);
                out.push((-h[0]).clamp(-1., 1.).acos());
            }
        }
        out
    }

    fn read_skeleton(path: &str, n: usize) -> Vec<(usize, usize, Q)> {
        let txt = std::fs::read_to_string(path).unwrap();
        let mut out = Vec::new();
        for line in txt.lines() {
            if line.starts_with('#') || line.trim().is_empty() { continue; }
            let f: Vec<&str> = line.split_whitespace().collect();
            assert_eq!(f.len(), 6);
            let x: usize = f[0].parse().unwrap(); let i: usize = f[1].parse().unwrap();
            assert!(is_frozen(n, x, i));
            let q: Q = std::array::from_fn(|k| f[2 + k].parse::<f64>().unwrap());
            assert!((dot(q, q) - 1.).abs() < 1e-12);
            out.push((x, i, q));
        }
        let count = (0..n.pow(3)).map(|x| (0..3).filter(|&i| is_frozen(n, x, i)).count()).sum::<usize>();
        assert_eq!(out.len(), count, "skeleton file must list every frozen link");
        out
    }

    // fixed <beta> <seed> <hot> <burn> <samples> <spacing> <n> <T> <skeleton file> <out prefix>
    fn fixed(a: &[String]) {
        let beta: f64 = a[2].parse().unwrap();
        assert!(beta < 8.0, "only the plain pair proposal is implemented");
        let seed: u64 = a[3].parse().unwrap();
        let hot = a[4] == "1";
        let burn: usize = a[5].parse().unwrap();
        let samples: usize = a[6].parse().unwrap();
        let spacing: usize = a[7].parse().unwrap();
        let n: usize = a[8].parse().unwrap();
        let tp: usize = a[9].parse().unwrap();
        let skel = read_skeleton(&a[10], n);
        let pre = &a[11];
        let mut rng = Rng { state: seed };
        let mut meas = Rng { state: seed ^ 0x6a09e667f3bcc909 };
        let mut lat = Lattice::new(n, tp, false, hot, &mut rng);
        for &(x, i, q) in &skel { lat.links[x][i] = q; }
        let frozen0: Vec<(usize, usize, Q)> = skel.clone();
        let cols = make_colours(&lat);
        check_colours(&lat, &cols);
        let ang = coarse_angles(&lat);
        let mn = ang.iter().cloned().fold(f64::INFINITY, f64::min);
        let open = |s: &str| std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}{s}")).unwrap();
        let mut fm = open(".csv");
        let mut fc = open(".colours.csv");
        let mut fh = open(".meta.txt");
        writeln!(fh, "args {}", a[1..].join(" ")).unwrap();
        writeln!(fh, "min_angle_from_minusI {:.12}", mn).unwrap();
        writeln!(fh, "coarse_angles {}", ang.iter().map(|v| format!("{v:.9}")).collect::<Vec<_>>().join(" ")).unwrap();
        let t0 = tests(&lat);
        writeln!(fh, "B_full_and_tests_at_start {:?}", t0).unwrap();
        for _ in 0..burn { cond_sweep(&mut lat, beta, &mut rng); }
        writeln!(fm, "single,average,spread,j_single,j_average,single_tl,average_tl,j_single_tl,j_average_tl,mean_tries").unwrap();
        let mut hdr = Vec::new();
        for t in ["j1", "j4", "j1tl", "j4tl"] { for k in 0..24 { hdr.push(format!("{t}_c{k}")); } }
        writeln!(fc, "{}", hdr.join(",")).unwrap();
        for _ in 0..samples {
            for _ in 0..spacing { cond_sweep(&mut lat, beta, &mut rng); }
            let orig = lat.links[..n.pow(3)].to_vec();
            let r = tests(&lat);
            let mut pc = [[0.; 24]; 4];
            let mut tries = 0u64; let mut draws = 0u64;
            for (k, col) in cols.iter().enumerate() {
                for &p in col { tries += pair_draw(&mut lat, p, beta, &mut meas); draws += 1; }
                let f = tests(&lat);
                for &p in col { tries += pair_draw(&mut lat, p, beta, &mut meas); draws += 1; }
                let g = tests(&lat);
                for (t, idx) in [0usize, 1, 3, 4].iter().enumerate() { pc[t][k] = (f[*idx] - g[*idx]).powi(2) / 2.; }
                for &p in col { lat.links[p.u.0][p.u.1] = orig[p.u.0][p.u.1]; lat.links[p.v.0][p.v.1] = orig[p.v.0][p.v.1]; }
            }
            for &(x, i, q) in &frozen0 { assert_eq!(lat.links[x][i], q, "frozen link changed"); }
            // G4 accumulates (f-g)^2/48 colour by colour; reproduce the same summation order
            let mut j = [0.; 4];
            for t in 0..4 { for k in 0..24 { j[t] += 2. * pc[t][k] / 48.; } }
            writeln!(fm, "{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.6}",
                r[0], r[1], r[2], j[0], j[1], r[3], r[4], j[2], j[3], tries as f64 / draws as f64).unwrap();
            let row: Vec<String> = pc.iter().flat_map(|v| v.iter().map(|x| format!("{x:.6e}"))).collect();
            writeln!(fc, "{}", row.join(",")).unwrap();
        }
    }

    // gen <beta> <seed> <hot> <burn cycles> <count> <gap cycles> <n> <T> <out prefix>
    // unconditioned Wilson chain (heat bath + reflection cycle, as G4's pilot); writes slice-0 skeletons
    fn gen(a: &[String]) {
        let beta: f64 = a[2].parse().unwrap();
        let seed: u64 = a[3].parse().unwrap();
        let hot = a[4] == "1";
        let burn: usize = a[5].parse().unwrap();
        let count: usize = a[6].parse().unwrap();
        let gap: usize = a[7].parse().unwrap();
        let n: usize = a[8].parse().unwrap();
        let tp: usize = a[9].parse().unwrap();
        let pre = &a[10];
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, hot, &mut rng);
        for _ in 0..burn { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
        let mut fa = std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}.angles.csv")).unwrap();
        writeln!(fa, "# args {}", a[1..].join(" ")).unwrap();
        writeln!(fa, "index,min_angle,mean_plaq_slice0,angles...").unwrap();
        for c in 0..count {
            for _ in 0..gap { lat.sweep(beta, &mut rng, false); lat.sweep(beta, &mut rng, true); }
            let ang = coarse_angles(&lat);
            let mn = ang.iter().cloned().fold(f64::INFINITY, f64::min);
            let mut pl = 0.; for x in 0..n.pow(3) { for i in 0..3 { pl += lat.plaquette(x, i, (i + 1) % 3); } }
            pl /= (3 * n.pow(3)) as f64;
            writeln!(fa, "{c},{mn:.9},{pl:.9},{}", ang.iter().map(|v| format!("{v:.6}")).collect::<Vec<_>>().join(",")).unwrap();
            let mut fs = std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}.skel{c}.txt")).unwrap();
            writeln!(fs, "# slice-0 skeleton from unconditioned chain, args {} index {c} min_angle {mn:.9}", a[1..].join(" ")).unwrap();
            for x in 0..n.pow(3) { for i in 0..3 { if is_frozen(n, x, i) {
                let q = lat.links[x][i];
                writeln!(fs, "{x} {i} {:.17e} {:.17e} {:.17e} {:.17e}", q[0], q[1], q[2], q[3]).unwrap();
            }}}
        }
    }

    pub fn run() {
        let a: Vec<String> = env::args().collect();
        match a.get(1).map(String::as_str) {
            Some("fixed") => { assert_eq!(a.len(), 12, "fixed beta seed hot burn samples spacing n T skel out"); fixed(&a) }
            Some("gen") => { assert_eq!(a.len(), 11, "gen beta seed hot burn count gap n T out"); gen(&a) }
            _ => panic!("mode fixed|gen"),
        }
    }
}
fn main() { m::run(); }
