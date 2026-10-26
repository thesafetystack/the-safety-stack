> Copied from release 2026-10-26 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# Annotation quality (agreement with model-made references)

This page has two evaluations, and both compare the annotations with labels that language models made; no human has
adjudicated either. Treat the numbers as agreement with careful model labellers, not as accuracy against ground
truth. An independent, adjudicated reference set is planned and these figures will be redone on it.

- **A reference set for techniques and models** (the sections up to "Next"): how well the two main annotations
  (safety techniques and AI models) agree with a model-made reference set of 100 documents.
- **A judge evaluation of every model judgement** (the last section): three language-model judges label samples
  of the triage, the relevance screen, the affiliations, the models and the techniques.

Both measure the main annotator, gpt-6-luna. Neither covers the 21 stand-in annotations (see Limits). The relevance
screen and the affiliations are covered by the judge evaluation only.

## What was measured
- **Data:** the shipped annotations of this release's build, on 100 documents. The documents were sampled from the
  screen-relevant corpus (papers 60, forum posts 30, lab blog posts 4, system/model cards 3, reports 3; systematic
  sampling within each kind, stratified by year and by how many models a deterministic matcher finds). Lengths run
  from 1.3k to 585k characters (median 52k).
- **Annotator under test:** gpt-6-luna (OpenAI), as run in production (techniques: one call plus a follow-up "glean" turn
  per document; models: one call per document over a candidate list from a deterministic name matcher).
- **Reference set (model-made; internally "gold v3"):** six independent blind labelling runs per document and task:
  Claude Opus 5.5 (claude-opus-5-5), Claude Sonnet 5.5 (claude-sonnet-5-5) and GPT Sol 6.1, each twice, with the same guide,
  taxonomy and rubric. They read the whole document. A label enters the reference set when at least 4 of the 6 runs
  give it. There was no adjudication pass. The labellers were stronger
  models with more time per document, but they share the general failure modes of language models.
- **Two levels:**
  - *Presence*: was the technique / model found at all (techniques by taxonomy slug, umbrella group nodes left out;
    models by catalogue node with any role of strength >= 1).
  - *Role*: (label, role) pairs at strength >= 2 of 4, e.g. a technique "used" or "evaluated", a model "evaluated" or
    "fine-tuned".
- Precision / recall / F1 are pooled over documents. Intervals are 95 % document-bootstrap intervals.

## Headline numbers

Agreement of gpt-6-luna with the model-made reference set (100 documents, no human adjudication):

| | Precision | Recall | F1 |
|---|---|---|---|
| Techniques, presence | 0.87 [0.83, 0.91] | 0.71 [0.66, 0.75] | 0.78 [0.74, 0.81] |
| Techniques, role (>= 2) | 0.70 [0.65, 0.74] | 0.72 [0.66, 0.76] | 0.71 [0.66, 0.74] |
| Models, presence | 0.90 [0.84, 0.96] | 0.93 [0.86, 0.97] | 0.92 [0.87, 0.96] |
| Models, role (>= 2) | 0.85 [0.80, 0.90] | 0.85 [0.79, 0.91] | 0.85 [0.81, 0.89] |

- **Techniques: misses, not wrong labels.** About 7 in 10 reference techniques are found. When one is found, its roles
  mostly agree: on found techniques the role-level F1 is 0.83, and the strongest role matches the reference's main
  role 87 % of the time.
- **Models:** for one of the 100 documents the provider refused gpt-6-luna's request. Scored as gpt-6-luna's answer,
  it is a miss and holds a third of the model misses; without it, presence recall is 0.96. (In the release, that
  document carries a stand-in annotation, which was not evaluated.)
- **Is model X named in this document?** Use the full model list of a document, including rows with all roles 0. It
  contains 94 % of the models the reference says the document names (97 % without the failed document), at 82 %
  precision. That list is the deterministic matcher's candidate list (`model_name_matches`, strong and weak hits),
  so this recall is the matcher's. Models the matcher does not know are only reported when the document engages them
  materially (`model_roles.payload.extra_models`). Rows with a role >= 1 contain only 77 % of named models: reference-only mentions get
  role 0 by design.
- **Hierarchy:** a prediction one level above or below the reference label (e.g. a model family instead of the specific
  version) counts as wrong above. For techniques this changes almost nothing (F1 0.78 -> 0.79 with full credit for
  related labels). For models it accounts for about half of the presence false positives (F1 0.92 -> 0.95).

## Omissions by severity
Every reference label was classified by an Opus reader of the document, without knowing whether gpt-6-luna found it:
- *core*: the document's headline method or main model;
- *substantive*: used, evaluated, analysed, or central to a section;
- *peripheral*: mentioned, cited, related work.
An AI assistant spot-checked 10 classifications against the texts (by searching them); all 10 agreed.

| Recall by class | Techniques | Models |
|---|---|---|
| core | 0.84 (53 of 63) | 1.00 (41 of 41) |
| substantive | 0.78 (180 of 231) | 0.90 (294 of 325); 0.96 without the failed document |
| peripheral | 0.58 (120 of 206) | 0.96 (218 of 228) |

- Of the 147 missed techniques, 86 are peripheral, 51 substantive and 10 core.
- 9 of 100 documents miss a core technique. No document misses its main model.
- Misses cluster in long, dense documents: two system cards, a long survey and a book account for a third of the
  technique misses.

## How much of the precision gap is the reference's?
- In a sample of 20 technique labels that production gave and the reference lacks, 15 were defensible readings of the
  text and 5 named the wrong technique. Most of these labels were given by 1-3 of the 6 reference runs, just below the
  4-of-6 threshold.
- In a sample of 20 such model labels, 10 were the right model at the wrong level of the catalogue, 4 the wrong
  version, and 6 defensible.

## Limits
- The reference is model-made, unadjudicated, and covers 100 documents. Intervals reflect document sampling only,
  not labeller error.
- Model labellers graded only the matcher's candidates. Model presence and role numbers cannot see models the matcher
  misses; the "named in this document" figure can.
- Severity classes come from one model pass. Boundaries (e.g. a panel of evaluated models vs a single focus model)
  need judgement.
- The reference sample was drawn from the corpus one build earlier. All 100 documents are present in this build with
  identical text.
- Run-to-run variation of the annotator is about ±0.02 F1. The shipped annotations score within that band of
  repeated evaluation runs of the same configuration.
- **Stand-ins.** For 17 documents (0.04 %) the provider refused gpt-6-luna's request. Their technique and/or model
  annotations (21 annotations: 11 techniques, 10 models) were supplied by claude-opus-5-5 or claude-sonnet-5-5 with
  the same prompt and rubric, quotes checked against the text. They carry `provenance = override`, name the model in
  `annotator` and point to the override row in `config_id`. They were not evaluated. For the 10 model stand-ins the
  name matcher's record has no hits (`status = failed_permanent`, `error_class = producer_call_failed`): the matcher
  output is stored only with a successful production call.
- **Not measured by the reference set:** the relevance screen (which documents are in) and the affiliation
  extraction; the judge evaluation below covers both.

## Next
An independent reference set (different sample, different labelling, with adjudication) is planned. This page will be
updated with it.

## Judge evaluation of every model judgement (judge-2026-10-25j)

A second evaluation covers every judgement the pipeline asks a language model to make: the triage that decides which
records get their full text fetched, the relevance screen that decides which documents are in this dataset, the
authors' affiliations, the models and the techniques. For each, a sample of build `ws1qpn8myzxah` (this release's
build) was labelled blind by three language-model judges, Claude Opus 5.5, GPT Sol 6.1 and Claude Sonnet 5.5, with the
production prompt's definitions as their guide and the whole document to read (production reads a window of long
documents in some judgements). The stand-in annotations are not in the samples. The samples, the judges' labels, the
method and the full scores are in the pipeline repository under `evals/judge-2026-10-25j/`; every number below is
generated from its `scores.json` files.

Production (gpt-6-luna) is scored against two references built from the judges: the **majority** (a label at least 2
of the 3 judges give; the headline) and the **consensus** of Opus and Sol (a label both give).

**Read the numbers with these caveats.**

- The judges are language models, not human annotators. Agreement with them is agreement with careful model labellers,
  not accuracy.
- The judges disagree with each other (second table). Production's agreement with them cannot be measured more finely
  than they agree among themselves: where a judge pair agrees no better than production agrees with each judge, these
  numbers do not separate production's errors from the judges'.
- Opus and Sonnet agree with each other far more than either agrees with Sol (technique presence F1 0.83 between Opus
  and Sonnet, 0.73 Opus-Sol, 0.65 Sol-Sonnet; screen S verdict κ 0.88 vs 0.53 and 0.55), so the majority leans towards
  them: where the two agree, Sol is outvoted.
- The consensus column keeps only what Opus and Sol agree on and drops the items (or labels) they disagree on. The
  hard cases leave with them, so the consensus numbers are optimistic.

| Judgement | Sample | What is judged | Metric | vs majority (2 of 3 judges) | vs consensus (Opus and Sol) |
|---|---|---|---|---|---|
| Triage | 200 records, weighted (a, b) | the triage verdict (relevant, borderline, not relevant) from a record's title and metadata; relevant or borderline = fetch the full text | records scored | 197 of 200 | 157 of 200 |
|  |  |  | fetch precision | 0.65 [0.53, 0.76] | 0.75 [0.62, 0.87] |
|  |  |  | fetch recall | 0.90 [0.80, 0.97] | 1.00 [1.00, 1.00] |
|  |  |  | fetch F1 | 0.76 [0.66, 0.84] | 0.86 [0.76, 0.93] |
|  |  |  | missed relevant: estimated documents among the 135,315 eligible records triage marked not relevant | 0 [0, 0] | 0 [0, 0] |
|  |  |  | missed relevant or borderline | 1,022 [252, 2,074] | 0 [0, 0] |
| Screen | 100 documents | the relevance screen that decides which documents are in the dataset: S (in the Safety Stack's scope), R (in the Shallow Review's), the overall verdict (relevant, borderline, irrelevant; this dataset ships `relevant`), and whether the converted text is usable | keep F1 (relevant or borderline vs irrelevant) | 0.92 (n 100) | 0.97 (n 89) |
|  |  |  | S verdict | agreement 0.78, κ 0.63 (n 100) | agreement 0.97, κ 0.94 (n 71) |
|  |  |  | R verdict | agreement 0.80, κ 0.66 (n 95) | agreement 0.92, κ 0.84 (n 71) |
|  |  |  | overall verdict | agreement 0.76, κ 0.60 (n 98) | agreement 0.89, κ 0.80 (n 76) |
|  |  |  | usability verdict | agreement 0.66, κ 0.22 (n 100) | agreement 0.70, κ 0.20 (n 71) |
| Affiliation | 100 documents | (author, affiliation as written) pairs; paper-type documents with full text | F1 [95 % CI]; precision, recall | F1 0.83 [0.70, 0.95]; P 0.82, R 0.84 (188 reference labels) | F1 0.84 [0.71, 0.95]; P 0.79, R 0.90 (169 reference labels) |
| Models | 100 documents | (model, role) pairs at strength >= 2 of 4 over the matcher's candidates | F1 [95 % CI]; precision, recall | F1 0.88 [0.84, 0.91]; P 0.90, R 0.87 (816 reference labels) | F1 0.88 [0.83, 0.91]; P 0.86, R 0.90 (753 reference labels) |
| Techniques | 100 documents | technique presence (taxonomy slug, any role) | F1 [95 % CI]; precision, recall | F1 0.76 [0.72, 0.79]; P 0.79, R 0.72 (354 reference labels) | F1 0.77 [0.73, 0.80]; P 0.76, R 0.77 (317 reference labels) |

Agreement between the judges, and of production with each judge (same metrics):

| Judgement, metric | Opus-Sol | Opus-Sonnet | Sol-Sonnet | production-Opus | production-Sol | production-Sonnet |
|---|---|---|---|---|---|---|
| Triage verdict, agreement (weighted, triage set (a)) | 0.92 | 0.97 | 0.91 | 0.94 | 0.93 | 0.93 |
| Screen keep F1 | 0.91 | 0.93 | 0.90 | 0.94 | 0.91 | 0.89 |
| Screen S verdict, κ | 0.53 | 0.88 | 0.55 | 0.63 | 0.72 | 0.62 |
| Screen R verdict, κ | 0.54 | 0.75 | 0.50 | 0.62 | 0.62 | 0.55 |
| Screen overall verdict, κ | 0.62 | 0.78 | 0.56 | 0.59 | 0.71 | 0.52 |
| Screen usability verdict, κ | 0.42 | 0.52 | 0.66 | 0.09 | 0.21 | 0.21 |
| Affiliation F1 | 0.91 | 0.99 | 0.91 | 0.83 | 0.88 | 0.83 |
| Models (model, role >= 2) F1 | 0.89 | 0.89 | 0.86 | 0.88 | 0.85 | 0.88 |
| Techniques presence F1 | 0.73 | 0.83 | 0.65 | 0.73 | 0.68 | 0.74 |

(a) Triage: 200 records of the 149,390 eligible, stratified by production's verdict and, for `not_relevant`, its
confidence; production's positives and its low-confidence `not_relevant` records are oversampled. The numbers are
population estimates with design weights and 95 % stratified bootstrap intervals; a record a reference has no label
for is re-weighted within its stratum. Where no miss was observed the bootstrap interval has zero width; the Wilson
interval per `not_relevant` stratum (missed relevant or borderline, majority) is the honest range there: confidence up
to 0.94: 4 of 69 items missed, estimate 1,022, Wilson 95 % interval [401, 2,465]; confidence 0.95-0.98: 0 of 40 items
missed, estimate 0, Wilson 95 % interval [0, 4,364]; confidence 0.99: 0 of 30 items missed, estimate 0, Wilson 95 %
interval [0, 7,705]. Triage decides whether a record's text is fetched; a missed record is, unless its text came
another way, a document this dataset does not contain.

(b) The proportional triage sample (100 records, self-weighting) has only 9 records production would fetch, too few to
estimate recall; against the majority its fetch decision agrees on 0.99 of records (κ 0.94).

Limits of this evaluation, besides the caveats above: 100 documents per judgement (200 records for triage);
proportional allocation leaves rare document types (system cards, evaluation reports, framework documents) without
items; the judges read the whole text where production read a window, which matters most for the usability verdict
(production judged an excerpt); intervals reflect document sampling only, not judge error.
