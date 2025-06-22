import csv
import json
import os
import re
from collections import defaultdict

INPUT_CSV = "Text/GovernmentUnits_National.txt"
OUTPUT_BASE = "../../../../countries/us"
VALID_FROM = None

# 50 U.S. states (alpha-2 codes, lowercase)
US_50_STATE_CODES = {
    'al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga',
    'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md',
    'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj',
    'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc',
    'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'
}

# Override subdivision unit type by state alpha (lowercase)
SUBDIVISION_TYPE_OVERRIDES = {
    "la": "parish",
    "ak": "borough",
    "dc": "ward",         # optional, not currently used in GNIS
    "pr": "municipio",
    "as": "district",
    "mp": "municipality",
    "vi": "island",
    "um": "area"
}

def get_top_level_type(code):
    if code in US_50_STATE_CODES:
        return "state"
    elif code == "dc":
        return "district"
    elif code == "um":
        return "outlying_area"
    else:
        return "territory"

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

# Containers
states = {}
counties_by_state = defaultdict(list)

with open(INPUT_CSV, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter="|")
    for lineno,row in enumerate(reader, start=1):
        if row["country_alpha"] != "US":
            continue

        try:
            unit_type = row["unit_type"]
            state_alpha = row["state_alpha"].lower()
            state_name = row["state_name"]
            county_name = row["county_name"]
            feature_name = row["feature_name"]
            feature_id = row["feature_id"]
            state_numeric = row["state_numeric"].zfill(2)
            county_numeric = row["county_numeric"].zfill(3)
        except KeyError as e:
            missing_key = e.args[0]
            raise KeyError(
                f"Missing key '{missing_key}' on line {lineno}. Row content: {row}"
            ) from e

        # Top-level units
        if unit_type == "STATE":
            state_type = get_top_level_type(state_alpha)
            states[state_alpha] = {
                "type": state_type,
                "name": {"en": state_name},
                "alternate_names": [],
                "valid_from": VALID_FROM,
                "valid_to": None,
                "meta": {
                    "fips": state_numeric,
                    "gnis_id": feature_id,
                },
                "parent_id": "us",
                "admin_level": 1
            }

        # Second-level units
        elif unit_type == "COUNTY":
            subdivision_type = SUBDIVISION_TYPE_OVERRIDES.get(state_alpha, "county")
            slug = slugify(county_name)

            counties_by_state[state_alpha].append({
                "filename": f"{slug}.json",
                "content": {
                    "type": subdivision_type,
                    "name": {
                        "en": f"{county_name} {subdivision_type.capitalize()}"
                    },
                    "alternate_names": [feature_name],
                    "valid_from": VALID_FROM,
                    "valid_to": None,
                    "meta": {
                        "fips": state_numeric + county_numeric,
                        "state_fips": state_numeric,
                        "county_fips": county_numeric,
                        "gnis_id": feature_id,
                    },
                    "parent_id": f"us/{state_alpha}",
                    "admin_level": 2,
                    "local_code": county_numeric,
                }
            })

# Write JSON files
for state_alpha, state_data in states.items():
    state_dir = os.path.join(OUTPUT_BASE, state_alpha)
    os.makedirs(state_dir, exist_ok=True)

    # Write top-level unit: index.json
    with open(os.path.join(state_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(state_data, f, indent=2, ensure_ascii=False)

    # Write second-level units
    for county in counties_by_state.get(state_alpha, []):
        outpath = os.path.join(state_dir, county["filename"])
        with open(outpath, "w", encoding="utf-8") as f:
            json.dump(county["content"], f, indent=2, ensure_ascii=False)
