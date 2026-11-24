import json,sys
r=json.load(open('results.json'));p=r['preds']
need=['P1','P2','P3','P4','P5','P7']
bad=[k for k in need if not p[k]]
print('required preds met' if not bad else 'FAILED %s'%bad); sys.exit(1 if bad else 0)
