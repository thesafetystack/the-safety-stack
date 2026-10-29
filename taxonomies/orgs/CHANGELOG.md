# Changelog: orgs

## 0.2.0 (draft, 2026-10-29)

- First version in this repository, in the catalogue envelope (schema `orgs-0.schema.json`). Built in the pipeline
  repository from 0.1.0 (named teams and labs as entries under their parent, the FAIR rule, unit words and US
  regions, an external review's accepted findings, recall additions), then the models makers' facets taken over
  here:
  - the tag `big-tech` on the 32 makers whose models-1.0.0 `meta.maker_facets.org_type` was `big-tech` (the other
    facet types correspond to `type`);
  - the 34 facet notes, appended to the entry's `note`;
  - `arc-institute` is the Arc Institute (US, a nonprofit; the models maker of Evo). The pipeline's 0.2.0 draft had
    the ROR record of ARC Institute Indonesia under that id; it is now `arc-institute-indonesia`. No affiliation in
    the dataset named either.
  - Every maker was already tagged `model-maker`, and every maker with a facet country already had it, except
    `arc-institute` above.
- 4,840 entries. sha256 `839d07ad6f9c4157604860743fb7af47935288e7c8ad26b12e759731d49bc997` (the pipeline's draft
  before the take-over: `c4ca7465e443…`).
