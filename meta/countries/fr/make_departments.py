import json
import unicodedata
from pathlib import Path

SRC = Path(__file__).with_name("departements.json")
# Navigate three levels up to the repository root then into countries/fr
BASE = Path(__file__).resolve().parents[3] / "countries" / "fr"


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    for ch in ["'", "’"]:
        s = s.replace(ch, "-")
    for ch in [",", "."]:
        s = s.replace(ch, "")
    s = s.replace(" ", "-")
    while "--" in s:
        s = s.replace("--", "-")
    return s


def main():
    with open(SRC, encoding="utf-8") as f:
        deps = json.load(f)
    for dep in deps:
        slug = slugify(dep["nom"])
        path = BASE / slug
        path.mkdir(parents=True, exist_ok=True)
        data = {
            "type": "department",
            "name": {"en": dep["nom"], "fr": dep["nom"]},
            "alternate_names": [],
            "valid_from": None,
            "valid_to": None,
            "parent_id": "fr",
            "admin_level": 1,
            "local_code": dep["code"],
            "meta": {"insee": dep["code"]},
        }
        with open(path / "index.json", "w", encoding="utf-8") as out:
            json.dump(data, out, indent=2, ensure_ascii=False)
    print("French department files generated.")


if __name__ == "__main__":
    main()
