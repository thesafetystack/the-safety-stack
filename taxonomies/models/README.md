# Models

File `models-0.9.0.yaml`, tag `models-0.9.0`: 1,877 nodes (310 families, 249 groups, 1,318 models) and 138 makers.
The file's own `version` field reads `'0.9'` (see CHANGELOG).

Top level:
- `version`: header.
- `meta.schema_version`: `'0.3'`.
- `meta.updated`: `2026-10-17`.
- `meta.makers`: maker key to display name, 138 makers.
- `meta.maker_facets`: per maker `org_type` (138), `country` (135, 16 countries), `note` (34).
- `nodes`: node key to node, 1,877 nodes.

Node fields (count of nodes that have the field):
- `kind` (1,877): `family` 310, `group` 249, `model` 1,318.
- `level` (249 groups): `generation` 162, `line` 59, `series` 28.
- `name`, `gloss`, `model_class` (1,877): display name, one-line description, classes (20 values).
- `parent` (1,808): the enclosing family or group; the 69 nodes without one are root families.
- `maker` (1,609): key of `meta.makers`, a list on 43 nodes.
- `mentions` (1,730), `weak_mentions` (264): lower-case surface strings for the matcher.
- `notes` (1,855), `uncertainties` (686): free text.
- `lifecycle` (1,325): dates of `released`, `announced`, `preview`, `deprecated`, `retired`.
- `confidence` (1,318 models): `verified` 516, `weak` 748, `stub` 54.
- `checked` (1,318 models, no family or group): date last checked, 2026-07-29 to 2026-10-18.
- `params` (1,047): `kind`, `total_m`, `active_m` (millions), `source`.
- `modalities` (1,270), `links` (1,028): input and output modalities; announcement, model card, paper URLs.
- `variant_of` and `variant_kind` (67), `based_on` (170), `distilled_from` (9), `same_weights_as` (3): references
  to other nodes.
- `representation_status` (113), `specialization` (208), `lab` (128), `tags` (127), `mentions_verbatim` (31).
