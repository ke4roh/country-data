# ISO 3166 Data Import – Snapshot 2025-06-05

This folder contains a snapshot of ISO 3166-1 data as captured on 2025-06-05,
used to populate the initial set of 249 top-level country entries in `data/`.

## Files
- `source.json` – Raw JSON payload from https://www.iso.org/obp/ui/#search/code/ (formatted for clarity only)
- `generate_country_json.py` – Python script used to extract fields and write `index.json` files
- `README.md` – This explanation

## Notes
- The `generate.py` script assumes this file structure and creates/updates `data/<country>/index.json` entries.
- The raw file is unmodified from the request except for line formatting.
- See Git commit history for origin and applied results.

## License
This data was sourced from iso.org for internal transformation. 
All identifiers (e.g., alpha-2, alpha-3, numeric codes) are public facts. 
The input data is preserved for reproducibility; no claim of copyright is made.

This snapshot and generated output are published under CC-BY-SA 4.0.
