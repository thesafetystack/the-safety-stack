# Risk generators

File `risk-generators-0.3.0.yaml`, a draft (`meta.status` `draft`, version 0.x: ids, definitions and structure may
still change): 10 families and 64 generators, schema `schemas/risk-generators-0.schema.json` (the catalogue envelope,
[../README.md](../README.md#the-catalogue-envelope)). It refers to the risk taxonomy 0.2.0 (`meta.references.risks`,
[../risks/](../risks/)). Not used to annotate the dataset; 0.3.0 itself has not been annotated with. Undecided items
are in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Purpose and scope

A generator is a standing condition, process or pressure that changes how often a risk event happens, how bad it is,
or how likely the defences are to stop it, and is not itself an instance of a harmful event type: what produces the
risks of [../risks/](../risks/). The taxonomy serves the stack's view of why defences fail together: defence in depth
works only as far as its layers fail independently, and a generator that degrades several layers counted against the
same risk is a candidate common cause. It links generators to the risks they feed or whose defences they weaken, and
to the technique families that reduce or measure them.

| id | family | generators | `curated` | common-cause candidates |
|---|---|---|---|---|
| `tr` | Training and optimisation | 8 | 0 | 5 |
| `ca` | Capabilities and cognition | 8 | 0 | 4 |
| `as` | Limits of assurance and oversight | 5 | 1 | 5 |
| `dp` | Deployment and affordances | 10 | 0 | 4 |
| `su` | Shared components, processes and monoculture | 6 | 5 | 6 |
| `or` | Developer and deployer organisations | 3 | 0 | 3 |
| `cm` | Competition and geopolitics | 5 | 1 | 3 |
| `ad` | Adversaries and offence-defence balance | 3 | 1 | 1 |
| `mf` | Multi-agent interaction factors | 8 | 3 | 1 |
| `so` | Societal and structural | 8 | 1 | 4 |

## File

- `version`, `meta`: `schema`, `status`, `updated`, `description`, `sources`, `references` (`risks: 0.2.0`); `fields`
  (what each entry field means), `technique_families` (the 18 values of `reduced_by`, `assessed_by`, `defeats` and
  `bypasses`), `crosswalk_keys` (the frameworks the `crosswalks` strings start with), `risk_edges`.
- `entries`: each family (`node: family`) followed by its generators (`node: generator`, `parent` the family; the
  id is the family id, a dot, the generator's name: `ca.situational-awareness`).
- `meta.risk_edges` (9): edges from a risk, not a generator: `defeats` (technique families whose layers the risk,
  once present, degrades: a scheming model defeats behavioural evaluations), `bypasses` (layers it skips: stolen
  weights skip every deployment-time layer), `escalates_to` (risks it leads to), `searched_by`.

Generator fields (count of generators that have the field):
- `id`, `node`, `name`, `parent`, `definition` (64); `status` (63 `draft`, 1 `provisional`: `tr.shallow-safety`,
  added from trial misfits with thin support).
- `tier` (64): `annotate` (52), a candidate for per-document labels; `curated` (12), for edges and the coverage map
  only, rarely stated in text.
- `background` (3: `ca.capability-level`, `dp.scale`, `as.immature-science`): label only when the document's
  argument depends on it, never for motivation boilerplate.
- `role` (64): the typical role, one or more of `hazard` (17), `cause` (25), `barrier` (36); see C7 below.
- `feeds` (42) and `weakens` (33): references `{id, name}` to risks 0.2.0 (a family id stands for the whole family);
  every generator has at least one. `weakens` is for barrier-role generators.
- `reduced_by` (64) and `assessed_by` (11): technique families that act on the generator, or measure it without
  reducing it; `non-technical` and `none-known` are values too. 31 generators have only `non-technical` or
  `none-known`.
- `common_cause` (36): a candidate common-cause mechanism, a hypothesis, never a measured correlation: `mech`, `scope`,
  `searched_by`, `defeats` (technique families), `note`.
- `contested` and `vs` (6): a weak boundary, and in words against what.
- `crosswalks` (64): the corresponding item in other frameworks (`meta.crosswalk_keys`), or `trial` for a generator
  that came from the annotation trial's misfit notes. `note` (4).
- No entry has `aliases` yet.

The technique families are those of the techniques taxonomy's 0.8 draft, which is not published here (techniques 1.x
has no families), plus `non-technical`; they do not resolve against [../techniques/](../techniques/).

## Boundaries

The criteria the definitions refer to (C1-C7):

- **C1, event type: risk or generator.** Fix the adverse endpoint. A statement that describes an instance of a
  harmful event or behaviour type is a risk, whether or not it succeeded or was intercepted (a blocked jailbreak is
  still `se.jailbreak`). A standing condition that changes the rate or severity of such events, or the chance they
  are intercepted, is a generator.
- **C2, one concept, one place; chains are edges.** When a risk produces another risk, or degrades or skips defences
  once present, that is an edge from the risk (`meta.risk_edges`), not a generator.
- **C3, missing control or generator.** A gap is a named control that the actor could adopt and has not, or has
  adopted weakly; it is what the stack's coverage map shows, not an entry here. A generator is the reason it did not
  (commercial pressure, culture, race, capture), a condition no actor in scope controls (the state of assurance
  science, the offence-defence balance), or a property that defeats controls whether or not they are present
  (opacity, evaluation awareness). "Monitoring fails because monitoring is weak" adds nothing. "The evaluation
  under-elicited the model" is a gap; "the model recognised the evaluation" is `ca.situational-awareness`.
- **C4, measurement: capability or propensity.** A property measured by eliciting the harmful behaviour is a
  propensity and belongs to the risks (the `ma` risks are propensities and behaviours). A property measured on a task
  that is not the harm (telling an evaluation transcript from deployment; planning over 50 steps) is a capability and
  is a generator. Label the proposition, not the experiment: one passage can support both.
- **C5, actors.** The existence and motives of attackers are a generator (`ad.motivated-actors`); the attack is a
  risk.
- **C6, common-cause candidates.** A generator gets `common_cause` when one mechanism may degrade two or more layers
  counted against the same risk. `mech` is the coupling (`substrate`, `convergent`, `operational`, `institutional`,
  `epistemic`, `environmental`), `scope` whether it couples layers of one stack or many models and developers,
  `searched_by` whether an optimiser (the model, an attacker, selection) searches for the joint hole.
- **C7, typical role.** `hazard` enlarges the potential for harm, `cause` raises the rate of risk events, `barrier`
  degrades defences. The same generator can play another role against another endpoint; the role in the file is the
  typical one.

## Annotation

As for risks ([../risks/README.md](../risks/README.md#annotation)): explicit only, each label with a quoted evidence
span and a relation (`discusses`, `mitigates`, `measures`, `demonstrates`); a family id alone when the document
engages a family generically and no generator fits; passing mentions stored and left out of views. A label means
"this document supports this claim", never "this developer has this condition"; what a document does not mention
stays unknown. Only `annotate`-tier generators are offered to annotators, and `background` ones only when the
argument depends on them. The draft prompt for 0.3.0 (not yet run) replaces explicit and implicit, which carried
little information, with a stance (`asserts`, `mentions`, `mitigates`, `demonstrates`, `measures`), co-annotates
risks so that C4 can be tested, and lets an annotator record a gap ("control deficiency, cause unstated").

## Pilot

The trial annotated draft v0.2 (57 leaves), not 0.3.0; 0.3.0 is v0.2 revised from the trial and two blind reviews by
language models of different families ([CHANGELOG.md](CHANGELOG.md)).

- **Sample.** 100 documents from the dataset, purposive and picked by keyword to be rich in generators (15 strata of
  3-10 documents), not random. Each annotator saw title, abstract and at most 1,500 words of text, selected toward
  causal and risk vocabulary, so the motivation and limitations passages are over-represented.
- **Annotators.** Three language models, blind to each other, with identical prompts: Claude Opus 5.5 and two GPT-6
  variants (through Codex).
- **Agreement** (mean pairwise Jaccard over each document's label set). Leaf: 0.68 over all pairs, 0.59 between Opus
  and GPT-6; family: 0.78 and 0.72. The two GPT-6 variants agree with each other at 0.84 (leaf), so the all-pairs
  figures and the label-weighted Fleiss kappa (0.79 leaf, 0.83 family) are inflated by the shared model family; the
  cross-family figure is the honest one.
- **Use.** 87 documents had at least one majority leaf (2.43 on average); three leaves were never used. Relations:
  `discusses` 558, `mitigates` 91, `demonstrates` 71, `measures` 22. 86-95% of labels were marked explicit.
- **Common causes.** Documents often name a generator that could couple layers (127 of 243 majority labels carry a
  common-cause candidate), but an explicit statement that layers fail together appeared in 2 of the 100 documents.
  Per-document annotation will not fill the common-cause view; it has to come from curated edges, with documents as
  evidence for single edges.
- **Recommendation of the draft:** no corpus-wide annotation yet. First a curated generator × technique-family matrix
  (`reduced_by`, `assessed_by`, `defeats` and the risk edges), drafted by a model and reviewed by a person. Then a
  second trial (about 300 random documents plus targeted cases, annotators from at least two model families, full
  texts or random excerpts, about 50 documents adjudicated by a person) before deciding on per-document labels.

Caveats: agreement is not accuracy, and there are no human labels; two of the three annotators are one model family;
the sample is purposive and the excerpts favour causal language, so label rates are not corpus rates; the
"negative controls" were not negatives (2 of 3 got majority labels, legitimately).
