fn cell_marks(lat: &Lattice) -> Vec<f64> {
    let n = lat.l;
    let mut values = Vec::with_capacity((n/2).pow(3));
    for z in (0..n).step_by(2) {
        for y in (0..n).step_by(2) {
            for x in (0..n).step_by(2) {
                let mut sum = 0.;
                for dy in 0..2 {
                    for dx in 0..2 {
                        let site = x+dx+n*(y+dy+n*z);
                        sum += face(lat,site,0,1,1)[0];
                    }
                }
                values.push(sum/4.);
            }
        }
    }
    values
}

pub fn cell_run() {
    let args: Vec<_> = env::args().collect();
    assert_eq!(args.len(),7);
    let beta: f64 = args[1].parse().unwrap();
    assert!(beta.is_finite() && beta >= 0.0, "the Wilson heat bath requires finite nonnegative beta");
    let seed: u64 = args[2].parse().unwrap();
    let n: usize = args[4].parse().unwrap();
    let burn: usize = args[5].parse().unwrap();
    let count: usize = args[6].parse().unwrap();
    assert!(n>=6 && n%2==0);
    let mut rng = Rng{state:seed};
    let mut measures = Rng{state:seed ^ 0x6a09e667f3bcc909};
    let mut lat=Lattice::new(n,2*n,false,args[3]=="1",&mut rng);
    for x in 0..n.pow(3) {
        for i in 0..3 {if frozen(&lat,x,i) {lat.links[x][i]=ONE;}}
    }
    for _ in 0..burn {conditional_sweep(&mut lat,beta,&mut rng);}
    let groups=colours(&lat);
    println!("sample,cell,value,d0,d1,d2,d3");
    for s in 0..count {
        for _ in 0..4 {conditional_sweep(&mut lat,beta,&mut rng);}
        let reference=lat.links[..n.pow(3)].to_vec();
        let baseline=cell_marks(&lat);
        let mut diffs=vec![[0.;4];baseline.len()];
        for (c,pairs) in groups.iter().enumerate() {
            // Verify all 24 at the first sample. Later samples can skip the 20 exact zeros.
            if c>=4 && s>0 {continue;}
            for &pair in pairs {draw(&mut lat,pair,beta,&mut measures);}
            let first=cell_marks(&lat);
            for &pair in pairs {draw(&mut lat,pair,beta,&mut measures);}
            let second=cell_marks(&lat);
            if c<4 {
                for i in 0..diffs.len() {diffs[i][c]=first[i]-second[i];}
            } else {
                assert_eq!(first,baseline);
                assert_eq!(second,baseline);
            }
            for &(_,_,_,(u,a),(v,b)) in pairs {
                lat.links[u][a]=reference[u][a];
                lat.links[v][b]=reference[v][b];
            }
        }
        for (i,d) in diffs.iter().enumerate() {
            println!("{s},{i},{:.12},{:.12},{:.12},{:.12},{:.12}",baseline[i],d[0],d[1],d[2],d[3]);
        }
    }
}
