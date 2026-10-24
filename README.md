# The Safety Stack: data

The Safety Stack catalogues public documents about technical AI safety: research papers and preprints, lab safety
frameworks and system cards, evaluation reports, blog and forum posts. Each document is annotated by language models
with the AI-safety techniques it discusses and the AI models it mentions, and how it relates to each (for example,
whether it proposes a technique, evaluates it, or reports that a lab uses it).

<!-- TODO(Tomáš): two or three sentences on what this is not (a catalogue and discovery aid, not a census, map or
verdict on labs or techniques; inclusion is not endorsement), and who runs it, how it is funded, and who decides
inclusion. -->

## What is where

| Where | What |
|---|---|
| This repository (`thesafetystack/data`) | the taxonomies (exact files of every version, schemas, changelogs); the dataset documentation ([dataset/](dataset/)); the corrections and overrides applied to releases ([dataset/overrides/](dataset/overrides/)); the taxonomy validator ([tools/](tools/)); issues for corrections, takedowns and suggestions |
| Hugging Face, `thesafetystack/the-safety-stack` (not yet public) | the dataset itself, one revision per release, with its dataset card |
| [thesafetystack.ai](https://thesafetystack.ai) | the project site |

<!-- TODO(Tomáš): confirm whether the HF dataset also carries copies of the pinned taxonomy files. The internal
variant, thesafetystack/the-safety-stack-private, is not mentioned here on purpose; add it if wanted. -->

The published dataset contains no document texts.

## The dataset

<!-- PLACEHOLDER: filled from dataset/FORMAT.md and dataset/QUALITY.md once they exist. Planned content: number of
documents and annotations in the latest release and its date; the file(s) and a two-line loading example; one real
reviewed row; how well the annotations agree with the reference set (with its limits) and what is known to be
missing. -->

- Format: see [dataset/FORMAT.md](dataset/FORMAT.md). *(placeholder)*
- Quality: see [dataset/QUALITY.md](dataset/QUALITY.md). *(placeholder)*
- Changes between releases: [dataset/CHANGELOG.md](dataset/CHANGELOG.md).

### What is included

*Draft, to be edited.* A document is included when it is publicly available and a language model screening its text
(for some documents only the title and abstract) judged it relevant to at least one of two questions:

- **The Stack question:** does the document carry something about a concrete technique for making a general-purpose
  AI system or agent safer, more honest, more controllable, more transparent or harder to misuse, or for measuring
  any of these? That is: the technique itself (at any maturity); evidence about it (results, failures, replications,
  negative results); evidence that an organisation uses, used or declined it; critique or expert judgement of it; or
  how techniques relate (surveys, taxonomies). A policy document counts only when it names, requires or assesses a
  concrete safeguard.
- **The Shallow Review question:** is the document technical AI safety research in the sense of the Shallow Review
  of Technical AI Safety, a yearly map of the field (work meant to prevent future AI systems from having large
  unintended negative effects), judged by topic and intent? Beyond techniques this covers agent foundations and
  decision theory aimed at AI, model psychology, multi-agent and cooperative AI theory, questions of what AI should be
  aligned to, critiques of the field, and safety and dangerous-capability evaluations. It excludes misuse and access
  controls, conventional security, and policy without a technical proposal.

The screen judges subject matter, not quality: an informal, unreviewed or self-interested source is included if it is
on topic. Documents the screen marked borderline are not included. Out of scope are documents that use the same words
in another field's sense ("alignment" of sequences, "safety" of a drug, "control" of a plant), capability work with no
safety component, and general machine learning.

Candidates come from keyword and author searches of scholarly indexes (OpenAlex, arXiv, Semantic Scholar), the
LessWrong and AI Alignment Forum forums, the blogs of frontier labs and AI-safety organisations, labs' model and system
card pages, a few newsletters, and sources added by hand. Searches reach back to 2015 (forums to 2006). The screen is
a model judgement with known errors in both directions; see [dataset/QUALITY.md](dataset/QUALITY.md). If a work is
missing or should not be here, see [Corrections](#corrections-takedowns-and-missing-works).

## Taxonomies

Two vocabularies, in [taxonomies/](taxonomies/):

- [techniques](taxonomies/techniques/): 234 AI-safety techniques (137 intervention, 32 monitoring, 65 assessment)
  and 9 group nodes. Current version 1.0.0.
- [models](taxonomies/models/): 1,877 AI model families, groups and models, with 138 makers. Current version 1.0.0.

Each version is a separate file, `<name>-<major>.<minor>.<patch>.yaml`, tagged with its file name without `.yaml`
(`techniques-1.0.0`, `models-1.0.0`). A released file is never edited; a change is a new file with a CHANGELOG entry.
From 1.0.0 on:

- Slugs (techniques) and node ids (models) are frozen within a major version: none is removed, merged, split or
  given a different meaning. A minor version may add new ones.
- Definition wording may be clarified in a minor or patch version without changing what it means.
- The definitions (techniques) and glosses (models) in a released file are the text the annotation model was shown
  when annotating with that version.

The 0.x files (techniques 0.9.1, models 0.9.0) stay for reference and carry no such guarantee. Check a file with
`uv run tools/taxonomy-schema-validator.py --all`; CI runs it on every push and pull request.

## Releases

Dataset releases are dated (`YYYY-MM-DD`) and planned weekly. Each release records:

- the taxonomy versions its annotations use, each with the sha256 of its file in this repository;
- the override files from [dataset/overrides/](dataset/overrides/) it applies, each with its sha256.

So for any release one can recover exactly which taxonomy files and which corrections went into it. There is no DOI
per release; a Zenodo record for the dataset series is planned.

<!-- TODO: where the release manifest lives (HF only, or also a copy here) and how a reader finds it; FORMAT.md. -->

## Licences

| What | Licence |
|---|---|
| Taxonomies, schemas, documentation and override files in this repository (everything outside `tools/`) | [CC0 1.0](LICENSE) |
| Dataset metadata and annotations (Hugging Face) | CC0 1.0 |
| Code in `tools/` | [MIT](tools/LICENSE) |
| Evidence quotes in the dataset | not covered by CC0: short excerpts from the documents, whose rights stay with their authors and publishers |

CC0 means no conditions; a citation is still appreciated.

## Corrections, takedowns and missing works

Use the issue forms on this repository ([new issue](https://github.com/thesafetystack/data/issues/new/choose)):

- **Correction**: an annotation or a metadata field is wrong.
- **Takedown**: you want a document, or your name, removed.
- **Missing work**: a document that fits the criterion above is not in the dataset.
- **Taxonomy suggestion**: a missing technique or model, a wrong definition, a merge or split.

<!-- TODO(Tomáš): a private contact (email) for takedowns that should not be posted publicly. -->
For a takedown you would rather not post publicly, write to *[private contact, to be added]*.

We acknowledge every report; we do not promise a date for resolving it. Accepted corrections and takedowns are
applied in the next release as override files ([dataset/overrides/](dataset/overrides/)). See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

For the taxonomies: [CITATION.cff](CITATION.cff) (GitHub shows it as "Cite this repository").

<!-- PLACEHOLDER: how to cite the dataset (Hugging Face dataset and release date; later the Zenodo concept DOI). -->
For the dataset: *[to be added]*.
