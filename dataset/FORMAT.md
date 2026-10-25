> Copied from release 2026-10-25 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# The Safety Stack: file format

One parquet file, `data/corpus.parquet`, one row per document, is the dataset; the other files resolve the ids its
rows carry or offer flatter views of it. The sections up to "Rules a reader should know" are written for people;
everything after "Generated reference" is generated from the release itself (`schema/mapping.yaml` describes every
field and how it is derived) and is meant to be searched, not read.

An internal variant with abstracts and full texts exists for the maintainers and is not distributed.

## Files

| Path | Rows | What |
|---|---|---|
| `data/corpus.parquet` | 39,269 | The full row per document: bibliographic fields, identity, content identifiers, release facts and every annotation (nested). The contract; everything else is derived from it or resolves its ids. |
| `views/documents.parquet` | 39,269 | A flat view, one row per document: bibliographic fields, the screen verdicts, technique and model lists, affiliations (columns below). The HF viewer's default; for browsing and simple filters. |
| `views/annotation_records.parquet` | 338,907 | Long view: release_id, doc_id and the metadata struct of every annotation, one row per document and kind. For coverage and provenance (override) queries across kinds. |
| `data/configs.parquet` | 26 | One row per config_id: the call that produced annotations (stage, prompt, model, parameters, taxonomy pin) or the overrides that supplied them. configs.json is the same as JSON. |
| `configs.json` |  | data/configs.parquet as JSON. |
| `overrides/` | 269 | The maintainers' and stand-in overrides of the pipeline's output, one JSON Lines file per overrides run (overrides/README.md lists them): kind, target, key, value, author, method, note, time. |
| `remap.jsonl` | 12 | Every value this release changed from the pipeline's (status remap), one line each: doc_id, kind, field, old, new, rule, reason. |
| `annotations.yaml` |  | The annotation kinds: internal workflow name, version, producing call, payload and record schema, capped and prose paths, config_ids. |
| `vocab.yaml` |  | A sentence for every value word that occurs in this release (VOCAB.md renders it). |
| `VOCAB.md` |  | vocab.yaml rendered. |
| `taxonomies/` |  | The techniques taxonomy and the models catalogue the annotations were graded against (byte-identical to the pinned versions; sha256 in release.json). |
| `prompts/` |  | The production prompt files as run, with the rubrics they include (their digests are in data/configs.parquet); including the pipeline's own header comments. |
| `schema/` |  | mapping.yaml (every field, its source and description), the arrow schema (row.arrow, row.arrow.txt), JSON Schemas of the row, of each kind's payload (payloads/) and annotation record (records/), of the overrides lines and the configs rows. |
| `examples/rows.json` |  | Four complete rows, pretty-printed: a preprint with every kind, a forum post, a corrected screen verdict, and a document whose model annotation is a stand-in. |
| `FORMAT.md` |  | This format description. |
| `README.md` |  | The dataset card. |
| `QUALITY.md` |  | How well the annotations agree with a model-made reference set. |
| `CHANGELOG.md` |  | Changes between releases. |
| `LICENSE` |  | CC0 1.0 for our annotations and documentation, with the third-party carve-outs. |
| `release.json` |  | The manifest: every file with its size and sha256, row counts, the build, the policy. |
| `SHA256SUMS` |  | sha256 of every file (sha256sum -c). |

**Which file to open.** `views/documents.parquet` for browsing and filters on labels (the HF viewer's default);
`data/corpus.parquet` for roles, quotes, provenance and everything else; `views/annotation_records.parquet` for
coverage and override audits across kinds.

### `views/documents.parquet`, column by column

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Document id (as in data/corpus.parquet). |
| `release_id` | string | Release this row comes from. |
| `title` | string | Title. |
| `abstract` | string | Abstract (NULL where this variant withholds abstracts; see release.abstract in the corpus). |
| `authors` | list<string> | Author names in byline order. |
| `published_date` | date | Publication date. |
| `published_precision` | string | day, year_inferred (a 1 January placeholder for a year-only date) or unknown. |
| `doc_type` | string | Document type from the providers. |
| `canonical_url` | string | The anchor source's canonical URL. |
| `stack_relevance` | string | Verdict of the Safety Stack question (relevant, borderline, irrelevant). |
| `shallow_review_relevance` | string | Verdict of the Shallow Review question (relevant, borderline, irrelevant). |
| `shallow_review_category` | string | Shallow Review top-level category the screen assigned. |
| `doc_class` | string | Document type read from the text by the screen call. |
| `text_usability` | string | Whether the converted text is usable as the document body (usable, degraded, unusable). |
| `techniques_status` | string | Status of the technique annotation (ok, empty, ...; NULL if not run). |
| `techniques` | list<string> | Every taxonomy slug the technique annotation lists for the document (any role, any strength >= 1). |
| `techniques_used` | list<string> | Slugs with role `used` >= 2 (the document's own work uses the technique, at least a paragraph's worth). |
| `techniques_evaluated` | list<string> | Slugs with role `evaluated` >= 2. |
| `techniques_introduced` | list<string> | Slugs with role `introduced` >= 2 (the document proposes the technique). |
| `models_status` | string | Status of the model annotation (ok, empty, ...). |
| `models` | list<string> | Catalogue models with any role >= 1 (the document engages with the model at least in a sentence). |
| `model_candidates` | list<string> | Every catalogue model the name matcher found, judged, including rows with every role 0: the list to use for "is model X named in this document" (QUALITY.md). |
| `affiliation_orgs` | list<string> | Organisation slugs of the authors' affiliations (paper-type documents with full text only; NULL otherwise). |
| `overridden` | list<string> | Kinds whose annotation was changed or supplied by an override (provenance mixed or override); [] for none. |
| `text_role` | string | Kind of content the annotations read (full_text, html, post, page, xml). |
| `text_bytes` | int64 | Size of the converted text in bytes. |
| `quote_chars` | int32 | Characters of quoted document text in the row's annotations. |

### `views/annotation_records.parquet`

One row per document and annotation kind: `release_id`, `doc_id`, then the metadata struct of that kind's record
flattened (`kind`, `version`, `status`, `error_class`, `config_id`, `decided_at`, `origin`, `annotator`,
`provenance`, `override_ids`, `override_fields`; defined under "the metadata struct" below). A kind not run for a
document has no row.

## The row in one screen

- **Bibliographic columns**: `doc_id`, `title`, `abstract` (`release.abstract` says whether it is shipped, withheld
  or never existed), `authors[]`, `published_date` with `published_precision`
  (`day`, `year_inferred` for the providers' 1 January placeholders, `unknown`), `doc_type`, `is_withdrawn`,
  `canonical_url`, `field_sources[]` (which source supplied each field).
- **`identity`**: the source records (`members[]`) merged into the document and every external id (`keys[]`: arXiv,
  DOI, OpenAlex, Semantic Scholar, forum post ids, URLs). Look a paper up by its arXiv id or DOI here.
- **`content`**: what was annotated, as identifiers: the fetched file (`content.source`: url, sha256, bytes, media
  type, time) and our Markdown conversion of it (`content.text`: sha256, bytes, converter, body). `content.text.body`
  holds the text only where `release.text = inline`; it is NULL where texts are not distributed.
- **`release`**: what this release did to the row: abstract policy, text policy, `quote_chars` (characters of quoted
  document text in the row) and `cuts[]` (every quote or surface shortened to the cap).
- **`annotations`**: one column per kind, each `{metadata, payload}`; NULL when the kind was not run for the
  document. `metadata` is the same struct in every kind: `kind`, `version`, `status`, `error_class`, `config_id`
  (resolved by `data/configs.parquet`), `decided_at`, `origin`, `annotator`, `provenance`, `override_ids`,
  `override_fields`. Kinds: `screen` (the call-level relevance verdict), `stack_relevance` and
  `shallow_review_relevance` (its two questions), `text_usability`, `doc_class` (all five from one call),
  `affiliation`, `safety_techniques` (techniques of the taxonomy with 12 role strengths 0-4), `model_roles` (AI
  models of the catalogue with 10 role strengths 0-4) and `model_name_matches` (the deterministic name matcher's raw
  hits, a record of the model_roles call). `annotations.other[]` is reserved for kinds without a typed column (empty).

All annotations are made by language models (and a deterministic matcher) and are not systematically reviewed by
people; a few hundred rows were corrected or added by the maintainers through overrides (`metadata.provenance`, the
`overrides/` files, whose `method` says how each was prepared). For 17 documents whose main-model request was
refused, the technique and/or model annotation is a stand-in by a Claude model (`annotator`, `provenance =
override`). Annotations record what a document says, not whether it is true. `QUALITY.md` reports how well they
agree with a model-made reference set.

## Ids and where they resolve

| In the row | Resolves via | To |
|---|---|---|
| `annotations.<kind>.metadata.config_id` | `data/configs.parquet` (`configs.json`) | the producing call: stage, prompt (file in `prompts/`), model and parameters, taxonomy pin, the pipeline's config digest |
| `...metadata.override_ids`, `identity.override_ids`, `identity.members[].override_id` | `overrides/*.jsonl` | kind, author, method, note, value, time of each override |
| `annotations.<kind>.metadata.kind`, `version` | `annotations.yaml`, `schema/payloads/` | the kind's producing call, payload schema, capped paths |
| `safety_techniques.payload.techniques[].slug`, `model_roles.payload.models[].node_id` | `taxonomies/` | the techniques taxonomy and the models catalogue |
| `content.text.sha256` | `content.text.body` (where `release.text = inline`) | the converted text the annotations judged |
| every value word | `vocab.yaml` (rendered at the end of this file) | one sentence each |

## Recipes

duckdb (the file is `d`):

```sql
CREATE VIEW d AS SELECT * FROM 'data/corpus.parquet';
-- documents where technique X is used with strength >= 3
SELECT doc_id, title FROM d, unnest(annotations.safety_techniques.payload.techniques) AS u(t)
WHERE t.slug = 'rlhf' AND t.roles.used >= 3;
-- models with any role in one document
SELECT m.node_id, m.roles FROM d, unnest(annotations.model_roles.payload.models) AS u(m)
WHERE doc_id = 'ssepg4p9vmv5w' AND m.roles.mentioned > 0;
-- coverage: every kind and status (the long view does this in one pass)
SELECT kind, status, count(*) FROM 'views/annotation_records.parquet' GROUP BY ALL ORDER BY ALL;
-- the same from the main file, for one kind
SELECT annotations.model_roles.metadata.status, count(*) FROM d GROUP BY ALL;
-- records changed or supplied by overrides
SELECT kind, provenance, config_id, count(*) FROM 'views/annotation_records.parquet'
WHERE provenance <> 'pipeline' GROUP BY ALL;
-- look a paper up by arXiv id
SELECT DISTINCT doc_id, title FROM d, unnest(identity.keys) AS u(k) WHERE k.kind = 'arxiv' AND k.value = '2310.10659';
```

polars:

```python
import polars as pl
d = pl.read_parquet("data/corpus.parquet")
techniques = (d.select("doc_id", pl.col("annotations").struct.field("safety_techniques").struct.field("payload")
                       .struct.field("techniques").alias("t"))
               .explode("t").unnest("t"))
used = techniques.filter((pl.col("slug") == "rlhf") & (pl.col("roles").struct.field("used") >= 3))
```

pandas (nested columns arrive as Python dicts and lists):

```python
import pandas as pd
d = pd.read_parquet("data/corpus.parquet")
st = d["annotations"].map(lambda a: a["safety_techniques"])
rows = [(doc, t["slug"], t["roles"]["used"]) for doc, a in zip(d["doc_id"], st) if a and a["payload"]["techniques"] is not None
        for t in a["payload"]["techniques"]]
techniques = pd.DataFrame(rows, columns=["doc_id", "slug", "used"])
```

Hugging Face `datasets`, from a local copy (the `documents` config is the flat view; `corpus` is the full row; the
card shows the same from the hub):

```python
from datasets import load_dataset
docs = load_dataset("parquet", data_files="views/documents.parquet", split="train")
corpus = load_dataset("parquet", data_files="data/corpus.parquet", split="train")
```

## Rules a reader should know

- **Not run vs failed vs empty.** `annotations.<kind>` NULL = the kind was not run for the document (affiliation runs
  only on paper-type documents with full text). `status = failed_permanent` = it was asked and no answer exists (the
  payload's lists are NULL; `error_class` says why). `status = empty` = decided, no positive label.
- **One call, several kinds.** The five screen kinds share `config_id` and `decided_at`; so do `model_roles` and
  `model_name_matches` (whose `annotator` is `matcher`), except where an override replaced the model_roles answer:
  the matcher record then keeps the original call's metadata (and, where that call failed, has no hits).
- **Provenance.** `pipeline` = the model's answer as produced; `mixed` = an override changed fields of it
  (`override_fields`), while `config_id`, `annotator`, `confidence` and the reasoning still describe the model's own
  answer; `override` = overrides supplied the whole payload (`config_id = override:<ids>`; the 21 stand-ins by Claude
  models are of this kind, with `annotator` naming the model and `decided_at` the time the override was added).
  `origin = human` marks a maintainers' override, not necessarily a per-item human review.
- **Candidates vs roles.** `model_roles.payload.models[]` lists every catalogue model the matcher found, including
  rows with every role 0 (flags usually say why; see the known inconsistencies). "Named in the document" = those rows minus `matcher_fp:` flags; "plays a
  role" = some role >= 1.
- **Strengths are prominence, not importance or confidence**: 0 absent, 1 a sentence, 2 a paragraph, 3 a main
  thread, 4 the document's headline for that role.
- **Quotes** are verbatim from our conversion of the document. Where the release caps quotes (`release.json`
  `policy.quote_cap_chars`), a quote or surface longer than 300 characters is cut at a word boundary and ends with `…` (listed in `release.cuts`); `anchored` and `offset`
  describe the original excerpt. Model-written text (reasoning, notes, glosses) is never cut. Quotes are the
  documents' owners' text, not covered by CC0.
- **Prompts** in `prompts/` are the production files as run, including the pipeline's own header comments; their
  digests are in `data/configs.parquet`.
- **The release is a projection.** A few statuses differ from the pipeline's on purpose (the status remap, listed
  line by line in `remap.jsonl`).
- **Stacking releases.** Every row of the corpus and of both views carries `release_id`; files of different releases
  can be concatenated.

## Generated reference (search, don't read)

Generated from `schema/mapping.yaml` and the data of release `2026-10-25`. Enumerated fields list the values that occur in this release; values defined but not used here are listed as reserved. Every value word has a sentence in [VOCAB.md](VOCAB.md).

### Top-level columns

| Field | Type | Nullable | Description |
|---|---|---|---|
| `release_id` | string | no | Release this row comes from (the export's date, e.g. 2026-10-25). Constant within a file; keeps rows self-identifying when releases are stacked. Also in the parquet file metadata and release.json. |
| `doc_id` | string | no | Document id (13 lowercase alphanumerics). Stable across releases; a merged document keeps the surviving id and lists the others in identity.former_doc_ids. |
| `title` | string | yes | Title (merged; field_sources says which source supplied it). |
| `abstract` | string | yes | Abstract or opening excerpt as a source supplied it. NULL in the public variant (release.abstract = withheld_pending_rights_review) and where none exists (none). Third-party text. |
| `authors[]` | list<struct> | yes | Byline authors in order, from the supplying source. |
| `authors[].name` | string | no | Author name as supplied. |
| `authors[].orcid` | string | yes | ORCID when the provider gives one. |
| `authors[].affiliation_raw` | string | yes | Affiliation string from the provider (OpenAlex institution name). Text-derived affiliations are the `affiliation` annotation. |
| `published_date` | date | yes | Publication date (the merged metadata.published_at, a UTC timestamp internally, as a date). See published_precision; the supplying source is field_sources[field = published_at]; per-source dates are identity.members[].published_at. |
| `published_precision` | string | no | How precise published_date is: `unknown` = no date; `year_inferred` = the date is exactly midnight UTC on 1 January, the providers' placeholder for a year-only date (a genuine midnight-1-January date is marked the same); `day` otherwise. Values: `day`, `year_inferred`, `unknown`. |
| `doc_type` | string | yes | Document type from the providers. Two model-assigned types also exist (annotations.doc_class.payload.doc_type from the screen call; doc_kind of safety_techniques and model_roles from the rubrics' own list of document kinds); vocab.yaml lists all three. Values: `preprint`, `paper`, `conference`, `journal`, `forum_post`, `lab_blog`, `system_card`, `model_card`, `framework_policy`, `book`, `other`. |
| `is_withdrawn` | bool | no | A source reports the work withdrawn. |
| `canonical_url` | string | yes | The anchor source's canonical URL (landing page). |
| `field_sources[]` | list<struct> | no | Provenance of each merged bibliographic field (title, abstract, authors, published date, doc_type). |
| `field_sources[].field` | string | no | The field (published_at = published_date). Values: `title`, `abstract`, `authors`, `published_at`, `doc_type`. |
| `field_sources[].source_id` | string | no | The source (identity.members[].source_id) that supplied it; the doc_id itself for a metadata override. |
| `field_sources[].origin` | string | no | `provider` = taken from the source's record; `human` = set by a maintainers' override (an overrides-file row of kind metadata_fix; its `method` says how much of it was AI-prepared). Values: `provider`, `human`. Reserved (defined, not in this release): `import`. |
| `identity` | struct | no | Which source records make up this document and how they were joined. |
| `identity.anchor_source_id` | string | no | The member whose record anchors the document. |
| `identity.channels[]` | list<string> | no | Distinct channels of the members. |
| `identity.former_doc_ids[]` | list<string> | no | Ids of documents merged into this one in earlier builds (look an old id up here). |
| `identity.override_ids[]` | list<string> | no | Identity overrides (merges, separations) applied to this document; rows in the overrides files. |
| `identity.members[]` | list<struct> | no | One entry per source record. |
| `identity.members[].source_id` | string | no | Member id; referenced by content.source_id, field_sources[].source_id, identity.keys[].source_id. |
| `identity.members[].channel` | string | no | Collector channel that produced the record (openalex, arxiv, semantic_scholar, lesswrong, alignmentforum, <lab>_blog, manual_url, ...). |
| `identity.members[].channel_class` | string | yes | Our distribution-policy class for the member's CHANNEL, not a statement about the work or its licence (a Semantic Scholar record of an arXiv preprint shows `restricted` while its arXiv member shows `open`). vocab.yaml defines the values. Values: `open`, `public_web`, `restricted`. Reserved (defined, not in this release): `api_tos`, `api_abstract`, `shadow`. |
| `identity.members[].key_kind` | string | no | Kind of the member's primary key (`fm_post` = ForumMagnum post id: LessWrong / Alignment Forum). Values: `doi`, `fm_post`, `url`, `openalex`, `s2`, `pmid`. |
| `identity.members[].key_value` | string | no | The primary key value. |
| `identity.members[].canonical_url` | string | yes | The record's canonical URL. |
| `identity.members[].title` | string | yes | Title as this source gives it. |
| `identity.members[].published_at` | timestamp[us, UTC] | yes | Publication timestamp as this source gives it (aggregators emit 1 January for year-only dates). |
| `identity.members[].doc_type` | string | yes | Document type as this source gives it. |
| `identity.members[].edge_kind` | string | no | How the member joined the document: `anchor`, `key:<kind>` (shared identifier), `match:<rule>` (title/author match), `human:merge` (an identity override). |
| `identity.members[].edge_to_source_id` | string | yes | The member it was joined to. |
| `identity.members[].override_id` | string | yes | The identity override that joined this member (edge_kind = human:merge). |
| `identity.members[].first_observed_at` | timestamp[us, UTC] | no | First time the collector saw the record (the per-source "first seen"). |
| `identity.members[].last_observed_at` | timestamp[us, UTC] | no | Last time the collector saw the record. |
| `identity.members[].withdrawn_at` | timestamp[us, UTC] | yes | When the source reported the record withdrawn, if ever. |
| `identity.members[].withdrawn_reason` | string | yes | The source's reason. |
| `identity.keys[]` | list<struct> | no | Every external identifier any member carries. Look a document up here (with the kind; arXiv ids without version, DOIs lower-case). |
| `identity.keys[].kind` | string | no | Identifier kind. Values: `arxiv`, `doi`, `openalex`, `s2`, `fm_post`, `url`, `pmid`, `zenodo`. |
| `identity.keys[].value` | string | no | Identifier value. |
| `identity.keys[].source_id` | string | no | The member that carries it. |
| `content` | struct | yes | The document text the annotations were made on, as two byte identifiers (the fetched source file and our Markdown conversion of it) plus where it came from. release.text says whether this variant carries the converted text itself (content.text.body). |
| `content.source_id` | string | yes | Member whose fetched content is the text. |
| `content.role` | string | yes | Kind of content the text came from (`html` = arXiv LaTeXML page; `full_text` = PDF; `post` = forum post body; `page` = web page; `xml` = publisher XML). Values: `full_text`, `html`, `xml`, `post`, `page`. Reserved (defined, not in this release): `readme`, `abstract`. |
| `content.quality` | string | yes | Rule-based conversion-quality bucket of the text (the model's own view is the text_usability annotation). Values: `ok`, `flagged`. Reserved (defined, not in this release): `failed`. |
| `content.source` | struct | no | The file fetched from the source, as an identifier (no bytes shipped in either variant). |
| `content.source.url` | string | yes | URL fetched (PDF or page); NULL for a collector-delivered body (forum posts). |
| `content.source.sha256` | string | yes | SHA-256 of the fetched file (PDF, HTML, or the collector's body). An identifier of the input, checkable by anyone who fetches the same URL and gets the same bytes. |
| `content.source.bytes` | int64 | yes | Size of the fetched file in bytes. |
| `content.source.media_type` | string | yes | Media type of the fetched file (application/pdf, text/html, text/markdown for a collector's body). |
| `content.source.captured_at` | timestamp[us, UTC] | no | When it was fetched (UTC). |
| `content.source.revision` | string | yes | Version label of the fetched item when the source has versions (arXiv `v2`). |
| `content.text` | struct | no | Our Markdown conversion of the source file: the basis of every text-based annotation. |
| `content.text.sha256` | string | yes | SHA-256 of the converted Markdown text (UTF-8). The identifier of what every annotation judged; content.text.body, where present, hashes to it. |
| `content.text.bytes` | int64 | yes | Size of the converted text in UTF-8 bytes. |
| `content.text.media_type` | string | yes | Media type of the converted text (text/markdown). |
| `content.text.converter` | string | yes | Converter stamp that produced the text, `<tool>@<version>+tier<k>` (e.g. fetchpdf-md@0.1.0+tierlatexml); `inband` for a collector-delivered body. |
| `content.text.body` | string | yes | The converted text itself (UTF-8 Markdown; up to a few MB), where this variant distributes texts (release.text = inline); NULL where it does not (release.text = not_distributed). Third-party text, not covered by CC0. |
| `release` | struct | no | What this release did to this row. Lets a reader tell a withheld value from an absent one, a cut quote from a short one, and see how much of the document is quoted. |
| `release.abstract` | string | no | `withheld_pending_rights_review`: an abstract exists internally; this release's policy withholds every abstract from the public variant until the redistribution terms are reviewed per supplier. `shipped`: the abstract column holds it. `none`: no source supplied one. Values: `withheld_pending_rights_review`, `none`. Reserved (defined, not in this release): `shipped`. |
| `release.text` | string | no | `not_distributed` (public): no document text ships; content.text.sha256 identifies it. `inline`: the converted text is in content.text.body of the same row. Values: `not_distributed`. Reserved (defined, not in this release): `inline`. |
| `release.quote_chars` | int32 | no | Characters (code points) of quoted document text shipped in this row's annotations, as serialised: repeats counted, ellipses included, surfaces excluded. For the rights statement; not a coverage ratio (content.text.bytes counts UTF-8 bytes). |
| `release.cuts[]` | list<struct> | no | Every quote or surface this release cut, with its original length; [] = nothing cut. A cut string ends with '…'. Producers already stop technique and model quotes at 300 characters at annotation time; those are not cuts and are not marked. |
| `release.cuts[].path` | string | yes | Path of the cut string with list indices, e.g. annotations.safety_techniques.payload.techniques[2].quotes[0].text. |
| `release.cuts[].chars` | int32 | yes | Original length in code points. |

### `annotations`: the metadata struct (every kind)

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.<kind>.metadata.kind` | string | no | The kind (= the column name; repeated so the metadata of all kinds can be stacked into one table). Values: `screen`, `doc_class`, `stack_relevance`, `shallow_review_relevance`, `text_usability`, `affiliation`, `safety_techniques`, `model_roles`, `model_name_matches`. |
| `annotations.<kind>.metadata.version` | int32 | no | Payload schema version of this kind (schema/payloads/<kind>-v<version>.schema.json). |
| `annotations.<kind>.metadata.status` | string | no | ok = decided with labels; empty = decided, no positive label (a model_roles `empty` record may still list zero-role candidates; an override-supplied payload gets the status its content earns: status_remap); failed_permanent = no answer (payload lists NULL; error_class says why); quarantined = withheld by the operator or a cap; the rest = not decided. A kind not run for the document is a NULL column, not a status. Values: `ok`, `empty`, `failed_permanent`. Reserved (defined, not in this release): `failed_transient`, `quarantined`, `skipped`, `not_attempted`, `partial`. |
| `annotations.<kind>.metadata.error_class` | string | yes | Reason for a non-ok status (query_invalid = the provider rejected the request; truncated = the reply hit the output cap; producer_call_failed = the record's producing call failed; vocab.yaml lists all). |
| `annotations.<kind>.metadata.config_id` | string | no | Readable, immutable id of the call that produced the payload: <producer kind>:<prompt name>:<model>:<first 8 hex of the pipeline's config digest> (screen:screen-v12:gpt-6-luna:63dc7d28 for all five records of the screen call); `override:<id>[+<id>...]` for a payload overrides supplied. A row of data/configs.parquet resolves it (stage, prompt, model, parameters, taxonomy pin, components, the full digest). |
| `annotations.<kind>.metadata.decided_at` | timestamp[us, UTC] | no | When the payload was produced (UTC). For an override-supplied payload, the time the override entered the overrides chain. |
| `annotations.<kind>.metadata.origin` | string | no | Tier of the effective decision: `ai_check` = the annotation stage's answer (a language-model call and its deterministic components; a stand-in model answer supplied as an override is ai_check too), `human` = a maintainers' override set the deciding value(s) (not necessarily a per-item human review: the override's `method` says how much of it was AI-prepared), `computed` / `rule` = derived without a model. Who produced the payload is `annotator`. Values: `ai_check`, `human`, `computed`. Reserved (defined, not in this release): `rule`, `import`. |
| `annotations.<kind>.metadata.annotator` | string | yes | Who or what produced the payload, as the provider names the model (gpt-6-luna, claude-opus-5-5), `matcher`, `rule` or `human`. On a `mixed` record it names the base answer's producer. |
| `annotations.<kind>.metadata.provenance` | string | no | Where the payload came from: `pipeline` = no override applied; `override` = overrides supplied the whole payload (config_id override:<ids>); `mixed` = field or item edits over a pipeline answer (config_id, decided_at and annotator describe the base model answer; override_fields lists what changed). Values: `pipeline`, `override`, `mixed`. |
| `annotations.<kind>.metadata.override_ids[]` | list<string> | no | Override rows (overrides files, column override_id) that produced or changed this record, in application order. Empty for an unmodified pipeline answer. |
| `annotations.<kind>.metadata.override_fields[]` | list<string> | no | Payload fields overrides set (e.g. [verdict, off_topic_reason]); items[<byline_index>] for a replaced affiliation item; [] when none. |

### `annotations.screen.payload` (version 1; internal `screen`)

The relevance screen: one call answers the Stack question (stack_relevance), the Shallow Review question (shallow_review_relevance), the text's usability (text_usability) and the document class (doc_class); this record is the call-level verdict. JSON Schema: `schema/payloads/screen-v1.schema.json` (the payload), `schema/records/screen-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.screen.payload.verdict` | string | yes | Call-level verdict = the more inclusive of the two question verdicts (stack_relevance, shallow_review_relevance): relevant if either is. Every shipped row is relevant. Values: `relevant`. Reserved (defined, not in this release): `borderline`, `irrelevant`. |
| `annotations.screen.payload.basis_role` | string | yes | Content role of the snapshot the model read (as content.role). It can differ from content.role when two snapshots converted to identical text: the text hash is the same (the build checks basis_digest = content.text.sha256). |
| `annotations.screen.payload.buckets[]` | list<string> | yes | Document buckets the model assigned (several allowed). Values: `paper`, `critique_commentary`, `eval_report`, `deployment_signal`, `lab_safety_doc`, `release_news`, `incident`, `offtopic`. |
| `annotations.screen.payload.quotes[]` | list<struct> | yes | Text excerpts supporting the verdict: {text, offset}; offset = code-point offset of the original excerpt in the exact converted text identified by content.text.sha256 (usable only with those bytes). Capped. |
| `annotations.screen.payload.off_topic_reason` | string | yes | The model's reason when it judged the document off topic (NULL on shipped rows unless an override set the verdict). |
| `annotations.screen.payload.confidence` | double | yes | Self-reported 0-1, derived: the maximum of the question confidences whose verdict matches the overall verdict; not calibrated; after a field override it still describes the model's own verdict. |
| `annotations.screen.payload.reasoning` | string | yes | The model's free-text reasoning (uncapped). Most read 'S is ... because ...; R is ... because ...': S = the Stack question (stack_relevance), R = the Shallow Review question (shallow_review_relevance). |
| `annotations.screen.payload.adjudication_tier` | int32 | yes | 1 = the first-pass model decided; 2 = a second pass adjudicated a borderline first pass. |
| `annotations.screen.payload.tier1_verdict` | string | yes | The first pass's verdict (differs from verdict after adjudication or an override). |

### `annotations.doc_class.payload` (version 1; internal `doc_class`)

Document class read from the text by the screen call. JSON Schema: `schema/payloads/doc_class-v1.schema.json` (the payload), `schema/records/doc_class-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.doc_class.payload.doc_type` | string | yes | Document type read from the text by the screen call (vocab.yaml; differs from the providers' doc_type). |
| `annotations.doc_class.payload.self_published` | bool | yes | The authors published it themselves (blog, forum, preprint without venue). |
| `annotations.doc_class.payload.primary_lang` | string | yes | Primary language code of the text. |

### `annotations.stack_relevance.payload` (version 1; internal `stack_relevance`)

Question S of the screen call: is the document in the Safety Stack's scope. JSON Schema: `schema/payloads/stack_relevance-v1.schema.json` (the payload), `schema/records/stack_relevance-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.stack_relevance.payload.verdict` | string | yes | relevant \| borderline \| irrelevant to the Safety Stack's scope (question S). Values: `relevant`, `borderline`, `irrelevant`. |
| `annotations.stack_relevance.payload.confidence` | double | yes | The model's self-reported confidence (0-1). |
| `annotations.stack_relevance.payload.quotes[]` | list<struct> | yes | Supporting excerpts {text, offset}; capped. |
| `annotations.stack_relevance.payload.basis_role` | string | yes | Content role judged. |
| `annotations.stack_relevance.payload.adjudication_tier` | int32 | yes | 1 \| 2 (see screen). |
| `annotations.stack_relevance.payload.tier1_verdict` | string | yes | The first pass's verdict. |

### `annotations.shallow_review_relevance.payload` (version 1; internal `sr_relevance`)

Question R of the screen call: is the document in the Shallow Review of AI safety's scope. JSON Schema: `schema/payloads/shallow_review_relevance-v1.schema.json` (the payload), `schema/records/shallow_review_relevance-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.shallow_review_relevance.payload.verdict` | string | yes | relevant \| borderline \| irrelevant to the Shallow Review of AI safety's scope (question R). Values: `relevant`, `borderline`, `irrelevant`. |
| `annotations.shallow_review_relevance.payload.confidence` | double | yes | The model's self-reported confidence (0-1). |
| `annotations.shallow_review_relevance.payload.quotes[]` | list<struct> | yes | Supporting excerpts {text, offset}; capped. |
| `annotations.shallow_review_relevance.payload.category` | string | yes | Shallow Review top-level category. Values: `black_box`, `evals`, `theory`, `white_box`, `none`, `multi_agent_first`, `labs`, `make_ai_solve_it`, `safety_by_construction`. |
| `annotations.shallow_review_relevance.payload.agenda` | string | yes | Shallow Review agenda slug (`new:<slug>` = proposed by the model, not in the Shallow Review list). |
| `annotations.shallow_review_relevance.payload.basis_role` | string | yes | Content role judged. |
| `annotations.shallow_review_relevance.payload.adjudication_tier` | int32 | yes | 1 \| 2. |
| `annotations.shallow_review_relevance.payload.tier1_verdict` | string | yes | The first pass's verdict. |

### `annotations.text_usability.payload` (version 1; internal `text_usability`)

The screen call's view of whether the converted text is usable as the document body. JSON Schema: `schema/payloads/text_usability-v1.schema.json` (the payload), `schema/records/text_usability-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.text_usability.payload.verdict` | string | yes | Is the converted text usable as the document body. Values: `usable`, `degraded`, `unusable`. |
| `annotations.text_usability.payload.issues[]` | list<string> | yes | Problems found. Values: `not_body`, `cut_off`, `garbled_maths`, `garbled_tables`, `bad_encoding`, `mostly_markup`, `stub`, `other`. |
| `annotations.text_usability.payload.note` | string | yes | Model free text (uncapped) describing the extracted text. |
| `annotations.text_usability.payload.basis_role` | string | yes | Content role judged. |
| `annotations.text_usability.payload.adjudication_tier` | int32 | yes | 1 \| 2. |

### `annotations.affiliation.payload` (version 1; internal `affiliation`)

Author affiliations read from the byline (paper-type documents with full text only). JSON Schema: `schema/payloads/affiliation-v1.schema.json` (the payload), `schema/records/affiliation-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.affiliation.payload.items[]` | list<struct> | yes | One item per byline author, in byline order. |
| `annotations.affiliation.payload.items[].author_name` | string | yes | Normalised author name (lower-cased, accents removed, name order normalised): the key that matches items to authors[]. Not a plain lower-casing of author_surface. |
| `annotations.affiliation.payload.items[].author_surface` | string | yes | The name as written in the text (verbatim surface; capped like quotes). |
| `annotations.affiliation.payload.items[].byline_index` | int32 | yes | Position in the byline, 0-based. |
| `annotations.affiliation.payload.items[].orcid` | string | yes | ORCID when found. |
| `annotations.affiliation.payload.items[].resolution` | string | yes | How the affiliation was resolved: openalex (provider), text, email_domain, xml, unknown. Values: `openalex`, `text`, `email_domain`, `xml`, `unknown`. |
| `annotations.affiliation.payload.items[].affiliations[]` | list<struct> | yes | Affiliations of the author. |
| `annotations.affiliation.payload.items[].affiliations[].surface` | string | no | Affiliation as written (verbatim surface; capped like quotes). |
| `annotations.affiliation.payload.items[].affiliations[].org_slugs[]` | list<string> | no | Organisation slugs (the models catalogue's maker slugs where the organisation is a lab). |

### `annotations.safety_techniques.payload` (version 1; internal `technique_staged`)

Which safety techniques of the techniques taxonomy the document engages with, in which roles and how prominently. JSON Schema: `schema/payloads/safety_techniques-v1.schema.json` (the payload), `schema/records/safety_techniques-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.safety_techniques.payload.doc_kind` | string | yes | The rubric's own kind of document (its list of document kinds, not the providers' doc_type; vocab.yaml). Values: `paper`, `blogpost`, `commentary`, `model_card`, `system_card`, `technical_report`, `eval_report`, `news`, `policy`, `other`. |
| `annotations.safety_techniques.payload.taxonomy_version` | string | yes | Techniques taxonomy version the slugs belong to (taxonomies/techniques-<version>.yaml). |
| `annotations.safety_techniques.payload.flags[]` | list<string> | yes | Document-level flags (free strings): no_techniques_found; menu_gap:<surface> = a technique the taxonomy lacks. |
| `annotations.safety_techniques.payload.techniques[]` | list<struct> | yes | One row per taxonomy slug found. |
| `annotations.safety_techniques.payload.techniques[].slug` | string | no | Taxonomy slug (joins the techniques taxonomy). |
| `annotations.safety_techniques.payload.techniques[].roles` | struct of 12 int32 | no | Struct of 12 int32 strengths 0-4, one per role (mentioned, cited_work, discussed, used, evaluated, modified, introduced, analyzed, attested_use, suspected_use, considered, critiqued). Strength = prominence of that role in this document: 0 absent, 1 trace (a sentence), 2 minor but real (a paragraph), 3 substantial (a main thread), 4 central (the document's headline for that role). mentioned >= every other role. vocab.yaml has the role definitions. Fields: mentioned, cited_work, discussed, used, evaluated, modified, introduced, analyzed, attested_use, suspected_use, considered, critiqued. |
| `annotations.safety_techniques.payload.techniques[].quotes[]` | list<struct> | no | Verbatim excerpts {text, anchored}; anchored = the original excerpt was found in the converted text (exact or after whitespace/punctuation normalisation); it says nothing about whether the excerpt supports the label, and after a release cut it describes the original, not the shipped string. Capped. |
| `annotations.safety_techniques.payload.techniques[].flags[]` | list<string> | no | Row flags from the rubric (free strings): recommended / rejected = the direction of a `considered` row; supportive; confirmed; claims_absent; quote_unverified; variant:<name>. vocab.yaml defines them. |
| `annotations.safety_techniques.payload.techniques[].note` | string | yes | The model's note on the row (free text, uncapped; some are `implemented_with: <method>` tags). |
| `annotations.safety_techniques.payload.extra_techniques[]` | list<struct> | yes | Off-taxonomy techniques the document engages with. |
| `annotations.safety_techniques.payload.extra_techniques[].name_as_written` | string | no | The name as the document writes it. |
| `annotations.safety_techniques.payload.extra_techniques[].gloss` | string | yes | The model's one-line description (free text). |
| `annotations.safety_techniques.payload.extra_techniques[].hint_technique` | string | yes | Nearest taxonomy slug, when the model named one. |
| `annotations.safety_techniques.payload.extra_techniques[].roles` | struct of 12 int32 | no | As techniques[].roles. Fields: mentioned, cited_work, discussed, used, evaluated, modified, introduced, analyzed, attested_use, suspected_use, considered, critiqued. |
| `annotations.safety_techniques.payload.extra_techniques[].quotes[]` | list<struct> | no | As techniques[].quotes. |
| `annotations.safety_techniques.payload.extra_techniques[].flags[]` | list<string> | no | As techniques[].flags. |

### `annotations.model_roles.payload` (version 3; internal `model_roles`)

Which AI models of the models catalogue the document names and which roles they play in it. JSON Schema: `schema/payloads/model_roles-v3.schema.json` (the payload), `schema/records/model_roles-v3.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.model_roles.payload.doc_kind` | string | yes | The rubric's own kind of document. Values: `paper`, `blogpost`, `commentary`, `model_card`, `system_card`, `technical_report`, `eval_report`, `news`, `policy`, `other`. |
| `annotations.model_roles.payload.flags[]` | list<string> | yes | Document-level flags explaining zero-role candidates (free strings): subsumed (a more specific node carries the roles), bib_only (named only in references), matcher_fp (the name match is not a model mention), not_found. The rubric asks for one flag per all-zero row; the model does not always comply (FORMAT's known inconsistencies give the counts): treat an all-zero row without a flag as unexplained. |
| `annotations.model_roles.payload.models[]` | list<struct> | yes | Every catalogue node the name matcher found, judge-reviewed: the candidates for "named here". Join node_id to taxonomies/models-<version>.yaml. |
| `annotations.model_roles.payload.models[].node_id` | string | no | Catalogue node graded (may be more specific than the matcher's). |
| `annotations.model_roles.payload.models[].matched_node_id` | string | yes | The matcher's node (= node_id except where the judge refined; the join key to model_name_matches). |
| `annotations.model_roles.payload.models[].roles` | struct of 10 int32 | no | Struct of 10 int32 strengths 0-4 (mentioned, cited_work, discussed, usage_experience, built_on, instrument, modified, evaluated_behavioral, analyzed_internals, introduced); the same 0-4 prominence scale as techniques; 0 = asked, not found. vocab.yaml has the role definitions. Fields: mentioned, cited_work, discussed, usage_experience, built_on, instrument, modified, evaluated_behavioral, analyzed_internals, introduced. |
| `annotations.model_roles.payload.models[].evidence[]` | list<struct> | no | Excerpts {roles [str], quote}: the roles each quote supports. Capped. Some quotes are table rows copied with their HTML tags. |
| `annotations.model_roles.payload.models[].note` | string | yes | The model's note on the row (free text, uncapped; 'graded on X' = the role is recorded on catalogue entry X). |
| `annotations.model_roles.payload.variant_models[]` | list<struct> | yes | Named derivatives of a catalogue model (fine-tunes, sizes) the document engages with. |
| `annotations.model_roles.payload.variant_models[].base_node_id` | string | no | The catalogue node they derive from. |
| `annotations.model_roles.payload.variant_models[].names_as_written[]` | list<string> | no | The derivative names as written. |
| `annotations.model_roles.payload.variant_models[].quote` | string | no | One supporting excerpt; capped. |
| `annotations.model_roles.payload.variant_models[].roles` | struct of 10 int32 | no | As models[].roles. Fields: mentioned, cited_work, discussed, usage_experience, built_on, instrument, modified, evaluated_behavioral, analyzed_internals, introduced. |
| `annotations.model_roles.payload.extra_models[]` | list<struct> | yes | Off-catalogue models the document engages with. |
| `annotations.model_roles.payload.extra_models[].name_as_written` | string | no | Name as written. |
| `annotations.model_roles.payload.extra_models[].quote` | string | no | One supporting excerpt; capped. |
| `annotations.model_roles.payload.extra_models[].roles` | struct of 10 int32 | no | As models[].roles. Fields: mentioned, cited_work, discussed, usage_experience, built_on, instrument, modified, evaluated_behavioral, analyzed_internals, introduced. |
| `annotations.model_roles.payload.extra_models[].node_id` | string | yes | Catalogue node the name resolves to, when exactly one does. |

### `annotations.model_name_matches.payload` (version 1; internal `model_regexp_matches`)

The deterministic name matcher's raw hits (a record of the model_roles call; annotator = matcher): the candidate list the model_roles judge saw. Where an override replaced the model_roles answer (provenance = override there), this record keeps the original call's metadata; if that call failed, it is failed_permanent with error_class producer_call_failed and no hits. JSON Schema: `schema/payloads/model_name_matches-v1.schema.json` (the payload), `schema/records/model_name_matches-v1.schema.json` (the record with its metadata).

| Field | Type | Nullable | Description |
|---|---|---|---|
| `annotations.model_name_matches.payload.matches[]` | list<struct> | yes | Every name-matcher hit (deterministic patterns over the text), strong entries first. |
| `annotations.model_name_matches.payload.matches[].node_id` | string | no | Catalogue node matched. |
| `annotations.model_name_matches.payload.matches[].surfaces[]` | list<string> | no | Matched strings in document order, duplicates kept (list length = occurrence count); capped like quotes. |
| `annotations.model_name_matches.payload.matches[].match_class` | string | no | strong (an unambiguous pattern) or weak. Values: `strong`, `weak`. |
| `annotations.model_name_matches.payload.ambiguous[]` | list<struct> | yes | Spans the matcher could not attribute to one node. |
| `annotations.model_name_matches.payload.ambiguous[].text` | string | no | The span; capped like quotes. |
| `annotations.model_name_matches.payload.ambiguous[].candidates[]` | list<string> | no | Candidate nodes. |
| `annotations.model_name_matches.payload.ambiguous[].match_class` | string | no | strong or weak. Values: . Reserved (defined, not in this release): `strong`, `weak`. |

### Coverage (records per kind and status)

| Kind | empty | failed_permanent | not_run | ok |
|---|---|---|---|---|
| `screen` | 0 | 0 | 0 | 39,269 |
| `doc_class` | 0 | 0 | 0 | 39,269 |
| `stack_relevance` | 0 | 0 | 0 | 39,269 |
| `shallow_review_relevance` | 0 | 0 | 0 | 39,269 |
| `text_usability` | 0 | 0 | 0 | 39,269 |
| `affiliation` | 0 | 0 | 14,514 | 24,755 |
| `safety_techniques` | 6,006 | 0 | 0 | 33,263 |
| `model_roles` | 9,901 | 0 | 0 | 29,368 |
| `model_name_matches` | 9,901 | 10 | 0 | 29,358 |

### Known inconsistencies

Counted in this release; none is repaired by the release code.

| Rows | What |
|---|---|
| 1 document(s) | screen.verdict is `relevant` while neither question's verdict is (the call-level rule says it should be the more inclusive of the two): sp84cqg8tfxe1 |
| 296 model rows in 159 documents | an all-zero candidate row of model_roles carries no flag or several, though the rubric asks for exactly one |
| 10 documents | model_name_matches does not share model_roles' config_id and decided_at: an override (stand-in) replaced the model_roles answer and the matcher record keeps the original call's |
| 18 documents | screen.basis_role differs from content.role: two snapshots converted to identical text; the text hash the screen judged is content.text.sha256 (checked by the build) |

### Capped strings

Cap: 300 characters; rule: a string longer than the cap is cut at the last word boundary at or before cap-1 code points and U+2026 '…' appended, so the shipped string is <= cap; a string of exactly the cap is kept whole; with no word boundary in reach it is cut at cap-1. Quote paths:

- `annotations.screen.payload.quotes[].text`
- `annotations.stack_relevance.payload.quotes[].text`
- `annotations.shallow_review_relevance.payload.quotes[].text`
- `annotations.safety_techniques.payload.techniques[].quotes[].text`
- `annotations.safety_techniques.payload.extra_techniques[].quotes[].text`
- `annotations.model_roles.payload.models[].evidence[].quote`
- `annotations.model_roles.payload.variant_models[].quote`
- `annotations.model_roles.payload.extra_models[].quote`

Surface paths (verbatim strings from the document, capped like quotes, not counted in `release.quote_chars`):

- `annotations.affiliation.payload.items[].author_surface`
- `annotations.affiliation.payload.items[].affiliations[].surface`
- `annotations.model_name_matches.payload.matches[].surfaces[]`
- `annotations.model_name_matches.payload.ambiguous[].text`

Model-written prose (never capped):

- `annotations.screen.payload.reasoning`
- `annotations.screen.payload.off_topic_reason`
- `annotations.text_usability.payload.note`
- `annotations.safety_techniques.payload.techniques[].note`
- `annotations.safety_techniques.payload.extra_techniques[].gloss`
- `annotations.model_roles.payload.models[].note`

Prose scrub: `annotations.model_roles.payload.models[].note`: `\b[Mm]enu (nodes|rows|entries)\b` → `catalogue entries`, `\b[Mm]enu (node|row|entry)\b` → `catalogue entry` (465 strings changed in this file).

### Status remap

The released status differs from the pipeline's in these cases; every changed value is a line of `remap.jsonl` (12 lines in this release).

- **override_empty**: when provenance = override AND status = ok AND the producer's own empty test holds for the payload (safety_techniques: techniques and extra_techniques both empty; model_roles: no models[] row with any role >= 1 AND variant_models and extra_models empty, workflows/annotate/model_roles/main.py); set {"status": "empty"}.
- **producer_call_failed**: when kind = model_name_matches AND status = failed_permanent AND the producing model_roles call failed (its record failed with the same error_class, or an override replaced it): the matcher ran before the judge call but its hits are persisted only with a successful call, so no output exists; set {"error_class": "producer_call_failed"}.
