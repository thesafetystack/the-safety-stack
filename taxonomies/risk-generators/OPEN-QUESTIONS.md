# Open questions: risk generators

For 0.4.0. Items shared with the risk taxonomy are also in [../risks/OPEN-QUESTIONS.md](../risks/OPEN-QUESTIONS.md).
Each question says whether the 0.4.0 review settled it (and how), or whether it needs a person's judgement. The
numbers 1-10 are those of 0.3.0.

## From 0.3.0

1. **Per-document annotation at all.** *Open, and now more pressing*: risks 0.3.0 retired the race risk to
   `cm.*`, so race, organisational and multi-agent documents that name no outcome get no risk label (`none`,
   `generator-only`, with the generator ids). Reviewers split: annotate some families (`so`, `cm`, `or`, `mf`, or
   `tr`, `ca`, `as`, at most three labels per document), pilot first on about 300 random documents, or curated edges
   only (2 of 100 trial documents stated a joint failure). The `generator-only` reason keeps the documents findable
   meanwhile. Related: whether `mf.network-effects`, `mf.commitment-trust` and `dp.multi-principal-interaction`
   (headline risk factors in the multi-agent literature, curated here for low trial agreement) move to the annotate
   tier.
2. **Passing mentions.** *Settled*: store and hide, as for risks. How the draft prompt's `mentions` stance relates to
   the engagement test is still to write down.
3. **Production annotator.** *Open*, as for risks: decide against human labels.
4. **AI R&D acceleration.** *Settled as both, linked*: `ca.ai-rnd` (the capability) feeds the risk
   `st.oversight-outpaced` (the harmful state). Whether to keep the risk is risk question 4.
5. **Race dynamics, governance failure, opacity and assurance.** *Settled*: race is `cm.*` only; the
   organisational part of governance is `or.*` (with the new `or.commitment-drift`); opacity is `as.opacity`. The
   risk `st.governance` keeps named failures of regulation, oversight, liability or accountability.
6. **Capability and propensity (C4).** *Restated* (who supplies the intent; both sides labelled when a passage
   supports both). *Open*: untested in annotation; context can elicit a disposition without instructing the act, and
   a self-model can be part of a simulated character, so the line may be fuzzier than the rule.
7. **A human gold set.** *Settled that it is needed*; the generator edges need their own audit, separate from labels:
   label agreement does not validate a causal link.
8. **AI welfare.** *Settled as edges, no new family*: commercial pressure and deployment scale feed `we.welfare`,
   immature science weakens its defences. *Open*: whether training against a model's preferences, copying and
   runtime scale, or deprecation deserve generators of their own.
9. **Naming.** *Open, and the reviewers' most frequent request*: rename "generators" to "risk factors", the term of
   the multi-agent risk literature, the international safety reports, lab frameworks and safety cases (others
   proposed "risk sources", "risk drivers", "causal and contextual factors"); and rename the role `hazard`, which
   clashes with the safety-engineering sense (a system state that leads to a loss), for example to `amplifier` or
   `exposure`, and `barrier` to `vulnerability` or `control-degradation`. A mechanical rename (directory, schema,
   ids unchanged), best done before the gold-set instructions are written, since they embed the terms.
10. **Technique families.** *Open, and now blocking edge curation*: the 22 families (the 0.8 draft's 17,
    `cooperative-ai`, `security-access-control`, `control-protocols`, `control-evaluations`, `non-technical`) are
    not the published technique taxonomy's. Map them to techniques 1.x group nodes before curating any edge, and
    split `non-technical` (standards and certification, mandated assessment and filing, internal governance,
    international agreements, organisational process), or the negative map will show governance, security and
    cooperative work as missing by construction.

## New in 0.4.0

11. **The curated edge record.** Reviewers agreed that every curated technique-to-risk and generator-to-technique
    edge needs a source, an epistemic tier, conditions, an effect direction (reduces, assesses, worsens, unknown),
    whether the argument holds against a model or attacker optimising against it (worst case over the model's
    propensity, not over inputs), the deployment surface (consumer chat, API, agentic, fine-tuning API, internal,
    open weights, stolen weights), and a falsifier for each common-cause hypothesis. One reviewer perspective (system
    safety) wants every displayed protection or gap claim tied to a scenario (system boundary, loss, hazard,
    constraint, responsible controller, control actions, feedback, process-model assumptions). The record format
    should be fixed, with one worked example, before any edge is curated.
12. **Generator candidates not added**: attack selection by a scheming model, prepotence (transformative effects
    humanity cannot collectively stop), introspection (self-knowledge that can help oversight as well as harm it),
    impairment of discourse about existential safety, LLM character as a shared substrate of several safety
    behaviours, capacity asymmetry between countries, the vulnerability of the affected population or
    infrastructure, the model's closed action-perception loop, and monitoring latency.
13. **Provisional generators.** The nine generators the review added rest on the reviews, not on trial data.
14. **Control structure.** One reviewer perspective (system safety) holds that a list of factors cannot replace a
    control structure (who enforces which constraint with what feedback), and that independence of layers is not
    sufficient for safety: correctly working components can interact unsafely. 0.4.0 added
    `as.feedback-inadequacy` and the independence wording; the structure is unchanged.
15. **Process persistence.** Agent-agnostic processes are marked with `searched_by: selection`; one reviewer
    perspective asked for curated pathways to state what restores the harmful trajectory after an actor resists, not
    only that it is self-reinforcing.
