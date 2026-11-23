// Isotropic SU(2) heat bath, periodic space and either open or periodic time.
use std::{env, f64::consts::TAU};
type Q = [f64; 4];
const ONE: Q = [1., 0., 0., 0.];
fn mul([a, b, c, d]: Q, [e, f, g, h]: Q) -> Q {
    [
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    ]
}
fn conj([a, b, c, d]: Q) -> Q {
    [a, -b, -c, -d]
}
fn dot(a: Q, b: Q) -> f64 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}
fn unit(a: Q) -> Q {
    let n = dot(a, a).sqrt();
    a.map(|x| x / n)
}

struct Rng {
    state: u64,
}
impl Rng {
    // SplitMix64 with open midpoints of 52-bit bins.
    fn u(&mut self) -> f64 {
        self.state = self.state.wrapping_add(0x9e3779b97f4a7c15);
        let mut z = self.state;
        z = (z ^ (z >> 30)).wrapping_mul(0xbf58476d1ce4e5b9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94d049bb133111eb);
        (((z ^ (z >> 31)) >> 12) as f64 + 0.5) / 4503599627370496.
    }
    fn gauss(&mut self) -> f64 {
        (-2. * self.u().ln()).sqrt() * (TAU * self.u()).cos()
    }
    fn haar(&mut self) -> Q {
        unit([self.gauss(), self.gauss(), self.gauss(), self.gauss()])
    }
    fn heat(&mut self, staple: Q, beta: f64) -> Q {
        let norm = dot(staple, staple).sqrt();
        if norm == 0. {
            return self.haar();
        }
        let k = norm * beta;
        let v = if k < 1. {
            loop {
                let q = self.haar();
                if self.u() <= (k * (q[0] - 1.)).exp() {
                    break q;
                }
            }
        } else {
            // Gamma(3/2,1) proposal for k(1-cos theta).
            let a = loop {
                let g = self.gauss();
                let x = -self.u().ln() + g * g / 2.;
                if x < 2. * k && self.u().powi(2) < 1. - x / (2. * k) {
                    break 1. - x / k;
                }
            };
            let t = 2. * self.u() - 1.;
            let (s, c) = (TAU * self.u()).sin_cos();
            let r = ((1. - a) * (1. + a)).sqrt();
            let xy = r * (1. - t * t).sqrt();
            [a, xy * c, xy * s, r * t]
        };
        mul(v, staple.map(|x| x / norm))
    }
}
struct Lattice {
    links: Vec<[Q; 4]>,
    plus: Vec<[usize; 4]>,
    minus: Vec<[usize; 4]>,
    l: usize,
    time: usize,
    open: bool,
}
impl Lattice {
    fn new(l: usize, time: usize, open: bool, hot: bool, rng: &mut Rng) -> Self {
        assert!(l >= 2 && time >= 4);
        let sizes = [l, l, l, time];
        let rows = l.pow(3) * time;
        let mut obj = Self {
            links: vec![[ONE; 4]; rows],
            plus: vec![[0; 4]; rows],
            minus: vec![[0; 4]; rows],
            l,
            time,
            open,
        };
        for x in 0..rows {
            let mut stride = 1;
            for (mu, n) in sizes.iter().enumerate() {
                let pos = (x / stride) % n;
                obj.plus[x][mu] = if pos + 1 < *n {
                    x + stride
                } else {
                    x - (n - 1) * stride
                };
                obj.minus[x][mu] = if pos > 0 {
                    x - stride
                } else {
                    x + (n - 1) * stride
                };
                if hot {
                    obj.links[x][mu] = rng.haar();
                }
                stride *= n;
            }
        }
        obj
    }
    fn weight(&self, x: usize, mu: usize, nu: usize) -> f64 {
        if !self.open {
            return 1.;
        }
        let t = x / self.l.pow(3);
        if mu == 3 || nu == 3 {
            if t + 1 == self.time {
                0.
            } else {
                1.
            }
        } else if t == 0 || t + 1 == self.time {
            0.5
        } else {
            1.
        }
    }
    fn staple(&self, x: usize, mu: usize) -> Q {
        let mut out = [0.; 4];
        let u = &self.links;
        for nu in 0..4 {
            if mu == nu {
                continue;
            }
            let back = self.minus[x][nu];
            let forward = mul(
                mul(u[x][nu], u[self.plus[x][nu]][mu]),
                conj(u[self.plus[x][mu]][nu]),
            );
            let reverse = mul(
                mul(conj(u[back][nu]), u[back][mu]),
                u[self.plus[back][mu]][nu],
            );
            let (a, b) = (self.weight(x, mu, nu), self.weight(back, mu, nu));
            for i in 0..4 {
                out[i] += a * forward[i] + b * reverse[i];
            }
        }
        out
    }
    fn sweep(&mut self, beta: f64, rng: &mut Rng, reflect: bool) {
        for x in 0..self.links.len() {
            for mu in 0..4 {
                let s = self.staple(x, mu);
                self.links[x][mu] = if reflect {
                    let norm2 = dot(s, s);
                    let old = self.links[x][mu];
                    if norm2 == 0. {
                        old
                    } else {
                        let c = 2. * dot(old, s) / norm2;
                        unit(std::array::from_fn(|i| c * s[i] - old[i]))
                    }
                } else {
                    rng.heat(s, beta)
                };
            }
        }
    }
    fn plaquette(&self, x: usize, mu: usize, nu: usize) -> f64 {
        dot(
            mul(self.links[x][mu], self.links[self.plus[x][mu]][nu]),
            mul(self.links[x][nu], self.links[self.plus[x][nu]][mu]),
        )
    }
    fn action(&self) -> f64 {
        (0..self.links.len())
            .map(|x| {
                (0..4)
                    .map(|mu| {
                        (0..mu)
                            .map(|nu| self.plaquette(x, mu, nu) * self.weight(x, mu, nu))
                            .sum::<f64>()
                    })
                    .sum::<f64>()
            })
            .sum()
    }
    fn slices(&self) -> Vec<[f64; 3]> {
        let volume = self.l.pow(3);
        let mut out = vec![[0.; 3]; self.time];
        for x in 0..self.links.len() {
            let row = &mut out[x / volume];
            let mut adj = [0.; 3];
            for mu in 0..3 {
                row[0] += self.plaquette(x, mu, (mu + 1) % 3) / (3 * volume) as f64;
                let mut y = x;
                let mut p = ONE;
                for _ in 0..self.l {
                    p = mul(p, self.links[y][mu]);
                    y = self.plus[y][mu];
                }
                adj[mu] = (4. * p[0] * p[0] - 1.) / 3.;
            }
            row[1] += (adj[0] + adj[1] + adj[2]) / (3 * volume) as f64;
            row[2] += (adj[0] - adj[1]) / volume as f64;
        }
        out
    }
    fn controls(&mut self, rng: &mut Rng) {
        let original = self.links.clone();
        let old = self.action();
        let g: Vec<Q> = (0..self.links.len()).map(|_| rng.haar()).collect();
        let slices = self.slices();
        for x in 0..self.links.len() {
            for mu in 0..4 {
                self.links[x][mu] = mul(mul(g[x], self.links[x][mu]), conj(g[self.plus[x][mu]]));
                if mu == 0 && x % self.l == self.l - 1 {
                    self.links[x][mu] = self.links[x][mu].map(|v| -v);
                }
            }
        }
        assert!((self.action() - old).abs() < 1e-9);
        for (a, b) in self.slices().iter().zip(slices) {
            for k in 0..3 {
                assert!((a[k] - b[k]).abs() < 2e-12);
            }
        }
        self.links = original.clone();
        let s = self.staple(0, 0);
        let prev = self.links[0][0];
        self.links[0][0] = rng.haar();
        let delta = dot(self.links[0][0], s) - dot(prev, s);
        assert!((self.action() - old - delta).abs() < 1e-9);
        self.links = original.clone();
        self.sweep(1., rng, true);
        assert!((self.action() - old).abs() < 1e-9);
        self.links = original;
    }
}
fn main() {
    let args: Vec<_> = env::args().collect();
    assert!(
        args.len() == 10,
        "L T beta seed hot(0/1) burn_blocks blocks sweeps_per_block open|periodic"
    );
    let integer = |i: usize| args[i].parse::<usize>().unwrap();
    let (l, t, beta) = (integer(1), integer(2), args[3].parse::<f64>().unwrap());
    let mut rng = Rng {
        state: args[4].parse().unwrap(),
    };
    let (burn, blocks, sweeps) = (integer(6), integer(7), integer(8));
    assert!(args[9] == "open" || args[9] == "periodic");
    let open = args[9] == "open";
    let mut lat = Lattice::new(l, t, open, integer(5) == 1, &mut rng);
    lat.controls(&mut rng);
    let lags = 6.min(t / 2);
    print!("block,observable,mean");
    for lag in 0..=lags {
        print!(",moment{lag}");
    }
    if open {
        for time in 0..t {
            print!(",slice{time}");
        }
    }
    println!();
    for block in 0..burn + blocks {
        let mut sums = vec![vec![0.; lags + 2 + if open { t } else { 0 }]; 3];
        for _ in 0..sweeps {
            lat.sweep(beta, &mut rng, false);
            lat.sweep(beta, &mut rng, true);
            if block < burn {
                continue;
            }
            let v = lat.slices();
            for k in 0..3 {
                for time in 0..t {
                    sums[k][0] += v[time][k];
                    if open {
                        sums[k][lags + 2 + time] += v[time][k];
                    }
                    for lag in 0..=lags {
                        if !open || (time >= t / 4 && time + lag < t - t / 4) {
                            sums[k][lag + 1] += v[time][k] * v[(time + lag) % t][k];
                        }
                    }
                }
            }
        }
        if block >= burn {
            for (k, label) in ["plaquette", "adjoint", "tensor"].iter().enumerate() {
                print!("{},{label}", block - burn);
                for (col, value) in sums[k].iter().enumerate() {
                    let origins = if !open || col == 0 {
                        t
                    } else if col <= lags + 1 {
                        t - 2 * (t / 4) - (col - 1)
                    } else {
                        1
                    };
                    assert!(origins > 0);
                    print!(",{:.15}", value / (origins * sweeps) as f64);
                }
                println!();
            }
        }
    }
}
