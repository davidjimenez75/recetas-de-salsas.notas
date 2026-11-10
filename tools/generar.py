"""Write the sauce notes (.es.md / .en.md), readme.md and desktop.ini files.

Usage: python generar.py

The recipes live in salsas_*.py (every file is loaded, in name order), and the
photo credits in creditos.json (filled by descargar.py). Everything is written
to the repository root, the folder above tools/.
"""
import glob
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def load_sauces():
    sauces = []
    for path in sorted(glob.glob(os.path.join(HERE, "salsas_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sauces += module.SALSAS
    return sauces


CREATED = "2026-11-10"
SALSAS = sorted(load_sauces(), key=lambda s: s["slug"])
CRED = json.load(open(os.path.join(HERE, "creditos.json"), encoding="utf-8"))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(text)


def credit(slug, lang):
    c = CRED[slug]
    author = c["artist"].replace('"', "").strip() or "Wikimedia Commons"
    who = f"[{author}]({c['page']})"
    if c["license"].lower().startswith("public domain"):
        lic = "dominio público" if lang == "es" else "public domain"
    else:
        url = c["license_url"].replace("http://", "https://").rstrip("/")
        url = url.removesuffix("/deed.en")
        url += "/deed.es" if lang == "es" else "/"
        lic = f"[{c['license']}]({url})"
    if lang == "es":
        return f"*Foto: {who}, {lic}, vía Wikimedia Commons.*"
    return f"*Photo: {who}, {lic}, via Wikimedia Commons.*"


def note(s, lang):
    d, other = s[lang], s["en" if lang == "es" else "es"]
    base = ["cocina", "receta", "salsa"] if lang == "es" else ["cooking", "recipe", "sauce"]
    tags = sorted(set(base + s[f"tags_{lang}"]))
    other_lang = "en" if lang == "es" else "es"
    L = ["---", f"created: {CREATED}", f"lang: {'es_ES' if lang == 'es' else 'en_US'}", "tags:"]
    L += [f"  - {t}" for t in tags]
    L += [f"title: {d['title']}", "type: Recipe", "---", f"# {d['title']}", "",
          f"![{d['title']}]({s['slug']}.jpg)", "", credit(s["slug"], lang), "",
          d["intro"], "", f"🥄 {d['meta']}", "",
          ("*In English:* " if lang == "es" else "*En español:* ")
          + f"[{other['title']}]({s['slug']}.{other_lang}.md)", "",
          "## Ingredientes" if lang == "es" else "## Ingredients", ""]
    L += [f"- {i}" for i in d["ing"]]
    L += ["", "## Preparación" if lang == "es" else "## Directions", ""]
    L += [f"{n}. {t}" for n, t in enumerate(d["steps"], 1)]
    L += ["", "## Consejos" if lang == "es" else "## Tips", ""]
    L += [f"- {t}" for t in d["tips"]]
    return "\n".join(L) + "\n"


def pizarra(slugs):
    L = ["[Pizarra]", "Columnas=2", ""]
    for n, slug in enumerate(slugs):
        y = 40 + n * 1228.91
        y = f"{y:.2f}".rstrip("0").rstrip(".")
        for lang, x in (("en", 40), ("es", 916)):
            L += [f"[{slug}.{lang}.md]", f"pos_x={x}", f"pos_y={y}", "color=yellow",
                  "color_strong=false", "style=mono", "rotation=0", "width=852", "height=0", ""]
        # The photo is only shown inside the notes: hide its own card.
        L += [f"[{slug}.jpg]", "pos_x=1792", f"pos_y={y}", "color=hidden",
              "color_strong=false", "style=mono", "rotation=0", "width=306.9", "height=0", ""]
    return "\n".join(L)


def readme():
    L = ["---", "id: recetas-de-salsas", "status: active", "tags:", "  - cooking", "  - recipes",
         "  - sauces", "title: recetas-de-salsas--Sauce recipes", "type: Index", "---",
         "# recetas-de-salsas--Sauce recipes", "",
         "Sauce recipes: mostly **Spanish sauces**, plus some **Japanese**, mild **Mexican**, **Italian** and **French** ones. They are sorted into one "
         "subfolder per letter (`a/`, `b/`, `c/`…), using the first letter of the sauce's own name, without "
         "the word «salsa» (so *salsa brava* goes in `b/brava`). Japanese, Italian and French sauces keep their own name "
         "(*goma dare* goes in `g/goma-dare`, *béarnaise* in `b/bearnaise`).", "",
         "Each sauce has one note per language, with the same name and the language code before `.md`:", "",
         "- `<sauce>.es.md`: in Spain Spanish (`lang: es_ES`).",
         "- `<sauce>.en.md`: in US English (`lang: en_US`), with US measurements (cups, ounces, °F).", "",
         "Both use `type: Recipe`. The photo sits next to them with the same name (`<sauce>.jpg`). "
         "Only freely licensed photos from Wikimedia Commons are used (public domain, CC0, CC BY or "
         "CC BY-SA), and each recipe credits the author and license.", "",
         "- **Vegan and alcohol-free:** "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "vegana" in s["tags_es"])
         + " (tagged `vegana` and `sin-alcohol`).",
         "- **Japanese:** "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "japon" in s["tags_es"])
         + " (tagged `japon`).",
         "- **Mexican, mild:** "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "mexico" in s["tags_es"])
         + " (tagged `mexico` and `poco-picante`; the chile is optional or seeded).",
         "- **Italian:** "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "italia" in s["tags_es"])
         + " (tagged `italia`).",
         "- **French:** "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "francia" in s["tags_es"])
         + " (tagged `francia`).",
         "- **Drink or ingredient photos:** no free photo of the finished dish was found for "
         + ", ".join(f"*{s['es']['title']}*" for s in SALSAS if "La foto muestra" in s["es"]["intro"])
         + ", so their notes show the drink or main ingredient instead, and say so.",
         "- **Hidden in Notas-Rust:** every photo is marked `color=hidden` in its folder's `desktop.ini`, "
         "so the board shows only the notes and the photo appears inside them. "
         "Use «Mostrar las ocultas» (Alt+H) to show the photos on the board.", "",
         "| Letter | Español | English | Photo license |", "| --- | --- | --- | --- |"]
    for s in SALSAS:
        p = f"{s['slug'][0]}/{s['slug']}"
        lic = CRED[s["slug"]]["license"]
        L.append(f"| {s['slug'][0].upper()} | [{s['es']['title']}]({p}.es.md) | "
                 f"[{s['en']['title']}]({p}.en.md) | {lic} |")
    L += ["", "The recipe texts are original. The photos keep their own licenses, as stated in each recipe.",
          "", "## Tools", "",
          "The notes, this readme and the `desktop.ini` files are generated by the Python scripts in "
          "`tools/` (they need Python 3 and ImageMagick):", "",
          "- `salsas_*.py`: the recipes, in Spanish and English.",
          "- `buscar.py`: searches Wikimedia Commons for freely licensed photos.",
          "- `fotos.txt`: the photo chosen for each sauce; `busquedas/` keeps the searches.",
          "- `descargar.py`: downloads the chosen photos and writes `creditos.json`.",
          "- `generar.py`: writes the notes, `readme.md` and the `desktop.ini` files.", "",
          "To add a sauce: add it to a `salsas_*.py` file, search for a photo with `buscar.py`, add it "
          "to `fotos.txt`, then run `descargar.py` and `generar.py`."]
    return "\n".join(L) + "\n"


def main():
    letters = {}
    for s in SALSAS:
        letters.setdefault(s["slug"][0], []).append(s["slug"])
        for lang in ("es", "en"):
            write(os.path.join(REPO, s["slug"][0], f"{s['slug']}.{lang}.md"), note(s, lang))
    for letter, slugs in letters.items():
        write(os.path.join(REPO, letter, "desktop.ini"), pizarra(slugs))
    write(os.path.join(REPO, "readme.md"), readme())
    write(os.path.join(REPO, "desktop.ini"),
          "[.ShellClassInfo]\nTop=1\nIconResource=..\\..\\icons\\favorites\\cooking.ico,0\n")
    write(os.path.join(REPO, ".gitignore"),
          "# notas-rust\nThumbs.db\n.DS_Store\n~$*\n*.tmp\nNotas-Rust.toml\n\n"
          "# tools: search thumbnails and Python cache\ntools/candidatos/\n__pycache__/\n")
    print(len(SALSAS), "sauces,", len(letters), "letters")


if __name__ == "__main__":
    main()
