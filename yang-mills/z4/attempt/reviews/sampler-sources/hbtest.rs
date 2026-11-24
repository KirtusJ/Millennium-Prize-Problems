// Exact-law test of wilson_mc.rs heat bath: for staple norm k (beta=1), E[a0] = I2(k)/I1(k).
// Prints k, mean a0, mean a0^2, n. Predicate (checked in hbtest.py): |mean - exact| <= 4 standard errors.
mod m {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    pub fn run() {
        let mut rng = Rng { state: 987654321 };
        for &k in &[0.5f64, 0.99, 1.01, 1.9, 2.1, 5.0, 10.0, 20.0] {
            let n = 400000;
            let s: Q = [0.3 * k, 0.4 * k, 0.5 * k, (0.5f64).sqrt() * k]; // norm k
            let (mut m1, mut m2) = (0., 0.);
            for _ in 0..n { let u = rng.heat(s, 1.0); let a = dot(u, s) / k; m1 += a; m2 += a * a; }
            println!("{k} {} {} {n}", m1 / n as f64, m2 / n as f64);
        }
    }
}
fn main() { m::run(); }
