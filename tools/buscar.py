"""Search Wikimedia Commons for freely licensed photos of each sauce.

Usage: python buscar.py busquedas/consultas-NN.json busquedas/candidatos-NN.json

The queries file maps each sauce slug to a list of search terms. Candidates with a
free license (public domain, CC0, CC BY, CC BY-SA) are written to the results file,
and a small thumbnail of each one is saved in candidatos/ (not committed) so they
can be reviewed, for example with ImageMagick's montage. Pick one per sauce and
add it to fotos.txt.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "recetas-de-salsas-notes/1.0 (personal notes script)"
FREE = re.compile(r"^(CC0|Public domain|PD|CC BY(-SA)? ?[0-9.]+|CC BY(-SA)?)", re.I)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "candidatos")


def api(params):
    params = {**params, "format": "json", "formatversion": "2"}
    url = API + "?" + urllib.parse.urlencode(params)
    return json.loads(get(url))


def get(url):
    for attempt in range(6):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(10 * (attempt + 1))
    raise RuntimeError("rate limited: " + url)


def strip(html):
    return re.sub(r"<[^>]+>", "", html or "").strip()


def search(query, limit=8):
    data = api({
        "action": "query", "generator": "search", "gsrsearch": f"filetype:bitmap {query}",
        "gsrnamespace": 6, "gsrlimit": limit, "prop": "imageinfo",
        "iiprop": "url|extmetadata|size", "iiurlwidth": 400,
    })
    pages = data.get("query", {}).get("pages", [])
    pages.sort(key=lambda p: p.get("index", 0))
    out = []
    for p in pages:
        ii = p["imageinfo"][0]
        md = ii.get("extmetadata", {})
        lic = strip(md.get("LicenseShortName", {}).get("value"))
        if not FREE.match(lic):
            continue
        out.append({
            "title": p["title"], "license": lic,
            "license_url": strip(md.get("LicenseUrl", {}).get("value")),
            "artist": strip(md.get("Artist", {}).get("value")),
            "thumb": ii.get("thumburl"), "w": ii["width"], "h": ii["height"],
            "page": ii.get("descriptionurl"),
        })
    return out


def main():
    queries = json.load(open(os.path.join(HERE, sys.argv[1]), encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    result = {}
    for slug, qs in queries.items():
        seen, cands = set(), []
        for q in qs:
            for c in search(q):
                if c["title"] not in seen:
                    seen.add(c["title"])
                    cands.append(c)
            time.sleep(2)
        cands = cands[:6]
        result[slug] = cands
        for i, c in enumerate(cands):
            dest = os.path.join(OUT, f"{slug}-{i}.jpg")
            if not os.path.exists(dest) and c["thumb"]:
                data = get(c["thumb"])
                with open(dest, "wb") as f:
                    f.write(data)
                time.sleep(2)
        print(slug, len(cands), file=sys.stderr)
    json.dump(result, open(os.path.join(HERE, sys.argv[2]), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
