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
// z1mx4 (c2-grow, T223) = z1mx3 with the mark list grown to the 7 coarse faces containing the changed skeleton edges
// (ring 1) and the 33 faces sharing a coarse edge with them (ring 2); references B (full xz coarse holonomy at the root)
// and T = 1 (plain trace, plaquettes of ring 1 only). D output = mean over colours (sparse accumulation) + per-colour diagonal.
// Predicates fixed before the first run of z1mx4 (asserted unless stated):
//  P1-P3, P5 as below (unchanged); P6 gauge invariance of all 308 marks to 1e-10 (gauge mode);
//  P8 (checked outside, ctl4.py) the 15 L1 marks equal the prior z1mx3 marks at the same seed to 1e-12 (same loops),
//     and the .csv output is byte-identical to z1mx3 at the same arguments (RNG calls unchanged).
//  P9 (gauge mode, printed; checked in notes) at d0 the faces xy000, xy200, yz204 have holonomy -I and every other
//     ring-1 face is at angle pi/2 (holonomy of i type).
// z1mx3 = z1mx2 + 4 yz plaquettes of the face (2,0,4). z1mx2 = z1mx with a larger mark list (extra run). z1mx (b2-matrix, T217): MINIMAL extension of z1m6.rs. The original outputs (.csv, .colours.csv,
// .meta.txt) and every RNG call are unchanged; added: a LIST of gauge-invariant marks X_1..X_n
// (marks()), written per measurement to <prefix>.X.csv, and per colour c the mean over measurements of
// (X'-X'')(X'-X'')^T/2 from the SAME two-copy refresh already used for f1,f4 (<prefix>.Dc.txt), so that
// D = mean over the 24 colours = (1/48) sum_c E[(X'-X'')(X'-X'')^T]. Mode "gauge" checks invariance.
// Added predicates (fixed before the first run):
//  P5 mark B.g1 equals column "single" and mean of B.g1..B.g4 equals column "average" to 1e-12 every
//     measurement (assert); tolerance: float rounding of a few quaternion products.
//  P6 (gauge mode) every mark is unchanged to 1e-10 under a random gauge transformation at all sites
//     (including skeleton sites, frozen links transformed); tolerance: rounding of ~20 products.
//  P7 (checked outside, ctl) columns of <prefix>.csv byte-identical to build/z1m6 at the same arguments.
// z1mx5 (d2-time, T226) = z1mx4 + mode "time" (and Y marks in gauge mode). Modes fixed/gen are untouched (byte-identity predicate
// T-P0 checked outside: z1mx5 fixed == z1mx4 fixed, all five output files, same arguments).
// Y marks on slice t (site index x + t*n^3; root_t = t*n^3): the SAME step lists as the 308 X marks, started at root_t.
//   Y^loc_k(t) = Re(B_t L_k(t))  (B-type; B_t = coarse xz holonomy at root_t, all links free), Re(L_k(t)) (T-type).
//   Y^tr_k(t)  = Re(B_0 P L_k(t) P^-1) (B-type; P = temporal path root_0 -> root_t along the root's time-like links,
//                 upward for t=1,2,3, downward for t=-1=T-1; B_0 = coarse xz holonomy at root_0 = frozen); T-type = Re(L_k(t)) (P drops out).
// Predicates fixed before the first run (asserted in gauge mode):
//  T-P1 every Y^loc_k(t), Y^tr_k(t) (t = 1,2,3,T-1) unchanged to 1e-10 under a random full gauge transformation.
//  T-P2 Y^loc_k(0) and Y^tr_k(0) equal X_k to 1e-12 (shift code reproduces the slice-0 marks).
// Mode time: identical chain (the same cond_sweep calls on rng; the two-copy refresh is NOT done, it used only the separate
//  meas RNG and restored the links, so the chain is unchanged: checked outside as T-P3, X.csv byte-identical to fixed mode).
//  Per stream it accumulates, for each of 8 blocks (t in 1,2,3,T-1) x (loc,tr): sum Y, sum Y Y^T (upper triangle),
//  sum m_j Y for the K weight vectors w_j (m_j = w_j . X(0)); plus sum m, sum m m^T. Also a small per-measurement csv of
//  m_j and w_j.Y(t) (8K columns) and the mean spatial plaquette of slices 0,1,2,3,T-1.
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


    // ---- c2-grow marks (z1mx4) ----
    // step codes: 0..3 = +x,+y,+z,+t ; 4..7 = -x,-y,-z,-t
    fn path(lat: &Lattice, x0: usize, steps: &[usize]) -> (Q, usize) {
        let mut h = ONE; let mut y = x0;
        for &s in steps {
            if s < 4 { h = mul(h, lat.links[y][s]); y = lat.plus[y][s]; }
            else { y = lat.minus[y][s - 4]; h = mul(h, conj(lat.links[y][s - 4])); }
        }
        (h, y)
    }
    fn closed(lat: &Lattice, steps: &[usize]) -> Q {
        let (h, y) = path(lat, 0, steps); assert_eq!(y, 0, "loop not closed"); h
    }
    fn inv(steps: &[usize]) -> Vec<usize> { steps.iter().rev().map(|&s| (s + 4) % 8).collect() }
    // ring 1: faces containing E_y=((2,0,0),y) or E_z=((2,0,0),z); ring 2: 33 faces sharing a coarse edge with ring 1 (faces.py)
    const RING1: [([usize; 3], (usize, usize)); 7] = [([0,0,0],(0,1)), ([0,0,0],(0,2)), ([2,0,0],(0,1)), ([2,0,0],(0,2)), ([2,0,0],(1,2)), ([2,0,4],(1,2)), ([2,4,0],(1,2))];
    const RING2: [([usize; 3], (usize, usize)); 33] = [([0,0,0],(1,2)), ([0,0,2],(0,1)), ([0,0,2],(0,2)), ([0,0,4],(0,1)), ([0,0,4],(0,2)), ([0,0,4],(1,2)), ([0,2,0],(0,1)), ([0,2,0],(0,2)), ([0,2,4],(0,2)), ([0,4,0],(0,1)), ([0,4,0],(0,2)), ([0,4,0],(1,2)), ([0,4,2],(0,1)), ([2,0,2],(0,1)), ([2,0,2],(0,2)), ([2,0,2],(1,2)), ([2,0,4],(0,1)), ([2,0,4],(0,2)), ([2,2,0],(0,1)), ([2,2,0],(0,2)), ([2,2,0],(1,2)), ([2,2,4],(0,2)), ([2,2,4],(1,2)), ([2,4,0],(0,1)), ([2,4,0],(0,2)), ([2,4,2],(0,1)), ([2,4,2],(1,2)), ([2,4,4],(1,2)), ([4,0,0],(0,1)), ([4,0,0],(0,2)), ([4,0,0],(1,2)), ([4,0,4],(1,2)), ([4,4,0],(1,2))];
    fn face_name(b: [usize; 3], pl: (usize, usize)) -> String {
        let pn = match pl { (0, 1) => "xy", (0, 2) => "xz", _ => "yz" };
        format!("{pn}{}{}{}", b[0], b[1], b[2])
    }
    // transport tail from the root to the face base along frozen links: x then y then z; coordinate 2 -> two + steps,
    // coordinate 4 -> two - steps (reproduces the prior transports: xy200 = +x+x, yz204 = +x+x-z-z)
    fn tail(b: [usize; 3]) -> Vec<usize> {
        let mut t = Vec::new();
        for d in 0..3 { match b[d] { 0 => {}, 2 => { t.push(d); t.push(d); }, 4 => { t.push(d + 4); t.push(d + 4); }, _ => panic!() } }
        t
    }
    // face loops: (name, steps) for 4 fine plaquettes g{ca}{cb} and (if partial) Rv, Rh, L_no11 in the face's plane (a,b)
    fn face_loops(b: [usize; 3], pl: (usize, usize), partial: bool) -> Vec<(String, Vec<usize>)> {
        let (a, c) = pl; let t0 = tail(b); let f = face_name(b, pl);
        let wrap = |inner: Vec<usize>| { let mut s = t0.clone(); s.extend(inner); s.extend(inv(&t0)); s };
        let mut v = Vec::new();
        for (ca, cb) in [(0, 0), (1, 0), (0, 1), (1, 1)] {
            let mut tt = vec![a; ca]; tt.extend(vec![c; cb]);
            let mut inner = tt.clone(); inner.extend([a, c, a + 4, c + 4]); inner.extend(inv(&tt));
            v.push((format!("{f}.g{ca}{cb}"), wrap(inner)));
        }
        if partial {
            v.push((format!("{f}.Rv"), wrap(vec![a, c, c, a + 4, c + 4, c + 4])));
            v.push((format!("{f}.Rh"), wrap(vec![a, a, c, a + 4, a + 4, c + 4])));
            v.push((format!("{f}.L_no11"), wrap(vec![a, a, c, a + 4, c, a + 4, c + 4, c + 4])));
        }
        v
    }
    // mark list: (name, reference 0 = B / 1 = T (trace), loop). Order: ring1 B (7 per face), ring2 B plaquettes,
    // ring2 B partial, ring1 T plaquettes. The first four marks are B.xy000.g00..g11 (P5).
    fn mark_loops() -> Vec<(String, usize, Vec<usize>)> {
        let mut v = Vec::new();
        for &(b, pl) in RING1.iter() { for (n, s) in face_loops(b, pl, true) { v.push((format!("B.{n}"), 0, s)); } }
        for &(b, pl) in RING2.iter() { for (n, s) in face_loops(b, pl, false) { v.push((format!("B.{n}"), 0, s)); } }
        for &(b, pl) in RING2.iter() { for (n, s) in face_loops(b, pl, true).into_iter().skip(4) { v.push((format!("B.{n}"), 0, s)); } }
        for &(b, pl) in RING1.iter() { for (n, s) in face_loops(b, pl, false) { v.push((format!("T.{n}"), 1, s)); } }
        v
    }
    fn mark_names(_lat: &Lattice) -> Vec<String> { mark_loops().into_iter().map(|(n, _, _)| n).collect() }
    fn marks_with(lat: &Lattice, ml: &[(String, usize, Vec<usize>)]) -> Vec<f64> {
        let b = loop_hol(lat, 0, 0, 2, 2);
        ml.iter().map(|(_, r, s)| { let l = closed(lat, s); if *r == 0 { mul(b, l)[0] } else { l[0] } }).collect()
    }
    fn marks(lat: &Lattice) -> Vec<f64> { marks_with(lat, &mark_loops()) }
    fn face_holonomies(lat: &Lattice) {
        for &(b, pl) in RING1.iter().chain(RING2.iter()) {
            let mut s = tail(b); let (a, c) = pl; s.extend([a, a, c, c, a + 4, a + 4, c + 4, c + 4]); s.extend(inv(&tail(b)));
            let h = closed(lat, &s);
            println!("face {} holonomy ({:.6},{:.6},{:.6},{:.6}) angle_from_-I {:.6}", face_name(b, pl), h[0], h[1], h[2], h[3], (-h[0]).clamp(-1., 1.).acos());
        }
    }
    fn gauge(a: &[String]) {
        // gauge <seed> <n> <T> <skeleton>
        let seed: u64 = a[2].parse().unwrap(); let n: usize = a[3].parse().unwrap(); let tp: usize = a[4].parse().unwrap();
        let skel = read_skeleton(&a[5], n);
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, true, &mut rng);
        for &(x, i, q) in &skel { lat.links[x][i] = q; }
        face_holonomies(&lat);
        let m0 = marks(&lat); let names = mark_names(&lat);
        let g: Vec<Q> = (0..lat.links.len()).map(|_| unit([rng.u() - 0.5, rng.u() - 0.5, rng.u() - 0.5, rng.u() - 0.5])).collect();
        let orig = lat.links.clone();
        for x in 0..orig.len() { for mu in 0..4 { lat.links[x][mu] = mul(mul(g[x], orig[x][mu]), conj(g[lat.plus[x][mu]])); } }
        let m1 = marks(&lat);
        lat.links = orig.clone();
        let mut worst = 0f64; for k in 0..m0.len() { worst = worst.max((m0[k] - m1[k]).abs()); }
        println!("marks {} names {}", m0.len(), names.join(","));
        println!("P6 max |mark change| under random full gauge transformation = {worst:.3e}");
        assert!(worst < 1e-10, "P6 failed");
        // residual stabiliser of the frozen skeleton: global constant h = exp(i pi/8) (rotation about B=i axis)
        let h = [(std::f64::consts::PI / 8.).cos(), (std::f64::consts::PI / 8.).sin(), 0., 0.];
        let g1a = closed(&lat, &mark_loops()[0].2);
        for x in 0..orig.len() { for mu in 0..4 { lat.links[x][mu] = mul(mul(h, orig[x][mu]), conj(h)); } }
        let mut fz = 0f64; for &(x, i, q) in &skel { for k in 0..4 { fz = fz.max((lat.links[x][i][k] - q[k]).abs()); } }
        let g1b = closed(&lat, &mark_loops()[0].2);
        println!("global exp(i pi/8): max frozen-link change {fz:.3e}; Re(j g1) {:.9} -> {:.9}; Re(k g1) {:.9} -> {:.9}",
            mul([0., 0., 1., 0.], g1a)[0], mul([0., 0., 1., 0.], g1b)[0], mul([0., 0., 0., 1.], g1a)[0], mul([0., 0., 0., 1.], g1b)[0]);
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
        let mut fx = open(".X.csv");
        let mut fd = open(".Dc.txt");
        let names = mark_names(&lat); let nm = names.len();
        writeln!(fx, "{}", names.join(",")).unwrap();
        let ml = mark_loops();
        let mut dsum = vec![0f64; nm * nm];
        let mut ddiag = vec![vec![0f64; nm]; 24];
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
            let x0 = marks_with(&lat, &ml);
            assert!((x0[0] - r[0]).abs() < 1e-12 && ((x0[0] + x0[1] + x0[2] + x0[3]) / 4. - r[1]).abs() < 1e-12, "P5");
            writeln!(fx, "{}", x0.iter().map(|v| format!("{v:.12}")).collect::<Vec<_>>().join(",")).unwrap();
            let mut pc = [[0.; 24]; 4];
            let mut tries = 0u64; let mut draws = 0u64;
            for (k, col) in cols.iter().enumerate() {
                for &p in col { tries += pair_draw(&mut lat, p, beta, &mut meas); draws += 1; }
                let f = tests(&lat);
                let xa = marks_with(&lat, &ml);
                for &p in col { tries += pair_draw(&mut lat, p, beta, &mut meas); draws += 1; }
                let g = tests(&lat);
                let xb = marks_with(&lat, &ml);
                let df: Vec<f64> = (0..nm).map(|u| xa[u] - xb[u]).collect();
                let nz: Vec<usize> = (0..nm).filter(|&u| df[u] != 0.).collect();
                for &u in &nz { ddiag[k][u] += df[u] * df[u] / 2.; for &v in &nz { dsum[u * nm + v] += df[u] * df[v] / 2.; } }
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
        // D = mean over the 24 colours of the per-colour mean over measurements of (X'-X'')(X'-X'')^T/2 (row-major n x n),
        // then 24 lines: per-colour diagonal (same normalisation, not divided by 24)
        writeln!(fd, "# z1mx4 marks {} measurements {} ; line 1 = D (mean over colours) row-major {}x{}; lines 2..25 = per-colour diagonal", nm, samples, nm, nm).unwrap();
        writeln!(fd, "{}", dsum.iter().map(|v| format!("{:.12e}", v / samples as f64 / 24.)).collect::<Vec<_>>().join(" ")).unwrap();
        for k in 0..24 { writeln!(fd, "{}", ddiag[k].iter().map(|v| format!("{:.12e}", v / samples as f64)).collect::<Vec<_>>().join(" ")).unwrap(); }
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

    // ---- d2-time additions (z1mx5) ----
    fn closed_at(lat: &Lattice, x0: usize, steps: &[usize]) -> Q {
        let (h, y) = path(lat, x0, steps); assert_eq!(y, x0, "loop not closed"); h
    }
    // temporal transport root_0 -> root_t: t in 1..T-1 upward if t <= T/2, else downward (T-t steps)
    fn tpath(lat: &Lattice, t: usize) -> Q {
        let tp = lat.time; let steps: Vec<usize> = if 2 * t <= tp { vec![3; t] } else { vec![7; tp - t] };
        let (h, y) = path(lat, 0, &steps); assert_eq!(y, t * lat.l.pow(3)); h
    }
    // returns (loc, tr) for slice t
    fn ymarks(lat: &Lattice, ml: &[(String, usize, Vec<usize>)], t: usize) -> (Vec<f64>, Vec<f64>) {
        let r = t * lat.l.pow(3);
        let bt = { let (h, y) = path(lat, r, &[0, 0, 2, 2, 4, 4, 6, 6]); assert_eq!(y, r); h };
        let b0 = loop_hol(lat, 0, 0, 2, 2);
        let p = tpath(lat, t);
        let mut lo = Vec::with_capacity(ml.len()); let mut tr = Vec::with_capacity(ml.len());
        for (_, kind, s) in ml {
            let l = closed_at(lat, r, s);
            if *kind == 0 { lo.push(mul(bt, l)[0]); tr.push(mul(b0, mul(mul(p, l), conj(p)))[0]); }
            else { lo.push(l[0]); tr.push(l[0]); }
        }
        (lo, tr)
    }
    fn ymarks0(lat: &Lattice, ml: &[(String, usize, Vec<usize>)]) -> (Vec<f64>, Vec<f64>) {
        let bt = loop_hol(lat, 0, 0, 2, 2);
        let lo: Vec<f64> = ml.iter().map(|(_, k, s)| { let l = closed_at(lat, 0, s); if *k == 0 { mul(bt, l)[0] } else { l[0] } }).collect();
        (lo.clone(), lo)
    }
    fn slices(tp: usize) -> [usize; 4] { [1, 2, 3, tp - 1] }
    fn slice_plaq(lat: &Lattice, t: usize) -> f64 {
        let n = lat.l; let mut s = 0.;
        for x in 0..n.pow(3) { for i in 0..3 { s += lat.plaquette(x + t * n.pow(3), i, (i + 1) % 3); } }
        s / (3 * n.pow(3)) as f64
    }
    fn ygauge(lat: &mut Lattice, rng: &mut Rng) {
        let ml = mark_loops(); let tp = lat.time;
        let x0 = marks_with(lat, &ml);
        let (l0, t0) = ymarks0(lat, &ml);
        let mut d0 = 0f64; for k in 0..x0.len() { d0 = d0.max((x0[k] - l0[k]).abs()).max((x0[k] - t0[k]).abs()); }
        println!("T-P2 max |Y(0) - X| = {d0:.3e}"); assert!(d0 < 1e-12, "T-P2 failed");
        let before: Vec<(Vec<f64>, Vec<f64>)> = slices(tp).iter().map(|&t| ymarks(lat, &ml, t)).collect();
        let g: Vec<Q> = (0..lat.links.len()).map(|_| unit([rng.u() - 0.5, rng.u() - 0.5, rng.u() - 0.5, rng.u() - 0.5])).collect();
        let orig = lat.links.clone();
        for x in 0..orig.len() { for mu in 0..4 { lat.links[x][mu] = mul(mul(g[x], orig[x][mu]), conj(g[lat.plus[x][mu]])); } }
        let after: Vec<(Vec<f64>, Vec<f64>)> = slices(tp).iter().map(|&t| ymarks(lat, &ml, t)).collect();
        lat.links = orig;
        let mut w = 0f64; let mut spread = 0f64;
        for (b, a) in before.iter().zip(after.iter()) { for k in 0..b.0.len() {
            w = w.max((b.0[k] - a.0[k]).abs()).max((b.1[k] - a.1[k]).abs()); spread = spread.max(b.0[k].abs());
        } }
        println!("T-P1 max |Y change| under random full gauge transformation (t=1,2,3,T-1; loc and tr; {} marks) = {w:.3e}; max|Y| {spread:.3}", 2 * 4 * x0.len());
        assert!(w < 1e-10, "T-P1 failed");
    }

    // time <beta> <seed> <hot> <burn> <samples> <spacing> <n> <T> <skeleton file> <weights file> <writeX 0|1> <out prefix>
    fn time(a: &[String]) {
        let beta: f64 = a[2].parse().unwrap();
        assert!(beta < 8.0);
        let seed: u64 = a[3].parse().unwrap();
        let hot = a[4] == "1";
        let burn: usize = a[5].parse().unwrap();
        let samples: usize = a[6].parse().unwrap();
        let spacing: usize = a[7].parse().unwrap();
        let n: usize = a[8].parse().unwrap();
        let tp: usize = a[9].parse().unwrap();
        let skel = read_skeleton(&a[10], n);
        let wtxt = std::fs::read_to_string(&a[11]).unwrap();
        let ws: Vec<Vec<f64>> = wtxt.lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty())
            .map(|l| l.split_whitespace().map(|v| v.parse::<f64>().unwrap()).collect()).collect();
        let write_x = a[12] == "1";
        let pre = &a[13];
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, hot, &mut rng);
        for &(x, i, q) in &skel { lat.links[x][i] = q; }
        let ml = mark_loops(); let nm = ml.len(); let kw = ws.len();
        for w in &ws { assert_eq!(w.len(), nm, "weight vector length"); }
        let open = |s: &str| std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{pre}{s}")).unwrap();
        let mut fh = open(".meta.txt");
        writeln!(fh, "args {}", a[1..].join(" ")).unwrap();
        let mut fx = if write_x { let mut f = open(".X.csv"); writeln!(f, "{}", mark_names(&lat).join(",")).unwrap(); Some(f) } else { None };
        let mut fs = open(".series.csv");
        let sl = slices(tp);
        let mut hdr: Vec<String> = (0..kw).map(|j| format!("m{j}")).collect();
        for &t in &sl { for d in ["loc", "tr"] { for j in 0..kw { hdr.push(format!("wY{j}_t{t}_{d}")); } } }
        for t in [0usize, 1, 2, 3, tp - 1] { hdr.push(format!("plaq_t{t}")); }
        writeln!(fs, "{}", hdr.join(",")).unwrap();
        let nb = 2 * sl.len();
        let mut sy = vec![vec![0f64; nm]; nb];
        let mut syy = vec![vec![0f64; nm * nm]; nb];
        let mut smy = vec![vec![0f64; kw * nm]; nb];
        let mut sm = vec![0f64; kw]; let mut smm = vec![0f64; kw * kw];
        for _ in 0..burn { cond_sweep(&mut lat, beta, &mut rng); }
        for _ in 0..samples {
            for _ in 0..spacing { cond_sweep(&mut lat, beta, &mut rng); }
            let x0 = marks_with(&lat, &ml);
            if let Some(f) = fx.as_mut() { writeln!(f, "{}", x0.iter().map(|v| format!("{v:.12}")).collect::<Vec<_>>().join(",")).unwrap(); }
            let m: Vec<f64> = ws.iter().map(|w| w.iter().zip(&x0).map(|(a, b)| a * b).sum()).collect();
            for j in 0..kw { sm[j] += m[j]; for k in 0..kw { smm[j * kw + k] += m[j] * m[k]; } }
            let mut row: Vec<String> = m.iter().map(|v| format!("{v:.10e}")).collect();
            for (ti, &t) in sl.iter().enumerate() {
                let (lo, tr) = ymarks(&lat, &ml, t);
                for (di, y) in [lo, tr].iter().enumerate() {
                    let b = 2 * ti + di;
                    for u in 0..nm { sy[b][u] += y[u]; let yu = y[u]; let r = &mut syy[b][u * nm..(u + 1) * nm]; for v in u..nm { r[v] += yu * y[v]; } }
                    for j in 0..kw { for u in 0..nm { smy[b][j * nm + u] += m[j] * y[u]; } }
                    for w in &ws { let v: f64 = w.iter().zip(y).map(|(a, b)| a * b).sum(); row.push(format!("{v:.10e}")); }
                }
            }
            for t in [0usize, 1, 2, 3, tp - 1] { row.push(format!("{:.10e}", slice_plaq(&lat, t))); }
            writeln!(fs, "{}", row.join(",")).unwrap();
            for &(x, i, q) in &skel { assert_eq!(lat.links[x][i], q, "frozen link changed"); }
        }
        let mut fmom = open(".mom.txt");
        writeln!(fmom, "# z1mx5 time moments: samples {samples} marks {nm} weights {kw} slices {:?} ; blocks b = 2*slice_index + (0 loc, 1 tr)", sl).unwrap();
        writeln!(fmom, "sm {}", sm.iter().map(|v| format!("{v:.15e}")).collect::<Vec<_>>().join(" ")).unwrap();
        writeln!(fmom, "smm {}", smm.iter().map(|v| format!("{v:.15e}")).collect::<Vec<_>>().join(" ")).unwrap();
        for b in 0..nb {
            writeln!(fmom, "sy {b} {}", sy[b].iter().map(|v| format!("{v:.15e}")).collect::<Vec<_>>().join(" ")).unwrap();
            writeln!(fmom, "smy {b} {}", smy[b].iter().map(|v| format!("{v:.15e}")).collect::<Vec<_>>().join(" ")).unwrap();
            let mut up = Vec::with_capacity(nm * (nm + 1) / 2);
            for u in 0..nm { for v in u..nm { up.push(format!("{:.11e}", syy[b][u * nm + v])); } }
            writeln!(fmom, "syy {b} {}", up.join(" ")).unwrap();
        }
    }
    fn gauge_t(a: &[String]) {
        // gauge_t <seed> <n> <T> <skeleton> : random hot configuration with the skeleton; T-P1, T-P2
        let seed: u64 = a[2].parse().unwrap(); let n: usize = a[3].parse().unwrap(); let tp: usize = a[4].parse().unwrap();
        let skel = read_skeleton(&a[5], n);
        let mut rng = Rng { state: seed };
        let mut lat = Lattice::new(n, tp, false, true, &mut rng);
        for &(x, i, q) in &skel { lat.links[x][i] = q; }
        ygauge(&mut lat, &mut rng);
        // also after 20 conditional sweeps (a thermal configuration)
        for _ in 0..20 { cond_sweep(&mut lat, 3.276133577, &mut rng); }
        ygauge(&mut lat, &mut rng);
    }

    pub fn run() {
        let a: Vec<String> = env::args().collect();
        match a.get(1).map(String::as_str) {
            Some("fixed") => { assert_eq!(a.len(), 12, "fixed beta seed hot burn samples spacing n T skel out"); fixed(&a) }
            Some("gauge") => { assert_eq!(a.len(), 6, "gauge seed n T skel"); gauge(&a) }
            Some("gen") => { assert_eq!(a.len(), 11, "gen beta seed hot burn count gap n T out"); gen(&a) }
            Some("time") => { assert_eq!(a.len(), 14, "time beta seed hot burn samples spacing n T skel weights writeX out"); time(&a) }
            Some("gauge_t") => { assert_eq!(a.len(), 6, "gauge_t seed n T skel"); gauge_t(&a) }
            _ => panic!("mode fixed|gen|time|gauge_t"),
        }
    }
}
fn main() { m::run(); }
