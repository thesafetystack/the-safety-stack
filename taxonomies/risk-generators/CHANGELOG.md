# Changelog: risk generators

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
