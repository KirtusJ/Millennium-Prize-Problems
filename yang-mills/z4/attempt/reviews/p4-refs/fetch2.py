"""fetch2.py -- second pass for keys that run1 left open (query defects, Crossref 429).

Usage: python3 fetch2.py <rawdir> <outfile>   (outfile opened with mode "x")

PREDICATES (fixed before the first run):
 Q1[key] the INSPIRE query returns exactly 1 hit whose title contains the expected keywords.
 Q2[key] the Crossref record of each DOI exists (HTTP 200) and its normalized title equals
         the normalized INSPIRE title (normalization: lowercase, keep [a-z0-9]; the only
         tolerance, from capitalization/markup differences between databases).
 Q3[key] book queries: some Crossref item has the expected title keywords AND an expected
         author family name.
 Q4[key] publisher landing page: HTTP 200 and a citation_title meta tag present.
No randomness. Delays: Crossref 2.5 s between calls (run1 got HTTP 429 at 0.4 s).
Exit 0 when the program completes; failures are data.
"""
import html, json, os, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "pcp-bib-worker/1.0 (research bibliography check)"}
IF = "titles,authors.full_name,publication_info,dois,imprints,isbns"
INSP = {
 "JW": ('t "Quantum Yang-Mills theory" and a Jaffe and a Witten', ["yang-mills"]),
 "OS73": ('a Osterwalder and a Schrader and j Commun.Math.Phys.,31', ["axioms"]),
 "OS75": ('a Osterwalder and a Schrader and j Commun.Math.Phys.,42', ["axioms"]),
 "OS78": ('a Osterwalder and a Seiler and j Annals Phys.,110', ["gauge", "lattice"]),
 "Guth80": ('a Guth and t nonconfining', ["nonconfining"]),
}
EXTRA_DOIS = {"AC22": "10.1214/24-AOP1702", "BS83": "10.1007/BF01208780"}
BOOKS = {"GJ": ("Glimm Jaffe Quantum Physics A Functional Integral Point of View", ["functional integral"], "Glimm"),
         "LL10": ("Lawler Limic Random Walk A Modern Introduction", ["random walk"], "Lawler"),
         "JW": ("Jaffe Witten Quantum Yang-Mills theory Millennium Prize Problems", ["yang"], "Jaffe")}
PAGES = {"GM82": "https://link.springer.com/article/10.1007/BF01961240",
         "LW86": "https://link.springer.com/article/10.1007/BF01211097",
         "OS73": "https://link.springer.com/article/10.1007/BF01645738",
         "ADC21": "https://annals.math.princeton.edu/2021/194-1/p03"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def get(url, raw, name, delay):
    time.sleep(delay)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        data = r.read()
    open(os.path.join(raw, name), "wb").write(data)
    return data


def cr(doi, raw, name):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    m = json.loads(get(url, raw, name, 2.5))["message"]
    o = {k: m.get(k) for k in ["title", "container-title", "volume", "issue", "page", "article-number", "issued", "published-print", "DOI", "publisher", "ISBN", "type", "edition-number"]}
    o["author"] = [(a.get("given"), a.get("family")) for a in m.get("author", [])]
    return url, o


def main():
    raw, outfile = sys.argv[1], sys.argv[2]
    os.makedirs(raw, exist_ok=True)
    out = open(outfile, "x")
    res, fails = {}, []
    def rec(k, p, v):
        res.setdefault(k, {}).setdefault("pred", {})[p] = v
        if not v:
            fails.append(f"{k}:{p}")
    for k, (q, kw) in INSP.items():
        try:
            url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode({"q": q, "fields": IF, "size": 5})
            hits = [h["metadata"] for h in json.loads(get(url, raw, k + ".insp2.json", 0.7))["hits"]["hits"]]
            res.setdefault(k, {})["inspire_url"] = url
            res[k]["inspire"] = hits
            t = hits[0]["titles"][0]["title"] if hits else ""
            rec(k, "Q1", len(hits) == 1 and all(w in t.lower() for w in kw))
            crs = []
            for i, d in enumerate([x["value"] for x in (hits[0].get("dois", []) if hits else [])]):
                try:
                    u, c = cr(d, raw, f"{k}.cr2_{i}.json"); crs.append({"url": u, "rec": c})
                except Exception as e:
                    crs.append({"doi": d, "error": repr(e)})
            res[k]["crossref"] = crs
            if crs:
                rec(k, "Q2", any("rec" in c and c["rec"]["title"] and norm(c["rec"]["title"][0]) == norm(t) for c in crs))
        except Exception as e:
            res.setdefault(k, {})["error"] = repr(e); fails.append(f"{k}:error")
    for k, d in EXTRA_DOIS.items():
        try:
            u, c = cr(d, raw, f"{k}.cr2.json"); res.setdefault(k, {})["crossref"] = [{"url": u, "rec": c}]
            rec(k, "Q2", True)
        except Exception as e:
            res.setdefault(k, {})["error"] = repr(e); rec(k, "Q2", False)
    for k, (qs, kw, fam) in BOOKS.items():
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": qs, "rows": 6})
        try:
            items = json.loads(get(url, raw, k + ".crq2.json", 2.5))["message"]["items"]
            lst = []
            for it in items:
                lst.append({kk: it.get(kk) for kk in ["title", "container-title", "DOI", "type", "publisher", "issued", "ISBN", "edition-number", "page", "volume"]}
                           | {"author": [(a.get("given"), a.get("family")) for a in it.get("author", [])],
                              "editor": [(a.get("given"), a.get("family")) for a in it.get("editor", [])]})
            res.setdefault(k + "_book", {})["url"] = url
            res[k + "_book"]["items"] = lst
            rec(k + "_book", "Q3", any(all(w in (i["title"] or [""])[0].lower() for w in kw) and any(fam == a[1] for a in i["author"]) for i in lst))
        except Exception as e:
            res.setdefault(k + "_book", {})["error"] = repr(e); rec(k + "_book", "Q3", False)
    for k, url in PAGES.items():
        try:
            h = get(url, raw, k + ".page.html", 1.5).decode("utf-8", "replace")
            metas = re.findall(r'<meta\s+name="(citation_[a-z_]+|dc\.[a-z]+)"\s+content="([^"]*)"', h)
            res.setdefault(k + "_page", {})["url"] = url
            res[k + "_page"]["meta"] = [(n, html.unescape(v)) for n, v in metas if n not in ("citation_reference",)][:40]
            ttl = re.search(r"<title>(.*?)</title>", h, re.S)
            res[k + "_page"]["html_title"] = html.unescape(ttl.group(1).strip()) if ttl else None
            rec(k + "_page", "Q4", any(n == "citation_title" for n, _ in metas))
        except Exception as e:
            res.setdefault(k + "_page", {})["error"] = repr(e); rec(k + "_page", "Q4", False)
    json.dump({"results": res, "failed_predicates": fails}, out, indent=1, ensure_ascii=False)
    out.close()
    print("FAILED:", fails)


if __name__ == "__main__":
    main()
