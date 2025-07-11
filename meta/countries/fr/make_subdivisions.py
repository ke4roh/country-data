import json
import os
from pathlib import Path

# Load source data
with open('regions.json', encoding='utf-8') as f:
    regions = json.load(f)
with open('departments.json', encoding='utf-8') as f:
    departments = json.load(f)

base_path = Path('../../..') / 'countries' / 'fr'

# Normalize function
def normalize(name: str) -> str:
    return (
        name.lower()
        .replace(' ', '_')
        .replace("'", '')
        .replace('-', '_')
        .replace('.', '')
        .replace(',', '')
    )

# Map of region code to normalized name
region_map = {}

for region in regions:
    code = region['code']
    name = region['nom']
    norm = normalize(name)
    region_map[code] = norm
    dir_path = base_path / norm
    os.makedirs(dir_path, exist_ok=True)
    data = {
        'type': 'region',
        'name': {'fr': name, 'en': name},
        'alternate_names': [],
        'valid_from': None,
        'valid_to': None,
        'parent_id': 'fr',
        'admin_level': 1,
        'local_code': code,
        'meta': {}
    }
    with open(dir_path / 'index.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

for dept in departments:
    code = dept['code']
    name = dept['nom']
    region_code = dept['codeRegion']
    region_norm = region_map.get(region_code)
    if not region_norm:
        continue
    file_name = normalize(name) + '.json'
    data = {
        'type': 'department',
        'name': {'fr': name, 'en': name},
        'alternate_names': [],
        'valid_from': None,
        'valid_to': None,
        'parent_id': f'fr/{region_norm}',
        'admin_level': 2,
        'local_code': code,
        'meta': {'region_code': region_code}
    }
    with open(base_path / region_norm / file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
print('Subdivisions generated.')
