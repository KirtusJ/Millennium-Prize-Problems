import sys, re, html, urllib.request
aid = sys.argv[1]
req = urllib.request.Request("https://arxiv.org/abs/"+aid, headers={"User-Agent":"python-urllib"})
try:
    t = urllib.request.urlopen(req, timeout=30).read().decode("utf-8","replace")
except Exception as e:
    print("ERROR", aid, e); sys.exit(1)
def m(n): return [html.unescape(x) for x in re.findall(r'<meta name="%s" content="([^"]*)"'%n, t)]
print("id:", aid)
print("title:", m("citation_title"))
print("authors:", m("citation_author"))
print("date:", m("citation_date"), m("citation_online_date"))
sub = re.search(r'\[Submitted on ([^\]]*)\]', t)
print("submitted:", sub.group(1) if sub else None)
