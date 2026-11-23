"""Exercise the archived Rust probe and APE code on a toron and an Abelian wave."""
import argparse
import math
from pathlib import Path
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parent.parents[3] / "g4" / "full-attempt"
FIXTURE = """
        if env::args().nth(1).as_deref() == Some("rank-check") {
            let mut rng = Rng { state: 1 };
            for n in [5usize, 6, 7, 8, 10] {
                let mut lat = Lattice::new(n, 4, true, false, &mut rng);
                let angle = PI / (2.*n as f64);
                for row in &mut lat.links {
                    row[0] = [angle.cos(), 0., 0., angle.sin()];
                }
                let toron = lat.smoothed_probes()[1];
                println!("{n} flat {:.15e} {:.15e}", toron[3], toron[6]);
                for eps in [0.04, 0.02] {
                    for (x,row) in lat.links.iter_mut().enumerate() {
                        let phase = eps*(2.*PI*(x % n) as f64/n as f64).cos()/n as f64;
                        row[0] = ONE;
                        row[1] = [phase.cos(), 0., 0., phase.sin()];
                    }
                    let wave = lat.smoothed_probes()[1];
                    println!("{n} {eps} {:.15e} {:.15e}", wave[6], wave[6]/(eps*eps));
                }
            }
            return;
        }
"""


def coefficient(n):
    k, remainder = divmod(n, 4)
    frac = remainder/4
    wave = 2*math.pi/n
    multiplier = (3 + math.cos(wave))/4
    return multiplier**(2*((n*n+6)//12)) / 2 * sum(
        w*(side/n)**2*math.sin(wave*side)**2 for side,w in ((k,1-frac),(k+1,frac)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rustc", default="rustc")
    args = parser.parse_args()
    original = (SOURCE/"physical-refinement"/"matched.rs").read_text()
    include = '"../two-site-gap/wilson_mc.rs"'
    entry = "pub fn run() {"
    assert original.count(include) == original.count(entry) == 1
    source = original.replace(include, f'r#"{SOURCE}/two-site-gap/wilson_mc.rs"#')
    with tempfile.TemporaryDirectory() as tmp:
        code = Path(tmp)/"instrument.rs"
        binary = Path(tmp)/"instrument"
        code.write_text(source.replace(entry, entry+FIXTURE))
        subprocess.run([args.rustc,"--edition=2021","-O",code,"-o",binary],check=True)
        lines = subprocess.check_output([binary,"rank-check"],text=True).splitlines()
    assert len(lines) == 15
    ratios = {}
    for line in lines:
        size, case, val, ratio = line.split()
        n = int(size)
        if case == "flat":
            assert abs(float(val)-4/3) < 2e-12 and abs(float(ratio)) < 1e-14
        else:
            ratios[n,float(case)] = float(ratio)
    for n in (5,6,7,8,10):
        prediction = coefficient(n)
        extrapolated = (4*ratios[n,.02]-ratios[n,.04])/3
        assert abs(extrapolated/prediction-1) < 1e-7
        print(f"{n:2}: analytic {prediction:.9f}, Rust extrapolation {extrapolated:.9f}")
    print(f"limiting coefficient: {math.exp(-math.pi**2/12)/32:.9f}")


if __name__ == "__main__":
    main()
