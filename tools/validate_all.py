import os
import json
import jsonschema
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = PROJECT_ROOT / "schema"
DATA_DIR = PROJECT_ROOT / "countries"

def load_schema(schema_name):
    schema_path = SCHEMA_DIR / schema_name
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    resolver = jsonschema.RefResolver(
        base_uri=f"file://{SCHEMA_DIR.as_posix()}/",
        referrer=schema
    )
    return schema, resolver

def validate_file(filepath, schema, resolver):
    with open(filepath, encoding="utf-8") as f:
        instance = json.load(f)
    jsonschema.validate(instance=instance, schema=schema, resolver=resolver)

def determine_schema(file_path):
    relative_parts = file_path.relative_to(DATA_DIR).parts
    if len(relative_parts) == 2:
        return "country.json"
    else:
        return "subdivision.json"

def main():
    counter=0
    failures = []
    for json_path in DATA_DIR.rglob("*.json"):
        schema_file = determine_schema(json_path)
        schema, resolver = load_schema(schema_file)
        try:
            validate_file(json_path, schema, resolver)
            counter = counter + 1
        except jsonschema.ValidationError as e:
            failures.append((json_path, e.message))

    if failures:
        for path, msg in failures:
            print(f"❌ {path}:\n  - {msg}")
        exit(1)
    else:
        print(f"✅ All {counter} JSON files are valid.")

if __name__ == "__main__":
    main()
