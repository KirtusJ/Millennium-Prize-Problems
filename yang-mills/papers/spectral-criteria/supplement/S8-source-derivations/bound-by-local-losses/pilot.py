"""Read eight finite-torus, same-skeleton streams and form ratios of stream means."""
from pathlib import Path
from zipfile import ZipFile
import io
import numpy as np

ROOT=Path(__file__).resolve().parent
FIELDS="ps,winding2,j_ps,j_winding2,d1_ps,d1_winding2,d4_ps,d4_winding2"


def estimates(sample):
    all_rows=np.concatenate(sample)
    j=all_rows[:,2:4].mean(axis=0)
    d1=all_rows[:,4:6].mean(axis=0)
    d4=all_rows[:,6:8].mean(axis=0)
    return np.column_stack([j,d1,d4,j/d4])


def report():
    with ZipFile(ROOT/"pilot.zip") as archive:
        assert len(archive.namelist())==16
        for design in ("b0","haar2","b3.276133577","N8"):
            rows=[]
            for i in range(4):
                data=archive.read(f"{design}-s{i}.csv")
                assert data.splitlines()[0].decode()==FIELDS
                table=np.loadtxt(io.BytesIO(data),delimiter=",",skiprows=1)
                assert table.shape==((384 if design=="haar2" else 96),8)
                assert np.isfinite(table).all() and (table>=0).all()
                rows.append(table)
            mean=estimates(rows)
            dropped=np.stack([estimates(rows[:i]+rows[i+1:]) for i in range(len(rows))])
            error=np.sqrt(3*((dropped-dropped.mean(axis=0))**2).mean(axis=0))
            for i,channel in enumerate(("plaquette sum","squared winding")):
                print(design,channel," ".join(f"{v:.6f}({s:.6f})" for v,s in zip(mean[i],error[i])))
            if design in ("b0","haar2"):
                expected=np.array([[7/96,1/4,1/4,7/24],[1/48,1/16,1/16,1/3]])
                print("Haar targets",expected.tolist())


if __name__=="__main__":
    report()
