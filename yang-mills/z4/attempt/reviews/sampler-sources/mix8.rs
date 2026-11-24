// Same-skeleton two-copy diagnostic on a finite periodic Wilson lattice.
mod pilot {
    #![allow(dead_code)]
    include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");
    type Edge = (usize, usize);
    type Pair = (usize, usize, usize, Edge, Edge);

    fn colours(lat: &Lattice) -> Vec<Vec<Pair>> {
        let n = lat.l;
        let mut groups = vec![Vec::new(); 24];
        for x in 0..n.pow(3) {
            let parity = [x%n%2, (x/n)%n%2, (x/(n*n))%2];
            for (o,(i,j)) in [(0,1),(0,2),(1,2)].into_iter().enumerate() {
                let u = (if parity[j]==1 { x } else { lat.plus[x][j] }, i);
                let v = (if parity[i]==1 { x } else { lat.plus[x][i] }, j);
                groups[8*o+parity[0]+2*parity[1]+4*parity[2]].push((x,i,j,u,v));
            }
        }
        groups
    }

    fn frozen(lat: &Lattice, x: usize, i: usize) -> bool {
        let n = lat.l;
        if x>=n.pow(3) || i==3 {return false;}
        let coord = [x%n,(x/n)%n,x/(n*n)];
        (0..3).all(|j| j==i || coord[j]%2==0)
    }

    fn conditional_sweep(lat: &mut Lattice, beta: f64, rng: &mut Rng) {
        for x in 0..lat.links.len() {
            for i in 0..4 {
                if !frozen(lat,x,i) {lat.links[x][i]=rng.heat(lat.staple(x,i),beta);}
            }
        }
    }

    fn draw(lat: &mut Lattice, pair: Pair, beta: f64, rng: &mut Rng) {
        let (x,i,j,(u,a),(v,b))=pair;
        let initial=lat.links[u][a];
        let complete=if beta>=8. {lat.staple(u,a)} else {[0.;4]};
        // Zeroing the partner removes just the common face from the staple.
        lat.links[u][a]=[0.;4];
        lat.links[v][b]=[0.;4];
        let hu=lat.staple(u,a);
        let hv=lat.staple(v,b);
        if beta>=8. {
            // Y = u dot O v for an exterior-dependent orthogonal O.
            // The initial pair chooses an envelope; each envelope samples the
            // same joint target. This avoids exp(-2 beta) acceptance in a twist.
            let shift:Q=std::array::from_fn(|n| initial[n]-(complete[n]-hu[n]));
            lat.links[u][a]=shift;
            let shifted=lat.staple(v,b);
            let reverse:Q=std::array::from_fn(|n| shifted[n]-hv[n]);
            let left:Q=std::array::from_fn(|n| hu[n]-shift[n]);
            loop {
                let first=rng.heat(left,beta);
                let second=rng.heat(shifted,beta);
                lat.links[u][a]=first;
                lat.links[v][b]=second;
                let exponent=lat.plaquette(x,i,j)-1.+dot(shift,first)
                    -dot(reverse,second)-dot(shift,shift)/2.;
                assert!(exponent<=2e-12);
                if rng.u().ln()<=beta*exponent {return;}
            }
        }
        loop {
            lat.links[u][a]=rng.heat(hu,beta);
            lat.links[v][b]=rng.heat(hv,beta);
            let y=lat.plaquette(x,i,j);
            debug_assert!(y.abs()<=1.+1e-12);
            if rng.u().ln()<=beta*(y-1.) {break;}
        }
    }

    fn observe(lat: &Lattice,beta:f64) -> [f64;2] {
        let n=lat.l;
        let ps=(0..n.pow(3)).map(|x| 1.-lat.plaquette(x,0,1)).sum::<f64>();
        let mut winding=ONE;
        let mut x=n+1;
        for _ in 0..n {
            winding=mul(winding,lat.links[x][2]);
            x=lat.plus[x][2];
        }
        [beta.max(1.)*ps/(n.pow(3) as f64).sqrt(),winding[0].powi(2)]
    }

    fn face(lat:&Lattice,x:usize,i:usize,j:usize,length:usize)->Q {
        let mut u=ONE;
        let mut y=x;
        for (d,forward) in [(i,true),(j,true),(i,false),(j,false)] {
            for _ in 0..length {
                if forward {u=mul(u,lat.links[y][d]);y=lat.plus[y][d];}
                else {y=lat.minus[y][d];u=mul(u,conj(lat.links[y][d]));}
            }
        }
        u
    }

    fn disk_probes(lat:&Lattice)->[f64;3] {
        let b=face(lat,0,0,2,2);
        let first=mul(b,face(lat,0,0,1,1))[0];
        let mut average=[0.;4];
        for x in 0..2 {for y in 0..2 {
            let mut site=0;
            let mut path=ONE;
            for (d,steps) in [(0,x),(1,y)] {
                for _ in 0..steps {path=mul(path,lat.links[site][d]);site=lat.plus[site][d];}
            }
            let g=mul(mul(path,face(lat,site,0,1,1)),conj(path));
            for i in 0..4 {average[i]+=g[i]/4.;}
        }}
        [first,mul(b,average)[0],1.-dot(average,average)]
    }

    fn fixed(args:&[String]) {
        assert_eq!(args.len(),10,"fixed beta seed hot burn samples side period sign");
        let beta=args[2].parse::<f64>().unwrap();
        let seed=args[3].parse::<u64>().unwrap();
        let mut rng=Rng{state:seed};
        let mut measures=Rng{state:seed ^ 0x6a09e667f3bcc909};
        let n=args[7].parse::<usize>().unwrap();
        let period=args[8].parse::<usize>().unwrap();
        let sign=args[9].parse::<f64>().unwrap();
        assert!(n>=6 && n%2==0 && period>=6 && period%2==0 && sign.abs()==1.);
        let mut lat=Lattice::new(n,period,false,args[4]=="1",&mut rng);
        for x in 0..n.pow(3) {for i in 0..3 {
            if frozen(&lat,x,i) {lat.links[x][i]=ONE;}
        }}
        lat.links[2][1]=[sign,0.,0.,0.];
        lat.links[2][2]=[0.,1.,0.,0.];
        assert_eq!(face(&lat,0,0,1,2),[sign,0.,0.,0.]);
        assert_eq!(face(&lat,0,0,2,2),[0.,1.,0.,0.]);
        for _ in 0..args[5].parse::<usize>().unwrap() {conditional_sweep(&mut lat,beta,&mut rng);}
        let sets=colours(&lat);
        println!("single,average,spread,j_single,j_average");
        for _ in 0..args[6].parse::<usize>().unwrap() {
            for _ in 0..6 {conditional_sweep(&mut lat,beta,&mut rng);}
            let original=lat.links[..n.pow(3)].to_vec();
            let readings=disk_probes(&lat);
            let mut j=[0.;2];
            for pairs in &sets {
                for &pair in pairs {draw(&mut lat,pair,beta,&mut measures);}
                let f=disk_probes(&lat);
                for &pair in pairs {draw(&mut lat,pair,beta,&mut measures);}
                let g=disk_probes(&lat);
                for t in 0..2 {j[t]+=(f[t]-g[t]).powi(2)/48.;}
                for &(_,_,_,(u,a),(v,b)) in pairs {
                    lat.links[u][a]=original[u][a];lat.links[v][b]=original[v][b];
                }
            }
            assert_eq!(face(&lat,0,0,1,2),[sign,0.,0.,0.]);
            assert_eq!(face(&lat,0,0,2,2),[0.,1.,0.,0.]);
            println!("{:.12},{:.12},{:.12},{:.12},{:.12}",readings[0],readings[1],readings[2],j[0],j[1]);
        }
    }


    // ===== z1-mix8 additions (G4 functions above unchanged) =====
    fn coarse_angles(lat:&Lattice)->Vec<(usize,usize,usize,f64)> {
        // angle from -I of every coarse (2x2) spatial face on slice 0: arccos(-Re U)
        let n=lat.l; let mut out=Vec::new();
        for x in 0..n.pow(3) {
            let c=[x%n,(x/n)%n,x/(n*n)];
            if c.iter().any(|v| v%2==1) {continue;}
            for (i,j) in [(0,1),(0,2),(1,2)] {
                let u=face(lat,x,i,j,2);
                out.push((x,i,j,(-u[0]).clamp(-1.,1.).acos()));
            }
        }
        out
    }
    fn traceless_unit(h:Q)->Q { let v=[0.,h[1],h[2],h[3]]; unit(v) }
    // tests: [f1,f4,spread,f1raw,f4raw] with bhat = normalised traceless part of xz holonomy, raw = holonomy itself
    fn probes2(lat:&Lattice)->[f64;5] {
        let h=face(lat,0,0,2,2);
        let b=traceless_unit(h);
        let g1=face(lat,0,0,1,1);
        let mut average=[0.;4];
        for x in 0..2 {for y in 0..2 {
            let mut site=0; let mut path=ONE;
            for (d,steps) in [(0,x),(1,y)] {
                for _ in 0..steps {path=mul(path,lat.links[site][d]);site=lat.plus[site][d];}
            }
            let g=mul(mul(path,face(lat,site,0,1,1)),conj(path));
            for i in 0..4 {average[i]+=g[i]/4.;}
        }}
        [mul(b,g1)[0],mul(b,average)[0],1.-dot(average,average),mul(h,g1)[0],mul(h,average)[0]]
    }
    fn measure_run(lat:&mut Lattice,beta:f64,rng:&mut Rng,measures:&mut Rng,burn:usize,samples:usize,label:&str) {
        let n=lat.l;
        let skel:Vec<(usize,usize,Q)>=(0..n.pow(3)).flat_map(|x| (0..3).map(move |i|(x,i))).filter(|&(x,i)| frozen(lat,x,i)).map(|(x,i)|(x,i,lat.links[x][i])).collect();
        let ang=coarse_angles(lat);
        let (mut amin,mut at)=(10.,(0,0,0));
        for &(x,i,j,a) in &ang { if a<amin {amin=a;at=(x,i,j);} }
        let w=face(lat,0,0,1,2); let h=face(lat,0,0,2,2);
        eprintln!("{{\"label\":\"{}\",\"beta\":{},\"side\":{},\"period\":{},\"W\":[{:.15},{:.15},{:.15},{:.15}],\"B_holonomy\":[{:.15},{:.15},{:.15},{:.15}],\"n_coarse_faces\":{},\"min_angle_from_minusI\":{:.15},\"min_at\":[{},{},{}],\"burn\":{},\"samples\":{},\"spacing\":6}}",
            label,beta,n,lat.time,w[0],w[1],w[2],w[3],h[0],h[1],h[2],h[3],ang.len(),amin,at.0,at.1,at.2,burn,samples);
        for _ in 0..burn {conditional_sweep(lat,beta,rng);}
        let sets=colours(lat);
        let mut head=String::from("single,average,spread,j_single,j_average,single_raw,average_raw,j_single_raw,j_average_raw");
        for k in 0..24 {head+=&format!(",c{}_single",k);} for k in 0..24 {head+=&format!(",c{}_average",k);}
        println!("{}",head);
        for _ in 0..samples {
            for _ in 0..6 {conditional_sweep(lat,beta,rng);}
            let original=lat.links[..n.pow(3)].to_vec();
            let r=probes2(lat);
            let mut j=[0.;4]; let mut pc=[[0.;24];2];
            for (k,pairs) in sets.iter().enumerate() {
                for &pair in pairs {draw(lat,pair,beta,measures);}
                let f=probes2(lat);
                for &pair in pairs {draw(lat,pair,beta,measures);}
                let g=probes2(lat);
                for (t,c) in [(0,0),(1,1),(2,3),(3,4)] {j[t]+=(f[c]-g[c]).powi(2)/48.;}
                for t in 0..2 {pc[t][k]=(f[t]-g[t]).powi(2)/2.;}
                for &(_,_,_,(u,a),(v,b)) in pairs {
                    lat.links[u][a]=original[u][a];lat.links[v][b]=original[v][b];
                }
            }
            for &(x,i,q) in &skel {assert_eq!(lat.links[x][i],q);}
            let mut line=format!("{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12}",r[0],r[1],r[2],j[0],j[1],r[3],r[4],j[2],j[3]);
            for t in 0..2 {for k in 0..24 {line+=&format!(",{:.12}",pc[t][k]);}}
            println!("{}",line);
        }
    }
    // mix beta seed hot burn samples side period delta : W=-cos d + k sin d on y-link at (2,0,0), z-link there = i
    fn mix(args:&[String]) {
        assert_eq!(args.len(),10,"mix beta seed hot burn samples side period delta");
        let beta=args[2].parse::<f64>().unwrap();
        let seed=args[3].parse::<u64>().unwrap();
        let mut rng=Rng{state:seed};
        let mut measures=Rng{state:seed ^ 0x6a09e667f3bcc909};
        let n=args[7].parse::<usize>().unwrap();
        let period=args[8].parse::<usize>().unwrap();
        let delta=args[9].parse::<f64>().unwrap();
        let mut lat=Lattice::new(n,period,false,args[4]=="1",&mut rng);
        for x in 0..n.pow(3) {for i in 0..3 { if frozen(&lat,x,i) {lat.links[x][i]=ONE;} }}
        lat.links[2][1]=[-delta.cos(),0.,0.,delta.sin()];
        lat.links[2][2]=[0.,1.,0.,0.];
        measure_run(&mut lat,beta,&mut rng,&mut measures,args[5].parse().unwrap(),args[6].parse().unwrap(),&format!("mix delta={}",delta));
    }
    // clear beta seed hot burn samples side period skeleton_file : frozen links read from text "x i a b c d"
    fn clear(args:&[String]) {
        assert_eq!(args.len(),10,"clear beta seed hot burn samples side period skelfile");
        let beta=args[2].parse::<f64>().unwrap();
        let seed=args[3].parse::<u64>().unwrap();
        let mut rng=Rng{state:seed};
        let mut measures=Rng{state:seed ^ 0x6a09e667f3bcc909};
        let n=args[7].parse::<usize>().unwrap();
        let period=args[8].parse::<usize>().unwrap();
        let mut lat=Lattice::new(n,period,false,args[4]=="1",&mut rng);
        let text=std::fs::read_to_string(&args[9]).unwrap();
        let mut count=0;
        for line in text.lines() {
            if line.starts_with('#') || line.trim().is_empty() {continue;}
            let v:Vec<&str>=line.split_whitespace().collect();
            let x:usize=v[0].parse().unwrap(); let i:usize=v[1].parse().unwrap();
            assert!(frozen(&lat,x,i));
            let q:Q=std::array::from_fn(|k| v[2+k].parse::<f64>().unwrap());
            lat.links[x][i]=unit(q); count+=1;
        }
        assert_eq!(count,3*n*(n/2)*(n/2));
        measure_run(&mut lat,beta,&mut rng,&mut measures,args[5].parse().unwrap(),args[6].parse().unwrap(),&format!("clear {}",args[9]));
    }
    // gen beta seed burn ncfg spacing side period outprefix : unconditioned heat bath + reflection cycles (as G4 pilot), hot start
    fn gen(args:&[String]) {
        assert_eq!(args.len(),10,"gen beta seed burn ncfg spacing side period outprefix");
        let beta=args[2].parse::<f64>().unwrap();
        let seed=args[3].parse::<u64>().unwrap();
        let mut rng=Rng{state:seed};
        let burn:usize=args[4].parse().unwrap(); let ncfg:usize=args[5].parse().unwrap(); let sp:usize=args[6].parse().unwrap();
        let n=args[7].parse::<usize>().unwrap(); let period=args[8].parse::<usize>().unwrap();
        let mut lat=Lattice::new(n,period,false,true,&mut rng);
        for _ in 0..burn {lat.sweep(beta,&mut rng,false);lat.sweep(beta,&mut rng,true);}
        println!("cfg,min_angle,mean_angle,n_below_pi4,plaquette_avg");
        for c in 0..ncfg {
            for _ in 0..sp {lat.sweep(beta,&mut rng,false);lat.sweep(beta,&mut rng,true);}
            let ang=coarse_angles(&lat);
            let amin=ang.iter().map(|a|a.3).fold(10.,f64::min);
            let amean=ang.iter().map(|a|a.3).sum::<f64>()/(ang.len() as f64);
            let nb=ang.iter().filter(|a| a.3<=std::f64::consts::FRAC_PI_4).count();
            let plaq=lat.action()/(6.*lat.links.len() as f64);
            println!("{},{:.12},{:.12},{},{:.12}",c,amin,amean,nb,plaq);
            let mut f=std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{}-cfg{}.skel",args[9],c)).unwrap();
            use std::io::Write;
            writeln!(f,"# slice-0 skeleton, beta {} seed {} cfg {} min_angle {:.15}",beta,seed,c,amin).unwrap();
            for x in 0..n.pow(3) {for i in 0..3 { if frozen(&lat,x,i) { let q=lat.links[x][i];
                writeln!(f,"{} {} {:.17e} {:.17e} {:.17e} {:.17e}",x,i,q[0],q[1],q[2],q[3]).unwrap(); }}}
            let mut g=std::fs::OpenOptions::new().write(true).create_new(true).open(format!("{}-cfg{}.angles",args[9],c)).unwrap();
            for a in &ang {writeln!(g,"{} {} {} {:.15}",a.0,a.1,a.2,a.3).unwrap();}
        }
    }

    pub fn run() {
        let args: Vec<String>=env::args().collect();
        if args.get(1).map(String::as_str)==Some("fixed") {fixed(&args);return;}
        if args.get(1).map(String::as_str)==Some("mix") {mix(&args);return;}
        if args.get(1).map(String::as_str)==Some("clear") {clear(&args);return;}
        if args.get(1).map(String::as_str)==Some("gen") {gen(&args);return;}
        assert!(args.len()==6 || args.len()==8,"beta seed hot burn samples [side period]");
        let beta=args[1].parse::<f64>().unwrap();
        let seed=args[2].parse::<u64>().unwrap();
        let hot=args[3]=="1";
        let burn=args[4].parse::<usize>().unwrap();
        let samples=args[5].parse::<usize>().unwrap();
        assert!(beta>=0. && beta.is_finite() && samples>0);
        let mut rng=Rng{state:seed};
        let mut measures=Rng{state:seed ^ 0x6a09e667f3bcc909};
        let n=if args.len()==8 {args[6].parse::<usize>().unwrap()} else {6};
        let period=if args.len()==8 {args[7].parse::<usize>().unwrap()} else {12};
        assert!(n>=6 && n%2==0 && period>=6 && period%2==0);
        let mut lat=Lattice::new(n,period,false,hot,&mut rng);
        let sets=colours(&lat);
        for _ in 0..burn { lat.sweep(beta,&mut rng,false); lat.sweep(beta,&mut rng,true); }
        println!("ps,winding2,j_ps,j_winding2,d1_ps,d1_winding2,d4_ps,d4_winding2");
        for _ in 0..samples {
            for _ in 0..3 {lat.sweep(beta,&mut rng,false); lat.sweep(beta,&mut rng,true);}
            let reference=lat.links.clone();
            let baseline=observe(&lat,beta);
            let mut j=[0.;2];
            for pairs in &sets {
                let mut first=[0.;2];
                for replica in 0..2 {
                    for &pair in pairs {draw(&mut lat,pair,beta,&mut measures);}
                    let f=observe(&lat,beta);
                    if replica==0 {first=f;} else {
                        for i in 0..2 {j[i]+=(first[i]-f[i]).powi(2)/48.;}
                    }
                }
                for &(_,_,_,(u,a),(v,b)) in pairs {
                    lat.links[u][a]=reference[u][a];
                    lat.links[v][b]=reference[v][b];
                }
            }
            let mut a=[[0.;2];2];
            let mut d=[[0.;2];2];
            for replica in 0..2 {
                lat.links.clone_from(&reference);
                for k in 1..=4 {
                    conditional_sweep(&mut lat,beta,&mut measures);
                    if k==1 || k==4 {
                        let t=usize::from(k==4);
                        let f=observe(&lat,beta);
                        if replica==0 {a[t]=f;} else {
                            for i in 0..2 {d[t][i]=(a[t][i]-f[i]).powi(2)/2.;}
                        }
                    }
                }
                for (x,row) in reference.iter().enumerate().take(lat.l.pow(3)) {
                    for i in 0..3 {if frozen(&lat,x,i) {assert_eq!(row[i],lat.links[x][i]);}}
                }
            }
            lat.links=reference;
            println!("{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12},{:.12}",
                baseline[0],baseline[1],j[0],j[1],d[0][0],d[0][1],d[1][0],d[1][1]);
        }
    }
}
fn main(){pilot::run();}
