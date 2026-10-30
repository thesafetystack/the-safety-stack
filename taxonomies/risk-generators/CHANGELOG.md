# Changelog: risk generators

## 0.4.0 (draft, 2026-10-30)

0.3.0 revised after the review that produced risks 0.3.0 (a panel of 17 simulated reader perspectives on four
language models, two rounds; [../risks/README.md](../risks/README.md#how-this-version-was-made)). 10 families, 74
generators (was 64; 55 `annotate`, 19 `curated`; 10 provisional; 45 with a common-cause candidate; 8 contested) and 12
risk edges (was 9). Refers to risks 0.3.0. Schema `risk-generators-1` (`risk-generators-0` plus `worsened_by`,
`amplifies` and `meta.retired`). Not annotated with.

- **C4 restated**: who supplies the intent decides (README, Boundaries). Instructed behaviour, a red-team attack
  policy or a model organism measures a capability; the model's own behaviour is a propensity; label both sides
  when a passage supports both. The old test (was the measured task the harm?) misfiled instructed tests and control
  evaluations. The `ca` family definition follows; `ca.evasion-replication`'s contested note says so.
- **References to risks 0.3.0**: `ma.reward-hacking` is `ma.spec-gaming`, `se.theft` is `se.weight-theft`, in every
  `feeds`, `weakens` and risk edge; every name is the risks file's. New links: `ca.ai-rnd` feeds
  `st.oversight-outpaced` (open question 4 of 0.3.0); `tr.human-data-priors` feeds `re.hallucination` (imitated
  falsehoods); `dp.irreversible-release` feeds `se.safeguard-removal` instead of `se.jailbreak`; `tr.shallow-safety`
  and `dp.post-deployment-change` weaken `se.safeguard-removal`; `or.commercial-pressure` feeds `ha.reliance` and
  `we.welfare`, `dp.scale` feeds `we.welfare`, and `as.immature-science` weakens `we.welfare` (open question 8 of
  0.3.0: no new family, edges instead).
- **New generators** (provisional; curated unless stated):
  - `as.trusted-capability-gap`: the models trusted not to scheme fall behind those they oversee; reduced by
    scalable oversight and non-technical means, assessed by control evaluations.
  - `as.per-interaction-scope`: safeguards judge one request or trajectory, so decomposed harm passes all of them
    together (convergent, searched by attackers).
  - `as.feedback-inadequacy`: the developer's picture of the deployed system stops matching it; contested against a
    gap (C3).
  - `dp.training-signal-access`: the system can influence its own reward, grader or training data (feeds reward
    tampering in `ma.spec-gaming`).
  - `dp.multi-principal-interaction`: delegates of many principals meet in one market, protocol or platform.
  - `su.shared-spec`: one usage policy or constitution generates the training data, classifier data, red-team targets
    and rubrics of every layer.
  - `or.commitment-drift` (annotate tier): commitments weaken as they start to bind; the gap between stated and actual
    practice, which risks 0.2.0 had inside `st.governance`.
  - `cm.coordination-deficit`: states cannot make or verify commitments with each other; contested against a gap
    (C3).
  - `so.cross-system-reinforcement`: the standing coupling between economy, culture and state through which a loss
    of human leverage in one weakens correction in the others (from the risk facet `mutual_reinforcement`).
- **Split and renamed**: `ad.motivated-actors` into `ad.non-state-actors` and `ad.state-actors` (a developer's
  safeguards do little against states; the TASRA types differ); `as.overseer-human-factors` into
  `as.oversight-loop-design` (the design of the oversight loop, not operators failing to check; the Reason "active
  failures" crosswalk replaced by STPA process models).
- **Edges fixed**:
  - `tr.optimising-against-oversight`: reduced by a non-technical decision (not to train or select against the
    monitor), assessed by interpretability and red-teaming, worsened by interpretability, guardrail classifiers and
    scalable oversight used as training signal; a note asks to record whether a document says monitor outputs were
    or were not used in training. 0.3.0 had interpretability reducing it, the reverse of the mechanism.
  - `tr.outcome-optimisation`: no longer reduced by `rl-reasoning`, which instantiates it (`worsened_by`).
  - `tr.ai-signal`: `constitutional-ai-feedback` moved from `reduced_by` to `worsened_by`.
  - `tr.underdetermination`: interpretability assesses it, does not reduce it.
  - `ca.capability-level`: `worsened_by` the safety-training families whose benchmarks track general capability (a
    family-level hypothesis, in a note).
  - `dp.scale`: guardrail classifiers do not reduce deployment scale; non-technical only.
  - `dp.internal-deployment`: reduced by control protocols.
  - `as.overseer-gap`: crosswalk "SR superintelligence can fool human supervisors" (moved from the risk
    `ma.scheming`).
  - `mf.mixed-motives` feeds `mx.conflict` and `mx.collusion`, not `mx.miscoordination` (miscoordination is the
    failure under compatible objectives); `mf.commitment-trust` covers harmful commitments (credible threats,
    commitment races) and also feeds miscoordination; `mf.network-effects` is a common-cause candidate
    (environmental, field); `mf.emergent-agency` feeds the `mx` family, not collusion; `mf.network-effects`,
    `mf.destabilising-dynamics` and `mf.emergent-agency` are assessed by red-team evaluation (multi-agent testbeds);
    `mf.selection-pressure` is annotate tier and reduced by cooperative-AI and non-technical means (it had
    `none-known` against the literature it cites).
  - `so.diffuse-responsibility`: also raises rates (role cause), feeds `st.disempowerment` and `mx`.
  - `or.safety-culture`: includes gradual migration toward the boundary of safe performance; labelled only when a
    document says how a control deteriorated.
  - `cm.geopolitical-race`: neutral on the race narrative; a document arguing against it engages it too.
  - `cm.corporate-race`, `cm.arbitrage-capture`, `so.adoption-pressure`, `so.reduced-human-reliance`: `searched_by:
    selection` and a note that they are agent-agnostic processes; `so.reduced-human-reliance` gets a common-cause
    record (institutional, field). `cm.corporate-race` and `cm.geopolitical-race` hold what risks 0.2.0 had as the
    retired race risk.
  - `dp.post-deployment-change`: "Deployed system differs from the evaluated one", including a released checkpoint
    other than the evaluated one. `dp.engineering-error`: leads with requirements and unstated safety constraints.
- **Risk edges**: `ma.scheming` no longer defeats `agentic-control`, and `ma.sabotage` defeats agentic control, not
  control protocols (control protocols and control evaluations are built against scheming and sabotage; their weak
  point is elicitation); new edges for `se.safeguard-removal` (defeats safety training, bypasses deployment-time
  classifiers), `ma.rogue-deployment` (escalates to `ma.sabotage` and `ma.loss-of-control`) and `st.disempowerment`
  (defeats non-technical layers and scalable oversight: the loss of the human correction mechanism).
- **New fields**: `worsened_by` (4 generators) and `amplifies` (4: `mf.information-asymmetry`, `mf.network-effects`,
  `so.reduced-human-reliance`, `so.adoption-pressure`).
- **Vocabulary**: `none-known` is `none-linked` (the old value read as "no technique exists", which is false for
  several multi-agent factors; now on `ca.situational-awareness`, `su.shared-data-methods`,
  `su.convergent-susceptibility`, `mf.network-effects`, `mf.destabilising-dynamics`, `mf.emergent-agency`); technique
  families `cooperative-ai`, `security-access-control`, `control-protocols` and `control-evaluations` added (22);
  `meta.fields`: an absent common-cause record does not claim independence; provisional covers the review; crosswalk
  key `review`.

Not taken: claim records on every edge (for the curated tables, which do not exist yet); generators for attack
selection by a scheming model (covered by `searched_by: model`), prepotence (overlaps `ca.capability-level` and
`dp.irreversible-release`), introspection (role unclear), impairment of safety discourse, LLM character as a shared
substrate, capacity asymmetry between countries, target vulnerability and the model's closed action-perception loop:
candidates in OPEN-QUESTIONS 12; merging the five "deployed differs from evaluated" generators or the competition
generators (the trial found mostly different valid claims; a which-one-it-blames rule is in the README instead);
moving `mf.selection-pressure` out of `mf`; renaming "generators" and the roles (open questions 9).

sha256 `2215a5184de9b1982a917a687cc2b482719af04fc458d1f0d65d7a81f86848a0`.

## 0.3.0 (draft, 2026-10-29)

- First version in this repository: the risk-generator taxonomy draft v0.3 in the catalogue envelope (schema
  `risk-generators-0.schema.json` on `../schemas/catalogue-0.schema.json`), converted mechanically. 10 families, 64
  generators (52 `annotate`, 12 `curated`; 3 `background`; 1 provisional; 36 with a common-cause candidate; 6
  contested) and 9 risk edges. Names, definitions, notes, roles, links, common-cause records and crosswalks are the
  draft's text and values.
  - Ids are the draft's, lowercased, with `_` written `-` (the catalogue id pattern): `TR` is `tr`,
    `TR.outcome_optimisation` is `tr.outcome-optimisation`; risk ids the same way, as in [risks
    0.2.0](../risks/CHANGELOG.md). Ids named in definitions, notes and `vs` texts are written the same way, except
    `OR.unverifiable_claims` (in `so.information-fragmentation`'s `vs`), a leaf the draft had dropped and no version
    has, kept as written.
  - One `entries` list in the draft's order, each family followed by its generators; `node` is `family` or
    `generator`, a generator's `parent` its family. `def` is `definition`, `cc` is `common_cause`, `xw` is
    `crosswalks`; the other fields keep their names. `provisional: true` (one generator) is `status: provisional`;
    every other entry is `status: draft`. `vs` stays free text.
  - `feeds`, `weakens`, and each risk edge's `risk` and `escalates_to`, are references `{id, name}` to risks 0.2.0,
    the name copied from the risks file. The draft's `technique_families` and `risk_edges` are `meta` keys; its
    header comments are `meta.fields`; `meta.crosswalk_keys` names the frameworks behind the crosswalk keys, from the
    draft's key table. `SR` is not in that table and is glossed from its use (the Shallow Review's orthodox
    problems).
- The risk ids: the draft wrote its links against the risk draft v0.1.1. All 40 risk ids it uses are in risks 0.2.0
  with the same id (it uses neither `RE.oversight`, removed in 0.2.0, nor `ST.rd_acceleration`, added in 0.2.0), so
  the links point to 0.2.0 unchanged. They were not reviewed against 0.2.0's widened definitions (`se.theft`,
  `se.poisoning`, `mu.military`, `ma.cot-unfaithful`, `ma.sabotage`, `ha.toxic`, among others). No generator links
  to `st.rd-acceleration`, `st.race`, `ha.privacy`, `ha.ip`, `ha.environment` or `we.welfare`.
- sha256 `6b2de883b6153f5324be2e7d34e77edd9e15f0133ab7df4f963b48e33bb164d9`.

## History, not published in this repository

- v0.3 (2026-10-29), from v0.2 after the annotation trial ([README.md](README.md#pilot)) and two blind reviews:
  - split `TR.exploitable_signal` into `TR.gameable_grader` and `TR.proxy_objective`;
  - added `AS.coverage_limits`, `MF.mixed_motives`, `SU.convergent_susceptibility` (split from
    `SU.shared_data_methods`), `DP.context_dependence`, `SO.information_fragmentation`, and `TR.shallow_safety`
    (provisional);
  - moved `TR.data_supply_chain` to `SU.supply_chain` (training and deployment dependencies);
  - renamed and narrowed `DP.critical_integration` to `DP.high_stakes_use`, tight coupling moved to
    `MF.network_effects`;
  - redefined `AS.immature_science`, `DP.scale`, `AS.overseer_gap`, `DP.post_deployment_change`,
    `DP.distribution_shift`, `SO.diffuse_responsibility`, `OR.weak_internal_governance`, `CM.actor_count`; `OR`
    broadened to deployer organisations;
  - new fields `tier` and `background`.
- v0.2 (2026-10-29): 10 families, 57 leaves, 31 with a common-cause candidate; the criteria revised after a first
  round of reviews (the event-type test C1 replacing a contained-harmless test).
- v0.1 (2026-10-29): 10 families, 51 leaves.
