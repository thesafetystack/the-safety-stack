# Risks

File `risks-0.2.0.yaml`, a draft (`meta.status` `draft`, version 0.x: ids, definitions and structure may still
change): 8 families and 39 risks, schema `schemas/risks-0.schema.json` (the catalogue envelope,
[../README.md](../README.md#the-catalogue-envelope)). Not yet used to annotate the dataset. Undecided items are in
[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md); the companion taxonomy of what produces these risks is
[../risk-generators/](../risk-generators/).

## Purpose and scope

A risk is a type of harmful event or state, and its instances, attempted or intercepted ones included: what goes
wrong. The taxonomy is meant for per-document annotation of the dataset (which risks a document engages and how), for
linking techniques to the risks they address, and for the per-risk view of the stack (which layers stand against a
risk, and where there are none). It is not a ranking of risks and says nothing about their likelihood.

| id | family | risks |
|---|---|---|
| `ma` | Misalignment and loss of control | 10 |
| `mu` | Misuse by humans | 5 |
| `se` | Security of AI systems | 4 |
| `re` | Reliability and accidents | 3 |
| `mx` | Multi-agent failures | 3 |
| `st` | Structural and societal-scale risks | 6 |
| `ha` | Present-day harms to people (coarse) | 7 |
| `we` | AI welfare and moral patienthood | 1 |

## File

- `version`, `meta`: `schema`, `status`, `updated`, `description`, `sources`; `rules` (the six annotation rules),
  `relations` (the four relations), `fields` (what each entry field means), `attrs` (the codes of `attrs`),
  `crosswalk_keys` (the classifications `siblings` refers to).
- `entries`: each family (`node: family`) followed by its risks (`node: risk`, `parent` the family; the id is the
  family id, a dot, the risk's name: `ma.scheming`).

Entry fields (count of risks that have the field):
- `id`, `node`, `name`, `parent`, `definition` (39), `status` (all `draft`; the entry's own, distinct from
  `meta.status`).
- `exclude` (24): neighbouring cases that are not this risk, with the risk they belong to.
- `facets` (7): optional multi-valued tags where a risk hides distinct threat models (`mu.cbrn`: `bio`, `chem`,
  `radiological_nuclear`). Not a third level.
- `contested` and `vs` (15): a boundary expected to have low agreement, and the neighbour's id.
- `attrs` (39): `sev` severity ceiling (`C` catastrophic, `S` societal, `I` individual), `hor` horizon (`N` now, `F`
  future systems, `B` both), `ben` whom a safeguard against the risk protects.
- `mit` (39): MIT AI Risk Repository v4 subdomain codes, crosswalk candidates, partial, not equivalences (empty for
  `ma.sabotage`). Every one of the 24 subdomains is listed by at least one risk.
- `siblings` (39, 4 empty): the corresponding category in other risk classifications (keys in
  `meta.crosswalk_keys`).
- No entry has `aliases` yet.

## Boundaries

- **Risk, generator, missing control.** A statement that describes an instance of a harmful event or behaviour type
  is a risk, whether it succeeded or was intercepted: a blocked jailbreak is still `se.jailbreak`. A standing
  condition, process or pressure that changes how often such events happen, how bad they are or how likely the
  defences are to stop them is a generator ([../risk-generators/](../risk-generators/README.md#boundaries), criteria
  C1-C7). A missing or weak defence for a given risk and model is a gap: it is what the stack's coverage map shows,
  not an entry of either taxonomy.
- **Capability and propensity.** A property measured by eliciting the harmful behaviour (does the model deceive its
  overseers in this sandbox?) is a propensity and belongs here; the `ma` risks are propensities and behaviours. A
  property measured on a task that is not the harm (can it tell an evaluation from deployment?) is a capability and
  is a generator. Two places in this file sit across the line: `mu.cbrn` includes dual-use capability evaluations that
  name no actor, and `st.rd-acceleration` is a capability trend kept as a risk (see the open questions).
- **Outcome and mechanism.** `ma.loss-of-control` is labelled whenever loss of control, takeover, human
  disempowerment by AI or existential catastrophe from misaligned AI is named, together with any mechanism risks
  (`ma.scheming`, `ma.power-seeking`), not instead of them.
- The `exclude` texts state the other pairwise boundaries.

## Annotation

The rules are `meta.rules`; the annotator prompt is built from them and from the definitions and excludes.

- **Explicit only, with evidence.** A label records what the document says, with a quoted evidence span. Nothing is
  inferred from what a document leaves unsaid; test prompts and attack examples used as stimuli are not risks the
  document engages (`stimuli`), nor is a capability limitation framed as a research goal (`capability_limits`).
- **Relations.** Each label carries one: `mitigates` (proposes, applies or evaluates a defence; the document itself
  must do so, naming a risk as motivation for unrelated work is `discusses`), `measures` (an evaluation, benchmark,
  detector, red team or audit of the risk, without the fix), `demonstrates` (shows the risk occurring: an attack, a
  model organism, an incident, an empirical finding), `discusses` (argues, analyses, surveys, forecasts or sets policy
  about it).
- **Family fallback.** A family id alone (`ma`, `mu`) is used only when the document engages the family generically
  ("the alignment problem", "misuse") and no risk fits, and never beside a risk of the same family.
- **Passing mentions.** A risk named once in a list (an overview, related work, a prohibited-use list) is labelled
  with `passing` true. Passing labels are stored; views leave them out by default.
- Facets are optional, multi-valued, and only on the 7 risks that have them.

## Pilot

The drafts before 0.2.0 were piloted: v0.1 on 20 documents, v0.1.1 (v0.1 with wording fixes) on 100, and 0.2.0's
draft re-run on 40 of them. v0.1 had the same 8 families and 39 leaves, with `re.oversight` where 0.2.0 has
`st.rd-acceleration`, and narrower definitions.

- **Sample.** 100 documents from the dataset, purposive, not random: 79 picked by keyword strata (rare families
  over-represented on purpose), 14 with no risk keyword in title or abstract (system and model cards, frameworks, lab
  posts), 2 passing-mention documents, 5 negative controls. Each annotator saw title, abstract and at most 1,500 words
  of text, selected toward risk passages.
- **Annotators.** Three language models, blind to each other, with identical prompts: Claude Opus and two GPT-6
  variants (through Codex).
- **Agreement** (Krippendorff's alpha over each document's label set, Jaccard distance). Three-way, on v0.1.1 and
  100 documents: 0.734 at risk level, 0.815 at family level. The two GPT-6 variants agree with each other at about
  0.91 and are not independent, so the honest figure is Opus against GPT-6: about 0.65 (risk) and 0.75 (family) on
  v0.1.1, and 0.74 and 0.83 on 0.2.0's draft, re-run on 40 of the 100 documents.
- **What the disagreement is.** Mostly whether a risk is engaged at all, not where a boundary lies: where two
  annotators both used a family, their risks were the same in 72% of cases, one added risks in 22%, and they
  substituted one risk for another in 6%. Merging risks barely raises agreement (45 labels to 37: +0.03; families
  only: +0.08).
- **Explicit only** changed almost nothing: 2-4% of labels were marked implicit.
- **Passing labels** were 26-32% of labels on v0.1.1 and 19-24% on v0.2; dropping them *lowered* agreement, because
  the annotators disagree on the flag itself. Hence: store them, and do not make views depend on the flag's precision.
- **Relations** matched in 86% of shared labels (82% on the re-run); most mismatches were `discusses` against
  `mitigates`.
- **Changes from the pilot to 0.2.0**: `re.oversight` removed (the lowest-agreement leaf, a risk factor; it is the
  generator family `as` now), the outcome-and-mechanism rule, the new risk `st.rd-acceleration`, widened definitions
  and six rules (see [CHANGELOG.md](CHANGELOG.md)). The widened `ha.toxic` did not validate (alpha 0.57 on the
  re-run).

Caveats: agreement is not accuracy, and there are no human labels; the effective number of independent annotators is
two; the sample is purposive, so frequencies are not corpus frequencies and per-risk figures for rare risks rest on
2-10 documents; excerpts, not full texts; 0.2.0 was checked on 40 documents by the same models whose disagreements
motivated the changes, not on held-out data (treat ±0.03 as noise).

## Crosswalk to regulatory and lab lists

From the draft's survey of other classifications (partial; `mit` and `siblings` hold the per-risk crosswalks):

| external category | 0.2.0 |
|---|---|
| EU GPAI Code of Practice, App. 1.4: CBRN; loss of control; cyber offence; harmful manipulation | `mu.cbrn`; `ma.loss-of-control` (and `ma` risks); `mu.cyber`; `ma.sycophancy` (model-driven) or `mu.influence` (actor-driven or unspecified) |
| OpenAI Preparedness Framework v2, tracked: biological and chemical; cybersecurity; AI self-improvement | `mu.cbrn`; `mu.cyber`; `st.rd-acceleration` |
| OpenAI Preparedness Framework v2, research: long-range autonomy; sandbagging; autonomous replication and adaptation; undermining safeguards; nuclear and radiological | `re.agentic` or `ma.power-seeking` (no clean fit); `ma.eval-gaming`; `ma.exfiltration`; `ma.sabotage`; `mu.cbrn` (`radiological_nuclear`) |
| Google DeepMind Frontier Safety Framework v3.1: CBRN, cyber, harmful manipulation; ML R&D; misalignment (stealth and situational awareness) | `mu.cbrn`, `mu.cyber`, `mu.influence` or `ma.sycophancy`; `st.rd-acceleration`; `ma.scheming` and `ma.eval-gaming` (facet `evaluation_awareness`) |
| Anthropic RSP v3.4: chemical and biological (two); misaligned AI in high-stakes settings; automated R&D | `mu.cbrn`; `ma.sabotage` (with `ma.scheming`, `ma.eval-gaming`); `st.rd-acceleration` |
| NIST AI 600-1 (12 risks) | CBRN `mu.cbrn`; confabulation `re.hallucination`; dangerous, violent or hateful and obscene content `ha.toxic`; data privacy `ha.privacy`; environment `ha.environment`; harmful bias or homogenisation `ha.bias` or `st.epistemic`; human-AI configuration `ha.reliance`; information integrity `st.epistemic` or `mu.influence`; information security `mu.cyber` or `se.*`; IP `ha.ip`; value chain `se.poisoning` |
