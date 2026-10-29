# Open questions: risks

Undecided for 0.2.0. Items shared with the risk-generator taxonomy are also in
[../risk-generators/OPEN-QUESTIONS.md](../risk-generators/OPEN-QUESTIONS.md).

1. **Passing mentions.** Passing labels were 19-32% of labels in the pilot, and the annotators disagree on the flag
   itself. Store them and leave them out of views (the current rule), or drop them at annotation time? Dropping them
   did not raise agreement in the pilot.
2. **Production annotator.** In the pilot Opus labelled sparsely and conservatively; GPT-6 labelled more broadly and
   used family ids more. They differ mainly on inclusion. Options: one model with a second-model audit, or the union
   of two with per-label confidence. The choice changes the coverage map: sparse labels make gaps look larger.
3. **Crimes committed by a rogue AI.** The `mu` family assumes a human adversary. When an AI acting on its own
   commits cybercrime or fraud, is it labelled with the `ma` mechanism only (`ma.exfiltration`, `ma.power-seeking`),
   or also with the harm (`mu.cyber`, `mu.fraud`), with `mu` redefined as harmful use of AI capabilities by a human or
   an AI? The second blurs the line between misuse and loss of control.
4. **AI R&D acceleration.** `st.rd-acceleration` is a risk here, as lab frameworks treat it, and contested against
   `ma.loss-of-control`; under the generator criteria it is a capability trend, and the generator taxonomy has
   `ca.ai-rnd`. Risk, generator, or both with a link?
5. **Generator-shaped risks.** `st.race`, the organisational part of `st.governance` (unsafe culture, the gap between
   stated and actual practice) and opacity and assurance limits (`re.oversight` was removed in 0.2.0, but the `re`
   family definition still says "opaque") are conditions rather than events under the generator criteria. Move them to
   the generator side (`cm.*`, `or.*`, `as.*`), or keep them as risks for documents that discuss them as concerns
   without naming an outcome?
6. **Capability and propensity.** Where the line falls in practice: `mu.cbrn` includes dual-use capability
   evaluations, and "situational awareness" or "deception" name both a capability (a generator) and a behaviour (a
   risk). The generator pilot did not label risks, so the line is untested.
7. **A human gold set.** About 50 of the pilot's 100 documents labelled by people would turn agreement figures into
   accuracy figures and show whether the sparse or the broad annotator is closer to a careful reader.
8. **Naming.** Is the axis "risks", "harms" or "hazards"? "Hazard" is also one of the generator roles.
9. **`ha.toxic`.** Its widened "unsafe advice" clause did not validate (alpha 0.57). Proposed and not tested:
   narrow it to advice the document itself frames as harmful, and route refusal-rate metrics for malicious requests to
   the family id `mu`.
