# Techniques

File `techniques-0.9.1.yaml`, tag `techniques-0.9.1`: 234 techniques (137 intervention, 32 monitoring, 65 assessment)
and 9 group nodes. The file's own `version` field reads `'0.9'` and `status` reads `draft` (see CHANGELOG).

Top level:
- `version`, `status`, `notes`: header; `notes` explains alias types, group nodes, `ml_methods` and `risk_note`.
- `techniques`: list of 234 entries.
- `group_nodes`: list of 9 entries.

Technique fields (count of entries that have the field):
- `slug` (234): identifier; in 8 slugs a dot separates a child from its parent.
- `name` (234): display name.
- `kind` (234): `intervention` 137, `monitoring` 32, `assessment` 65.
- `status` (234): `final` 214, `provisional` 20.
- `origin` (234): `v0.8` 143, `new-2026-10` 52, a 0.9 addition 30, a 0.9 split 9.
- `definition` (234): what the technique is and is not.
- `parent` (13): a group node (9) or another technique (4).
- `aliases` (115): `synonym` and `instance` (shown to annotators), `legacy` (former names, lookup only).
- `ml_methods` (173): typical implementations, 40 distinct labels.
- `risk_note` (148): the risk addressed, informal.
- `source_papers` (48): free-text paper pointers.
- `note` (66): curation remarks.
- `v08_name` (12): the 0.8 name the entry continues.
- `absorbed` (14): 0.8 entries folded in, `;`-separated.

Group node fields: `slug`, `name`, `definition`, `children` (49 references to 46 techniques in all), `aliases` (1 node).

Alias strings across techniques and group nodes: 136 synonym, 83 instance, 55 legacy.
