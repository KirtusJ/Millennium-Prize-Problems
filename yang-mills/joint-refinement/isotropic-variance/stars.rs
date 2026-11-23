// Conditional mean and variance of one spatial Wilson plane sum.
mod measurement {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::{BufWriter, Write};

    fn mean_over_k(k: f64) -> f64 {
        assert!((0.0..=64.0).contains(&k));
        // I2(k)/(k I1(k)), including its continuous limit at zero.
        let mut d = 260.0;
        for j in (2..130).rev() {
            d = 2.0*j as f64 + k*k/d;
        }
        1.0/d
    }

    impl Lattice {
        fn pair(&self, x: usize, mu: usize, nu: usize) -> Q {
            let u = &self.links;
            let y = self.minus[x][nu];
            let a = mul(mul(u[x][nu], u[self.plus[x][nu]][mu]), conj(u[self.plus[x][mu]][nu]));
            let b = mul(mul(conj(u[y][nu]), u[y][mu]), u[self.plus[y][mu]][nu]);
            std::array::from_fn(|i| a[i]+b[i])
        }

        fn observe(&self, time: usize, beta: f64, out: &mut impl Write) {
            let n = self.l;
            let volume = n.pow(3);
            let norm = (volume as f64).sqrt();
            for normal in 0..3 {
                let mu = (normal+1)%3;
                let nu = (normal+2)%3;
                let mut raw = 0.0;
                let mut predicted = 0.0;
                let mut variance = 0.0;
                for pos in 0..volume {
                    let coords = [pos%n,(pos/n)%n,pos/(n*n)];
                    if (coords[normal]+coords[nu])%2 != 0 { continue; }
                    let x = time*volume+pos;
                    let a = self.pair(x,mu,nu);
                    let h = self.staple(x,mu);
                    let h2 = dot(h,h);
                    let k = beta*h2.sqrt();
                    let t = mean_over_k(k);
                    let u = k*t;
                    let parallel2 = if h2==0.0 { 0.0 } else { dot(h,a).powi(2)/h2 };
                    let var = beta*beta*(t*dot(a,a)+(1.0-4.0*t-u*u)*parallel2);
                    assert!(var >= -1e-10);
                    raw += beta*(2.0-dot(self.links[x][mu],a));
                    predicted += beta*(2.0-beta*t*dot(h,a));
                    variance += var;
                }
                for v in [raw/norm,predicted/norm,variance/volume as f64] {
                    out.write_all(&v.to_le_bytes()).unwrap();
                }
            }
        }
    }

    fn conditional_test() {
        let n=6;
        let beta=3.4;
        let volume=n*n*n;
        let mut rng=Rng{state:648929};
        let mut lat=Lattice::new(n,8,false,true,&mut rng);
        let time=3;
        let mut bytes=Vec::new();
        lat.observe(time,beta,&mut bytes);
        let readings:Vec<_>=bytes.chunks_exact(8).map(|b| f64::from_le_bytes(b.try_into().unwrap())).collect();
        let stars:Vec<_>=(0..volume).filter(|p| (p%n+p/(n*n))%2==0).map(|p| {
            let x=time*volume+p;
            (x,lat.staple(x,1),lat.pair(x,1,2))
        }).collect();
        let reference=beta*(0..volume).map(|p| 1.0-lat.plaquette(time*volume+p,1,2)).sum::<f64>()/(volume as f64).sqrt();
        assert!((reference-readings[0]).abs()<1e-11);
        let mut m=0.0;
        let mut s=0.0;
        let draws=10_000;
        for i in 1..=draws {
            let sum=stars.iter().map(|&(x,h,a)| {
                let u=rng.heat(h,beta);
                lat.links[x][1]=u;
                beta*(2.0-dot(u,a))
            }).sum::<f64>()/(volume as f64).sqrt();
            let d=sum-m;
            m+=d/i as f64;
            s+=d*(sum-m);
        }
        let v=s/(draws-1) as f64;
        bytes.clear();
        lat.observe(time,beta,&mut bytes);
        let reread:Vec<_>=bytes.chunks_exact(8).map(|b| f64::from_le_bytes(b.try_into().unwrap())).collect();
        assert_eq!(reread[1],readings[1]);
        assert_eq!(reread[2],readings[2]);
        assert!((m-readings[1]).abs()<6.0*(readings[2]/draws as f64).sqrt());
        assert!((v/readings[2]-1.0).abs()<0.08);
        println!("fixed exterior: mean {:.8} vs {:.8}, variance {:.8} vs {:.8}",m,readings[1],v,readings[2]);
    }

    pub fn run() {
        let args: Vec<_> = env::args().collect();
        if args.len()==2 && args[1]=="--test" { conditional_test(); return; }
        assert!(args.len()==8 || args.len()==9,"side beta seed hot burn count new-output [extent/side]");
        let n:usize=args[1].parse().unwrap();
        let beta:f64=args[2].parse().unwrap();
        let seed=args[3].parse().unwrap();
        let burn:usize=args[5].parse().unwrap();
        let count:usize=args[6].parse().unwrap();
        assert!(n>=6 && n%2==0 && beta>0.0 && 6.0*beta<64.0 && count>0);
        assert!(args[4]=="0" || args[4]=="1");
        let mut rng=Rng{state:seed};
        let width:usize=args.get(8).map_or(6,|s|s.parse().unwrap());
        assert!(width>=3);
        let first=(width-1)*n/2;
        let mut lat=Lattice::new(n,width*n+1,true,args[4]=="1",&mut rng);
        let file=std::fs::OpenOptions::new().write(true).create_new(true).open(&args[7]).unwrap();
        let mut out=BufWriter::new(file);
        for step in 1..=burn+3*count {
            lat.sweep(beta,&mut rng,false);
            lat.sweep(beta,&mut rng,true);
            if step>burn && (step-burn)%3==0 {
                for t in [first,first+n] { lat.observe(t,beta,&mut out); }
            }
        }
        out.flush().unwrap();
    }
}
fn main() { measurement::run(); }
