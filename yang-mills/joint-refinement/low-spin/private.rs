// Conditional moments of erased winding lines on the matched open Wilson trajectories.
mod wilson {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    use std::io::{BufWriter, Write};

    fn bessel(order: usize, x: f64) -> f64 {
        let mut term = (1..=order).fold(1.0, |v,k| v*x/(2.0*k as f64));
        let mut sum = term;
        for k in 1..160 {
            term *= (x*x/4.0)/((k*(k+order)) as f64);
            sum += term;
            if term <= 1e-17*sum { return sum; }
        }
        panic!("Bessel series did not converge");
    }
    fn ratios(x:f64) -> (f64,f64) {
        if x==0.0 { return (0.0,0.0); }
        let first=bessel(1,x);
        (bessel(3,x)/first,bessel(5,x)/first)
    }
    fn chi2(x:f64) -> f64 { 4.0*x*x-1.0 }
    fn chi4(x:f64) -> f64 { 16.0*x.powi(4)-12.0*x*x+1.0 }

    impl Lattice {
        fn conditional(&self, time:usize, beta:f64) -> [[f64;3];4] {
            let n=self.l;
            let mut full=[0.;3];
            let mut kept=[0.;3];
            let mut mean=[0.;3];
            let mut var=[0.;3];
            for axis in 0..3 {
                for u in 0..n { for v in 0..n {
                    let mut coord=[0;3];
                    coord[(axis+1)%3]=u;
                    coord[(axis+2)%3]=v;
                    let coarse=u%2==0 && v%2==0;
                    let mut pos=coord[0]+n*(coord[1]+n*(coord[2]+n*time));
                    let (mut actual,mut mode)=(ONE,ONE);
                    let (mut k2,mut k4)=(1.0,1.0);
                    for s in 0..n {
                        let d=(s+u+v)%n;
                        let link=self.links[pos][axis];
                        actual=mul(actual,link);
                        if !coarse && d%2==0 && (d/2)%3==axis {
                            let staple=self.staple(pos,axis);
                            let scale=dot(staple,staple).sqrt();
                            let (a,b)=ratios(beta*scale);
                            k2*=a; k4*=b;
                            mode=mul(mode,if scale>0. {staple.map(|w|w/scale)} else {ONE});
                        } else { mode=mul(mode,link); }
                        pos=self.plus[pos][axis];
                    }
                    let c=chi2(actual[0]);
                    let m=k2*chi2(mode[0]);
                    full[axis]+=c;
                    mean[axis]+=m;
                    if coarse {kept[axis]+=c;}
                    else {
                        let vv=1.0+m+k4*chi4(mode[0])-m*m;
                        assert!(vv>=-1e-11 && vv<=4.0+1e-10);
                        var[axis]+=vv;
                    }
                }}
            }
            let mut out=[[0.;3];4];
            let scale=3.0*(n*n) as f64;
            for i in 0..3 {
                let (j,k)=((i+1)%3,(i+2)%3);
                out[0][i]=(full[j]-full[k])/scale;
                out[1][i]=4.0*(kept[j]-kept[k])/scale;
                out[2][i]=(mean[j]-mean[k])/scale;
                out[3][i]=(var[j]+var[k])/(scale*scale);
            }
            out
        }
    }
    #[cfg(test)]
    mod tests {
        use super::*;

        // Compress the known parts of a winding. A fixed quaternion precedes each
        // heat-bath sample, with one final fixed factor after the last sample.
        struct Line {
            axis: usize,
            pieces: Vec<(Q,Q)>,
            last: Q,
        }

        fn lines(lat: &Lattice, time: usize) -> Vec<Line> {
            let n=lat.l;
            let mut out=Vec::new();
            for axis in 0..3 {
                for y in 0..n { for z in 0..n {
                    let mut fixed=ONE;
                    let mut pieces=Vec::new();
                    for x in 0..n {
                        let mut c=[0;3];
                        c[axis]=x; c[(axis+1)%3]=y; c[(axis+2)%3]=z;
                        let site=c[0]+n*(c[1]+n*(c[2]+n*time));
                        let grade=(x+y+z)%n;
                        if (y%2+z%2)>0 && grade%6==2*axis {
                            pieces.push((fixed,lat.staple(site,axis)));
                            fixed=ONE;
                        } else { fixed=mul(fixed,lat.links[site][axis]); }
                    }
                    out.push(Line{axis,pieces,last:fixed});
                }}
            }
            out
        }

        fn draw(lines:&[Line], n:usize, beta:f64, rng:&mut Rng) -> [f64;3] {
            let mut sums=[0.;3];
            for line in lines {
                let mut w=ONE;
                for &(fixed,staple) in &line.pieces {
                    w=mul(mul(w,fixed),rng.heat(staple,beta));
                }
                sums[line.axis]+=chi2(mul(w,line.last)[0]);
            }
            std::array::from_fn(|i| (sums[(i+1)%3]-sums[(i+2)%3])/(3*n*n) as f64)
        }

        #[test]
        fn conditional_two_slice_readback() {
            let beta=3.4;
            for n in [6,10] {
                let mut rng=Rng{state:351893+n as u64};
                let mut lat=Lattice::new(n,n+3,true,false,&mut rng);
                for _ in 0..4 {lat.sweep(beta,&mut rng,false);}
                let times=[1,n+1];
                let expected=times.map(|t| lat.conditional(t,beta));
                let paths=times.map(|t| lines(&lat,t));
                let count=8192;
                let mut sum=[0.;15];
                let mut sum2=[0.;15];
                for _ in 0..count {
                    let d:[[_;3];2]=std::array::from_fn(|j| {
                        let f=draw(&paths[j],n,beta,&mut rng);
                        std::array::from_fn(|i| f[i]-expected[j][2][i])
                    });
                    let v:[f64;15]=std::array::from_fn(|k|{
                        let i=k%3;
                        match k/3 {
                            0=>d[0][i], 1=>d[1][i],
                            2=>d[0][i].powi(2)-expected[0][3][i],
                            3=>d[1][i].powi(2)-expected[1][3][i],
                            _=>d[0][i]*d[1][i],
                        }
                    });
                    for k in 0..15 {sum[k]+=v[k]; sum2[k]+=v[k]*v[k];}
                }
                let zs:[f64;15]=std::array::from_fn(|k|sum[k]/(sum2[k]-sum[k].powi(2)/count as f64).sqrt());
                let worst=zs.iter().map(|z|z.abs()).fold(0.0,f64::max);
                println!("N={n} fixed-exterior maximum standardized discrepancy {worst:.4}");
                assert!(worst<6.0);
            }
        }
    }

    pub fn run() {
        let args:Vec<String>=env::args().collect();
        assert_eq!(args.len(),8,"side beta seed hot burn count output");
        let n:usize=args[1].parse().unwrap();
        let beta:f64=args[2].parse().unwrap();
        let mut rng=Rng{state:args[3].parse().unwrap()};
        let burn:usize=args[5].parse().unwrap();
        let count:usize=args[6].parse().unwrap();
        assert!(n>=6 && n%2==0 && beta>0.0 && beta<=4.0 && count>0);
        let mut lat=Lattice::new(n,6*n+1,true,args[4]=="1",&mut rng);
        let file=std::fs::OpenOptions::new().write(true).create_new(true).open(&args[7]).unwrap();
        let mut out=BufWriter::new(file);
        for step in 1..=burn+3*count {
            lat.sweep(beta,&mut rng,false);
            lat.sweep(beta,&mut rng,true);
            if step>burn && (step-burn)%3==0 {
                for t in [5*n/2,7*n/2] {
                    for row in lat.conditional(t,beta) {
                        for v in row {out.write_all(&v.to_le_bytes()).unwrap();}
                    }
                }
            }
        }
        out.flush().unwrap();
    }
}
fn main(){wilson::run();}
