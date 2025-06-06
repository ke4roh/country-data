import os
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent.parent
INPUT_FILE = HERE / "iso-3166.json"
OUTPUT_ROOT = PROJECT_ROOT / "countries"

def slugify_country_code(code):
    return code.lower()

def extract_country_record(entry):
    d = entry.get("d", {})
    c = {
        "type": "country",
        "name": {
            "en": d.get("148", ""),
            "fr": d.get("160", "")
        },
        "alternate_names": [name.strip() for name in d.get("158", "").strip("[]").split(",") if name.strip()],
        "meta": {
            "iso_3166_1_alpha2": d.get("144", ""),
            "iso_3166_1_alpha3": d.get("166", ""),
            "iso_3166_1_numeric": d.get("162", ""),
            "iso_path": d.get("156", "")
        },
        "valid_from": None
    }
    if d.get("174") or d.get("170"):
        c["change_notes"] = {}
        if d.get("174"):
            c["change_notes"]["en"]=d.get("174")
        if d.get("170"):
            c["change_notes"]["fr"]=d.get("170")
    return c

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    try:
        countries = raw_data[0]["rpc"][0][3][1]
    except (KeyError, IndexError, TypeError):
        print("Could not extract countries from expected RPC structure.")
        return

    for entry in countries:
        record = extract_country_record(entry)
        country_code = record["meta"]["iso_3166_1_alpha2"]
        if not country_code:
            continue
        output_dir = os.path.join(OUTPUT_ROOT, country_code.lower())
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "index.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        print(f"Wrote {output_path}")

if __name__ == "__main__":
    main()
