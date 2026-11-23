"""Analyze block means of Wilson paths; no additional packages needed."""
import csv
import io
import math
import re
import statistics
import sys
from fractions import Fraction
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile

SPEC = re.compile(r"(open-)?L(\d+)-T(\d+)-b(\d+)-seed(\d+)-h([01])-burn(\d+)-n(\d+)-s(\d+)\.csv")
NAN = float("nan")


def max_lag(t, open_time):
    return min(6, t-2*(t//4)-1 if open_time else t//2)


def read_data(archive):
    ensembles = defaultdict(list)
    with ZipFile(archive) as files:
        for name in sorted(files.namelist()):
            match = SPEC.fullmatch(name)
            assert match, name
            boundary, *numbers = match.groups()
            l, t, beta, seed, hot, burn, n, sweeps = map(int, numbers)
            rows = defaultdict(list)
            with files.open(name) as stream:
                records = csv.DictReader(io.TextIOWrapper(stream, encoding="ascii"))
                for row in records:
                    obs = row["observable"]
                    assert int(row["block"]) == len(rows[obs])
                    cols = [k for k in row if k not in ("block", "observable")]
                    rows[obs].append([float(row[k]) for k in cols])
            assert set(rows) == {"plaquette","adjoint","tensor"}
            for obs, chain in rows.items():
                width = 2+max_lag(t,bool(boundary))+(t if boundary else 0)
                assert len(chain) == n and all(len(r)==width for r in chain)
                protocol = ("open-long" if burn >= 200 else "open") if boundary else "periodic"
                key = (protocol, l, t, beta, obs)
                ensembles[key].append((hot, chain))
    for chains in ensembles.values():
        chains.sort(key=lambda item: item[0])
        assert [h for h, _ in chains] == [0,1]
    return ensembles


def observables(row, t, open_time, obs):
    end = 2+max_lag(t,open_time)
    means = row[end:]
    if open_time:
        cut = t//4
        mean = statistics.fmean(means[cut:t-cut])
    else:
        mean = row[0]
    corr = []
    for j, moment in enumerate(row[1:end]):
        if obs=="tensor":
            # Axis permutation fixes the tensor expectation to zero at every slice.
            baseline = 0.
        elif open_time:
            baseline = statistics.fmean(means[i]*means[i+j] for i in range(cut,t-cut-j))
        else:
            baseline = mean*mean
        corr.append(moment-baseline)
    eff = [math.log(corr[j]/corr[j+1]) if min(corr[j:j+2])>0 else NAN
           for j in range(1,min(4,len(corr)-1))]
    return [mean,*corr,*eff]


def stats(key, chains, group):
    protocol, _, t, _, obs = key
    open_time = protocol != "periodic"
    batches = []
    for _, seq in chains:
        assert len(seq) % group == 0
        for start in range(0,len(seq),group):
            batches.append([statistics.fmean(col) for col in zip(*seq[start:start+group])])
    count = len(batches)
    totals = list(map(math.fsum,zip(*batches)))
    full = observables([x/count for x in totals],t,open_time,obs)
    jack = [observables([(a-b)/(count-1) for a,b in zip(totals,row)],t,open_time,obs)
            for row in batches]
    # The point estimate is the plug-in estimate. Delete-batch errors include the subtraction.
    errors = []
    for col in zip(*jack):
        avg = statistics.fmean(col)
        errors.append(math.sqrt((count-1)/count*sum((v-avg)**2 for v in col)))
    return full, errors


def report(source, dest):
    writer=csv.writer(dest,lineterminator="\n")
    writer.writerow(["boundary","L","T","beta","observable","stream","group_blocks",
                     "quantity","estimate","batch_error"])
    for key,chains in sorted(read_data(source).items()):
        boundary,l,t,beta,obs=key
        lag=max_lag(t,boundary!="periodic")
        quantities=["mean",*(f"C{i}" for i in range(lag+1)),
                    *(f"m{j}{j+1}" for j in range(1,min(4,lag)))]
        for label,sample in [("pooled",chains),("cold",chains[:1]),("hot",chains[1:])]:
            for group in ([1,4,8] if label=="pooled" else [4]):
                vals,errs=stats(key,sample,group)
                for q,v,e in zip(quantities,vals,errs):
                    writer.writerow([boundary,l,t,beta,obs,label,group,
                                     q,format(v,".11g"),format(e,".11g")])


def start_plot(source):
    rows=read_data(source)
    data=[]
    for protocol in ("open","open-long"):
        key=(protocol,2,96,64,"adjoint")
        for chain in rows[key]:
            vals,errs=stats(key,[chain],4)
            edges=[str(Fraction(round((vals[0]+s*errs[0])*10**6),10**6)) for s in (-1,1)]
            data.append([1+len(data),*edges])
    return dict(title="SU(2) open slab: hot and cold starts",
                provenance="observed",source="Wilson simulation, spatial side 2, time 96, beta 64. One batch standard error.",
                x_label="1-2 short, 3-4 long, cold then hot",
                y_label="mean normalized adjoint loop",x_domain=[1,4],y_domain=["13/20","19/20"],
                series=[dict(name="Central half of slab",data=data)])


if __name__=="__main__":
    root=Path(__file__).resolve().parent
    with (Path(sys.argv[1]).open("w",newline="",encoding="ascii") if len(sys.argv)>1
          else __import__("contextlib").nullcontext(sys.stdout)) as output:
        report(root/"wilson-blocks.zip", output)
