// Replay the archived open Wilson chains, measuring the eight blocking origins.
mod wilson {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::{BufWriter, Write};

    impl Lattice {
        fn anchor_probes(&self, time: usize) -> [[f64; 3]; 8] {
            let mut rows = [[0.0; 3]; 8];
            for site in 0..self.l.pow(3) {
                let x = site + self.l.pow(3)*time;
                let mut adj = [0.0; 3];
                for (axis, value) in adj.iter_mut().enumerate() {
                    let mut pos = x;
                    let mut loop_value = ONE;
                    for _ in 0..self.l {
                        loop_value = mul(loop_value, self.links[pos][axis]);
                        pos = self.plus[pos][axis];
                    }
                    *value = (4.0*loop_value[0]*loop_value[0]-1.0)/3.0;
                }
                let parity = site%2 + 2*((site/self.l)%2) + 4*((site/self.l.pow(2))%2);
                for i in 0..3 {
                    rows[parity][i] += adj[(i+1)%3]-adj[(i+2)%3];
                }
            }
            for row in &mut rows {
                for value in row { *value /= (self.l/2).pow(3) as f64; }
            }
            rows
        }
    }

    pub fn measure() {
        let args: Vec<String> = env::args().collect();
        if args.get(1).map(String::as_str)==Some("fields") {
            use std::io::Read;
            let n = args[2].parse().unwrap();
            let nt = args[3].parse().unwrap();
            let mut lat = Lattice::new(n, nt, false, false, &mut Rng { state: 1 });
            let mut buf = Vec::new();
            std::io::stdin().read_to_end(&mut buf).unwrap();
            assert_eq!(buf.len(), n*n*n*nt*3*4*8);
            let mut values = buf.chunks_exact(8).map(|x| f64::from_le_bytes(x.try_into().unwrap()));
            for row in &mut lat.links {
                for link in row.iter_mut().take(3) {
                    for component in link { *component = values.next().unwrap(); }
                }
            }
            let mut output = std::io::stdout().lock();
            for time in 0..nt {
                for origin in lat.anchor_probes(time) {
                    for value in origin { output.write_all(&value.to_le_bytes()).unwrap(); }
                }
            }
            return;
        }
        assert_eq!(args.len(), 8, "N beta seed hot burn count output");
        let n: usize = args[1].parse().unwrap();
        let beta = args[2].parse().unwrap();
        let mut rng = Rng { state: args[3].parse().unwrap() };
        let burn: usize = args[5].parse().unwrap();
        let count: usize = args[6].parse().unwrap();
        assert!(n>=4 && n%2==0 && count>0);
        let mut lattice = Lattice::new(n, 6*n+1, true, args[4]=="1", &mut rng);
        let output = std::fs::OpenOptions::new().create_new(true).write(true).open(&args[7]).unwrap();
        let mut file = BufWriter::new(output);
        for step in 1..=burn+3*count {
            lattice.sweep(beta,&mut rng,false);
            lattice.sweep(beta,&mut rng,true);
            if step>burn && (step-burn)%3==0 {
                for time in [5*n/2, 7*n/2] {
                    for row in lattice.anchor_probes(time) {
                        for v in row { file.write_all(&v.to_le_bytes()).unwrap(); }
                    }
                }
            }
        }
        file.flush().unwrap();
    }
}

fn main() { wilson::measure(); }
