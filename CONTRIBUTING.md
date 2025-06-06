# Contributing to Administrative Subdivisions of Countries

Thanks for your interest in improving this dataset. This project aims to provide a durable, structured, and verifiable record of administrative subdivisions of countries across time.

## 🧭 Scope and Intent

- The core dataset covers **administrative divisions** above the municipality level for all recognized countries, starting from the foundation of the League of Nations.
- Changes should prioritize **verifiability** and **historical accuracy**.
- This is not a geopolitical advocacy project. Disputes are documented, not resolved.

## 🧩 How to Contribute

1. **Mind the Schema**
   All data must conform to the JSON schema defined in `/schema/country.schema.json`. Use the provided validator tool in `/tools` to check before submitting.
   Schemas may evolve, especially in the early stages. Once stabilized, schema changes that would break existing data or tooling must meet a high bar for necessity and clarity. Contributors are encouraged to propose additions or clarifications rather than fundamental redesigns.

2. **File Placement**
   - Each country has a folder in `/countries/` using its ISO alpha-2 code (lowercase), e.g. `countries/us/`
   - Each country's primary data file is `index.json`.

3. **Meta Sources**
   - If adding or modifying data based on an external source, include the raw source in `/meta/` when possible.
   - Link to the source in the `meta.source` field of the JSON object.

4. **Commits and Pull Requests**
   - Commit messages should be clear and include the country code(s) affected.
   - If you're making historical changes, include the years affected in the PR title or description.

## 📝 Commit Message Conventions

This project uses the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard to make history meaningful, automate changelogs, and enable easier auditing of structural changes (especially over time). All commits should follow this format:

```
<type>(optional scope): <short summary>
[optional body]
[optional footer(s)]
```


### ✅ Common `<type>` Values

| Type         | Purpose                                                                 |
|--------------|-------------------------------------------------------------------------|
| `init`       | initial data population                                                 |
| `feat`       | Incorporating a recent change                                           |
| `fix`        | A correction to data or schema that was previously incorrect            |
| `docs`       | Documentation-only changes                                              |
| `refactor`   | Restructuring data layout or renaming without changing semantics        |
| `chore`      | General tooling, linting, metadata, or automation (no schema/data)      |
| `schema`     | Changes to a schema file                                                |
| `meta`       | Updates to the `_meta` folder, raw source data, or historical context   |
| `test`       | Add or modify a validation or structural test script                    |
| `historical` | Introduce data representing historical context or past configurations   |
| `group`      | Add or modify a group membership definition                             |

> Avoid vague commit types like `update` or `change`. Instead, pick a type that reflects intent and permanence.

---

### 🔒 Enforcing Message Format (Locally)

We use [Commitizen](https://github.com/commitizen-tools/commitizen) to enforce [Conventional Commits](https://www.conventionalcommits.org/) commit message formatting. Install it once per clone:

```bash
make setup-dev
```

To **check your commit messages,** run:

```bash
make check-commits
```

You can also use Commitizen's interactive commit tool (optional, but helpful):

```bash
poetry run cz commit
```

This walks you through a guided prompt for type, scope, and message content.

> **Tip:** Avoid `git commit -m` unless you're confident the message conforms to the project's required format.

## 🚨 Rules

- No unverified changes. Every factual assertion must be traceable to a source.
- All text fields must use **UTF-8 with full Unicode and diacritics preserved**.
- Names must include `en` and `fr` entries at a minimum.
- Avoid duplicating data that can be referenced from standard databases (e.g., link to IANA TZ, don’t copy).

## 📬 Feedback and Feature Requests

Feel free to open issues if you:
- Find an inconsistency
- Want to propose an enhancement (e.g., alternate language coverage, additional metadata)
- Have historical knowledge to contribute

---

We welcome careful, respectful, and well-documented contributions.
