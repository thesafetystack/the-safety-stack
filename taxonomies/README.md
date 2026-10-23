# Taxonomies

- `techniques/`: AI-safety techniques (intervention, monitoring, assessment) and group nodes.
- `models/`: AI model families, groups and models, with their makers.
- Layout: `<name>/<name>-<major>.<minor>.<patch>.yaml` per version, `<name>/CHANGELOG.md`, `<name>/README.md`.
- Schemas: `<name>/schemas/<name>-<major>.schema.json`, one JSON Schema per major version; the validator picks it
  from the file name.
