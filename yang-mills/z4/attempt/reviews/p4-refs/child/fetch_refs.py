"""Fetch bibliographic records for four refs + control. Usage: fetch_refs.py OUTDIR (new dir; files opened mode 'x').
Predicates fixed before first run:
 P0 control: arXiv record of 1803.01950 has title containing 'Yang-Mills for probabilists' and author Chatterjee.
 P1 FiveD11: arXiv 1110.4210 exists (API returns an entry with a title) and title contains 'five'.
 P2 BCH26: arXiv 2610.08144 exists (entry with title) and authors include Bastounis, Circelli, Hansen.
 P3 KT02: hep-lat/0108017 exists, authors include Kovacs and Tomboulis, journal_ref contains 'Phys. Rev. D 65' and '074501'.
 P4 CCK07: 0705.2629 exists, authors include Cherrington, Christensen, Khavkine, title contains 'Dual computations of non-abelian Yang-Mills on the lattice'.
Fields (authors,title,journal,volume,year,page,doi,arxiv) taken only from fetched records; else UNCONFIRMED.
Tolerance: none numeric; string matches case-insensitive. Timeout 30s, 2 retries (own choice)."""
import sys, os, json, time, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
out = sys.argv[1]; os.makedirs(out)
def get(u):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"refcheck/1.0"}), timeout=30).read().decode()
        except Exception as e:
            err = repr(e); time.sleep(2)
    return "ERROR "+err
IDS = {"control":"1803.01950","FiveD11":"1110.4210","BCH26":"2610.08144","KT02":"hep-lat/0108017","CCK07":"0705.2629"}
NS = {"a":"http://www.w3.org/2005/Atom","x":"http://arxiv.org/schemas/atom"}
res = {}
for k,i in IDS.items():
    r = {}
    u = "http://export.arxiv.org/api/query?id_list="+i
    t = get(u); r["arxiv_url"]=u
    try:
        e = ET.fromstring(t).find("a:entry",NS)
        r["arxiv"] = {"id": e.find("a:id",NS).text, "title": " ".join(e.find("a:title",NS).text.split()),
          "authors":[a.find("a:name",NS).text for a in e.findall("a:author",NS)],
          "published": e.find("a:published",NS).text,
          "journal_ref": (e.find("x:journal_ref",NS).text if e.find("x:journal_ref",NS) is not None else None),
          "doi": (e.find("x:doi",NS).text if e.find("x:doi",NS) is not None else None)}
    except Exception as ex:
        r["arxiv"] = {"error": repr(ex), "raw": t[:300]}
    u = "https://inspirehep.net/api/arxiv/"+i; r["inspire_url"]=u
    t = get(u)
    try:
        m = json.loads(t)["metadata"]
        pi = (m.get("publication_info") or [{}])
        r["inspire"] = {"title": m["titles"][0]["title"], "authors":[a["full_name"] for a in m.get("authors",[])],
          "pub": pi, "dois": m.get("dois")}
    except Exception as ex:
        r["inspire"] = {"error": repr(ex), "raw": t[:200]}
    dois = []
    if r["arxiv"].get("doi"): dois.append(r["arxiv"]["doi"])
    for d in (r["inspire"].get("dois") or []):
        if d["value"] not in dois: dois.append(d["value"])
    r["crossref"] = {}
    for d in dois:
        u = "https://api.crossref.org/works/"+urllib.parse.quote(d); t = get(u)
        try:
            w = json.loads(t)["message"]
            r["crossref"][d] = {"url":u,"title":w.get("title"),"container":w.get("container-title"),"volume":w.get("volume"),
              "page":w.get("page"),"article-number":w.get("article-number"),"issued":w.get("issued"),
              "authors":[(a.get("given","")+" "+a.get("family","")) for a in w.get("author",[])]}
        except Exception as ex:
            r["crossref"][d] = {"url":u,"error":repr(ex),"raw":t[:150]}
    res[k]=r
with open(os.path.join(out,"records.json"),"x") as f: json.dump(res,f,indent=1)
# predicates
def tl(s): return (s or "").lower()
P = {}
a=res["control"]["arxiv"]; P["P0"] = "yang-mills for probabilists" in tl(a.get("title")) and any("Chatterjee" in x for x in a.get("authors",[]))
a=res["FiveD11"]["arxiv"]; P["P1"] = "title" in a and "five" in tl(a["title"])
a=res["BCH26"]["arxiv"]; P["P2"] = "title" in a and all(any(n in x for x in a.get("authors",[])) for n in ["Bastounis","Circelli","Hansen"])
a=res["KT02"]["arxiv"]; P["P3"] = all(any(n in x for x in a.get("authors",[])) for n in ["Kovacs","Tomboulis"]) and "Phys. Rev. D 65" in (a.get("journal_ref") or "") and "074501" in (a.get("journal_ref") or "")
a=res["CCK07"]["arxiv"]; P["P4"] = all(any(n in x for x in a.get("authors",[])) for n in ["Cherrington","Christensen","Khavkine"]) and "dual computations of non-abelian yang-mills on the lattice" in tl(a.get("title"))
with open(os.path.join(out,"predicates.json"),"x") as f: json.dump(P,f,indent=1)
print(json.dumps(P)); 
for k,r in res.items(): print(k, json.dumps({"arxiv":r["arxiv"],"inspire":r["inspire"],"crossref":r["crossref"]})[:1800]); print()
