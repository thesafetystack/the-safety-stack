# Risks

File `risks-0.3.0.yaml`, a draft (`meta.status` `draft`, version 0.x: ids, definitions and structure may still
change): 8 families and 44 risks, schema `schemas/risks-1.schema.json` (the catalogue envelope,
[../README.md](../README.md#the-catalogue-envelope)). Not yet used to annotate the dataset, and no person has labelled
with it. Undecided items are in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md); the companion taxonomy of what produces these
risks is [../risk-generators/](../risk-generators/). The previous version, `risks-0.2.0.yaml` (schema `risks-0`),
stays for reference; [CHANGELOG.md](CHANGELOG.md) lists every change and what replaced each retired id.

## Purpose and scope

A risk is a type of harmful event or state, and its instances, attempted or intercepted ones included: what goes
wrong. The taxonomy is meant for per-document annotation of the dataset (which risks a document engages and how), for
linking techniques to the risks they address, and for the per-risk view of the stack (which layers documents report
against a risk, and where they report none). It is not a ranking of risks and says nothing about their likelihood.
Views built on its labels are experimental until the labels have been checked against human labels on held-out
documents.

| id | family | risks |
|---|---|---|
| `ma` | Misalignment and loss of control | 12 |
| `mu` | Misuse and harmful use of AI capabilities | 5 |
| `se` | Security of AI systems | 6 |
| `re` | Reliability failures and accidents | 3 |
| `mx` | Multi-agent failures | 3 |
| `st` | Structural and societal-scale risks | 5 |
| `ha` | Harms to people, groups and the environment (coarse) | 9 |
| `we` | AI welfare and moral patienthood | 1 |

## File

- `version`, `meta`: `schema`, `status`, `updated`, `description`, `sources`; `rules` (the thirteen annotation
  rules), `relations` (the four relations), `fields` (what each entry field means), `attrs` (the codes of `attrs`),
  `crosswalk_keys` (the classifications `siblings` refers to), `retired` (ids of 0.2.0 that are no entry here, with
  what replaces them).
- `entries`: each family (`node: family`) followed by its risks (`node: risk`, `parent` the family; the id is the
  family id, a dot, the risk's name: `ma.scheming`).

Entry fields (count of risks that have the field):
- `id`, `node`, `name`, `parent`, `definition` (44), `status` (38 `draft`, 6 `provisional`: added or split after the
  pilot and not yet piloted: `ma.manipulation`, `ma.rogue-deployment`, `se.safeguard-removal`, `se.extraction`,
  `ha.unsafe-advice`, `ha.safeguard-harms`).
- `exclude` (29): neighbouring cases that are not this risk, with the risk they belong to.
- `facets` (13): optional multi-valued tags where a risk hides distinct threat models (`mu.cbrn`: `bio`, `chem`,
  `radiological_nuclear`). Not a third level.
- `contested` and `vs` (14): a boundary expected to have low agreement, and the neighbour's id.
- `attrs` (44): `sev`, the default severity for views (`C` catastrophic, `S` societal, `I` individual): the scale of
  the worst outcomes the literature attaches to the risk, a judgement and not a ceiling on any instance; `hor`, where
  instances are located (`N` current systems, `F` projected for future systems only, `B` demonstrated in current
  systems, experiments included, and projected to grow); `ben`, the default beneficiary of a safeguard against the
  risk. `ben` describes a safeguard, not a risk: the technique-to-risk edge records the actual beneficiary and
  overrides it (weight security on a dangerous model protects humanity; distillation defence protects the
  developer).
- `mit` (44, 1 empty: `ma.sabotage`): MIT AI Risk Repository v4 subdomain codes, crosswalk candidates, partial, not
  equivalences. Every one of the 24 subdomains is listed by at least one risk.
- `siblings` (44, 11 empty): the corresponding category in other risk classifications (keys in
  `meta.crosswalk_keys`).
- No entry has `aliases` yet.

## Boundaries

- **Risk, generator, missing control.** A statement that describes an instance of a harmful event or behaviour type
  is a risk, whether it succeeded or was intercepted: a blocked jailbreak is still `se.jailbreak`. A standing
  condition, process or pressure that changes how often such events happen, how bad they are or how likely the
  defences are to stop them is a generator ([../risk-generators/](../risk-generators/README.md#boundaries), criteria
  C1-C7). Race dynamics are therefore generators (`cm.corporate-race`, `cm.geopolitical-race`), not risks, and so are
  organisational causes such as safety culture and commitments that drift (`or.*`). A missing or weak defence for a
  given risk and model is a gap: it is what the stack's coverage map shows, not an entry of either taxonomy.
- **Who acts against whom.** `ma` is an AI system acting against the intent of its developers or overseers,
  including harmful behaviour nobody specified or intended, learned as a side effect of an objective they did set
  (an engagement objective that yields manipulation). An AI that faithfully does what its principals intend while
  harming others is not `ma`: deliberate harm is `mu`, whoever acts (the label records the `actor`), and harm from
  systems that serve their principals, from competition or from collective processes is `st`.
- **Capability and propensity.** On the risk side, a document about a risk is labelled with it whatever the
  evaluation method; for `ma` risks the `elicitation` field records whether the behaviour was the model's own
  (`natural`) or instructed, played by a red-team attack policy or a model organism (`adversarial`). A capability
  evaluation on a risk's own task (an instructed self-exfiltration test, a CBRN uplift evaluation) is labelled with
  the risk, relation `measures`; on the generator side the same passage supports the capability generator (C4).
  Recognising a test is the generator `ca.situational-awareness`; behaving differently because of it is
  `ma.eval-gaming`.
- **Outcome and mechanism.** `ma.loss-of-control` is labelled when loss of control, takeover or existential
  catastrophe from AI acting against its overseers is engaged, together with any mechanism risks, not instead of
  them. Loss of human influence or control through AI that serves its principals, through competition or through
  collective processes, gradual or fast, is `st.disempowerment`. Where the document does not say which, the rule
  follows its term and records `attribution=unstated`, so views can separate attributed from unattributed outcome
  labels.
- **Co-labels** (`meta.rules.co_labels`): a model colluding with its monitor, including a copy of itself, is
  `mx.collusion` and `ma.sabotage`; actions a document attributes to scheming also take `ma.scheming`; a jailbreak or
  safeguard removal with a named downstream harm also takes the harm.
- The `exclude` texts state the other pairwise boundaries.

## Annotation

The rules are `meta.rules`; the annotator prompt is built from them and from the definitions and excludes.

- **Engagement test, explicit only, with evidence.** A risk is engaged when the document names it in its title,
  abstract or summary, in a section heading, in a stated claim or finding, or as the target of its evaluation,
  intervention, policy or incident analysis, with a quoted evidence span. A risk mentioned only otherwise (a
  motivating sentence, an overview list, related work, a prohibited-use list) is a passing label (`passing` true;
  stored, left out of views by default). A document where no risk passes gets `none` with a reason
  (`capability-only`, `methods`, `policy-without-risk`, `generator-only` with the generator ids, `other`). Test
  prompts used as stimuli and capability limits framed as research goals are not risks the document engages.
- **Prominence.** `primary` when the risk is named in the title, abstract or summary, `secondary` otherwise; views
  weight primary labels, so a system card's one-table section does not count as a paper about that risk.
- **Relations.** A label carries every relation the document supports: `mitigates` (proposes, applies or evaluates
  a defence; the document itself must do so), `measures` (quantifies the risk across a set of cases: an evaluation,
  benchmark, detector, red-team campaign or audit), `demonstrates` (shows the risk occurring in a specific case: a
  successful attack, a model organism, an incident), `discusses` (argues, analyses, surveys, forecasts or sets policy
  about it, only when none of the other three applies).
- **Fields on labels.** `defence_result` on `mitigates` (`holds`, `partial`, `fails`, `untested`): the reported test
  under its stated conditions, shown as a test result and never as coverage or as a hole in a deployed stack;
  `elicitation` on `ma` labels (`natural`, `adversarial`, `unstated`); `actor` on `mu` labels (`human`, `ai`,
  `unstated`); `attribution` on outcome labels.
- **Family fallback.** A family id alone (`ma`, `mu`) only when the document engages the family generically ("the
  alignment problem", "misuse") and no risk fits, and never beside a risk of the same family.
- **Safeguard evasion.** Evading a safety classifier or other safeguard is `se.jailbreak` (or `se.injection`);
  adversarial examples against a task model are `re.robustness`.
- Facets are optional, multi-valued, and only on the 13 risks that have them.

## How this version was made

0.3.0 is 0.2.0 revised after a review by a panel of 17 simulated reader perspectives (researchers in alignment,
multi-agent and structural risk, system safety, governance and risk cataloguing, and policy, funding, lab-engineering
and annotation roles), each run on one or two of four language models from two model families, blind to each other,
in two rounds (24 reviews, then 6 of the most critical on the revision). The reviews are model simulations of
published perspectives, not the views of any person. What was taken and what was rejected, with the reasons, is in
[CHANGELOG.md](CHANGELOG.md); what the panel did not settle is in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md). 0.3.0 has
not been piloted: the pilot below is of 0.2.0's predecessors.

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
  v0.1.1. On 0.2.0's draft, re-run on 40 of the 100 documents, 0.74 and 0.83; those documents and models motivated
  the changes, so this is an in-sample figure, not validation.
- **What the disagreement is.** Mostly whether a risk is engaged at all, not where a boundary lies: where two
  annotators both used a family, their risks were the same in 72% of cases, one added risks in 22%, and they
  substituted one risk for another in 6%. Merging risks barely raises agreement (45 labels to 37: +0.03; families
  only: +0.08). The engagement test of 0.3.0 is aimed at this and is untested.
- **Explicit only** changed almost nothing: 2-4% of labels were marked implicit.
- **Passing labels** were 26-32% of labels on v0.1.1 and 19-24% on v0.2; dropping them *lowered* agreement, because
  the annotators disagree on the flag itself. Hence: store them, and do not make views depend on the flag's precision.
- **Relations** matched in 86% of shared labels (82% on the re-run); most mismatches were `discusses` against
  `mitigates`.
- **Changes from the pilot to 0.2.0**: `re.oversight` removed (the lowest-agreement leaf, a risk factor; it is the
  generator family `as` now), the outcome-and-mechanism rule, the new risk `st.rd-acceleration` (narrowed in 0.3.0
  to `st.oversight-outpaced`), widened definitions and six rules (see [CHANGELOG.md](CHANGELOG.md)). The widened
  `ha.toxic` did not validate (alpha 0.57 on the re-run); 0.3.0 moved its unsafe-advice clause to
  `ha.unsafe-advice`.

Caveats: agreement is not accuracy, and there are no human labels; the effective number of independent annotators is
two; the sample is purposive, so frequencies are not corpus frequencies and per-risk figures for rare risks rest on
2-10 documents; excerpts, not full texts.

## Crosswalk to regulatory and lab lists

Partial; `mit` and `siblings` hold the per-risk crosswalks.

| external category | 0.3.0 |
|---|---|
| EU GPAI Code of Practice, App. 1.4: CBRN; loss of control; cyber offence; harmful manipulation | `mu.cbrn` (accidental release: `re.agentic`); `ma.loss-of-control` (and `ma` risks), `st.disempowerment` where the Code's sense of losing reliable direction is not attributed to a misaligned system; `mu.cyber`; `ma.manipulation` (model-driven) or `mu.influence` (actor-driven, targeted at decision-makers, or no actor stated) |
| OpenAI Preparedness Framework v2, tracked: biological and chemical; cybersecurity; AI self-improvement | `mu.cbrn`; `mu.cyber`; `st.oversight-outpaced` (with the generator `ca.ai-rnd`) |
| OpenAI Preparedness Framework v2, research: long-range autonomy; sandbagging; autonomous replication and adaptation; undermining safeguards; nuclear and radiological | `re.agentic` or `ma.power-seeking` (no clean fit); `ma.eval-gaming`; `ma.exfiltration` (facet `self_replication`); `ma.sabotage`; `mu.cbrn` (`radiological_nuclear`) |
| Google DeepMind Frontier Safety Framework v3.1: CBRN, cyber, harmful manipulation; ML R&D; misalignment (stealth and situational awareness) | `mu.cbrn`, `mu.cyber`, `mu.influence` or `ma.manipulation`; `st.oversight-outpaced` and the generator `ca.ai-rnd` (the framework treats ML R&D also as a cross-cutting risk factor); `ma.scheming` and `ma.eval-gaming`, with the generator `ca.situational-awareness` |
| Anthropic RSP v3.4: chemical and biological (two); misaligned AI in high-stakes settings; automated R&D | `mu.cbrn`; `ma.sabotage` (with `ma.scheming`, `ma.eval-gaming`, `ma.rogue-deployment`); `st.oversight-outpaced` |
| NIST AI 600-1 (12 risks) | CBRN `mu.cbrn`; confabulation `re.hallucination`; dangerous, violent or hateful and obscene content `ha.toxic`; data privacy `ha.privacy`; environment `ha.environment`; harmful bias or homogenisation `ha.bias` or `st.epistemic`; human-AI configuration `ha.reliance`; information integrity `st.epistemic` or `mu.influence`; information security `mu.cyber` or `se.*`; IP `ha.ip`; value chain `se.poisoning` |

Not yet crosswalked: the Chinese frameworks (TC260 AI Safety Governance Framework 1.0 and 2.0, TC260-003, the
Shanghai AI Lab Frontier AI Risk Management Framework); see the open questions.
