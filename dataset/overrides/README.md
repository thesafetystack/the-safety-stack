# Overrides

Corrections and other changes applied to dataset releases on top of what the pipeline produced: a fixed annotation
or metadata field, a withdrawn document, a document added by hand, an annotation supplied by hand or by another model
where the pipeline's annotator failed.

- One file per correction or override run. Files are append-only: a file is never edited or deleted once added; a
  later change is a new file.
- Each row has a `kind` that says what it does. The kinds, the other fields and the file format are defined in
  [../FORMAT.md](../FORMAT.md#override-files).
- Each release lists the override files it includes, each with its sha256, so it is clear afterwards exactly which
  rows went into which release.

<!-- TODO: file naming (e.g. YYYY-MM-DD-<short-name>.<ext>) once the format is fixed. -->
