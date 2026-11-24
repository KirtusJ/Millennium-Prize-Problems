// Matched 5-to-10 comparison on the same 75 straight coarse winding lines.
mod compare {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");

    fn observe(lat: &Lattice, sample: usize) {
        let n = lat.l;
        let stride = n/5;
        let lag = stride;
        let period = lat.time;
        let mut hits = [[0u32; 4]; 4];
        for dir in 0..3 {
            for a in (0..n).step_by(stride) {
                for b in (0..n).step_by(stride) {
                    let mut bins = Vec::with_capacity(period);
                    let mut coords = [0; 3];
                    coords[(dir+1)%3] = a;
                    coords[(dir+2)%3] = b;
                    let base = coords[0]+n*(coords[1]+n*coords[2]);
                    for t in 0..period {
                        let start = base+n.pow(3)*t;
                        let mut x = start;
                        let mut winding = ONE;
                        for _ in 0..n {
                            winding = mul(winding,lat.links[x][dir]);
                            x = lat.plus[x][dir];
                        }
                        assert_eq!(start,x);
                        let value = winding[0].powi(2);
                        bins.push((4.*value).floor().min(3.) as usize);
                    }
                    for t in 0..period {
                        hits[bins[t]][bins[(t+lag)%period]] += 1;
                    }
                }
            }
        }
        print!("{sample}");
        for row in hits { for count in row { print!(",{count}"); } }
        println!();
    }

    pub fn run() {
        let args: Vec<_> = env::args().collect();
        assert!(args.len()==7 || args.len()==8);
        let beta: f64 = args[1].parse().unwrap();
        let mut rng = Rng{state:args[2].parse().unwrap()};
        let n: usize = args[4].parse().unwrap();
        assert!(n==5 || n==10);
        let burn: usize = args[5].parse().unwrap();
        let count: usize = args[6].parse().unwrap();
        let period = args.get(7).map(|p| p.parse::<usize>().unwrap()).unwrap_or(2*n);
        assert!(period>=2*n);
        let mut lat = Lattice::new(n,period,false,args[3]=="1",&mut rng);
        for _ in 0..burn {lat.sweep(beta,&mut rng,false);}
        for s in 0..count {
            for _ in 0..3 {lat.sweep(beta,&mut rng,false);}
            observe(&lat,s);
        }
    }
}

fn main() {compare::run()}
