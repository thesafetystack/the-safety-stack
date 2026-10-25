# Overrides

Corrections and other changes applied to dataset releases on top of what the pipeline produced: a fixed annotation
or metadata field, a merged duplicate, a document added by hand, an annotation supplied by another model where the
main annotator's request failed.

For now the override files ship with each release on Hugging Face, under `overrides/`, not here: one JSON Lines file
per overrides run, oldest first, each row with a `kind`. The release's
[overrides/README.md](https://huggingface.co/datasets/thesafetystack/the-safety-stack/blob/main/overrides/README.md)
lists the files with their row counts, authors and methods; the row fields are in the release's
`schema/overrides.schema.json`. Each release's manifest (copies in [../releases/](../releases/)) lists the override
files it includes, and its `SHA256SUMS` gives their sha256. Override files are append-only: a file is never edited
once released; a later change is a new file.
