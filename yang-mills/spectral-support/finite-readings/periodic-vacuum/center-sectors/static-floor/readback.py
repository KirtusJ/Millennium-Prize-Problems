"""Compare the period midpoint in absolute Z4 tensor normalization on the archived chains."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import sys
from zipfile import ZipFile

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check import G4_HASH, Z4, Z4_HASH


def report(period, chains):
    midpoint = chains[:,period//2]
    error = midpoint.std(ddof=1)/np.sqrt(len(chains))
    print(f"T={period} chains={len(chains)} midpoint={midpoint.mean():.9f} "
          f"SE={error:.9f} equal_time={chains[:,0].mean():.9f}")


def readback(path):
    raw = Z4.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == Z4_HASH
    doc = json.loads(raw)
    rows = np.asarray(doc["sOO"])
    report(doc["T"], (rows[:,0,0]/2+rows[:,1,1]/6)/2)
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == G4_HASH
    with ZipFile(io.BytesIO(raw)) as z:
        for base in ("d3_b4","d3_b4_T48"):
            meta = json.loads(z.read(f"rerun/{base}.json"))
            with np.load(io.BytesIO(z.read(f"rerun/{base}.npz")), allow_pickle=False) as data:
                rows = data["C_E"][:,:,0,0,:].sum(axis=0)/data["nmeas"].sum()
            assert rows.shape == (meta["NCH"],meta["T"]//2+1)
            report(meta["T"],rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    readback(parser.parse_args().archive)
