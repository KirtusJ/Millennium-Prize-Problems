// Spatial plaquette fields and zero-momentum blocked rectangles on the same open slabs.
mod measurement {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::{BufWriter, Write};

    impl Lattice {
        fn rectangle(&self, site: usize, i: usize, j: usize) -> f64 {
            let path = |first: usize, second: usize| {
                let mut x = site;
                let mut q = ONE;
                for dir in [first,first,second,second] {
                    q = mul(q,self.links[x][dir]);
                    x = self.plus[x][dir];
                }
                q
            };
            dot(path(i,j),path(j,i))
        }
        fn record(&self, t: usize, beta: f64, output: &mut impl Write) {
            let n = self.l;
            let volume = n.pow(3);
            let mut coarse = [0.0;3];
            for pos in 0..volume {
                let x = t*volume+pos;
                let even = pos%n%2==0 && (pos/n)%n%2==0 && pos/(n*n)%2==0;
                for (axis, sum) in coarse.iter_mut().enumerate() {
                    let (i,j) = ((axis+1)%3,(axis+2)%3);
                    let energy = beta*(1.0-self.plaquette(x,i,j));
                    output.write_all(&energy.to_le_bytes()).unwrap();
                    if even { *sum += beta*(1.0-self.rectangle(x,i,j)); }
                }
            }
            for v in coarse { output.write_all(&v.to_le_bytes()).unwrap(); }
        }
    }

    pub fn run() {
        let args:Vec<_> = env::args().collect();
        assert!(args.len()==8 || args.len()==9,"side beta seed hot burn count new-output [extent/side]");
        let n:usize=args[1].parse().unwrap();
        let beta:f64=args[2].parse().unwrap();
        let mut rng=Rng{state:args[3].parse().unwrap()};
        let burn:usize=args[5].parse().unwrap();
        let count:usize=args[6].parse().unwrap();
        assert!(n>=6 && n%2==0 && count>0 && beta>0.0);
        let length:usize=args.get(8).map_or(6,|s|s.parse().unwrap());
        assert!(length>=3);
        let left=(length-1)*n/2;
        let mut lat=Lattice::new(n,length*n+1,true,args[4]=="1",&mut rng);
        let fp=std::fs::OpenOptions::new().write(true).create_new(true).open(&args[7]).unwrap();
        let mut out=BufWriter::new(fp);
        for step in 1..=burn+3*count {
            lat.sweep(beta,&mut rng,false);
            lat.sweep(beta,&mut rng,true);
            if step>burn && (step-burn)%3==0 {
                for t in [left,left+n] { lat.record(t,beta,&mut out); }
            }
        }
        out.flush().unwrap();
    }
}
fn main(){measurement::run();}
