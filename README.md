# The Safety Stack taxonomies

- Two controlled vocabularies used to annotate documents on AI safety: [techniques](taxonomies/techniques/) (AI-safety
  techniques) and [models](taxonomies/models/) (AI models and their makers).
- Current files: `taxonomies/techniques/techniques-1.0.0.yaml`, `taxonomies/models/models-1.0.0.yaml` (first
  releases; content identical to techniques 0.9.1 and models 0.9.0, which stay for reference).
- Data: the annotated dataset will be on Hugging Face (`thesafetystack/the-safety-stack`) and Zenodo; both pending.
- Validate: `uv run tools/taxonomy-schema-validator.py --all`, or pass file paths. CI runs it on every push and pull
  request.
- Versions: a file is named `<name>-<major>.<minor>.<patch>.yaml`; a released file is never edited, a change is a new
  file with a CHANGELOG entry.
- Tags: the file name without `.yaml` (`techniques-1.0.0`, `models-1.0.0`; earlier `techniques-0.9.1`, `models-0.9.0`).
- Licence: CC BY 4.0 ([LICENSE](LICENSE)), the whole repository.
- Citation: [CITATION.cff](CITATION.cff); DOIs pending.
- Contact: issues on this repository.
