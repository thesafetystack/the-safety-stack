# Risk generators

File `risk-generators-0.4.0.yaml`, a draft (`meta.status` `draft`, version 0.x: ids, definitions and structure may
still change): 10 families and 74 generators, schema `schemas/risk-generators-1.schema.json` (the catalogue envelope,
[../README.md](../README.md#the-catalogue-envelope)). It refers to the risk taxonomy 0.3.0 (`meta.references.risks`,
[../risks/](../risks/)). Not used to annotate the dataset; neither 0.3.0 nor 0.4.0 has been annotated with. Undecided
items are in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md). The previous version, `risk-generators-0.3.0.yaml` (schema
`risk-generators-0`, on risks 0.2.0), stays for reference; [CHANGELOG.md](CHANGELOG.md) lists every change.

## Purpose and scope

A generator is a standing condition, process or pressure that changes how often a risk event happens, how bad it is,
or how likely the defences are to stop it, and is not itself an instance of a harmful event type: what produces the
risks of [../risks/](../risks/). The taxonomy serves the stack's view of why defences fail together: defence in depth
works only as far as its layers fail independently, and a generator that degrades several layers counted against the
same risk is a candidate common cause. It links generators to the risks they feed or whose defences they weaken, and
to the technique families that reduce, measure or worsen them. Every link is a hypothesis to be curated, with a
source, by a person: none is a finding.

| id | family | generators | `curated` | common-cause candidates | provisional |
|---|---|---|---|---|---|
| `tr` | Training and optimisation | 8 | 0 | 5 | 1 |
| `ca` | Capabilities and cognition | 8 | 0 | 4 | 0 |
| `as` | Limits of assurance and oversight | 8 | 4 | 8 | 3 |
| `dp` | Deployment and affordances | 12 | 2 | 4 | 2 |
| `su` | Shared components, processes and monoculture | 7 | 6 | 7 | 1 |
| `or` | Developer and deployer organisations | 4 | 0 | 4 | 1 |
| `cm` | Competition and geopolitics | 6 | 2 | 4 | 1 |
| `ad` | Adversaries and offence-defence balance | 4 | 1 | 1 | 0 |
| `mf` | Multi-agent interaction factors | 8 | 2 | 2 | 0 |
| `so` | Societal and structural | 9 | 2 | 6 | 1 |

## File

- `version`, `meta`: `schema`, `status`, `updated`, `description`, `sources`, `references` (`risks: 0.3.0`); `fields`
  (what each entry field means), `technique_families` (the 22 values of `reduced_by`, `assessed_by`, `worsened_by`,
  `defeats` and `bypasses`), `crosswalk_keys` (the frameworks the `crosswalks` strings start with), `risk_edges`,
  `retired` (ids of 0.3.0 that are no entry here, with what replaces them).
- `entries`: each family (`node: family`) followed by its generators (`node: generator`, `parent` the family; the
  id is the family id, a dot, the generator's name: `ca.situational-awareness`).
- `meta.risk_edges` (12): edges from a risk, not a generator: `defeats` (technique families whose layers the risk,
  once present, degrades: a scheming model defeats behavioural evaluations), `bypasses` (layers it skips: stolen
  weights skip every deployment-time layer), `escalates_to` (risks it leads to), `searched_by`.

Generator fields (count of generators that have the field):
- `id`, `node`, `name`, `parent`, `definition` (74); `status` (64 `draft`, 10 `provisional`: `tr.shallow-safety`,
  added from trial misfits with thin support, and nine added by the 2026-10-30 review with no trial support).
- `tier` (74): `annotate` (55), a candidate for per-document labels; `curated` (19), for edges and the coverage map
  only, rarely stated in text (eight of the nine generators the review added are curated).
- `background` (3: `ca.capability-level`, `dp.scale`, `as.immature-science`): label only when the document's
  argument depends on it, never for motivation boilerplate.
- `role` (74): the typical role, one or more of `hazard` (19), `cause` (29), `barrier` (43); see C7 below.
- `feeds` (48) and `weakens` (40): references `{id, name}` to risks 0.3.0 (a family id stands for the whole family);
  every generator has at least one, and every risk is linked from at least one generator, directly or through its
  family. `weakens` is for barrier-role generators.
- `reduced_by` (74), `assessed_by` (16) and `worsened_by` (4): technique families that act on the generator, measure
  it without reducing it, or whose use can intensify it (monitors and interpretability used as a training signal for
  `tr.optimising-against-oversight`; reasoning RL for `tr.outcome-optimisation`; AI feedback for `tr.ai-signal`;
  safety training's capability externalities for `ca.capability-level`). `non-technical` and `none-linked` (no
  family is linked in this file, which does not claim that none exists) are values too. 34 generators have only
  `non-technical` or `none-linked`.
- `amplifies` (4): other generators this one strengthens (feedback loops and compounding risk factors:
  `mf.information-asymmetry` → `mf.commitment-trust`, `mf.network-effects` → `mf.selection-pressure`,
  `so.reduced-human-reliance` ↔ `so.adoption-pressure`, → `so.cross-system-reinforcement`).
- `common_cause` (45): a candidate common-cause mechanism, a hypothesis, never a measured correlation: `mech`,
  `scope`, `searched_by`, `defeats` (technique families), `note`. An absent record means no mechanism is named
  here; it does not claim that layers fail independently.
- `contested` and `vs` (8): a weak boundary, and in words against what.
- `crosswalks` (74): the corresponding item in other frameworks (`meta.crosswalk_keys`); `trial` for a generator from
  the annotation trial's misfit notes, `review` for one the 2026-10-30 review added. `note` (11).
- No entry has `aliases` yet.

The technique families are those of the techniques taxonomy's 0.8 draft, which is not published here (techniques 1.x
has no families), plus `cooperative-ai` (bargaining, commitment and mechanism-design methods, so that multi-agent
factors are not shown as having no technique), `security-access-control` (weight security, insider controls, access
tiers, account enforcement), `control-protocols` (trusted monitoring, trusted editing, resampling: split from
`agentic-control`) and `control-evaluations` (evaluations against a red-team attack policy: split from
`redteam-eval`), and `non-technical`; they do not resolve against [../techniques/](../techniques/). Mapping them to
the published technique taxonomy comes before any edge is curated (OPEN-QUESTIONS 10).

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
- **C4, capability or propensity: who supplies the intent.** Behaviour the model produces on its own, sampled under
  stated conditions, is a propensity and belongs to the risks (the `ma` risks are propensities and behaviours).
  Behaviour produced on instruction, played by a red-team attack policy or a model organism, and performance on a
  task that is not the harm (telling an evaluation transcript from deployment; planning over 50 steps) measure a
  capability, which is a generator. Recognising a test is a capability (`ca.situational-awareness`); behaving
  differently because of it is the risk `ma.eval-gaming`. Label the proposition, not the experiment, and label both
  sides when a passage supports both: a capability evaluation on a risk's own task (an instructed self-exfiltration
  test) is the risk with relation `measures` and `elicitation: adversarial` on the risk side, and the capability
  generator (`ca.evasion-replication`) here. (0.3.0 drew the line by whether the measured task was the harm; that
  misfiled instructed tests and control evaluations.)
- **C5, actors.** The existence and motives of attackers are generators (`ad.non-state-actors`, `ad.state-actors`);
  the attack is a risk.
- **C6, common-cause candidates.** A generator gets `common_cause` when one mechanism may degrade two or more layers
  counted against the same risk. `mech` is the coupling (`substrate`, `convergent`, `operational`, `institutional`,
  `epistemic`, `environmental`), `scope` whether it couples layers of one stack or many models and developers,
  `searched_by` whether an optimiser (the model, an attacker, selection) searches for the joint hole; `selection`
  also marks agent-agnostic processes (races, adoption pressure, arbitrage), which persist whoever the participants
  are and are reduced by changing the selection environment, not by fixing one actor. An absent record does not
  claim independence: independence is the hypothesis that would need evidence.
- **C7, typical role.** `hazard` enlarges the potential for harm, `cause` raises the rate of risk events, `barrier`
  degrades defences. The same generator can play another role against another endpoint; the role in the file is the
  typical one. (The role name `hazard` clashes with the safety-engineering sense, a system state that leads to a
  loss; see OPEN-QUESTIONS 9.)
- **Generator to generator.** `amplifies` records that one generator strengthens another; a loop
  (`so.reduced-human-reliance` ↔ `so.adoption-pressure`) is two entries. It is not a risk edge (C2): the risk
  produced is linked by `feeds`.

## Annotation

As for risks ([../risks/README.md](../risks/README.md#annotation)): explicit only, each label with a quoted evidence
span and a relation (`discusses`, `mitigates`, `measures`, `demonstrates`); a family id alone when the document
engages a family generically and no generator fits; passing mentions stored and left out of views. A label means
"this document supports this claim", never "this developer has this condition"; what a document does not mention
stays unknown. Only `annotate`-tier generators are offered to annotators, and `background` ones only when the
argument depends on them. The draft prompt for 0.3.0 (not yet run) replaces explicit and implicit, which carried
little information, with a stance (`asserts`, `mentions`, `mitigates`, `demonstrates`, `measures`), co-annotates
risks so that C4 can be tested, and lets an annotator record a gap ("control deficiency, cause unstated"). A risk
annotation that finds no risk but a generator records `none` with reason `generator-only` and the generator ids
([../risks/README.md](../risks/README.md#annotation)), so race, organisational and multi-agent documents are not
lost while per-document generator annotation is undecided.

Where neighbouring generators are named together, label the one the document varies, measures or blames:

- `tr.outcome-optimisation` (the strength and horizon of optimisation), `tr.gameable-grader` (the grader or
  environment that is exploited), `tr.proxy-objective` (the objective itself is wrong).
- Competition, by who is under pressure: `cm.corporate-race` (developers against each other), `cm.geopolitical-race`
  (states), `or.commercial-pressure` (priorities inside one organisation), `so.adoption-pressure` (adopters across
  the economy and the state), `mf.selection-pressure` (selection acting on AI systems' dispositions).
- The deployed system differs from the evaluated one: `dp.post-deployment-change` (weights or components changed),
  `dp.context-dependence` (harness, prompt or conversation), `dp.distribution-shift` (the world), `dp.scale` (how
  often rare failures occur), `as.coverage-limits` (what testing could sample).

## Pilot

The trial annotated draft v0.2 (57 leaves), not 0.3.0 or 0.4.0; 0.3.0 is v0.2 revised from the trial and two blind
reviews by language models of different families, and 0.4.0 is 0.3.0 revised after a review by a panel of 17
simulated reader perspectives in two rounds, run on four language models from two families
([../risks/README.md](../risks/README.md#how-this-version-was-made), [CHANGELOG.md](CHANGELOG.md)).

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
