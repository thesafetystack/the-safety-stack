# Techniques

**Draft.** File `techniques-1.2.0.yaml` (`meta.status` `draft`, not tagged, not used to annotate any release): 246
techniques (149 intervention, 32 monitoring, 65 assessment), 14 group nodes and 10 layers; schema
`schemas/techniques-3.schema.json` (the catalogue envelope, [../README.md](../README.md#the-catalogue-envelope)). It is
techniques 1.1.0 (tag `techniques-1.1.0`, 234 techniques, 9 group nodes, schema `techniques-2`) with the changes in
[CHANGELOG.md](CHANGELOG.md): 12 techniques and 5 group nodes added; no id removed, merged or renamed.
`techniques-1.2.0.md` is a readable view of the same content, with the confusable pairs and their rules. Released
versions 1.1.0, 1.0.0 and 0.9.1 stay for reference.

## What counts as a technique

A **technique** is a safety-relevant intervention, monitor or assessment applied to an AI model or system (its
training data, training, weights or internals, serving stack, agent scaffold, access or release) for a safety
purpose: preventing, detecting, measuring or limiting harm from the model's behaviour, from its misuse, or from attacks
on it, including privacy, fairness and content-rights harms. A general **ML method** (RLHF, adversarial training,
fine-tuning, distillation, probing, reinforcement learning, retrieval, self-consistency sampling) is a procedure, not a
technique by itself: RLHF that trains an assistant to be harmless is the technique `rlhf`; RLHF that raises a
summariser's leaderboard score is the method and gets no row.

- **`counts_when`** (51 entries, those named after or built on a general method) states the purpose a use must
  serve; a use for another purpose gets no row on that entry. An entry without it has a definition that already fixes
  the safety purpose.
- `counts_when` is about **purpose, not evidence**: proposals, recommendations and critiques count, and the roles
  record whether the document uses, evaluates or only mentions the technique. A capability task counts when the
  document presents it as an explicit proxy for the safety use.
- The purpose must be **stated or evident**. A developer's plain statement that its user-facing assistant or agent was
  post-trained with RLHF, DPO or another preference method counts as `rlhf` (with AI feedback, `rlaif`): the
  fictional *Kestrel 2* system card line "post-trained with RLHF" gets a row; the fictional *Orrin-7B* summariser tuned
  with DPO on human quality ratings to top a leaderboard does not.
- **Absence is never inferred from silence**: that a lab lacks or dropped a technique is recorded only from an explicit
  statement or a described implementation that contradicts the entry.
- **Group nodes** take a bare umbrella term only when the specific technique is neither stated nor evident; a
  technique **`parent`** takes the unstated cases of its children; parent and child are never coded for the same
  practice. A technique may be a child of several groups. A dot in an id has no meaning of its own (the dotted ids are
  1.0.0 history), and a `parent` that names a group node (9 entries, also 1.0.0 history) means only what the group's
  `children` list says; membership is defined by `children`.
- **Kinds**: an intervention changes training, access, execution or outputs; a monitor produces operational signals
  during use; an assessment produces findings from a bounded investigation.
- **Out of scope**: agent-foundations proposals (AI boxing as a thought experiment, coherent extrapolated volition,
  eliciting latent knowledge as a theoretical problem, corrigibility theory, oracle-AI designs); such content maps to
  an entry only where it is that entry in practice. **Undecided, left as gaps**: protections applied by data owners
  against generative misuse, system hazard analysis of AI deployments, DNA-synthesis screening, cognitive forcing in
  user interfaces, model-welfare measures and evaluations (including model-initiated conversation termination),
  unlearning without weight updates, audio-channel defences for speech models.

## File

Top level: `version`; `meta` (`schema` `techniques-3`, `status`, `updated`, `description`, `sources`, `layers`);
`entries` (techniques, then group nodes).

- `meta.layers` (10): `id`, `name`, `definition`; the v0.9 dashboard groups, promoted into the file. Subgroups stay a
  view outside this file. Layer, group and technique ids are disjoint.
- Technique fields: `id`, `node` (`technique`), `name`, `kind` (`intervention` | `monitoring` | `assessment`),
  `status` (`final` | `provisional`), `origin` (`v0.8`, `new-2026-10`, a 0.9 addition or split, `1.2.0`), `layer`
  (a `meta.layers` id; the validator checks it), `tags` (`pre-llm`: the entry's literature is mostly about non-LLM
  models, i.e. classifiers, perception or control; 2 entries), `definition`, `counts_when` (51), `parent`, `aliases`
  (`{text, kind}`: `synonym` and `instance` are shown to annotators, `legacy` are former names for lookup only),
  `ml_methods`, `risk_note`, `source_papers`, `note`, `v08_name`, `absorbed`.
- Group node fields: `id`, `node` (`group`), `name`, `definition`, `children`, `aliases` (`synonym`, `legacy`).
- The annotation model would be shown each technique's id, kind, name, status, shown aliases, parent, definition and
  `counts_when`, and each group node's id, name, synonyms, children and definition, exactly as in the file.

## Compatibility with 1.1.0

The CHANGELOG classes every change. Whether 1.2.0 can be a minor version depends on one reading of
[../README.md](../README.md#versioning) that is proposed, not settled (a bullet extending "a minor version may add new identifiers" to coverage extensions that keep every earlier label correct; not yet in that README):

- **Additions** (12 techniques, 5 group nodes): minor under the current rule.
- **Clarifications** (wording, moved purpose clauses, group definitions, names, British spelling): minor.
- **Coverage extensions** (an alias or a named sub-case that lets an entry match more documents, e.g. perplexity
  filters as jailbreak detectors, impact penalties as side-effect minimisation, diffusion safety guidance as
  safety-guided decoding, input transformations as prompt rewriting): every use labelled correctly under 1.1.0 stays
  correct, but recall changes, so counts are not comparable across versions without care. Minor only under the
  proposed reading.
- **Eligibility conditions** (`counts_when` added where the 1.1.0 definition had no purpose wording, e.g.
  `machine-unlearning`, `representation-concept-suppression`, `self-verification`, `introspection-training`,
  `groundedness-faithfulness-verification`, `hidden-private-chain-of-thought`, fingerprinting, judge audits,
  calibration evaluation, interpretable-by-design): uses without the stated purpose get no row. Treated here as
  clarification, since 1.1.0 scoped the whole file to AI-safety techniques and non-safety uses were never intended
  labels; but recall can drop on these entries, and under a strict reading this is a narrowing. Their rows are the
  precision-audit set in the re-ask plan.
- **The legibility split**: `cot-faithfulness-monitorability-training` becomes the parent of three children and keeps
  its 1.1.0 meaning; its release-2026-10-27 rows remain broad evidence under 1.1.0, and which child each one is stays
  unknown until re-asked. Minor only under the proposed reading.
- **Annotation-policy changes**: the parent rule now applies per practice, not per document (also on
  `dangerous-capability-evaluation`); the implicit-application rule for assistant RLHF / RLAIF is stated; the bare
  synonym "adversarial training" moves from `adversarial-training-jailbreak-robustness` to the new group node
  `adversarial-training`; two shown aliases of `constitutional-classifiers` are removed.

Labels new in 1.2.0 create unknown coverage for documents annotated with earlier versions, not negatives.
