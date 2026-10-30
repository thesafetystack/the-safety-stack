# Open questions: risks

For 0.3.0. Items shared with the risk-generator taxonomy are also in
[../risk-generators/OPEN-QUESTIONS.md](../risk-generators/OPEN-QUESTIONS.md). Each question says whether the 0.3.0
review settled it (and how), or whether it needs a person's judgement. The numbers 1-9 are those of 0.2.0.

## From 0.2.0

1. **Passing mentions.** *Settled*: store them and leave them out of views (every reviewer who answered); 0.3.0 adds
   an operational engagement test, so the flag follows from where the risk is named rather than from a judgement,
   and a `prominence` field. Whether the test raises agreement is untested.
2. **Production annotator.** *Open.* One model with an audit by a second (the union inflates coverage and doubles
   the engagement problem), or the union of two with per-label confidence (sparse labels make false gaps, the error
   a gap map can least afford)? Reviewers split; most said to decide it against human labels, not by argument.
3. **Crimes committed by a rogue AI.** *Taken, with dissent*: `mu` is deliberate harm by any actor, with an `actor`
   field; an AI acting on its own also takes the `ma` mechanism. Dissent: keep `mu` human and put a harm-domain facet
   on `ma` risks instead, so the misuse-versus-misalignment line stays sharp. A person should confirm.
4. **AI R&D acceleration.** *Partly settled*: the capability is the generator `ca.ai-rnd`; the risk is narrowed to
   `st.oversight-outpaced`, the harmful state, linked from `ca.ai-rnd`. *Open*: keep that risk (the lab frameworks
   need a node) or drop it (a capability trend is not a harm, and two nodes double-count coverage)?
5. **Generator-shaped risks.** *Settled for* `st.race` (retired to `cm.*`) *and* `st.governance` (narrowed to named
   failures; organisational causes are `or.*`); opacity was already the generator `as.opacity`. *Open*: race
   documents that name no outcome now have no risk label (`none`, `generator-only`); that is acceptable only if
   generators are annotated per document (generator question 1).
6. **Capability and propensity.** *Settled as a rule*: who supplies the intent decides; a capability evaluation on
   a risk's own task is labelled with the risk and `elicitation`, and the capability generator on the generator side.
   *Open*: whether annotators can apply it; context can elicit a disposition without instructing the act.
7. **A human gold set.** *Settled that it is needed* (every reviewer): about 50 held-out documents, two annotators
   and adjudication, stratified by family, with documents that should get no label, Chinese-language documents and
   organisational and structural documents; before any public coverage or gap view. *Open*: who labels it, and a
   decided worked example under each of the 14 contested pairs first.
8. **Naming.** *Settled*: keep "risks". The clash with the generator role `hazard` is generator question 9.
9. **`ha.toxic`.** *Settled*: unsafe advice is `ha.unsafe-advice`; refusal rates on malicious requests with no named
   harm are the family id `mu`.

## New in 0.3.0

10. **An outcome node independent of mechanism.** The rule decides loss of control by attribution and records
    `attribution=unstated` where the document does not say. Some reviewers held that this still turns the words
    "loss of control" into a claim that an AI acted against its overseers, and that a fast collective failure of
    obedient systems is awkward under both `ma.loss-of-control` and `st.disempowerment`; they asked for one outcome
    leaf, labelled whatever the cause, beside the mechanism leaves. Others wanted the misuse / misalignment /
    structural split kept sharp. A restructure; needs a person.
11. **An accountability record.** Whether to record, at least in the gold-set pilot, who is responsible, whether
    responsibility is unified or diffuse, whether the harm was anticipated, and whether it was intended or knowingly
    tolerated (each with `unstated`): the distinctions that decide which intervention applies. Dropped earlier for
    annotation cost.
12. **Structure inside `ma`.** Proposals: an attribute marking each `ma` risk as cause (specification, goal
    generalisation), behaviour or outcome, so training-time techniques link to causes; or a scheming / non-scheming
    split. 0.3.0 only separates the scheming disposition from the actions, with a co-label rule.
13. **Severity.** `sev` is now a default for views, but several reviewers held that severity belongs to scenarios
    and claims, not to risk types. Keep it as a default, move it to the edges, or drop it?
14. **Provisional risks.** The six new risks (`ma.manipulation`, `ma.rogue-deployment`, `se.safeguard-removal`,
    `se.extraction`, `ha.unsafe-advice`, `ha.safeguard-harms`) rest on the review, not on pilot data.
15. **Families by who is at fault.** One reviewer perspective (system safety) held that partitioning by who acts
    against whom is chain-of-events thinking: losses involve AI, users, attackers and organisations together, and
    accidents arise from interactions of working components. 0.3.0 widened `re`; the family structure is unchanged.
16. **Chinese frameworks.** No crosswalk to the TC260 AI Safety Governance Framework 1.0 and 2.0, TC260-003 or the
    Shanghai AI Lab Frontier AI Risk Management Framework, the lists Chinese developers report against. Needs the
    primary texts. Related: the corpus is mostly English, so a gap may be unobserved work rather than absent work.
