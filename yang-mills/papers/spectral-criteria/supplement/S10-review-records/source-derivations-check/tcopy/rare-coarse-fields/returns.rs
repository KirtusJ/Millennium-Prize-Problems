// Same coarse spatial loop on two distinct Euclidean-time slices.
mod experiment {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");

    const RADII: [f64; 6] = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2];

    fn coarse_trace(lat: &Lattice, start: usize, i: usize, j: usize) -> f64 {
        let mut x = start;
        let mut loop_value = ONE;
        for (axis, positive) in [(i,true), (j,true), (i,false), (j,false)] {
            for _ in 0..2 {
                if positive {
                    loop_value = mul(loop_value, lat.links[x][axis]);
                    x = lat.plus[x][axis];
                } else {
                    x = lat.minus[x][axis];
                    loop_value = mul(loop_value, conj(lat.links[x][axis]));
                }
            }
        }
        debug_assert_eq!(start, x);
        loop_value[0]
    }

    fn observe(lat: &Lattice, sample: usize) {
        let thresholds = RADII.map(|r| -r.cos());
        let mut counts = [[0usize; 4]; 6];
        let (n, period) = (lat.l, lat.time);
        let nobs = 3*(n/2).pow(3)*period;
        let mut sequence = vec![0.0; period];
        for z in (0..n).step_by(2) {
            for y in (0..n).step_by(2) {
                for x in (0..n).step_by(2) {
                    let site = x + n*(y+n*z);
                    for (i,j) in [(0,1),(0,2),(1,2)] {
                        for (t, value) in sequence.iter_mut().enumerate() {
                            *value = coarse_trace(lat, site+t*n.pow(3), i, j);
                        }
                        for t in 0..period {
                            for (h, &cut) in thresholds.iter().enumerate() {
                                if sequence[t] <= cut {
                                    counts[h][0] += 1;
                                    for (b, lag) in [1, 2, n/2].iter().enumerate() {
                                        counts[h][b+1] += (sequence[(t+lag)%period] <= cut) as usize;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        for (r, [hits, one, two, half_box]) in RADII.iter().zip(counts) {
            println!("{sample},{r},{nobs},{hits},{one},{two},{half_box}");
        }
    }

    pub fn run() {
        let args: Vec<_> = env::args().collect();
        assert_eq!(args.len(), 8);
        let beta: f64 = args[1].parse().unwrap();
        let mut rng = Rng{state: args[2].parse().unwrap()};
        let hot = args[3] == "1";
        let n: usize = args[4].parse().unwrap();
        let period: usize = args[5].parse().unwrap();
        let burn: usize = args[6].parse().unwrap();
        let samples: usize = args[7].parse().unwrap();
        assert!(n>=6 && n%2==0 && period>n/2);
        let mut lat = Lattice::new(n, period, false, hot, &mut rng);
        for _ in 0..burn {
            lat.sweep(beta, &mut rng, false);
        }
        println!("sample,theta,exposures,hits,lag1,lag2,lag_half_box");
        for s in 0..samples {
            for _ in 0..3 {
                lat.sweep(beta, &mut rng, false);
            }
            observe(&lat, s);
        }
    }
}

fn main() { experiment::run() }
