# The Safety Stack: data

The Safety Stack is a planned catalogue of AI safety techniques. Frontier labs describe their safety approach as
defence in depth: a stack of techniques at every layer from data collection to deployment. No single resource collects
them. For each technique the catalogue is to gather the papers, evidence of effectiveness and cost, implementations,
and what is known about its deployment across labs and models, including informal sources (expert opinions,
forecasts, compliance filings) labelled as such, and to record what was looked for and not found. The project builds
on the Shallow Review of Technical AI Safety and is meant to supply data for its 2026 edition. Project page:
[The AI Safety Stack on Manifund](https://manifund.org/projects/the-ai-safety-stack).

- **For:** safety researchers getting oriented in the field; funders looking for neglected work and expert opinion;
  evaluators and policy analysts who need an overview of the stack and an index of sources.
- **Not for:** tracking individuals beyond paper authorship; judging or ranking labs' safety efforts; calls to action
  other than research recommendations.
- **Team:** Tomáš Gavenčiak (lead; Alignment of Complex Systems group, Charles University, Prague; Arb Research),
  Jacob Livingston Slosser (Pioneer Centre for AI, University of Copenhagen; CheatSheet; Juriscription), Dan Elton
  (Metascience Observatory), Gavin Leech (advisor; Arb Research).

### This release

The dataset is one deliverable of the project. Release 2026-10-25, the first, has 39,269 public documents on
technical AI safety (preprints and papers, LessWrong and Alignment Forum posts, lab blog posts, system and model
cards), each annotated by a language model with which of the 234 techniques of the techniques taxonomy it engages with
and in what role (uses, evaluates, proposes, critiques, reports a lab using it), which of the 1,877 AI models of the
models catalogue it names and in what role, its document class, and, where a full text was available, its authors'
affiliations. The taxonomies, the prompts and per-field provenance ship with the data.

It is not the catalogue: there are no per-technique summaries of evidence and no deployment status yet. It is not a
census: the relevance screen misses relevant documents and lets some irrelevant ones in. The annotations are
model-made and not systematically reviewed by people (a few hundred rows were corrected by the maintainers; the
override files say which and how); they record what a document says, not whether it is true. Inclusion is not
endorsement, and nothing here is a verdict on a lab or a technique.

## What is where

| Where | What |
|---|---|
| This repository (`thesafetystack/data`) | the taxonomies (exact files of every version, schemas, changelogs); copies of each release's documentation ([dataset/](dataset/)) and manifest ([dataset/releases/](dataset/releases/)); the taxonomy validator ([tools/](tools/)); issue forms for corrections, takedowns and suggestions |
| [Hugging Face, `thesafetystack/the-safety-stack`](https://huggingface.co/datasets/thesafetystack/the-safety-stack) | the dataset: data files, dataset card, the taxonomy files and prompts used, the override files applied, the manifest; one revision per release |
| [thesafetystack.ai](https://thesafetystack.ai) | the project site |

Neither this repository nor the Hugging Face dataset is public yet.

The published dataset contains no document texts and, in this release, no abstracts. An internal variant with
abstracts and full texts exists for the maintainers and is not distributed.

## The dataset

The [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is the place to start; it
describes the files and how to load them.

```python
from datasets import load_dataset
docs = load_dataset("thesafetystack/the-safety-stack", "documents", split="train")   # flat view, one row per document
rlhf = docs.filter(lambda r: "rlhf" in (r["techniques_used"] or []))
corpus = load_dataset("thesafetystack/the-safety-stack", "corpus", split="train")    # the full row with every annotation
```

- **Format:** [dataset/FORMAT.md](dataset/FORMAT.md) (files, columns, ids, recipes) and
  [dataset/VOCAB.md](dataset/VOCAB.md) (every value word with a sentence).
- **Quality:** against a model-made reference set of 100 documents, with no human adjudication yet, the technique
  annotation finds about 7 in 10 reference techniques (presence F1 0.78) and the model annotation reaches presence
  F1 0.92. The 21 stand-in annotations (17 documents) and the relevance screen were not evaluated. Details and limits:
  [dataset/QUALITY.md](dataset/QUALITY.md).
- **Changes between releases:** [dataset/CHANGELOG.md](dataset/CHANGELOG.md).

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

Dataset releases are dated (`YYYY-MM-DD`) and planned weekly. Each release's manifest, `release.json`, records the
build, row counts, the taxonomy versions its annotations use (each with the sha256 of its file, the same file as in
this repository), the override files it applies, and every file with its size and sha256. A copy of each manifest and
its `SHA256SUMS` is kept in [dataset/releases/](dataset/releases/), so it stays clear what each release contained.
There is no DOI per release; a Zenodo record for the dataset series is planned.

## Licences

| What | Licence |
|---|---|
| Taxonomies, schemas and documentation in this repository (everything outside `tools/`) | [CC0 1.0](LICENSE) |
| What we made in the dataset: the annotations, the identity and provenance structure, the release metadata, the prompts and documentation | CC0 1.0 |
| Bibliographic records in the dataset (titles, authors, dates, identifiers) | as their providers supply them, under those providers' terms |
| Quoted document text in the dataset (evidence quotes) | its owners'; not covered by CC0 |
| Code in `tools/` | [MIT](tools/LICENSE) |

CC0 means no conditions; a citation is still appreciated.

Before release 1 this repository stated CC BY 4.0; the commits tagged `techniques-0.9.1`, `techniques-1.0.0`,
`models-0.9.0` and `models-1.0.0` still carry that LICENSE file. The same taxonomy files are now CC0 1.0.

## Corrections, takedowns and missing works

- **Takedowns and other private requests:** email [info@thesafetystack.ai](mailto:info@thesafetystack.ai), for
  example to have a document, or your name, removed.
- **Public reports:** use the issue forms on this repository
  ([new issue](https://github.com/thesafetystack/data/issues/new/choose)):
  - **Correction**: an annotation or a metadata field is wrong.
  - **Missing work**: a document that fits the criterion above is not in the dataset.
  - **Taxonomy suggestion**: a missing technique or model, a wrong definition, a merge or split.
  - **Takedown**, if you are fine asking in public.

We acknowledge every report; we do not promise a date for resolving it. Accepted corrections and takedowns are
applied in the next release as override files, which ship with the release on Hugging Face
([dataset/overrides/](dataset/overrides/)). See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

For the dataset, as on the card: The Safety Stack dataset, release 2026-10-25,
https://huggingface.co/datasets/thesafetystack/the-safety-stack.

For the taxonomies: [CITATION.cff](CITATION.cff) (GitHub shows it as "Cite this repository").
