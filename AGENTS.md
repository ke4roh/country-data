This is instructions for bots (or people who like things really clear).

To add administrative subdivisions for a country to the repository:
- Fetch data from an official source (e.g., geo.api.gouv.fr) for administrative subdivisions down to above the city level.  note the license.
- Provide a script to convert that dataset to our `countries/XX/*/index.json` format.  Rather than creating a leaf index.json in its own folder, create [name].json in what would be its parent.  For example `countries/US/NC/Wake.json`  `tools/flatten_leaves.py` can be used to make that process easier.  This is important because it reduces the number of `stat(2)` calls for repo operations and traversal of the tree.
- Update or create a README under `meta/countries/XX` with source and licensing details.
- Ensure all JSON files pass `tools/validate_all.py`.

For all changes:
- Ensure the commit message comports with the standards set forth for commitizen in pyproject.toml.
