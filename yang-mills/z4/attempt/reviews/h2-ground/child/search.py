"""Predicate (fixed before first run): P1 = at least one INSPIRE hit whose title contains
(torus or 'finite volume' or 'small volume') AND ('2+1' or 'three dimensions' or 'two spatial' or '2 + 1')
AND ('SU(2)' or 'Yang-Mills'). P1 true -> candidate for reading; false -> no candidate (NOT FOUND from this endpoint).
Exit 0 always if endpoint answers; exit 2 if no query answered (endpoint defect). Results file opened mode 'x'."""
import json,subprocess,sys,time,urllib.parse
qs=['t "Yang-Mills" and t torus','t "SU(2)" and t "finite volume"','t "gauge theory" and t "2+1" and t volume',
    't "Yang-Mills" and t "quantum mechanics"','t "Yang-Mills" and t "three dimensions" and t volume','t "gauge" and t "small torus"',
    'a van baal and t torus','a luscher and t "small volume"']
out=open(sys.argv[1],'x'); answered=0; cand=[]
for q in qs:
    r=subprocess.run(['curl','-s','-m','25','-G','https://inspirehep.net/api/literature','--data-urlencode','q='+q,'--data-urlencode','size=10','--data-urlencode','fields=titles,authors.full_name,publication_info'],capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception: out.write('QUERY FAILED: %s\n'%q); continue
    answered+=1; out.write('Q %s -> total %s\n'%(q,d['hits']['total']))
    for h in d['hits']['hits']:
        t=h['metadata']['titles'][0]['title']; l=t.lower()
        out.write('  '+t[:100]+'\n')
        if any(k in l for k in ['torus','finite volume','small volume']) and any(k in l for k in ['2+1','three dimensions','two spatial','2 + 1']) and ('su(2)' in l or 'yang-mills' in l): cand.append(t)
    time.sleep(1)
out.write('answered=%d candidates=%d %s\n'%(answered,len(cand),cand)); out.close()
print('answered',answered,'candidates',len(cand),cand); sys.exit(0 if answered else 2)
