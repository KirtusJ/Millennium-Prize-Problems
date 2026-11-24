import csv, math
D='/home/user/z4-workers/e2-repair/results/N-d0/'
n=0; s=0.0; js=0.0; xs=[]
for i in range(32):
    with open(D+f's{i}.csv', newline='') as f:
        for r in csv.DictReader(f):
            xs.append(float(r['single'])); js+=float(r['j_single'])
n=len(xs); m=math.fsum(xs)/n
var=math.fsum((x-m)**2 for x in xs)/n
out=f"rows={n}\nmean_single={m:.12g}\npop_var_single={var:.12g}\nmean_j_single={js/n:.12g}\n"
print(out)
with open('out.txt','x') as f: f.write(out)
