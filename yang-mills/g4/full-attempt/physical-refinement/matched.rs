// rustc --edition=2021 -O matched.rs -o matched
mod wilson {
    #![allow(dead_code)]
    include!("../two-site-gap/wilson_mc.rs");
    use std::f64::consts::PI;
    use std::io::{self, Write};
    type Slice = [f64; 14]; // plaquette, adjoint, E winding/local, T2 winding/local (three each)

    impl Lattice {
        fn step(&self, x: &mut usize, p: &mut Q, axis: usize, forward: bool) {
            if forward {
                *p = mul(*p, self.links[*x][axis]);
                *x = self.plus[*x][axis];
            } else {
                *x = self.minus[*x][axis];
                *p = mul(*p, conj(self.links[*x][axis]));
            }
        }
        fn clover(&self, x: usize, i: usize, j: usize, k: usize) -> Q {
            let dirs = [(i, true), (j, true), (i, false), (j, false)];
            let mut out = [0.; 4];
            for start in 0..4 {
                let (mut y, mut p) = (x, ONE);
                for side in 0..4 {
                    let (axis, fwd) = dirs[(side + start) % 4];
                    for _ in 0..k {
                        self.step(&mut y, &mut p, axis, fwd);
                    }
                }
                for a in 1..4 {
                    out[a] += p[a] * 0.25;
                }
            }
            out
        }
        fn probes(&self) -> Vec<Slice> {
            let volume = self.l.pow(3);
            let mut rows = vec![[0.; 14]; self.time];
            let lower = self.l / 4;
            let frac = (self.l % 4) as f64 / 4.;
            for x in 0..self.links.len() {
                let row = &mut rows[x / volume];
                let mut winds = [[0.; 4]; 3];
                let mut adj = [0.; 3];
                let mut bfields = [[[0.; 4]; 3]; 2];
                for i in 0..3 {
                    let (j, k) = ((i + 1) % 3, (i + 2) % 3);
                    row[0] += self.plaquette(x, j, k) / 3.;
                    let (mut y, mut p) = (x, ONE);
                    for _ in 0..self.l {
                        self.step(&mut y, &mut p, i, true);
                    }
                    adj[i] = (4. * p[0] * p[0] - 1.) / 3.;
                    winds[i] = [0., p[0] * p[1], p[0] * p[2], p[0] * p[3]];
                    bfields[0][i] = self.clover(x, j, k, lower);
                    if frac > 0. {
                        bfields[1][i] = self.clover(x, j, k, lower + 1);
                    }
                }
                row[1] += adj.iter().sum::<f64>() / 3.;
                for i in 0..3 {
                    let (j, k) = ((i + 1) % 3, (i + 2) % 3);
                    row[2 + i] += adj[j] - adj[k];
                    row[8 + i] += dot(winds[j], winds[k]);
                    for (field, f) in bfields.iter().zip([1. - frac, frac]) {
                        row[5 + i] += f * (dot(field[j], field[j]) - dot(field[k], field[k]));
                        row[11 + i] += f * dot(field[j], field[k]);
                    }
                }
            }
            for row in &mut rows {
                for v in row {
                    *v /= volume as f64;
                }
            }
            rows
        }
        fn local_square(&self, x: usize, k: usize) -> f64 {
            // Average the four anchors to center the scalar at a vertex.
            let mut total = 0.;
            for i in 0..3 {
                let dirs = [
                    (i, true),
                    ((i + 1) % 3, true),
                    (i, false),
                    ((i + 1) % 3, false),
                ];
                for offset in 0..4 {
                    let (mut y, mut p) = (x, ONE);
                    for edge in 0..4 {
                        let (d, pos) = dirs[(offset + edge) % 4];
                        for _ in 0..k {
                            self.step(&mut y, &mut p, d, pos);
                        }
                    }
                    total += p[0];
                }
            }
            total / 12.
        }
        fn spatial_modes(&self) -> Vec<[f64; 26]> {
            let n = self.l;
            let volume = n.pow(3);
            let phases: Vec<_> = (0..n)
                .map(|x| {
                    let a = TAU * x as f64 / n as f64;
                    [a.cos(), a.sin(), (2. * a).cos(), (2. * a).sin()]
                })
                .collect();
            let mut rows = vec![[0.; 26]; self.time];
            for x in 0..self.links.len() {
                let cell = self.local_square(x, 1);
                let lower = if n / 4 == 1 {
                    cell
                } else {
                    self.local_square(x, n / 4)
                };
                let frac = (n % 4) as f64 / 4.;
                let matched = if frac == 0. {
                    lower
                } else {
                    (1. - frac) * lower + frac * self.local_square(x, n / 4 + 1)
                };
                for (reading, density) in [cell, matched].into_iter().enumerate() {
                    let row = &mut rows[x / volume];
                    let base = 13 * reading;
                    row[base] += density;
                    for (axis, coord) in [x % n, (x / n) % n, (x / (n * n)) % n]
                        .into_iter()
                        .enumerate()
                    {
                        for (j, phase) in phases[coord].iter().enumerate() {
                            row[base + 1 + j / 2 * 6 + axis * 2 + j % 2] += density * phase;
                        }
                    }
                }
            }
            for v in rows.iter_mut().flatten() {
                *v /= volume as f64;
            }
            rows
        }
        fn smoothed_probes(&mut self) -> Vec<Slice> {
            let volume = self.l.pow(3);
            let mut plaquettes = vec![0.; self.time];
            for x in 0..self.links.len() {
                for i in 0..3 {
                    plaquettes[x / volume] += self.plaquette(x, (i + 1) % 3, (i + 2) % 3) / 3.;
                }
            }
            let original = self.links.clone();
            let mut next = self.links.clone();
            let iterations = (self.l * self.l + 6) / 12;
            for _ in 0..iterations {
                for (x, row) in next.iter_mut().enumerate() {
                    for mu in 0..3 {
                        let mut sum = self.links[x][mu].map(|z| 4. * z);
                        for nu in 0..3 {
                            if nu == mu {
                                continue;
                            }
                            let back = self.minus[x][nu];
                            let forward = mul(
                                mul(self.links[x][nu], self.links[self.plus[x][nu]][mu]),
                                conj(self.links[self.plus[x][mu]][nu]),
                            );
                            let reverse = mul(
                                mul(conj(self.links[back][nu]), self.links[back][mu]),
                                self.links[self.plus[back][mu]][nu],
                            );
                            for c in 0..4 {
                                sum[c] += forward[c] + reverse[c];
                            }
                        }
                        row[mu] = if dot(sum, sum) > 0. {
                            unit(sum)
                        } else {
                            self.links[x][mu]
                        };
                    }
                }
                std::mem::swap(&mut self.links, &mut next);
            }
            let mut result = self.probes();
            for (row, p) in result.iter_mut().zip(plaquettes) {
                row[0] = p / volume as f64;
            }
            self.links = original;
            result
        }
        fn sf_set(&mut self, eta: f64, background: bool) {
            let n = self.l;
            assert_eq!(self.time, n + 1);
            for t in 0..=n {
                if !background && t != 0 && t != n {
                    continue;
                }
                let angle = (-eta + (2. * eta - PI) * t as f64 / n as f64) / n as f64;
                let (s, c) = angle.sin_cos();
                for x in t * n.pow(3)..(t + 1) * n.pow(3) {
                    for d in 0..3 {
                        self.links[x][d] = [c, 0., 0., s];
                    }
                }
            }
        }
        fn sf_sweep(&mut self, beta: f64, rng: &mut Rng, reflect: bool) {
            let volume = self.l.pow(3);
            for x in 0..self.links.len() {
                let t = x / volume;
                for mu in 0..4 {
                    if t == self.l || (t == 0 && mu < 3) {
                        continue;
                    }
                    let staple = self.staple(x, mu);
                    let old = self.links[x][mu];
                    self.links[x][mu] = if !reflect {
                        rng.heat(staple, beta)
                    } else if dot(staple, staple) > 0. {
                        let c = 2. * dot(old, staple) / dot(staple, staple);
                        unit(std::array::from_fn(|i| c * staple[i] - old[i]))
                    } else {
                        old
                    };
                }
            }
        }
        fn sf_derivative(&self, beta: f64) -> f64 {
            let n = self.l;
            let mut sum = 0.;
            for (t, sgn) in [(0, -1.), (n, 1.)] {
                for x in t * n.pow(3)..(t + 1) * n.pow(3) {
                    for mu in 0..3 {
                        let u = self.links[x][mu];
                        let du = mul([0., 0., 0., sgn / n as f64], u);
                        sum += dot(du, self.staple(x, mu));
                    }
                }
            }
            -beta * sum
        }
    }
    fn checks() {
        let mut rng = Rng { state: 317123 };
        let mut l = Lattice::new(5, 6, true, true, &mut rng);
        l.controls(&mut rng);
        let initial = l.probes();
        let modes = l.spatial_modes();
        for (s, m) in initial.iter().zip(&modes) {
            assert!((s[0] - m[0]).abs() < 3e-13);
        }
        let smoothed = l.smoothed_probes();
        let gs: Vec<_> = (0..l.links.len()).map(|_| rng.haar()).collect();
        for x in 0..l.links.len() {
            for mu in 0..4 {
                let q = mul(mul(gs[x], l.links[x][mu]), conj(gs[l.plus[x][mu]]));
                l.links[x][mu] = if mu == 1 && (x / l.l) % l.l == 0 {
                    q.map(|v| -v)
                } else {
                    q
                };
            }
        }
        let changed = l.probes();
        for (u, v) in l
            .spatial_modes()
            .iter()
            .flatten()
            .zip(modes.iter().flatten())
        {
            assert!((u - v).abs() < 3e-12);
        }
        for (u, v) in l
            .smoothed_probes()
            .iter()
            .flatten()
            .zip(smoothed.iter().flatten())
        {
            assert!((u - v).abs() < 5e-12);
        }
        for (a, b) in initial.iter().flatten().zip(changed.iter().flatten()) {
            assert!((a - b).abs() < 3e-12);
        }
        let links = l.links.clone();
        let n = l.l;
        for swap in [false, true] {
            for x in 0..links.len() {
                let (i, j, rest) = (x % n, (x / n) % n, x / (n * n));
                let y = if swap {
                    j + n * i + n * n * rest
                } else {
                    (n - i) % n + n * j + n * n * rest
                };
                for mu in 0..4 {
                    l.links[x][mu] = if !swap && mu == 0 {
                        conj(links[l.minus[y][0]][0])
                    } else {
                        links[y][if swap && mu < 2 { 1 - mu } else { mu }]
                    };
                }
            }
            for (a, b) in l.probes().iter().zip(&changed) {
                for idx in 0..14 {
                    let (mut src, mut sign) = (idx, 1.);
                    if idx >= 2 {
                        let axis = (idx - 2) % 3;
                        if swap {
                            if axis < 2 {
                                src = idx - axis + (1 - axis);
                            }
                            if idx < 8 {
                                sign = -1.;
                            }
                        } else if idx >= 8 && axis != 0 {
                            sign = -1.;
                        }
                    }
                    assert!((a[idx] - sign * b[src]).abs() < 4e-12);
                }
            }
        }
        let mut sf = Lattice::new(5, 6, true, false, &mut rng);
        let (beta, eta, h) = (3.2, PI / 4., 1e-5);
        sf.sf_set(eta, true);
        let d0 = sf.sf_derivative(beta);
        let k = -24. * 25. * (PI / 50.).sin();
        assert!((k / d0 - 4. / beta).abs() < 1e-12);
        sf.sf_sweep(beta, &mut rng, false);
        let derivative = sf.sf_derivative(beta);
        sf.sf_set(eta + h, false);
        let plus = sf.action();
        sf.sf_set(eta - h, false);
        let minus = sf.action();
        assert!((derivative + beta * (plus - minus) / (2. * h)).abs() < 2e-6);
        sf.sf_set(eta, false);
        let old = sf.action();
        sf.sf_sweep(beta, &mut rng, true);
        assert!((old - sf.action()).abs() < 1e-8);
        println!("gauge, center, cubic tensors, local action, overrelaxation, SF tree-level and SF derivative checks passed");
    }
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        if args.get(1).map(String::as_str) == Some("holonomies") {
            use std::io::BufRead;
            let mut rng = Rng { state: 1 };
            let mut lat = Lattice::new(4, 4, true, false, &mut rng);
            for line in std::io::stdin().lock().lines() {
                let values: Vec<f64> = line
                    .unwrap()
                    .split_whitespace()
                    .map(|s| s.parse().unwrap())
                    .collect();
                assert_eq!(values.len(), 12);
                for row in &mut lat.links {
                    for axis in 0..3 {
                        row[axis].copy_from_slice(&values[4 * axis..4 * axis + 4]);
                    }
                }
                let s = lat.probes()[0];
                println!(
                    "{:.16} {:.16} {:.16} {:.16} {:.16} {:.16}",
                    s[2], s[3], s[4], s[8], s[9], s[10]
                );
            }
            return;
        }
        if args.get(1).map(String::as_str) == Some("check") {
            checks();
            return;
        }
        assert_eq!(
            args.len(),
            11,
            "open|smooth|modes|sf N time_intervals beta seed hot burn samples stride file"
        );
        let num = |i: usize| args[i].parse::<usize>().unwrap();
        let (n, t, beta, hot, burn, samples, stride) = (
            num(2),
            num(3),
            args[4].parse::<f64>().unwrap(),
            num(6) == 1,
            num(7),
            num(8),
            num(9),
        );
        let sf = args[1] == "sf";
        let smooth = args[1] == "smooth";
        let modes = args[1] == "modes";
        assert!(
            (sf || smooth || modes || args[1] == "open")
                && n >= 4
                && stride > 0
                && t >= n
                && beta > 0.
        );
        let mut rng = Rng {
            state: args[5].parse().unwrap(),
        };
        let mut lat = Lattice::new(n, t + 1, true, hot, &mut rng);
        if sf {
            lat.sf_set(PI / 4., !hot);
        }
        let file = std::fs::OpenOptions::new()
            .write(true)
            .create_new(true)
            .open(&args[10])
            .unwrap();
        let mut out = io::BufWriter::new(file);
        for step in 1..=burn + samples * stride {
            if sf {
                lat.sf_sweep(beta, &mut rng, false);
                lat.sf_sweep(beta, &mut rng, true);
            } else {
                lat.sweep(beta, &mut rng, false);
                lat.sweep(beta, &mut rng, true);
            }
            if step <= burn || (step - burn) % stride != 0 {
                continue;
            }
            if sf {
                out.write_all(&lat.sf_derivative(beta).to_le_bytes())
                    .unwrap();
            } else {
                if modes {
                    for v in lat.spatial_modes().iter().flatten() {
                        out.write_all(&(*v as f32).to_le_bytes()).unwrap();
                    }
                    continue;
                }
                let rows = if smooth {
                    lat.smoothed_probes()
                } else {
                    lat.probes()
                };
                for v in rows.iter().flatten() {
                    out.write_all(&(*v as f32).to_le_bytes()).unwrap();
                }
            }
        }
        out.flush().unwrap();
    }
}
fn main() {
    wilson::run();
}
