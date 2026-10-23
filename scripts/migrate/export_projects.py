"""One-off: export legacy project data to src/data/projects.json and tech-categories.json.

Run from the repository root:  python -I scripts/migrate/export_projects.py
Reads portfolio/projects.py and portfolio/translations.py only; never writes into legacy files.

Legacy quirks handled here:
- Project ids are not unique (12-19 repeat). New ids are assigned so that sorting by id
  descending reproduces the legacy display order (stable sort by legacy id, descending).
- Polish descriptions were looked up by the non-unique id, so several projects showed another
  project's text. Each project now takes the `proj_desc_*` entry whose English text matches its
  own description (similarity >= MATCH_THRESHOLD); otherwise the Polish text is left empty
  for a reviewed translation.
"""

import ast
import difflib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from portfolio.translations import TRANSLATIONS  # noqa: E402

MATCH_THRESHOLD = 0.75

CATEGORY_IDS = {
    "Programming Languages": ("languages", "Języki programowania", "--tech-cyan"),
    "Testing Tools": ("testing", "Narzędzia testowe", "--tech-blue"),
    "Databases": ("databases", "Bazy danych", "--tech-purple"),
    "Frameworks & Technologies": ("frameworks", "Frameworki i technologie", "--tech-pink"),
    "DevOps & Tools": ("devops", "DevOps i narzędzia", "--tech-green"),
    "Other": ("other", "Inne", "--tech-orange"),
}


def literal(src: str, name: str):
    match = re.search(rf"^{name} = (.*?^[\]\}}])", src, re.S | re.M)
    return ast.literal_eval(match.group(1))


def slugify(text: str) -> str:
    text = text.lower().replace("&", " ").replace("(", " ").replace(")", " ")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def polish_description(description: str) -> str:
    en, pl = TRANSLATIONS["en"], TRANSLATIONS["pl"]
    keys = [k for k in en if k.startswith("proj_desc_")]
    best = max(keys, key=lambda k: difflib.SequenceMatcher(None, en[k], description).ratio())
    ratio = difflib.SequenceMatcher(None, en[best], description).ratio()
    return pl[best] if ratio >= MATCH_THRESHOLD else ""


def main() -> None:
    src = (ROOT / "portfolio" / "projects.py").read_text(encoding="utf-8")
    projects = literal(src, "PROJECTS_DATA")
    categories = literal(src, "TECH_CATEGORIES")
    image_map = json.loads((ROOT / "scripts" / "migrate" / "image_map.json").read_text(encoding="utf-8"))
    # Reviewed (or draft) Polish copy for texts the legacy app only had in English.
    drafts = json.loads((ROOT / "scripts" / "migrate" / "polish_drafts.json").read_text(encoding="utf-8"))

    ordered = sorted(projects, key=lambda p: p["id"], reverse=True)
    out, slugs = [], set()
    for index, p in enumerate(ordered):
        slug = slugify(p["title"])
        assert slug not in slugs, f"duplicate slug {slug}"
        slugs.add(slug)
        legacy_image = p["image"].lstrip("/")
        image = f"../assets/projects/{image_map[legacy_image]}" if legacy_image else None
        # Projects without a legacy screenshot use a generated placeholder (make_placeholders.py).
        if image is None and (ROOT / "src" / "assets" / "projects" / f"{slug}.png").exists():
            image = f"../assets/projects/{slug}.png"
        out.append(
            {
                "id": len(ordered) - index,
                "slug": slug,
                "title": p["title"],
                "description": {
                    "en": p["description"],
                    "pl": polish_description(p["description"]) or drafts["descriptions"].get(slug, ""),
                },
                "technologies": p["technologies"],
                "domain": p["domain"],
                "platform": p["platform"],
                "type": "client" if p["project_type"] == "Client Projects" else "personal",
                "status": "completed" if p["status"] == "Completed" else "in-progress",
                "achievements": {"en": p.get("achievements", []), "pl": drafts["achievements"].get(slug, [])},
                "image": image,
                "imageAlt": {"en": f"{p['title']} screenshot", "pl": f"Zrzut ekranu: {p['title']}"} if image else None,
                "github": p["github"] or None,
                "demo": p["demo"] or None,
            }
        )
    if all(p["imageAlt"] is None for p in out):
        raise SystemExit("no images mapped")
    for p in out:
        if p["imageAlt"] is None:
            del p["imageAlt"]

    used = {t for p in out for t in p["technologies"]}
    cats, placed = [], set()
    for name, data in categories.items():
        cid, pl_label, token = CATEGORY_IDS[name]
        techs = [t for t in data["techs"] if t in used and t not in placed]
        placed.update(techs)
        cats.append({"id": cid, "label": {"en": name, "pl": pl_label}, "colorToken": token, "techs": techs})
    uncategorized = sorted(used - placed)
    if uncategorized:
        print("uncategorized technologies (added to 'other'):", uncategorized)
        cats[-1]["techs"].extend(uncategorized)

    data_dir = ROOT / "src" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "projects.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    facets = {
        "domains": [{"value": d, "label": {"en": d, "pl": drafts["domains"][d]}} for d in sorted({p["domain"] for p in out})],
        "platforms": [{"value": k, "label": {"en": k, "pl": v}} for k, v in drafts["platforms"].items()],
    }
    (data_dir / "facets.json").write_text(json.dumps(facets, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (data_dir / "tech-categories.json").write_text(json.dumps(cats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    img_dir = ROOT / "src" / "assets" / "projects"
    img_dir.mkdir(parents=True, exist_ok=True)
    for old, new in image_map.items():
        shutil.copyfile(ROOT / "assets" / old, img_dir / new)
    shutil.copyfile(ROOT / "assets" / "logo.png", ROOT / "src" / "assets" / "profile.png")
    (ROOT / "public").mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "assets" / "favicon.ico", ROOT / "public" / "favicon.ico")

    missing = [p["slug"] for p in out if not p["description"]["pl"]]
    uneven = [p["slug"] for p in out if len(p["achievements"]["en"]) != len(p["achievements"]["pl"])]
    print(f"projects: {len(out)}; missing Polish description: {missing}; uneven achievements: {uneven}")


if __name__ == "__main__":
    main()
