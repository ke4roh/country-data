This directory provides source material for French administrative divisions.

The file `departements.json` was downloaded from [geo.api.gouv.fr](https://geo.api.gouv.fr/departements) on 2025‑07‑05. It lists each department with its INSEE code and associated region code. Data from this API is published under the [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence).

The script `make_departments.py` converts `departements.json` into the folder structure under `countries/fr/`.
