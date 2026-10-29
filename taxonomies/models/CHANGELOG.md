# Changelog: models

## 1.1.0 (draft, 2026-10-28; not tagged)

- Organisation references: maker keys and the new `lab_id` are ids of the organisation vocabulary (`orgs-0.x`, the
  pipeline's `taxonomy/orgs-<version>.yaml`; its move to this repository is pending), each beside a display name.
  - Maker `internlm` is now `shanghai-ai-lab` (display name unchanged, "Shanghai AI Laboratory (InternLM)") in
    `meta.makers`, `meta.maker_facets` and the `maker` of 31 nodes; the node id `internlm` (the model family) is
    unchanged. The other 137 maker keys were already organisation ids.
  - Every node with `lab` (128) gains `lab_id`: DeepMind → `deepmind`, Microsoft Research → `microsoft-research`,
    ByteDance Seed and Seed → `bytedance-seed`, OpenBMB → `openbmb`, FAIR → `meta-ai`, Google Research →
    `google-research`, OpenMOSS → `openmoss`, Microsoft AI → `microsoft-ai`. `lab` keeps the display string.
    `bytedance-seed` and `microsoft-ai` are entries from orgs 0.2.0 on.
- No node, name, gloss or mention changes; `meta.updated` 2026-10-28. Schema `models-1.schema.json` unchanged (nodes
  allow further fields).
- A reader keyed on the maker `internlm` must use `shanghai-ai-lab`.
- sha256 `c10a6dace9c75c6a9f8ffc5bf3aa6c9b425f1b270394379d05fe832146df2fa2`.

## 1.0.0 (2026-10-24)

- First release; content identical to 0.9.0: same 1,877 nodes and 138 makers, field for field; `meta.updated` stays
  `2026-10-17`, the date of the content.
- Header only: `version` `'1.0.0'` (was `'0.9'`). The file has no `status` field; its schema has none.
- Schema `models-1.schema.json`: `models-0.schema.json` with the version pattern for major 1.
- sha256 `d7f1bae80e5b1dd9a978cecad8d78cba7be7adebd0fa5bdc99692b731aa4acb5`.

## 0.9.0 (2026-10-17, `meta.updated`)

- 1,877 nodes: 310 families, 249 groups (162 generations, 59 lines, 28 series), 1,318 models; 138 makers.
- Identical to the pipeline's pinned `configs/models.yaml`, sha256
  `ce35fb95729991de3a5cea8d29829d22ed202b236f6a57308140cc23a9643315`.
- The `version` field inside the file (`'0.9'`) will be corrected at 1.0.0.
