"""Exercise Z4 and G4 operators on identical inhomogeneous link fields."""
import argparse
import importlib.util
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import numpy as np

YM = Path(__file__).resolve().parents[2]
Z4 = YM / "z4/attempt/reviews/k1-mc8/mcbox.py"
G4 = YM / "g4/full-attempt/physical-refinement/matched.rs"


def build(tmp, rustc):
    # Add an input adapter inside the module containing the private probes method.
    # Both winding products, spatial averages and component definitions are original.
    adapter = r"""
    pub fn read_fields() {
        use std::io::Read;
        let args: Vec<String> = env::args().collect();
        let (n, nt) = (args[1].parse().unwrap(), args[2].parse().unwrap());
        let mut lat = Lattice::new(n, nt, false, false, &mut Rng { state: 1 });
        let mut raw = Vec::new();
        std::io::stdin().read_to_end(&mut raw).unwrap();
        let mut values = raw.chunks_exact(8).map(|x| f64::from_le_bytes(x.try_into().unwrap()));
        let mut out = std::io::stdout().lock();
        for _ in 0..args[3].parse::<usize>().unwrap() {
            for row in &mut lat.links {
                for link in row.iter_mut().take(3) {
                    for value in link { *value = values.next().unwrap(); }
                }
            }
            for s in lat.probes() {
                for i in [2,3,4,8,9,10] { out.write_all(&s[i].to_le_bytes()).unwrap(); }
            }
        }
        assert!(values.next().is_none());
    }
"""
    source = G4.read_text(encoding="utf8")
    for before, after in [('include!("../two-site-gap/wilson_mc.rs");', 'include!("wilson_mc.rs");'),
                          ("    pub fn run() {", adapter + "\n    pub fn run() {"),
                          ("wilson::run();", "wilson::read_fields();")]:
        assert source.count(before) == 1
        source = source.replace(before, after)
    (tmp/"reader.rs").write_text(source, encoding="utf8")
    (tmp/"wilson_mc.rs").write_bytes((G4.parent.parent/"two-site-gap/wilson_mc.rs").read_bytes())
    exe = tmp/("reader.exe" if __import__("os").name == "nt" else "reader")
    subprocess.run([rustc, "--edition=2021", "-Awarnings", "-O", tmp/"reader.rs", "-o", exe], check=True)
    return exe


def check(module, exe, field):
    replicas, _, nt, n = field.shape[:4]
    data = field[:, 1:].transpose(0,2,5,4,3,1,6).astype("<f8").tobytes()
    raw = subprocess.check_output([exe,str(n),str(nt),str(replicas)],input=data)
    g4 = np.frombuffer(raw, "<f8").reshape(-1,6)
    out = module.operators(field)
    e = out["E"][...,0].reshape(-1,2)
    t = out["T2"][...,0].reshape(-1,3)
    # Lift the orthonormal traceless components back to the three cyclic differences.
    axes = np.array([[1,-1,0],[1,1,-2]]) / np.sqrt([[2],[6]])
    cyclic = np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
    expected = (4/3)*e @ axes @ cyclic.T
    np.testing.assert_allclose(g4[:,:3],expected,atol=3e-14,rtol=0)
    np.testing.assert_allclose(-4*g4[:,3:],t[:,[2,1,0]],atol=3e-14,rtol=0)
    np.testing.assert_allclose(g4[:,:3]@g4[:,:3].T/3, (32/9)*(e@e.T/2),atol=3e-14,rtol=0)
    assert np.max(abs(g4[:,3:]-t[:,[2,1,0]])) > 0.01
    return g4


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rustc", default="rustc")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("z4box", Z4)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rng = np.random.default_rng(112346)
    with TemporaryDirectory() as folder:
        exe = build(Path(folder),args.rustc)
        for n in (2,4):
            field = rng.normal(size=(7,4,6,n,n,n,4))
            field /= np.linalg.norm(field,axis=-1,keepdims=True)
            frames = rng.normal(size=field[:,0].shape)
            frames /= np.linalg.norm(frames,axis=-1,keepdims=True)
            original = check(module,exe,field)
            transformed = check(module,exe,module.gauge_tr(field,frames))
            np.testing.assert_allclose(original,transformed,atol=3e-14,rtol=0)
            print("spatial side",n,"matched slice readings",2*len(original))
