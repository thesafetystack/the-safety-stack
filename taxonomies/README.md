# Taxonomies

- `techniques/`: AI-safety techniques (intervention, monitoring, assessment) and group nodes.
- `models/`: AI model families, groups and models, with their makers.
- Layout: `<name>/<name>-<major>.<minor>.<patch>.yaml` per version, `<name>/CHANGELOG.md`, `<name>/README.md`.
- Schemas: `<name>/schemas/<name>-<major>.schema.json`, one JSON Schema per major version; the validator picks it
  from the file name.

## Versioning

- A released file is never edited; a change is a new file with a CHANGELOG entry. Each file has an annotated tag,
  its file name without `.yaml`.
- From 1.0.0 on, identifiers (technique and group-node slugs, model node ids) are frozen within a major version:
  none is removed, merged, split or given a different meaning. A minor version may add new identifiers.
- Definition wording (technique and group-node `definition`, model `gloss`) may be clarified in a minor or patch
  version without changing what it means. Anything that changes the meaning of an existing identifier needs a new
  major version.
- The definitions and glosses in a released file are the text the annotation model was shown when annotating with
  that version. A dataset release records which version of each taxonomy it used, with the file's sha256.
- 0.x versions (techniques 0.9.1, models 0.9.0) stay for reference and carry none of these guarantees.
