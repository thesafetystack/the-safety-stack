> Copied from release 2026-10-25 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# Annotation quality, first version (agreement with a model-made reference set)

This page reports how well the two model-made annotations in this release (safety techniques and AI models) agree
with a reference set. **The reference set is itself model-made.** No human has adjudicated it. Treat the numbers
as agreement with careful model labellers, not as accuracy against ground truth. An independent, adjudicated
reference set is planned and these figures will be redone on it.

The numbers measure the main annotator, gpt-6-luna. They do not cover the 21 stand-in annotations (see Limits), the
relevance screen or the affiliations.

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
- **Not measured:** the relevance screen (which documents are in; its error rate in both directions is unknown) and
  the affiliation extraction. A check is planned.

## Next
An independent reference set (different sample, different labelling, with adjudication) is planned. This page will be
updated with it.
