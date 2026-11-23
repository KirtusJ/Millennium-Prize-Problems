"""fetch.py -- fetch bibliographic records for the p4-refs keys.

Usage: python3 fetch.py <rawdir> <outfile>
  rawdir : directory OUTSIDE the work dir where raw JSON/XML records are stored
  outfile: result JSON (opened with mode "x": never overwritten)

Sources: INSPIRE literature API (primary for physics), arXiv export API
(for every key with an arXiv id), Crossref /works/<doi> (for every DOI found),
Crossref bibliographic query (books only). No randomness (no seed needed).

PREDICATES (fixed before the first run):
 P1[key]  the INSPIRE (or, for books, Crossref) query returns >=1 hit, and the
          chosen hit's title contains every expected keyword of that key.
 P2[key]  where the brief states journal volume and year, the record's
          journal volume and year equal the brief's values.
 P3[key]  where a DOI is found, the Crossref record exists and its title equals
          the INSPIRE/arXiv title after normalization.
 P4[key]  where an arXiv id is given, the arXiv API record exists and its title
          equals the INSPIRE title after normalization (if INSPIRE has the key).
Tolerance: none numerical. Titles are compared after normalization
(lowercase, TeX/accents removed, only [a-z0-9] kept) because INSPIRE, Crossref
and arXiv differ in capitalization and markup; this is the only tolerance and
its source is that formatting difference. A failure is printed, never hidden.
Exit code 0 always when the program runs to completion (failures are data).
"""
import json, os, re, sys, time, unicodedata, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "pcp-bib-worker/1.0 (research bibliography check)"}
IFIELDS = "titles,authors.full_name,publication_info,dois,arxiv_eprints,imprints,isbns,document_type"

# key: (inspire query or None, arXiv id or None, expected title keywords, (vol, year) or None)
KEYS = {
 "OS73": ('t "Axioms for Euclidean Green" and j Commun.Math.Phys.,31', None, ["axioms", "euclidean"], ("31", 1973)),
 "OS75": ('t "Axioms for Euclidean Green" and j Commun.Math.Phys.,42', None, ["axioms", "euclidean"], ("42", 1975)),
 "KQR21": (None, "2104.02090", ["distributions", "minkowski"], None),
 "OS78": ('t "Gauge field theories on a lattice" and a Osterwalder', None, ["gauge", "lattice"], ("110", 1978)),
 "Lu77": ('a Luscher and j Commun.Math.Phys.,54', None, ["transfer", "matrix"], ("54", 1977)),
 "FILS78": ('t "Phase transitions and reflection positivity" and j Commun.Math.Phys.,62', None, ["reflection", "positivity"], ("62", 1978)),
 "SZZ23": (None, "2204.12737", ["stochastic", "strong coupling"], None),
 "Guth80": ('a Guth and j Phys.Rev.D,21', None, ["nonconfining"], ("21", 1980)),
 "FS82": ('a Frohlich and a Spencer and j Commun.Math.Phys.,83', None, ["massless", "symmetry restoration"], ("83", 1982)),
 "GM82": ('a Gopfert and j Commun.Math.Phys.,82', None, ["confinement", "static quarks"], ("82", 1982)),
 "AC22": (None, "2202.10375", ["correlation decay"], None),
 "Ch21": (None, "2006.16229", ["quark confinement"], None),
 "Ch18": (None, "1803.01950", ["probabilists"], None),
 "To07": (None, "0707.2179", ["confinement", "su(2)"], None),
 "IS07": (None, "0711.4930", ["tomboulis"], None),
 "IS08": (None, "0803.3019", ["tomboulis"], None),
 "KT02": (None, "hep-lat/0108017", [], ("65", 2002)),
 "TY85": ('a Tomboulis and a Yaffe and j Commun.Math.Phys.,100', None, ["finite temperature"], ("100", 1985)),
 "BS83": ('a Borgs and a Seiler and j Commun.Math.Phys.,91', None, ["nonzero temperature"], ("91", 1983)),
 "ADC21": (None, "1912.07973", ["marginal triviality"], ("194", 2021)),
 "Sin81": ('a Singer and j Phys.Scripta,24', None, ["orbit space"], ("24", 1981)),
 "CCK07": (None, "0705.2629", ["dual computations"], None),
 "Cr79": ('doi 10.1103/PhysRevLett.43.553', None, ["critical dimensionality"], ("43", 1979)),
 "FiveD11": (None, "1110.4210", [], None),
 "LW86": ('a Luscher and j Commun.Math.Phys.,105', None, ["scattering states"], ("105", 1986)),
 "FHK93": (None, "hep-lat/9208012", ["asymptotic scaling"], ("392", 1993)),
 "Te98": (None, "hep-th/9812187", ["glueball masses"], None),
 "LTW04": (None, "hep-lat/0404008", ["glueballs", "k-strings"], None),
 "BCH26": (None, "2610.08144", [], None),
 "SS23": (None, "2211.15176", ["glueball spectroscopy", "gradient flow"], ("107", 2023)),
 "GJ": ('t "Quantum Physics: A Functional Integral Point of View"', None, ["functional integral"], None),
}
BOOKS = {"GJ": "Glimm Jaffe Quantum Physics A Functional Integral Point of View",
         "LL10": "Lawler Limic Random Walk A Modern Introduction"}
BOOK_KW = {"GJ": ["functional integral"], "LL10": ["random walk"]}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = re.sub(r"\$|\\[a-zA-Z]+", "", s)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def get(url, raw, name, delay):
    time.sleep(delay)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    with open(os.path.join(raw, name), "wb") as f:
        f.write(data)
    return data


def inspire(q, raw, name):
    url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode({"q": q, "fields": IFIELDS, "size": 5})
    d = json.loads(get(url, raw, name, 0.6))
    return url, [h["metadata"] for h in d["hits"]["hits"]]


def arxiv(aid, raw, name):
    url = "https://export.arxiv.org/api/query?id_list=" + aid
    root = ET.fromstring(get(url, raw, name, 3.1))
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    e = root.find("a:entry", ns)
    if e is None or e.find("a:title", ns) is None:
        return url, None
    t = lambda p: (e.find(p, ns).text.strip() if e.find(p, ns) is not None and e.find(p, ns).text else None)
    return url, {"title": " ".join(t("a:title").split()),
                 "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)],
                 "published": t("a:published"), "journal_ref": t("x:journal_ref"), "doi": t("x:doi"),
                 "id": t("a:id")}


def crossref(doi, raw, name):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    m = json.loads(get(url, raw, name, 0.4))["message"]
    keep = ["title", "container-title", "volume", "page", "article-number", "issued", "DOI", "publisher", "ISBN", "type", "edition-number"]
    out = {k: m.get(k) for k in keep}
    out["author"] = [(a.get("given"), a.get("family")) for a in m.get("author", [])]
    return url, out


def main():
    raw, outfile = sys.argv[1], sys.argv[2]
    os.makedirs(raw, exist_ok=True)
    out = open(outfile, "x")
    res, fails = {}, []
    for key, (q, aid, kw, vy) in KEYS.items():
        r = {"key": key, "predicates": {}}
        safe = key
        try:
            ih = None
            if aid:
                q2 = "arxiv:" + aid
                r["inspire_url"], hits = inspire(q2, raw, safe + ".inspire.json")
            else:
                r["inspire_url"], hits = inspire(q, raw, safe + ".inspire.json")
            r["inspire_nhits"] = len(hits)
            if hits:
                ih = hits[0]
                r["inspire"] = ih
            if aid:
                r["arxiv_url"], ax = arxiv(aid, raw, safe + ".arxiv.xml")
                r["arxiv"] = ax
            else:
                ax = None
            title = (ih["titles"][0]["title"] if ih else (ax["title"] if ax else ""))
            ok1 = bool(title) and all(k in title.lower() for k in kw)
            r["predicates"]["P1"] = ok1
            if vy and ih:
                pi = [p for p in ih.get("publication_info", []) if p.get("journal_volume")]
                r["predicates"]["P2"] = any(p.get("journal_volume") == vy[0] and p.get("year") == vy[1] for p in pi)
            elif vy:
                r["predicates"]["P2"] = False
            dois = [d["value"] for d in (ih or {}).get("dois", [])]
            if not dois and ax and ax.get("doi"):
                dois = [ax["doi"]]
            r["crossref"] = []
            for i, d in enumerate(dois[:2]):
                try:
                    u, c = crossref(d, raw, f"{safe}.crossref{i}.json")
                    r["crossref"].append({"url": u, "rec": c})
                except Exception as e:  # recorded, not hidden
                    r["crossref"].append({"doi": d, "error": repr(e)})
            if dois:
                ct = [c["rec"]["title"][0] for c in r["crossref"] if "rec" in c and c["rec"]["title"]]
                r["predicates"]["P3"] = any(norm(t) == norm(title) for t in ct)
            if aid and ax and ih:
                r["predicates"]["P4"] = norm(ax["title"]) == norm(ih["titles"][0]["title"])
            elif aid:
                r["predicates"]["P4"] = bool(ax) and not ih  # arXiv-only record
        except Exception as e:
            r["error"] = repr(e)
        for p, v in r["predicates"].items():
            if not v:
                fails.append(f"{key}:{p}")
        res[key] = r
        print(key, r["predicates"], r.get("error", ""), flush=True)
    for key, qs in BOOKS.items():
        r = {"key": key, "predicates": {}}
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": qs, "rows": 5})
        try:
            items = json.loads(get(url, raw, key + ".crossrefq.json", 0.4))["message"]["items"]
            r["crossref_query_url"] = url
            r["items"] = [{k: it.get(k) for k in ["title", "DOI", "type", "publisher", "issued", "ISBN", "edition-number"]}
                          | {"author": [(a.get("given"), a.get("family")) for a in it.get("author", [])]} for it in items]
            r["predicates"]["P1"] = any(all(k in (it.get("title") or [""])[0].lower() for k in BOOK_KW[key]) for it in items)
        except Exception as e:
            r["error"] = repr(e)
        for p, v in r["predicates"].items():
            if not v:
                fails.append(f"{key}:{p}")
        res[key + "_book"] = r
        print(key, r["predicates"], r.get("error", ""), flush=True)
    json.dump({"results": res, "failed_predicates": fails}, out, indent=1, ensure_ascii=False)
    out.close()
    print("FAILED:", fails)


if __name__ == "__main__":
    main()
