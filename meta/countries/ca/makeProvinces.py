import os
import json
from pathlib import Path

# Data source: Provinces and Territories of Canada
subdivisions = [
    {"name_en": "Newfoundland and Labrador", "name_fr": "Terre‑Neuve‑et‑Labrador", "abbrev_en": "N.L.", "abbrev_fr": "T.-N.-L.", "code": "NL", "sgc": "10", "region": "Atlantic"},
    {"name_en": "Prince Edward Island", "name_fr": "Île-du-Prince-Édouard", "abbrev_en": "P.E.I.", "abbrev_fr": "Î.-P.-É.", "code": "PE", "sgc": "11", "region": "Atlantic"},
    {"name_en": "Nova Scotia", "name_fr": "Nouvelle-Écosse", "abbrev_en": "N.S.", "abbrev_fr": "N.-É.", "code": "NS", "sgc": "12", "region": "Atlantic"},
    {"name_en": "New Brunswick", "name_fr": "Nouveau-Brunswick", "abbrev_en": "N.B.", "abbrev_fr": "N.-B.", "code": "NB", "sgc": "13", "region": "Atlantic"},
    {"name_en": "Quebec", "name_fr": "Québec", "abbrev_en": "Que.", "abbrev_fr": "Qc", "code": "QC", "sgc": "24", "region": "Quebec"},
    {"name_en": "Ontario", "name_fr": "Ontario", "abbrev_en": "Ont.", "abbrev_fr": "Ont.", "code": "ON", "sgc": "35", "region": "Ontario"},
    {"name_en": "Manitoba", "name_fr": "Manitoba", "abbrev_en": "Man.", "abbrev_fr": "Man.", "code": "MB", "sgc": "46", "region": "Prairies"},
    {"name_en": "Saskatchewan", "name_fr": "Saskatchewan", "abbrev_en": "Sask.", "abbrev_fr": "Sask.", "code": "SK", "sgc": "47", "region": "Prairies"},
    {"name_en": "Alberta", "name_fr": "Alberta", "abbrev_en": "Alta.", "abbrev_fr": "Alb.", "code": "AB", "sgc": "48", "region": "Prairies"},
    {"name_en": "British Columbia", "name_fr": "Colombie-Britannique", "abbrev_en": "B.C.", "abbrev_fr": "C.-B.", "code": "BC", "sgc": "59", "region": "British Columbia"},
    {"name_en": "Yukon", "name_fr": "Yukon", "abbrev_en": "Y.T.", "abbrev_fr": "Yn", "code": "YT", "sgc": "60", "region": "Territories"},
    {"name_en": "Northwest Territories", "name_fr": "Territoires du Nord‑Ouest", "abbrev_en": "N.W.T.", "abbrev_fr": "T.N.-O.", "code": "NT", "sgc": "61", "region": "Territories"},
    {"name_en": "Nunavut", "name_fr": "Nunavut", "abbrev_en": "Nvt.", "abbrev_fr": "Nt", "code": "NU", "sgc": "62", "region": "Territories"}
]

base_path = Path("../../../countries/ca")

for entry in subdivisions:
    path = base_path / entry["code"].lower() / "index.json"
    os.makedirs(path.parent, exist_ok=True)
    
    index_data = {
        "type": "province",
        "name": {
            "en": entry["name_en"],
            "fr": entry["name_fr"]
        },
        "alternate_names": [entry["abbrev_en"], entry["abbrev_fr"]],
        "valid_from": None,
        "valid_to": None,
        "parent_id": "ca",
        "admin_level": 1,
        "local_code": entry["sgc"],
        "meta": {
            "iso_alpha_code": entry["code"],
            "region": entry["region"]
        }
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

print("Subdivision files generated successfully.")
