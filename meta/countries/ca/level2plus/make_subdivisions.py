import csv
import json
from pathlib import Path

# File paths
eng_csv = "sgc-cgt-2021-structure-eng.csv"
fra_csv = "sgc-cgt-2021-structure-fra.csv"

def fill_code(level,raw_code):
    code_raw = raw_code
    level = int(level)
    if level == 2:
        code = code_raw.zfill(2)
    elif level == 3:
        code = code_raw.zfill(4)
    elif level == 4:
        code = code_raw.zfill(7)
    else:
        code = code_raw  # leave untouched for level 1 or unknown
    return code

# Load English structure
eng_data = {}
with open(eng_csv, encoding="ISO-8859-1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        level = int(row["Level"])
        if level<3:
            continue
        entity_type = row["Hierarchical structure"]
        code = fill_code(level,row["Code"])
        eng_data[code] = {
            "level": int(level),
            "name": row["Class title"]
        }

# Load French structure
fra_data = {}
with open(fra_csv, encoding="ISO-8859-1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        level = int(row["Niveau"])
        if level<3:
            continue
        code = fill_code(level,row["Code"])
        fra_data[code] = row["Titres de classes"]

# Output directory base
base_path = Path("../../../../countries/ca")

# Province code map
prov_map = {
    "10": "nl", "11": "pe", "12": "ns", "13": "nb", "24": "qc", "35": "on",
    "46": "mb", "47": "sk", "48": "ab", "59": "bc", "60": "yt", "61": "nt", "62": "nu"
}


# Normalize name to safe folder format
def normalize(name):
    return name.lower().replace(" ", "_").replace(".", "").replace(",", "").replace("__", "_")

# Write entries
for code, entry in eng_data.items():
    if code not in fra_data:
        continue
    level = entry["level"]
    name_en = entry["name"]
    name_fr = fra_data[code]
    prov_prefix = code[:2]
    prov_abbr = prov_map.get(prov_prefix)
    if not prov_abbr:
        print(f"Skipping unknown province code {prov_prefix} in {code}")
        continue

    norm_name = normalize(name_en)

    # Determine output folder structure
    if level == 2:
        folder = base_path / prov_abbr
        parent_id = f"ca/{prov_abbr}"
    elif level == 3:
        folder = base_path / prov_abbr / norm_name
        parent_id = f"ca/{prov_abbr}"
    elif level == 4:
        parent_code = code[:4]  # parent division code (level 3)
        parent_name = eng_data.get(parent_code, {}).get("name", parent_code)
        norm_parent = normalize(parent_name)
        folder = base_path / prov_abbr / norm_parent / norm_name
        parent_id = f"ca/{prov_abbr}/{norm_parent}"
    else:
        folder = base_path / f"level{level}" / code
        parent_id = f"ca"

    folder.mkdir(parents=True, exist_ok=True)

    output = {
        "type": normalize(entity_type),
        "name": {
            "en": name_en,
            "fr": name_fr
        },
        "alternate_names": [],
        "valid_from": None,
        "valid_to": None,
        "parent_id": parent_id,
        "admin_level": level,
        "local_code": code,
        "meta": {
            "sgc_province": prov_prefix if level > 2 else None
        }
    }

    with open(folder / "index.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

print("All administrative levels (1–4) index.json files created with level 4 nested inside level 3 folders.")

