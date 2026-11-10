"""Download the chosen photos from Wikimedia Commons and record their credits.

Reads fotos.txt, one sauce per line:

    <slug> busquedas/candidatos-NN.json <key> <index>   photo picked from a search result
    <slug> = <other-slug>                               reuse another sauce's photo

Each photo is saved as <letter>/<slug>.jpg (max 1280 px, via ImageMagick), and its
author and license go to creditos.json. Photos that already exist are skipped.
"""
import json
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
API = "https://commons.wikimedia.org/w/api.php"
UA = "recetas-de-salsas-notes/1.0 (personal notes script)"


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


def photo_path(slug):
    return os.path.join(REPO, slug[0], f"{slug}.jpg")


def main():
    cred_path = os.path.join(HERE, "creditos.json")
    creditos = json.load(open(cred_path, encoding="utf-8"))
    aliases = []
    for line in open(os.path.join(HERE, "fotos.txt"), encoding="utf-8"):
        parts = line.split()
        if not parts:
            continue
        slug = parts[0]
        if parts[1] == "=":
            aliases.append((slug, parts[2]))
            continue
        src, key, index = parts[1], parts[2], int(parts[3])
        c = json.load(open(os.path.join(HERE, src), encoding="utf-8"))[key][index]
        creditos[slug] = {k: c[k] for k in ("title", "page", "license", "license_url", "artist")}
        dest = photo_path(slug)
        if os.path.exists(dest):
            continue
        q = urllib.parse.urlencode({"action": "query", "titles": c["title"], "prop": "imageinfo",
                                    "iiprop": "url", "iiurlwidth": 1280, "format": "json",
                                    "formatversion": 2})
        ii = json.loads(get(API + "?" + q))["query"]["pages"][0]["imageinfo"][0]
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        tmp = dest + ".download"
        with open(tmp, "wb") as f:
            f.write(get(ii.get("thumburl") or ii["url"]))
        subprocess.run(["magick", tmp, "-auto-orient", "-resize", "1280x1280>", "-strip",
                        "-quality", "85", dest], check=True)
        os.remove(tmp)
        print(slug, c["license"], c["artist"])
        time.sleep(2)
    for slug, other in aliases:
        creditos[slug] = creditos[other]
        if not os.path.exists(photo_path(slug)):
            os.makedirs(os.path.dirname(photo_path(slug)), exist_ok=True)
            shutil.copy(photo_path(other), photo_path(slug))
    json.dump(creditos, open(cred_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
