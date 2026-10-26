> Copied from release 2026-10-26 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# Changelog

## 2026-10-26

- The two flat views (`views/documents.parquet`, `views/annotation_records.parquet`) are dropped; `data/corpus.parquet`
  is the hub's default configuration. FORMAT.md has recipes for flat tables built from it.
- QUALITY.md adds a judge evaluation of every model judgement (triage, relevance screen, affiliations, models,
  techniques): three language-model judges, production scored against their majority and against the agreement of
  two of them; the reference-set numbers are unchanged. The card summarises both.

## Release 1 (2026-10-25)

- First release. One row per screen-relevant document; annotations as one typed column per kind
  (`annotations.<kind>` = `{metadata, payload}`), with the metadata struct shared by every kind.
- Public variant: abstracts withheld pending a per-supplier rights review; quotes and verbatim surfaces cut to 300
  characters at a word boundary (`release.cuts`); no document text.
- The 17 documents for which the main annotator's request was refused carry stand-in annotations by Claude models
  (21 annotations; `provenance = override`).
