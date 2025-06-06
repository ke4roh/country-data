# Country Data

> *A durable, verifiable, and time-aware ledger of the world’s political subdivisions—past and present.*

---

## 🌍 Purpose

This project aims to document the administrative subdivisions of countries over time in a machine- and human-readable format. It includes changes in boundaries, status, and jurisdiction at the level **just above cities and municipalities**, from the early 20th century to the present day.

We focus on **verifiable records**, **historical fidelity**, and **interoperability** with systems like ISO 3166-2, Wikidata, and the IANA time zone database. The eventual goal is a complete, queryable catalog of the world’s administrative layers from **the founding of the League of Nations onward**.

---

## 🕯️ In Tribute to Gwillim Law

This project is inspired by and stands in tribute to the work of **Gwillim Law (1943–2016)**, author of *Administrative Subdivisions of Countries* and creator of [Statoids.com](http://www.statoids.com). His meticulous, quiet stewardship of geopolitical truth has served countless researchers, developers, and logistics systems over the decades.

Whether or not this dataset directly builds upon his, it **continues in his spirit**—of careful citation, structured documentation, and global respect.

---

## 🔍 Project Principles

- **Verifiability:** Every record must be traceable to a public, official, or scholarly source.
- **Temporal Integrity:** Changes must be tagged with start and end dates (or open-ended).
- **Minimal Bias:** We document claims, not make them. Disputed territories are recorded as such.
- **Clarity Over Completeness:** Better to be correct for a few countries than sloppy for the world.

---

## 📁 Project Structure

- `countries/` — Organized by continent → country → subdivision
- `meta/` — Raw content and scripts for translating it into standard format
- `schema/` — JSON Schemas defining data formats
- `tools/` — Scripts for validation and snapshot generation

Example:
```
countries/
us/
co/
broomfield.json
```

## 📜 License

Content is licensed under **Creative Commons Attribution-ShareAlike 4.0 (CC-BY-SA 4.0)**.

---

## 🤝 Contributing

We welcome contributors who value precision and citation.

### You can:
- Propose new subdivisions or corrections (with sources)
- Add historical entries (e.g., Yugoslavia, USSR)
- Submit a changelog entry in `timeline/changes.csv`

### Guidelines:
- Use ISO codes where possible (`US`, `FR`, `JP`)
- Include `valid_from` and `valid_to` dates
- Link to government gazettes, census bureaus, or scholarly sources
- Use UTF-8 Unicode (with diacritics where appropriate)
- PRs should update the relevant JSON + changelog entry

---

## 📬 Contact & Coordination

If you'd like to help coordinate or mirror this project (e.g. on Wikidata or OpenStreetMap), please open an issue or contact the maintainer.
