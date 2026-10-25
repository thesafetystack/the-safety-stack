> Copied from release 2026-10-25 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# Changelog

## Release 1

- First release. One row per screen-relevant document; annotations as one typed column per kind
  (`annotations.<kind>` = `{metadata, payload}`), with the metadata struct shared by every kind.
- Public variant: abstracts withheld pending a per-supplier rights review; quotes and verbatim surfaces cut to 300
  characters at a word boundary (`release.cuts`); no document text.
- The 17 documents for which the main annotator's request was refused carry stand-in annotations by Claude models
  (21 annotations; `provenance = override`).
