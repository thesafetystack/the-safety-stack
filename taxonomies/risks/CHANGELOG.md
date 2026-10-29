# Changelog: risks

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
