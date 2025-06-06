import json
import os
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, exceptions

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "country.json"
DATA_ROOT = Path(__file__).resolve().parent.parent / "data"

def load_schema(schema_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_country_files(data_root):
    for root, dirs, files in os.walk(data_root):
        for file in files:
            if file.endswith(".json"):
                yield Path(root) / file

def validate_country_file(validator, path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if errors:
                print(f"❌ {path}:")
                for err in errors:
                    loc = ".".join([str(p) for p in err.path])
                    print(f"  - {loc}: {err.message}")
            else:
                print(f"✅ {path}")
        except json.JSONDecodeError as e:
            print(f"❌ {path} — JSON parse error: {e}")

def main():
    schema = load_schema(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    print("Validating country files...\n")

    for path in find_country_files(DATA_ROOT):
        validate_country_file(validator, path)

if __name__ == "__main__":
    main()
