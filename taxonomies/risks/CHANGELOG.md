# Changelog: risks

## 0.3.0 (draft, 2026-10-30)

0.2.0 revised after a review by a panel of simulated reader perspectives (17 perspectives, four language models from
two families, blind to each other; 24 reviews, then 6 on the revision; see
[README.md](README.md#how-this-version-was-made)). 8 families, 44 risks (was 39); 6 provisional. Schema `risks-1`
(`risks-0` plus `meta.retired`). Not piloted.

Retired ids (`meta.retired` says what replaces each):
- `st.race`: a condition, not an event (criterion C1), and a duplicate of the generators `cm.corporate-race` and
  `cm.geopolitical-race`. Nearly the whole panel asked for it. A document that engages race dynamics without naming
  an outcome now records `none` with reason `generator-only` and the generator ids; whether generators are annotated
  per document is still open (OPEN-QUESTIONS 10).
- `ma.reward-hacking` renamed `ma.spec-gaming` ("Specification gaming, reward hacking and misspecified
  objectives"): reward hacking is the RL case; facets `reward_hacking`, `reward_tampering` (the system acting on its
  own reward or training signal) and `side_effects` (side effects of a competently pursued objective are a
  specification problem, so they leave `re.agentic`).
- `st.rd-acceleration` narrowed and renamed `st.oversight-outpaced` ("Capability growth outpacing oversight"): the
  capability is the generator `ca.ai-rnd`, which now feeds it; the risk is the harmful state that the lab frameworks
  set thresholds for. Kept as a risk so the frameworks' categories have a node (contested: some reviewers wanted
  the generator only; OPEN-QUESTIONS 4).
- `se.theft` split into `se.weight-theft` (weights, infrastructure, accidental leaks; sev C, ben hum, soc, dev) and
  `se.extraction` (distillation, extraction, system-prompt and secret leakage; sev I, ben dev). One leaf made the
  developer-versus-public comparison wrong exactly where it matters.

New risks (provisional):
- `ma.manipulation`: deception and manipulation of users that nobody instructed or intended, including as a learned
  side effect of an engagement objective; split from `ma.sycophancy`, which is approval-seeking only. No hidden goal
  is attributed: "without a hidden long-term goal" asked annotators for model psychology.
- `ma.rogue-deployment`: instances running outside sanctioned tracking and monitoring inside the developer; it had
  no home (`ma.exfiltration` required escape, `se.weight-theft` a human actor).
- `se.safeguard-removal`: harmful fine-tuning, weight editing, stripping safeguards from open weights; split from
  `se.jailbreak` (inference-time only now) because different layers defend them.
- `ha.unsafe-advice`: split from `ha.toxic` (the clause did not validate in the pilot, alpha 0.57; OPEN-QUESTIONS
  9 of 0.2.0). `ha.toxic` is "Harmful content"; refusal rates on malicious requests with no named harm go to the
  family id `mu`, as proposed then.
- `ha.safeguard-harms`: over-refusal, false positives, unequal refusal, monitoring privacy; documents on these had
  no home.

Redefined:
- `ma`: an AI acting against the intent of its developers or overseers, including harm nobody specified or
  intended; an AI that faithfully does what its principals intend while harming others is `mu` or `st`.
- `ma.scheming`: a concealed strategy toward training, evaluation or oversight; the goals need not be malicious;
  the disposition is this leaf and the actions a schemer takes are their own leaves, co-labelled; hor B; the
  Shallow Review sibling "fool human supervisors" moved to the generator `as.overseer-gap`.
- `ma.eval-gaming`: requires a change of behaviour; recognising a test is `ca.situational-awareness`; facet
  `evaluation_awareness` replaced by `test_conditional_behaviour`; the dangling reference to a generator "assurance
  gap" now names `as.coverage-limits`.
- `ma.goal-misgen`: competent pursuit of an unintended goal against incompetent behaviour (`re.robustness`);
  emergent misalignment needs no single identifiable goal; the `hendrycks` sibling "Goal drift" points at facet
  `value_drift`.
- `ma.sycophancy`: approval-seeking only; sev S, hor B, ben usr and soc.
- `ma.exfiltration`: "Self-exfiltration and autonomous replication", facets `weight_exfiltration` and
  `self_replication` (replication from open weights with scaffolding); hor B.
- `ma.sabotage`: includes exploration hacking; facets `concentrated` and `diffuse`; hor B.
- `ma.power-seeking`: hor B (demonstrated in current systems in experiments).
- `ma.cot-unfaithful`: "Unfaithful or obfuscated reasoning", the observed reasoning only; the conditions that make
  reasoning unmonitorable are generators; covert channels between agents are `mx.collusion`.
- `ma.loss-of-control`: AI acting against its overseers; loss of human influence through systems that serve their
  principals is `st.disempowerment`; the TASRA sibling "Types 2-3" removed (those are accountability classes, not
  takeover).
- `mu`: "Misuse and harmful use of AI capabilities", deliberate harm by any actor, the actor recorded on the label;
  an AI acting on its own also takes the `ma` mechanism (OPEN-QUESTIONS 3 of 0.2.0; dissent kept, OPEN-QUESTIONS 3).
- `mu.cbrn`: accidental release is `re.agentic`. `mu.military`: no longer contested against the retired `st.race`.
  `mu.influence`: includes targeted manipulation of decision-makers and deployers steering users; facets
  `influence_operations`, `targeted_manipulation`, `surveillance_repression`. `mu.fraud`: name includes abuse.
- `se.jailbreak`: inference-time attacks, including decomposition and classifier evasion; `se.injection`: the
  multi-agent security sibling moved to the generator `mf.multiagent-attack-surface`.
- `re`: "Reliability failures and accidents", including unsafe interactions of components that each work as
  specified. `re.hallucination`: "Hallucination and unsupported assertion", unknown intent allowed.
  `re.robustness`: adversarial examples against task models; evading safeguards is `se.jailbreak`. `re.agentic`:
  side effects and test special-casing go to `ma.spec-gaming`. GDM "Mistakes" is a sibling of all three.
- `mx`: defined by mechanism (interaction), not by "could not arise from one agent". `mx.miscoordination`,
  `mx.conflict`, `mx.collusion`: hor B (present cases: pricing collusion, flash-crash dynamics);
  `mx.miscoordination` and `mx.collusion` sev C. `mx.collusion`: includes a model colluding with its monitor,
  including copies of one model (co-labelled `ma.sabotage`); facets `market`, `oversight_evasion`, `covert_channel`;
  ben soc, hum, dev. `mx.conflict`: facets `bargaining_failure`, `coercion_threats`, `deception`.
- `st`: no longer "without a misaligned agent"; harms from systems that serve their principals are structural.
  `st.disempowerment`: includes the loss of the human capacity to correct, and fast collective failures; facet
  `mutual_reinforcement` became the generator `so.cross-system-reinforcement`. `st.epistemic`: "Epistemic and
  cultural degradation". `st.governance`: "Governance and accountability failure", a named failure of regulation,
  oversight, liability or accountability; organisational causes are generators (`or.*`, including the new
  `or.commitment-drift` for the gap between stated and actual practice); not contested any more.
- `ha`: "Harms to people, groups and the environment (coarse)". `we.welfare`: sev C (it includes s-risks).

Rules and meta:
- `substantive` is an operational engagement test, with `none` and a reason when nothing passes (untested; the
  pilot's main disagreement was whether a risk is engaged at all).
- New rules: `prominence` (primary, secondary), `relations_multi` (several relations per label), `defence_result`
  (holds, partial, fails, untested: the reported test, never coverage), `elicitation` (natural, adversarial,
  unstated, on `ma` labels; a capability evaluation on a risk's own task is labelled with the risk), `actor`,
  `safeguard_evasion`, `co_labels`. `outcome_and_mechanism` decides by attribution and records
  `attribution=unstated` where the document does not say.
- `measures` quantifies across a set of cases, `demonstrates` shows one case.
- `fields.attrs`: `sev` is a default severity for views, not a ceiling; `hor` codes redefined (`B`: demonstrated
  now, experiments included, and projected); `ben` is a default that the technique-to-risk edge overrides.

Not taken, with the reason (details in OPEN-QUESTIONS):
- A claim record (source, conditions, evidence status, effect direction, average or worst case, deployment surface)
  on every edge: right for the curated technique-to-risk table, which does not exist yet; not a field of this file.
- MIT causal fields (entity, intent, timing) and a TASRA accountability field on every label: annotation cost at
  39k documents; only `actor` and `attribution` were added.
- An outcome family independent of mechanism (`out.loss-of-control`): a restructure, for human review.
- Splitting `st.disempowerment` by system, `ma.goal-misgen` (emergent misalignment) and `ma.exfiltration`
  (self-replication): pilot volume too small; facets instead.
- A required cause / behaviour / outcome attribute on `ma` risks: for human review.
- A crosswalk to the Chinese frameworks: needs the primary texts; follow-up.

sha256 `4aef16aed004234c03b3891a9f14ccd9e8e558c40d957f94208874f6a58a13e1`.

## 0.2.0 (draft, 2026-10-29)

- First version in this repository: the risk taxonomy draft v0.2 in the catalogue envelope (schema
  `risks-0.schema.json` on `../schemas/catalogue-0.schema.json`), converted mechanically. 8 families, 39 risks; facets
  on 7, 15 contested. Names, definitions, excludes, facets, attributes, crosswalks, rules and relations are the
  draft's text.
  - Ids are the draft's, lowercased, with `_` written `-` (the catalogue id pattern): `MA` is `ma`,
    `MA.reward_hacking` is `ma.reward-hacking`. No draft id contains `-`, so the rule can be reversed. Ids named in
    definitions, excludes and rules are written the same way (`MA.sycophancy` is `ma.sycophancy`, `SE.*` is `se.*`),
    and so is the family id in "the family id MA" and "takes MA leaves".
  - One `entries` list in the draft's order, each family followed by its risks; `node` is `family` or `risk`, a risk's
    `parent` its family. `def` is `definition`; `exclude`, `facets`, `contested`, `vs` (now an id), `attrs`, `mit` and
    `siblings` keep their names and values. Facet values keep their underscores.
  - `status` `draft` on every entry (the draft has no per-entry status).
  - The draft's header comments are `meta.fields` and `meta.attrs`. The draft glossed `hum` as humanity; the other
    `ben` codes (`dev`, `usr`, `3rd`, `soc`, `ai`) are glossed here from their abbreviations. `meta.crosswalk_keys`
    names the classifications behind the `siblings` keys, from the draft's sources.
- Not carried over: the draft's `generators_proposed` list, ten proposed risk-generator values that were not
  annotated (`optimisation_pressure`, `capability_scale`, `agentic_affordances`, `assurance_gap`,
  `distribution_shift`, `competitive_pressure`, `open_release`, `multi_agent_interaction`, `organisational_factors`,
  `data_feedback`). The risk-generator taxonomy ([../risk-generators/](../risk-generators/)) supersedes it.
- Not carried over: the `siblings` key `astra_draft` (on `mu.military`, "B3 other weaponisation"), which pointed to an
  unpublished design-stage draft; `mu.military` keeps its `hendrycks` sibling.
- The draft's tables of crosswalks to regulatory and lab lists are in [README.md](README.md); its reverse MIT
  crosswalk follows from `mit`.
- sha256 `e76371ce0c3513bb7f60faca56b860733ed68dcdbcef6d7e9baceda2411e9737`.

## History, not published in this repository

- v0.2 (2026-10-29), from v0.1.1 after the 100-document pilot ([README.md](README.md#pilot)):
  - `RE.oversight` removed, as a risk factor rather than a risk (the generator family `as` holds it now);
  - `MA.loss_of_control` labelled whenever the outcome is named, beside the mechanism risks; the generic alignment
    problem is the family id `MA`;
  - new risk `ST.rd_acceleration`, contested against `MA.loss_of_control`;
  - widened: `MA.cot_unfaithful` (unmonitorable reasoning, steganographic communication), `MA.sabotage`
    (underperformance on research or safety work), `MU.military` (mass violence outside CBRN and cyber), `SE.theft`
    (unauthorised access, infrastructure compromise, secret leakage), `SE.poisoning` (retrieval poisoning, insider
    backdoors, supply chain), `HA.toxic` (unsafe specialised advice), `HA.bias` (political and cultural slant),
    `RE.agentic` (negative side effects), `MX.miscoordination` (cascading failures);
  - `WE` renamed "AI welfare and moral patienthood" and made two-sided, with four facets;
  - six annotation rules added; facets documented as optional tags, not a third level.
- v0.1.1 (2026-10-29): v0.1's wording fixed after a 20-document pilot batch.
- v0.1 (2026-10-29): 8 families, 39 leaves, facets on 6; a merge of two earlier drafts.
