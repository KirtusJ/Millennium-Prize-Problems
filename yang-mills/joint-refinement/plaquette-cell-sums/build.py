"""Build the multi-cell entry point with the existing Wilson pair and face routines."""
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

root=Path(__file__).resolve().parent
replicas=root.parent/"full-complement/replicas.rs"
sampler=root.parents[1]/"g4/full-attempt/two-site-gap/wilson_mc.rs"


def build(rustc,output):
    source=replicas.read_text(encoding="utf8")
    marker="    fn fixed(args:"
    assert source.count(marker)==1
    prefix=source.split(marker)[0]
    include='include!("../../g4/full-attempt/two-site-gap/wilson_mc.rs");'
    assert prefix.count(include)==1
    prefix=prefix.replace(include,'include!(env!("WILSON_SAMPLER_SOURCE"));')
    with TemporaryDirectory() as folder:
        path=Path(folder)/"cell_sampler.rs"
        path.write_text(prefix+(root/"cells.rs").read_text(encoding="utf8")+
                        "\n}\nfn main(){pilot::cell_run();}\n",encoding="utf8")
        subprocess.run([rustc,"--edition=2021","-O",path,"-o",output],
                       env={**os.environ,"WILSON_SAMPLER_SOURCE":str(sampler.resolve())},check=True)


if __name__=="__main__":
    build(sys.argv[1],Path(sys.argv[2]).resolve())
