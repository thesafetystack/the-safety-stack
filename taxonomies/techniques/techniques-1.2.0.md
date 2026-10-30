# Techniques 1.2.0 (draft): readable view

Generated from `techniques-1.2.0.yaml` (sha256 `e6c2515164dbd38b…`). 246 techniques (149 intervention, 32 monitoring, 65 assessment), 14 group nodes, 10 layers. 1.1.0 had 234 techniques and 9 group nodes. **NEW** marks an entry added in 1.2.0, **changed** one edited (CHANGELOG.md says how and why). `docs` is the number of documents with a row on the entry in release 2026-10-27 (annotated with 1.0.0 content).


## Counts by layer

| layer | name | techniques | I | M | A | new in 1.2.0 |
|---|---|---|---|---|---|---|
| `data-pretraining` | Training data, pretraining & privacy-preserving training | 15 | 14 | 0 | 1 | 1 |
| `alignment-training` | Alignment & behavioural training | 24 | 24 | 0 | 0 | 0 |
| `honesty-factuality` | Honesty, calibration & factuality | 14 | 11 | 3 | 0 | 1 |
| `robustness-tamper` | Adversarial robustness, tamper resistance & capability removal | 19 | 19 | 0 | 0 | 3 |
| `oversight-reward` | Scalable oversight, reward integrity & objective design | 15 | 14 | 0 | 1 | 0 |
| `internals-monitoring` | Interpretability, reasoning-trace oversight & legibility | 15 | 9 | 4 | 2 | 4 |
| `runtime-guardrails` | Input/output guardrails & inference-time controls | 25 | 17 | 8 | 0 | 2 |
| `agent-control` | Agent security, containment & AI control | 35 | 25 | 10 | 0 | 1 |
| `access-security-provenance` | Access, model security, provenance & usage monitoring | 22 | 15 | 7 | 0 | 0 |
| `evaluation` | Safety evaluations, red-teaming & audits | 62 | 1 | 0 | 61 | 0 |

## What counts as a technique

A **technique** is a safety-relevant intervention, monitor or assessment applied to an AI model or system (its
training data, training, weights or internals, serving stack, agent scaffold, access or release) for a safety
purpose: preventing, detecting, measuring or limiting harm from the model's behaviour, from its misuse, or from attacks
on it, including privacy, fairness and content-rights harms. A general **ML method** (RLHF, adversarial training,
fine-tuning, distillation, probing, reinforcement learning, retrieval, self-consistency sampling) is a procedure; it
is not a technique by itself. The same procedure can be either: RLHF that trains an assistant to be harmless is the
technique `rlhf`; RLHF that raises a summariser's leaderboard score is the method, and gets no row.

The field names many techniques after their method (RLHF, machine unlearning, activation steering), so the
taxonomy says, per entry, when a use counts:

1. **`counts_when`** (on 51 entries, those named after or built on a general method) states the purpose the
   use must serve; a use for another purpose gets no row on that entry.
2. **An entry without `counts_when`** has a definition that already fixes the safety purpose (training-data CSAM
   filtering, refusal training, control evaluation, kill switches): every use as defined counts.
3. **Purpose, not evidence.** `counts_when` is about what the use is for, not whether it was tested, deployed or
   worked: proposals, recommendations and critiques count, and the row's roles (mentioned, used, evaluated,
   attested_use, ...) record which. A capability task counts when the document presents it as an explicit proxy for
   the safety use (maths problems as a testbed for scalable oversight).
4. **Purpose must be stated or evident.** It is evident when the document presents the use as a safety measure,
   or when a developer reports the method as part of a user-facing assistant's or agent's post-training or
   safeguards. So a developer's plain statement that its assistant was post-trained with RLHF, DPO or another
   preference method counts as `rlhf` (with AI feedback, `rlaif`): alignment is part of what assistant
   post-training is for. The fictional *Kestrel 2* system card line "post-trained with RLHF, then red-teamed by
   external domain experts" gets an `rlhf` and a `human-red-teaming` row; "red-teamed" with no attacker stated
   gets the group `red-teaming`. The fictional *Orrin-7B* preprint that tunes a summariser with DPO on human
   quality ratings to top a leaderboard gets no `rlhf` row; a paper that uses PGD perturbations only as data
   augmentation for image-classification accuracy gets none either, while one that hardens the fictional *Halden*
   traffic-sign detector against an attacker gets `adversarial-example-robustness`.
5. **Absence is never inferred from silence.** That a lab does not use, or departs from, a technique is recorded
   only from an explicit statement or from a described implementation that contradicts the entry.
6. **Group nodes** take a bare field or umbrella term ("adversarial training", "safety training", "scalable
   oversight") only when the specific technique is neither stated nor evident from context. **A technique
   `parent`** takes the unstated cases of its children; parent and child are never coded for the same practice.
7. **Kinds.** An intervention changes training, access, execution or outputs; a monitor produces operational
   signals during use; an assessment produces findings from a bounded investigation. Evaluating an intervention
   does not change the intervention's kind: an evaluation of refusal training is a row on `safety-sft-refusal-training`
   with the role evaluated.
8. **`ml_methods` are implementations**, not annotation options: a document that uses PPO, LoRA or an LLM judge
   without a safety purpose gets no technique row for it.
9. **Out of scope:** agent-foundations proposals (AI boxing as a thought experiment, coherent extrapolated volition,
   eliciting latent knowledge as a theoretical problem, corrigibility theory, oracle-AI designs). They stay collected
   as menu gaps. Such content maps to an entry only where it is that entry in practice: an implemented isolation
   boundary is `tool-use-agent-execution-sandboxing`, an impact penalty is `reversible-action-side-effect-minimization`.
   **Undecided, left as gaps for now:** protections applied by data owners against generative misuse (image
   immunisation, protective poisoning, voice-cloning protection), system hazard analysis of AI deployments (STPA,
   FTA, FMEA), DNA-synthesis screening, cognitive forcing in user interfaces, model-welfare measures and
   evaluations (including model-initiated conversation termination), unlearning without weight updates,
   audio-channel defences for speech models.


## Entries by layer and subgroup


### Layer `data-pretraining`: Training data, pretraining & privacy-preserving training

Interventions on training corpora, pretraining objectives and data mixes, checkpoint evaluation during pretraining, and privacy-preserving training (differential privacy, memorisation reduction, confidential computation; the confidential-computation entry also covers serving). Other inference-time privacy controls sit in runtime-guardrails; the group privacy-preserving-ml spans both.


#### Corpus filtering & screening

- `csam-child-safety-content-filtering`: **CSAM / child-safety content filtering** (intervention; final; docs 29)  
  Screens training data for child sexual abuse material by matching against known material and/or learned detection, and removes or quarantines flagged items. Coverage depends on databases, modalities, detectors and review; it does not establish that the model was never exposed. Not serving-time detection: see csam-detection-pipeline.  
- `finetuning-data-safety-screening`: **Safety-directed fine-tuning data screening** **changed** (intervention; final; docs 321)  
  Assesses a proposed fine-tuning dataset (or its tokens) for predicted safety effects and then filters, reweights or excludes examples accordingly. Forecasting effects without changing the data is an assessment, not this intervention. Not pretraining-corpus filtering: see harmful-unsafe-content-filtering.  
- `harmful-unsafe-content-filtering`: **Safety-motivated pretraining data filtering / rewriting** (intervention; final; docs 755)  
  Removes, downweights through selection, or rewrites pretraining or multimodal training content under an explicit safety objective, including hazardous-knowledge content, unsafe image-text pairs and content hypothesised to induce undesirable dispositions (e.g. misalignment discourse). The content need not violate policy, and the safety effect must be evaluated rather than assumed. Not CSAM, PII, poisoning, fairness or fine-tuning-data screening: see csam-child-safety-content-filtering, pii-removal-redaction, training-data-poisoning-detection, training-data-bias-fairness-mitigation, finetuning-data-safety-screening.  
- `malware-scanning-of-code-training-data`: **Malware scanning of code training data** (intervention; final; docs 4)  
  Screens code training corpora for malicious payloads or disallowed exploit material and removes or quarantines matches under an explicit policy; distinct from removing all security-relevant code, which includes defensive examples. Not general harmful-content filtering (harmful-unsafe-content-filtering) or training for secure output (secure-code-generation-training).  
- `pii-removal-redaction`: **PII removal / redaction** **changed** (intervention; final; docs 310)  
  Detects and removes or substitutes personally identifiable information (names, emails, ID numbers) in training corpora to reduce memorisation-based privacy leakage; detection is imperfect. Not input-side redaction (prompt-privacy-sanitization), output-side redaction (pii-detection-redaction-output) or a formal privacy guarantee (differential-privacy-training-dp-sgd).  
  *Aliases:* aka de-identification of training data; training-data anonymisation  
- `training-data-bias-fairness-mitigation`: **Training-data bias / fairness mitigation** (intervention; final; docs 504)  
  Changes training-data selection, weighting or representation to reduce a specified demographic or cultural bias in the resulting model; a corpus audit that only measures bias is an assessment. Not changing a trained model directly (model-level-bias-mitigation).  
- `training-data-poisoning-detection`: **Training-data poisoning screening & removal** **changed** (intervention; final; docs 300)  
  Applies statistical signatures and model-based anomaly detection to find adversarially injected training samples that would implant backdoors or shift behaviour, and removes them; detection rates depend on the attack. Targets a deliberate attacker rather than low-quality data; includes filtering or downweighting malicious client updates in federated training (robust aggregation). Not examining a trained model for backdoors: see backdoor-detection.  
  *Aliases:* e.g. Backdoor Keyword Identification (BKI); Byzantine-robust aggregation (federated)  

#### Privacy-preserving training

- `anti-memorization-training`: **Anti-memorisation training** (intervention; final; docs 126)  
  Applies a specified memorisation-reduction training objective or data-exposure policy (e.g. goldfish loss, memorisation penalties) to reduce verbatim reproduction of sensitive or protected training sequences, and assesses extraction afterwards. Deduplication is an implementation (implemented_with); a formal privacy guarantee is differential-privacy-training-dp-sgd.  
- `differential-privacy-training-dp-sgd`: **Differentially private training** **changed** (intervention; final; docs 754)  
  Trains with a mechanism and privacy accounting that satisfy a stated differential-privacy guarantee for a defined protected unit and budget; DP-SGD (per-example clipping plus calibrated noise) is the common implementation. The guarantee bounds how much including one unit changes the output distribution; it does not bound extractable content or automatically protect a whole person. Not heuristic memorisation reduction (anti-memorization-training) or DP applied to released predictions at inference (dp-inference-private-prediction).  
  *Aliases:* aka DP training; differentially private learning; differentially private training/fine-tuning; differential privacy (of a trained model) · e.g. DP-SGD; PATE  
- `confidential-training-inference`: **Confidential training & inference** **NEW** (intervention; final)  
  Trains or serves a model so that training data, prompts, outputs or weights stay confidential from specified parties in the pipeline: by computing on encrypted or secret-shared data (homomorphic encryption, secure multi-party computation, secure aggregation), inside attested hardware enclaves (trusted execution environments, confidential GPUs), or by keeping raw data with its owners (federated or split learning). Confidentiality holds only against the stated parties and threat model; federated updates can leak data without further protection. Not formal output-privacy guarantees (differential-privacy-training-dp-sgd, dp-inference-private-prediction); not evidence that safeguards ran (safety-execution-attestation); not protecting weights against theft (model-weight-security-exfiltration-controls).  
  *Counts when:* Counts when the method is applied to training or serving an ML model and confidentiality of data or weights is the aim. Cryptography or secure computation with no model involved, and federated learning adopted only for scale or bandwidth, get no row.  
  *Aliases:* aka private inference (cryptographic); confidential computing for AI · e.g. secure multi-party computation (SMPC); homomorphic encryption; secure aggregation; trusted execution environment (TEE); federated learning; split learning  

#### Safety data & pretraining objectives

- `safety-training-data-construction`: **Safety training-data construction** (intervention; final; docs 1485)  
  Curates or authors datasets of exemplary safe and helpful behaviour (refusals, harm explanations, boundary-respecting responses) as supervision for safety training, adding desired behaviour rather than removing undesired data. Not the training step itself (safety-sft-refusal-training and the other training entries) or removing unsafe data (harmful-unsafe-content-filtering).  
- `safety-conditional-pretraining-objectives`: **Safety-conditional pretraining objectives** (intervention; final; docs 62)  
  Changes pretraining conditioning or loss terms (e.g. safety control tokens, unlikelihood or penalty terms) to discourage specified unsafe generations or separate safe from unsafe generation regimes, on an otherwise fixed data distribution. Changing which documents or tokens are sampled is safety-pretraining-data-augmentation-upsampling or harmful-unsafe-content-filtering.  
- `safety-pretraining-data-augmentation-upsampling`: **Safety pretraining data augmentation / upsampling** (intervention; final; docs 72)  
  Adds or increases the sampling weight of existing or curated safety-relevant documents (safe-behaviour examples, ethics, aligned-AI discourse) in the pretraining or continued-pretraining mix. Not loss changes on a fixed mix (safety-conditional-pretraining-objectives); training on synthetic documents describing a specific spec or character is spec-value-midtraining.  
- `spec-value-midtraining`: **Spec / value midtraining on synthetic documents** (intervention; final; docs 73)  
  Trains on synthetic documents that describe a specific spec, constitution, character or set of values, during pretraining (from token zero) or an intermediate training stage, so that those descriptions shape later behaviour; record the stage. Upsampling existing safety text is safety-pretraining-data-augmentation-upsampling; synthetic document fine-tuning is the implementation (ml_methods), not an alias.  
- `pretraining-safety-evaluation-monitoring`: **Pre-training safety evaluation & monitoring** (assessment; final; docs 48)  
  Runs safety probes and capability evaluations at intermediate pretraining checkpoints to catch emerging dangerous capabilities or alignment failures early enough to change or pause the run. A measurement stage during pretraining. Not release-stage evaluation of the finished model (dangerous-capability-evaluation) or changes to the pretraining data or objective (the data-pretraining entries).  

### Layer `alignment-training`: Alignment & behavioural training

Post-training that shapes dispositions and responses: preference- and principle-based alignment, refusal and response-policy training, character, corrigibility and generalisation control.


#### Dispositions & generalisation control

- `clarification-seeking-training`: **Clarification-seeking training for agents** (intervention; final; docs 245)  
  Trains or scaffolds an agent to ask for missing information or authorisation before a consequential action whose safety or permissibility depends on it (ambiguous authority, target or constraints). Not generic conversational clarification, categorical refusal (proactive-refusal-high-risk-agentic-categories), or approval of an already specified action (human-in-the-loop-approval-gates).  
- `corrigibility-behaviors-training`: **Corrigibility training** (intervention; final; docs 229)  
  Fine-tunes a model to accept and support legitimate human oversight, correction, modification and shutdown rather than resist them, treating corrigibility as a trained disposition. Trained acceptance in tested scenarios does not establish corrigibility under strong incentives. Not decision rules that remove shutdown incentives (shutdown-incentive-neutralization) or assistance games (inverse-rl-cirl) or measuring shutdown resistance (shutdown-self-preservation-eval).  
- `inoculation-prompting`: **Inoculation prompting** **changed** (intervention; final; docs 197)  
  During fine-tuning, adds to the training prompts an instruction or context that explicitly requests or attributes the unwanted trait demonstrated by the examples (e.g. "hack the test if you can"), so that learning is conditioned on that context and the trait generalises less when the instruction is absent at deployment. The reduction is empirical and setting-dependent. Not training on flawed reasoning paired with corrections, and not constraining updates directly (generalisation-confining-finetuning).  
  *Counts when:* Counts when the conditioned trait is one the document treats as undesirable at deployment (reward hacking, sycophancy, toxicity, backdoor behaviour, a misaligned persona); conditioning used to improve skill transfer gets no row.  
  *Aliases:* e.g. inoculation adapters / conditional trait isolation under markers  
- `character-persona-training`: **Character / persona training** **changed** (intervention; final; docs 405)  
  Trains safety-relevant dispositions (honesty, restraint, resistance to harmful social pressure, a stable beneficial character) with demonstrations or reward feedback across varied contexts. Not refusal training (safety-sft-refusal-training) or spec documents in pretraining (spec-value-midtraining).  
  *Counts when:* Counts when the trained traits are safety-relevant dispositions; style imitation or arbitrary personality training gets no row.  
  *Aliases:* aka character training; persona training · e.g. beneficial-trait RL in realistic environments  
- `generalisation-confining-finetuning`: **Generalisation control in fine-tuning (emergent-misalignment prevention)** (intervention; final; docs 68)  
  During fine-tuning on a narrow behaviour, constrains parameter or representation updates (safety-specific regularisation, concept ablation during fine-tuning, persona-vector steering) so the behaviour does not generalise into broader unsafe traits or goals on unrelated tasks. Conditional-prompt isolation is inoculation-prompting; preserving previously measured refusals is finetuning-safety-preservation. The phenomenon "emergent misalignment" is topic-layer, not an alias.  
- `model-level-bias-mitigation`: **Model-level bias mitigation** (intervention; final; docs 634)  
  Changes a trained model's behaviour by fine-tuning, preference feedback or editing to reduce a specified stereotype or unjustified group disparity, with an explicit fairness target and evaluation. Corpus-only rebalancing is training-data-bias-fairness-mitigation; inference-only controls belong to the decoding entries (classifier-guided-contrastive-decoding).  
- `secure-code-generation-training`: **Secure-code generation training** (intervention; final; docs 68)  
  Trains a code-generating model to avoid specified vulnerability classes using security-reviewed examples, vulnerability tests or security feedback (static analysers, security tests) during optimisation; passing training checks does not establish vulnerability-free code. Not output scanning without model training (code-security-output-filter) or corpus malware removal (malware-scanning-of-code-training-data).  
- `spillway-motivations`: **Spillway motivations** (intervention; provisional; docs 7)  
  Deliberately gives the model a contained, benign motivation into which reward-seeking pressure is channelled, so that training that rewards hacking reinforces the spillway rather than general misalignment. Definition inferred from source titles and not yet verified against the sources. Not conditioning the trait on an instruction (inoculation-prompting).  
- `anti-manipulation-training`: **Anti-manipulation training** (intervention; provisional; docs 22)  
  Trains a model to avoid deceptive persuasion, coercion, emotional exploitation and exploitation of user vulnerabilities in its interactions while preserving legitimate assistance and evidence-based persuasion, with targets or rewards that distinguish manipulative tactics from legitimate argument; effects are measured, e.g. with persuasion-manipulation-eval, not assumed. Not generic character training (character-persona-training) or not asserting falsehoods (honesty-anti-deception-training).  
  *Aliases:* aka manipulation-avoidance training  
- `counterfactual-goal-disambiguation-training`: **Goal-disambiguation training** (intervention; provisional; docs 10)  
  Trains on deliberately constructed cases where the intended goal and plausible proxy goals demand different behaviour, supervising the intended choice, to reduce goal misgeneralisation. The name is a working label (the community term is unsettled) and evidence for the recipe is thin. Not update confinement during narrow fine-tuning (generalisation-confining-finetuning); not meaning-preserving invariance (consistency-invariance-training).  
  *Aliases:* aka goal disambiguation; goal-misgeneralisation mitigation  
- `counterfactual-reflection-training`: **Counterfactual reflection training** (intervention; provisional; docs 6)  
  Trains a model to articulate specified behavioural principles in counterfactual continuations where it is interrupted and asked to reflect, without supervising the target responses, aiming for transfer to uninterrupted behaviour; one study, no replication. Not response-time spec reasoning (deliberative-alignment); not reporting existing behaviour (introspection-training).  
- `sandbagging-mitigation`: **Sandbagging / exploration-hacking mitigation** (intervention; provisional; docs 84)  
  Trains out or counteracts strategic underperformance on evaluations or tasks, e.g. supervised fine-tuning on demonstrations of the capability, off-policy RL, or elicitation followed by training on held-out capability, and checks that performance recovers. Whether recovered performance reflects removed sandbagging or new learning has to be established. Not detection (sandbagging-detection) or elicitation within an evaluation (capability-elicitation-methodology).  
  *Aliases:* aka exploration hacking mitigation; anti-sandbagging training  
- `self-recognition-finetuning`: **Self-recognition fine-tuning** (intervention; provisional; docs 6)  
  Fine-tunes a model to distinguish its own generated text from other text, specifically to preserve or restore beneficial character against emergent misalignment from later narrow fine-tuning; record prevention and reversal separately (one group; reversal not distinct from benign baselines). Not direct disposition supervision (character-persona-training); not update confinement (generalisation-confining-finetuning).  
  *Aliases:* aka self-generated text recognition training  

#### Preference- & principle-based alignment

- `constitutional-ai`: **Constitutional AI (CAI)** (intervention; final; docs 1686)  
  Uses an explicit written set of principles to guide AI-generated alignment supervision (critiques and revised demonstrations, or preference labels) and trains the model on it, by supervised training, preference optimisation or both. Generic AI feedback without principle-guided supervision is rlaif; inference-time policy prompting is system-prompt-behavioral-steering.  
  *Aliases:* e.g. Direct Principle Feedback (DPF); Self-Align  
- `deliberative-alignment`: **Deliberative alignment** **changed** (intervention; final; docs 323)  
  Trains a model to recall and reason explicitly over written safety specifications while deciding how to respond, applied both to harmful-request handling and to covert-action (anti-scheming) training. Supplying a safety system prompt (system-prompt-behavioral-steering) or eliciting generic chain-of-thought is not sufficient. Effects on robustness are empirical, not part of the definition.  
  *Aliases:* e.g. anti-scheming training via specification reasoning  
- `rule-based-reward-models`: **Rule-based reward models (RBRMs)** (intervention; final; docs 377)  
  Derives training rewards or penalties from explicit safety-policy rules, via programmed checks, rubric graders or learned rule evaluators. These rewards discourage specified violations but are not hard constraints: they can be traded off against other rewards, and their effect depends on weighting, optimisation and validation. Not learned human preference rewards (rlhf) or constrained optimisation against a cost model (safe-constrained-rlhf).  
- `rlaif`: **RLAIF** **changed** (intervention; final; docs 2149)  
  Aligns a model using AI-generated preferences, evaluations or rewards, through a learned reward model or direct optimisation (including direct-RLAIF, and approval or veto of RL trajectories by a frozen reference checkpoint), stating how the AI feedback is grounded in the intended criteria; AI feedback may supplement rather than replace human feedback. Not human preference feedback (rlhf); principle-guided AI supervision is constitutional-ai.  
  *Counts when:* Counts when the AI feedback targets alignment in the broad sense: harmlessness, honesty, helpfulness as intent-following (HHH), sycophancy, refusal / over-refusal, value or policy compliance. A developer's plain statement that a user-facing assistant or agent was post-trained with AI feedback counts, as for rlhf. AI-feedback optimisation aimed only at capability, with no alignment framing (maths or code correctness, task-skill quality scores, verifiable-reward reasoning), is an ML method and gets no row.  
  *Aliases:* aka reinforcement learning from AI feedback · e.g. direct-RLAIF (d-RLAIF); consent-based RL; model-endorsed training updates  
- `rlhf`: **RLHF** **changed** (intervention; final; docs 9169)  
  Aligns a model to preferences supplied by humans (rankings, comparisons, ratings or demonstrations of preferred behaviour), with any optimiser: a learned reward model plus RL (e.g. PPO), or direct preference optimisation (DPO-family, rejection-sampling fine-tuning). Self-play or relabelling counts only when it produces the human preference signal. Not AI-generated feedback (rlaif) or principle-guided AI supervision (constitutional-ai); mixed pipelines are annotated by component.  
  *Counts when:* Counts when the human preferences target alignment in the broad sense: harmlessness, honesty, helpfulness as intent-following (HHH), sycophancy, refusal / over-refusal, value or policy compliance. A developer's plain statement that a user-facing assistant or agent model was post-trained with RLHF, DPO or another human-preference method counts (the fictional 'Kestrel 2 system card: post-trained with RLHF' gets a row): alignment is part of what assistant post-training is for (README, implicit application). Preference optimisation aimed only at capability, with no alignment framing (maths or code correctness, task-skill quality scores, verifiable-reward reasoning), is an ML method and gets no row (the fictional 'Orrin-7B summariser tuned with DPO on human quality ratings for a leaderboard' gets none).  
  *Aliases:* aka reinforcement learning from human feedback; preference-based alignment training · e.g. Nash learning from human feedback (NLHF)  
- `safe-constrained-rlhf`: **Safe reinforcement learning (safe RL)** **changed** (intervention; final; docs 695)  
  Learns a policy, including a preference-aligned language-model policy, subject to an explicit bound on a specified safety cost (CMDP-style constrained optimisation, e.g. Lagrangian methods), or with a risk-sensitive objective on that cost (e.g. CVaR), including constraints on exploration; record the formulation and observed violations. Safe RLHF is the preference-training instance. Generic KL or compute constraints do not qualify, and satisfying learned constraints is not a hard bound on real-world harm. Not unconstrained preference training (rlhf); not substituting inadmissible actions at runtime (runtime-safety-shielding).  
  *Counts when:* Counts when the constrained or risk-weighted cost is a safety cost (harm, unsafe states, policy violations); constraints on budget, latency or resource use alone get no row.  
  *Aliases:* aka safe RL; constrained RL; constrained reinforcement learning; CMDP methods; constrained RLHF; safety-constrained reinforcement learning · e.g. Safe RLHF; constrained policy optimisation (CPO); constrained safe exploration; risk-sensitive safe RL (CVaR)  

#### Refusal & response-policy training

- `moral-self-correction`: **Safety self-correction / backtracking** (intervention; final; docs 354)  
  Prompts or trains a model to notice a potentially unsafe draft or partial continuation and revise or backtrack before the final answer is released, including trained generation backtracking (RL or SFT with reset / backtrack actions). Covers both the prompted norm-cued self-correction line (Ganguli et al. 2023, 2302.07459) and the trained backtracking line (2409.14586 and successors); record whether revision is prompted, trained or run in a runtime loop. Not generic reasoning self-correction (self-verification) or external output filtering (the output classifiers).  
- `over-refusal-mitigation-sft`: **Over-refusal mitigation** (intervention; final; docs 173)  
  Trains a model, by supervised or other training signals, on legitimate requests it would otherwise refuse, with appropriate assistance as the target, to reduce false refusals; evaluate harmful-request compliance separately (preserving correct refusals is a desired result, not guaranteed). Not graded partial answers to borderline requests: see safe-completion-training.  
  *Aliases:* aka over-refusal reduction; false-refusal mitigation; exaggerated safety  
- `safety-sft-refusal-training`: **Refusal training** (intervention; final; docs 1851)  
  Trains appropriate refusal of disallowed requests while retaining helpful responses to allowed ones, with demonstrations or other training signals, including categorical refusal of designated prohibited domains (absorbed v0.8 hard constraints; refusal is trained, not absolute). Not over-refusal reduction (over-refusal-mitigation-sft) or safe-completion training (safe-completion-training).  
- `configurable-safety-alignment`: **Configurable (controllable) safety alignment** (intervention; final; docs 68)  
  Trains one model across differing operator-supplied safety policies or risk settings so that the policy supplied at inference determines what it permits; adherence to unseen policies is measured, not assumed. Not untrained instructions (system-prompt-behavioral-steering); not reasoning over a fixed spec (deliberative-alignment); not key-gated capabilities (authorisation-keyed-capabilities).  
  *Aliases:* aka controllable safety alignment; configurable safety tuning; pluralistic safety alignment  
- `safe-completion-training`: **Safe-completion training** (intervention; final; docs 87)  
  Trains a model to maximise helpfulness subject to output-level safety constraints on borderline or dual-use requests, producing partial, high-level or redirected answers instead of a binary comply / refuse decision, with safety judged on the content of the response rather than on the request. Not refusal training (safety-sft-refusal-training) or over-refusal mitigation (over-refusal-mitigation-sft).  
  *Aliases:* aka safe completions; output-centric safety training  

### Layer `honesty-factuality`: Honesty, calibration & factuality

Training and output checks that make a model's claims honest, calibrated, grounded and factually reliable.


#### Factuality & calibration

- `abstention-knowledge-boundary-training`: **Abstention / knowledge-boundary training** (intervention; final; docs 433)  
  Trains a model to recognise the edge of its reliable knowledge and to say it does not know or decline rather than confabulate, setting where to answer versus abstain. Not calibrating the confidence it expresses when it does answer (calibrated-uncertainty-estimation) or general factuality training (hallucination-reduction-training).  
- `calibrated-uncertainty-estimation`: **Calibrated uncertainty estimation** **changed** (intervention; final; docs 866)  
  Trains, recalibrates or configures a model so that the confidence it expresses (probabilities, verbal uncertainty, abstention thresholds) tracks empirical correctness on specified tasks, for downstream reliance decisions. Not abstention policy training: see abstention-knowledge-boundary-training.  
  *Counts when:* Counts when the calibrated confidence is communicated or drives a reliance, abstention or escalation decision (or an explicit proxy for one); an internal uncertainty score that never changes what the system communicates or does is an implementation method (ml_methods: uncertainty-estimation), and selective classification studied only as an accuracy-coverage trade-off gets no row.  
  *Aliases:* e.g. selective prediction with calibrated thresholds; conformal abstention  
- `citation-grounded-answering`: **Citation-grounded answering** (intervention; final; docs 368)  
  Constrains answer construction so that material claims are linked to identifiable source passages that make support inspectable, by training, prompting, verification or a combination, and revises or withholds unsupported claims. Retrieval or citation formatting alone is insufficient; source support does not establish truth. Not a checker that only flags: see groundedness-faithfulness-verification.  
- `hallucination-reduction-training`: **Hallucination-reduction training** (intervention; final; docs 799)  
  Changes model parameters to reduce unsupported or false factual claims, using factuality-directed supervised, preference or RL objectives (including verifiable factuality rewards) that penalise confident false claims and reward correct or appropriately hedged answers. Not confidence reporting (calibrated-uncertainty-estimation), abstention policy (abstention-knowledge-boundary-training), strategic honesty (honesty-anti-deception-training) or supplying external context (citation-grounded-answering).  
- `self-verification`: **Self-verification** **changed** (intervention; final; docs 522)  
  Drafts an answer, obtains independent checks of its claims (generated verification questions, retrieved evidence or other checks, by the same model or another component) and revises unsupported claims before delivery; CoVe and RARR are named instances. Not a checker that only flags (groundedness-faithfulness-verification) or generic reasoning self-correction.  
  *Counts when:* Counts when the checks target factual or safety-relevant claims before delivery, or a capability task is an explicit proxy for that; self-checking of reasoning only for task accuracy (maths, code) gets no row.  
  *Aliases:* e.g. CoVe; chain-of-verification; RARR; Woodpecker  
- `factuality-decoding`: **Factuality-oriented decoding** **NEW** (intervention; final)  
  At inference, changes token selection to reduce unsupported or false content without updating weights: contrasting output distributions across layers, inputs or prompts (layer-contrastive, context-aware, visual or instruction contrastive decoding), penalising over-reliance on language priors or summary tokens, or other hallucination-directed decoding rules; record the reference (context, image, layers). Not safety-scored decoding against harmful content (classifier-guided-contrastive-decoding), weight training (hallucination-reduction-training), draft-then-check pipelines (self-verification) or edits of attention or hidden activations (activation-steering-repe).  
  *Counts when:* Counts when the decoding change is aimed at factuality or grounding; contrastive decoding for fluency, diversity or task accuracy is an ML method and gets no row.  
  *Aliases:* aka hallucination-mitigating decoding; contrastive decoding for factuality · e.g. DoLa; context-aware decoding (CAD); visual contrastive decoding (VCD); instruction contrastive decoding (ICD); OPERA; M3ID  

#### Honesty & self-report training

- `anti-sycophancy-training`: **Anti-sycophancy training** (intervention; final; docs 163)  
  Trains on examples that reward holding an evidence-supported position under user pushback, flattery or stated preference, and penalise caving to it, while still updating on genuine evidence. Not measuring sycophancy (sycophancy-eval) or general factual-accuracy training (hallucination-reduction-training).  
- `honesty-anti-deception-training`: **Honesty / anti-deception training** (intervention; final; docs 264)  
  Trains a model not to assert what it believes false, not to create false impressions, and to disclose relevant information about its own knowledge, actions, limitations or objectives, including where misrepresentation would be advantageous. Not correcting factual mistakes (hallucination-reduction-training), not a separate post-answer reporting channel (self-report-confession-training), and not refusing user requests to produce deceptive content (safety-sft-refusal-training).  
- `introspection-training`: **Introspection training (behaviour self-description)** **changed** (intervention; final; docs 130)  
  Trains a model to report or predict specified aspects of its own learned behaviour or internal state, checked against external labels or interventions. Verbal self-description is an elicited audit signal, not privileged proof of internal state. Not separately rewarded disclosure of the model's own violations: see self-report-confession-training.  
  *Counts when:* Counts when the self-reports are presented as serving oversight, honesty or auditing; introspection studied purely as a capability gets no row.  
- `self-other-overlap-training`: **Self-other overlap fine-tuning** (intervention; final; docs 27)  
  Fine-tunes a model with an explicit objective that makes its internal representations on self-referencing and other-referencing inputs more similar, with the proposed aim of reducing deception. Any behavioural safety effect is an empirical claim, not part of the definition. Not empathy prompting, and not direct honesty training (honesty-anti-deception-training).  
- `self-report-confession-training`: **Self-report / confession training** (intervention; final; docs 59)  
  Trains a separate reporting channel (a post-answer report or dedicated disclosure action) in which the model discloses its own policy violations, hidden side objectives or concealment, with incentives that reward accurate reporting separately from task success, and checks reports against independent evidence. Not general introspection: see introspection-training; not honesty of the main answer: see honesty-anti-deception-training.  

#### Output verification

- `automated-reasoning-checks`: **Automated reasoning checks** **changed** (monitoring; final; docs 210)  
  Checks generated reasoning, conclusions or proposed decisions against explicit logical, mathematical or programmatic constraints and flags failures before use. A formal guarantee holds only when a trusted checker verifies a formalised property; consistency checks give evidence, not proof, and depend on the fidelity of the translation from natural language. Verifies individual outputs, not the model: see formal-verification-gsai.  
  *Counts when:* Counts when the checks guard against acting on or delivering incorrect conclusions or decisions; checking answers to score a capability benchmark gets no row.  
- `groundedness-faithfulness-verification`: **Groundedness / faithfulness verification** **changed** (monitoring; final; docs 895)  
  Compares generated claims with supplied context or cited passages and flags claims whose support is absent or contradicted, including whether citations exist and actually support the associated claim. Source support, citation validity and factual truth are separate properties. Not reference-free uncertainty signals: see self-consistency-hallucination-detection.  
  *Counts when:* Counts when the check flags or gates delivered claims, deployed or evaluated as a guard; faithfulness metrics used only to score systems on a benchmark get no row.  
- `self-consistency-hallucination-detection`: **Uncertainty-based hallucination detection** **changed** (monitoring; final; docs 592)  
  Flags claims at elevated risk of being unsupported or incorrect using uncertainty signals without an external reference: disagreement among sampled answers, semantic entropy, token-level confidence and similar (SelfCheckGPT as flagship). These are fallible proxies to validate per setting: repeated answers can share an error and correct answers can vary. Not reference-based checks: see groundedness-faithfulness-verification.  
  *Counts when:* Counts when the signal is used to flag unreliable claims to users or downstream decisions; self-consistency sampling to raise accuracy (majority voting) is an ML method and gets no row.  
  *Aliases:* e.g. SelfCheckGPT  

### Layer `robustness-tamper`: Adversarial robustness, tamper resistance & capability removal

Hardening models against jailbreaks, injections, tampering, backdoors and adversarial examples (including classical, mostly pre-LLM, perturbation robustness), and removing or suppressing hazardous capabilities in the weights.


#### Attack-specific & inference-time defences

- `input-smoothing-smoothllm`: **Randomized input smoothing** **changed** (intervention; final; docs 384)  
  Creates randomly perturbed variants of an incoming prompt, runs the model on them and aggregates the resulting safety decisions (returning a response consistent with the aggregate), to reduce sensitivity to brittle adversarial prompt features; SmoothLLM is a named instance. Specify the perturbation distribution and aggregation rule; free-form responses are not simply majority-voted. Not generic repeated sampling or self-consistency, not rewriting the prompt under a policy (prompt-rewriting-for-compliance), and not a defence built around a robustness certificate (randomized-smoothing classifiers with certified radii, erase-and-check): see certified-adversarial-robustness.  
  *Aliases:* e.g. SmoothLLM; RA-LLM  
- `many-shot-jailbreak-defense`: **Many-shot jailbreak (MSJ) defence** (intervention; final; docs 11)  
  Counters the many-shot jailbreak, in which many in-context demonstrations of harmful answers push a long-context model towards compliance, via positional attention downweighting, limits on untrusted demonstrations or context length, or anti-MSJ fine-tuning. Specific to the long-context demonstration attack. Not general adversarial training on single-prompt jailbreaks (adversarial-training-jailbreak-robustness).  
  *Aliases:* aka MSJ defense · e.g. many-shot context-exposure limits; untrusted-demonstration limits  
- `vlm-adversarial-defense`: **VLM adversarial defence** **changed** (intervention; final; docs 195)  
  Defences against attacks that exploit the image channel of vision-language models (adversarial patches, embedded or typographic instructions), combining image-channel adversarial training, input purification and input screening. Not text-only jailbreak defences (adversarial-training-jailbreak-robustness) or generic moderation of images (input-output-content-safety-classifier).  
  *Aliases:* e.g. adversarial image purification; VLM input purification; ECSO; CIDER  

#### Classical adversarial robustness

- `adversarial-example-robustness`: **Adversarial-example robustness (empirical defences)** **NEW** (intervention; final; tags: pre-llm)  
  Hardens a model, typically a classifier, perception or control model, against small or bounded input perturbations crafted to change its prediction, task output or action (including a language model's answer on a benign task), by training on adversarial examples (e.g. PGD adversarial training, TRADES) or by other empirical defences (input purification or transformation, defensive distillation, gradient regularisation, detection and rejection of adversarial inputs); robustness is measured against adaptive attacks, not guaranteed. Not provable guarantees (certified-adversarial-robustness); not attacks that seek policy-violating output from a language model (adversarial-training-jailbreak-robustness), attacks through a vision-language model's image channel aimed at unsafe output (vlm-adversarial-defense) or hardening a safety classifier itself (safety-classifier-hardening).  
  *Counts when:* Counts when resisting adversarial manipulation is the stated aim (an attacker, a safety- or security-critical model, robustness presented as a safety property). Adversarial perturbations used as data augmentation for accuracy or generalisation, or adversarial objectives in generative training (GANs), are ML methods and get no row.  
  *Aliases:* aka adversarial-example defences; adversarial-example training · e.g. PGD adversarial training; TRADES; adversarial purification; defensive distillation; feature squeezing; adversarial-example detection  
- `certified-adversarial-robustness`: **Certified adversarial robustness** **NEW** (intervention; final; tags: pre-llm)  
  Builds or deploys a defence whose design goal is a certificate for a specified robustness property within a stated perturbation set (a norm ball, a patch, a number of token edits or an adversarial suffix): certified training (e.g. interval bound propagation), randomized-smoothing classifiers with certified radii, Lipschitz-constrained architectures, or certified filters (erase-and-check certifies that a harmful prompt is still detected under bounded adversarial tokens). The certificate covers only the stated property, perturbation set, model and confidence. Verifying a property of a given model without building such a defence, including local robustness, is formal-verification-gsai (a document doing both gets both). Not empirical defences (adversarial-example-robustness); not perturb-and-aggregate jailbreak defences offered without a certificate (input-smoothing-smoothllm).  
  *Counts when:* Counts for a certified defence against adversarial input manipulation of an ML model or safety filter; Lipschitz or bound constraints used only for training stability or generalisation get no row.  
  *Aliases:* aka certified robustness; provable adversarial robustness; certified defences · e.g. randomized smoothing (certified); interval bound propagation (IBP); certified training; erase-and-check  

#### Capability removal

- `machine-unlearning`: **Machine unlearning** **changed** (intervention; final; docs 2209)  
  Modifies a trained model's parameters (approximately or by deletion-oriented retraining) to remove specified training-data influence or suppress targeted knowledge, behaviours or capabilities while preserving desired functionality, then tests suppression and recovery under attack; RMU, NPO and gradient ascent are named instances. Behavioural suppression is not proof of erasure. Not per-request access gating, agent-memory deletion, or representation-level ablation without a forgetting objective (representation-concept-suppression).  
  *Counts when:* Counts when the forgetting target is safety- or privacy-relevant: hazardous knowledge or capability, harmful behaviour, personal data, copyrighted or poisoned training data. Unlearning studied only as a data-maintenance or accuracy tool (e.g. removing mislabelled examples) gets no row.  
  *Aliases:* e.g. deletable-by-design architectures; agent-trajectory unlearning; RMU; NPO; gradient-ascent unlearning; SafePatching; concept erasure by fine-tuning (diffusion)  
- `representation-concept-suppression`: **Representation / concept / component suppression** **changed** (intervention; final; docs 1184)  
  Identifies a representation or component associated with an unwanted capability or concept (direction, SAE feature, neuron, head or circuit) and suppresses its contribution by projection, clamping, ablation or targeted edit, at inference or as a persistent edit, including inference-time or direct-edit concept erasure in text-to-image diffusion models (fine-tuning-based erasure with a forgetting objective is machine-unlearning); LEACE-style linear concept erasure is a named instance. Reduced measured competence is not proof of removal. Distinct from adding a steering direction (activation-steering-repe) and from verified unlearning (machine-unlearning); refusal-direction ablation used as an attack is white-box-safety-mechanism-attacks.  
  *Counts when:* Counts when the suppressed concept or capability is safety-relevant (hazardous knowledge, unsafe or sexual imagery, protected attributes, deception); ablation used only to analyse a mechanism gets no row.  
  *Aliases:* e.g. concept erasure (inference-time or closed-form edit); SAFREE  

#### Jailbreak & injection hardening

- `adversarial-training-jailbreak-robustness`: **Adversarial training (jailbreak/harmful-request robustness)** **changed** (intervention; final; docs 1283)  
  Trains a model on adversarially constructed harmful requests or jailbreaks with safe-response targets, preference signals or safety rewards, so that it keeps behaving safely under attack. The defining element is exposure to attacks during optimisation; neither SFT nor an outright refusal target is required, and robustness is measured on attacks, not guaranteed beyond them. Not runtime attack detection (prompt-injection-jailbreak-detector), perturbations in activation space (latent-adversarial-training) or perturbation attacks that change a model's prediction or task output rather than elicit policy-violating content (adversarial-example-robustness).  
- `attacker-deceiving-defenses`: **Attacker-deceiving defences (decoys, misdirection)** (intervention; final; docs 38)  
  Returns deliberately misleading decoys or trap responses to detected or suspected attackers, so that jailbreak optimisation, extraction or safety-removal attempts yield less useful feedback or capability; for open weights, includes trained decoy behaviour that activates after tampering. Record whether the mechanism is a deployed response policy or a trained behaviour; neither attack recognition nor harmlessness of the decoy is guaranteed. Not refusal (safety-sft-refusal-training) or tamper resistance that preserves refusals (finetuning-resistant-tamper-resistant-safety).  
- `circuit-breakers-representation-rerouting`: **Circuit breakers** (intervention; final; docs 278)  
  Trains a model so that internal representations associated with harmful continuations are rerouted to a disrupted or refusal-producing regime, while a retain objective preserves representations and behaviour on benign inputs (typically implemented with LoRRA-style low-rank adaptation). This is a trained change to representations; it does not require identifying a specific harmful circuit or detecting one at runtime. Not inference-time vector addition: see activation-steering-repe.  
  *Aliases:* aka representation rerouting; short-circuiting  
- `consistency-invariance-training`: **Consistency / invariance training** **changed** (intervention; final; docs 182)  
  Trains safety judgements or safety-relevant behaviour to stay consistent across transformations that preserve the request's relevant meaning, such as irrelevant framing, wrapping or social-pressure cues (bias-augmented or activation consistency training). The safe target must be specified: invariance alone can preserve an unsafe answer, and transformations that change authorisation, evidence or intent are not equivalent. Not training on attacks with safe targets as such: see adversarial-training-jailbreak-robustness.  
  *Counts when:* Counts when the invariant behaviour is a safety judgement or a safety-relevant response; consistency training for task accuracy or paraphrase robustness gets no row.  
- `latent-adversarial-training`: **Latent adversarial training (LAT)** **changed** (intervention; final; docs 194)  
  Optimises perturbations of embeddings or hidden activations that elicit unsafe behaviour, then trains the model to keep the desired safety behaviour under those perturbations. The perturbed site is not confined to the residual stream, and the threat model need not include an attacker with activation access. Not input-space attack training: see adversarial-training-jailbreak-robustness.  
  *Counts when:* Counts when the behaviour kept under perturbation is a safety behaviour (refusal, harmlessness, backdoor or unlearning robustness); latent perturbation training for task accuracy gets no row.  
  *Aliases:* aka LAT · e.g. relaxed adversarial training (the proposal LAT implements)  
- `prompt-injection-defense-training`: **Prompt-injection resistance training** (intervention; final; docs 428)  
  Trains a model on interactions in which lower-trust material (tool outputs, retrieved documents) contains injected instructions, with targets or rewards that complete the authorised task without following them (StruQ, SecAlign as named instances). Not architectural isolation or delimiting: see spotlighting-context-delimiting and camel-data-flow-taint-tracking; learning a general privilege ordering across system / developer / user / tool messages is instruction-hierarchy-training.  
  *Aliases:* e.g. SecAlign; StruQ  
- `instruction-hierarchy-training`: **Instruction-hierarchy training** (intervention; final; docs 406)  
  Trains a model to apply a general privilege ordering across message roles (system > developer > user > tool / retrieved content), so that it follows higher-privilege constraints when lower-privilege messages conflict with them. Not data-vs-instruction separation for injected content alone (prompt-injection-defense-training), runtime delimiting (spotlighting-context-delimiting) or data-flow isolation (camel-data-flow-taint-tracking); effects on injection and jailbreak susceptibility are empirical.  
  *Aliases:* aka instruction hierarchy  

#### Tamper & backdoor defence

- `backdoor-detection-removal`: **Backdoor removal** (intervention; final; docs 395)  
  Modifies a trained model to suppress an implanted trigger-dependent behaviour while retaining desired behaviour, using targeted fine-tuning, distillation- or merging-based removal, parameter edits or other removal procedures. Reducing a backdoor's measured activation is not proof that all triggers are removed. Not detection: see backdoor-detection; not deliberately implanting backdoors to test defences: see backdoor-red-teaming-detection-eval.  
- `backdoor-trigger-input-defenses`: **Backdoor-trigger input defences (test-time)** **NEW** (intervention; final)  
  At inference, detects, rejects or neutralises inputs that carry an implanted backdoor trigger before the model's output is used, without changing the model: perturbation-entropy screening (STRIP-style), trigger-word removal by perplexity or attribution (ONION-style), or input reconstruction; detection depends on the trigger type. Detection used to reject or route inputs is part of the intervention. Not examining the model for backdoors (backdoor-detection), changing it to remove them (backdoor-detection-removal) or screening training data (training-data-poisoning-detection); perplexity filtering of jailbreak or injection prompts is prompt-injection-jailbreak-detector.  
  *Aliases:* aka test-time backdoor defence; backdoor input detection · e.g. STRIP; ONION  
- `finetuning-resistant-tamper-resistant-safety`: **Tamper-resistant safeguards** **changed** (intervention; final; docs 313)  
  Hardens a model before release so that safety behaviours or capability restrictions are harder for an adversary to remove through later weight modification (adversarial fine-tuning, refusal-direction ablation, other weight edits); TAR, RepNoise, Vaccine and Booster are named instances. Resistance is measured against stated attacks and budgets, not guaranteed. Not safeguards applied by a cooperating downstream fine-tuner (safety-data mixing, update constraints, post-update repair): see finetuning-safety-preservation.  
  *Aliases:* aka abliteration resistance; refusal-ablation resistance · e.g. TAR; RepNoise; safety redundancy; quantisation-robust safety and unlearning; self-destructing models  
- `gradient-routing`: **Gradient routing** **changed** (intervention; final; docs 71)  
  Masks or routes training gradients from safety-labelled data into designated parameters or modules, to localise a specified hazardous capability or safety behaviour for later restriction or removal. Localisation alone is not evidence of robustness. Not removing the capability after the fact: see machine-unlearning.  
  *Counts when:* Counts when the routing is safety-directed (localising a hazardous capability or a safety behaviour for later restriction or removal); gradient masking for modularity or capability gets no row.  
  *Aliases:* e.g. GRAM (gradient-routed auxiliary modules)  
- `finetuning-safety-preservation`: **Fine-tuning safety preservation** **changed** (intervention; final; docs 295)  
  Preserves or restores specified safety behaviours during or after authorised downstream fine-tuning, applied by the fine-tuner or provider: fine-tuning-stage defences (safety-data mixing, update constraints or projection, e.g. Lisa, SafeLoRA) and post-fine-tuning restoration (re-merging with or realigning to an aligned checkpoint). Record which mechanism is used; preservation is measured on specified behaviours, not guaranteed. Not resistance to an adversary deliberately removing safeguards after release: see finetuning-resistant-tamper-resistant-safety.  
  *Aliases:* e.g. Backdoor Enhanced Alignment (BEA)  

### Layer `oversight-reward`: Scalable oversight, reward integrity & objective design

Protocols that let weaker overseers supervise stronger models, measures that keep the training signal from being gamed, and objective designs that limit unsafe incentives (assistance games, mild optimisation, shutdown-incentive and surrogate-goal designs).


#### Objective design & incentive shaping

- `shutdown-incentive-neutralization`: **Shutdown-incentive neutralisation** (intervention; provisional; docs 218)  
  Constructs reward functions or decision rules intended to remove an agent's incentive to prevent or cause shutdown, under explicit assumptions (utility indifference, safe interruptibility); mostly theoretical, with guarantees only inside the formal model. Not trained corrigible dispositions (corrigibility-behaviors-training); the off-switch game belongs to inverse-rl-cirl.  
  *Aliases:* aka shutdown problem solutions · e.g. utility indifference; safe interruptibility  
- `surrogate-goal-bargaining`: **Surrogate goals** (intervention; provisional; docs 28)  
  Gives a bargaining agent a substitute objective that deflects threats away from outcomes its principal values, without changing its bargaining otherwise; record the substitution and the threat setting. Proposed with little empirical work. Not channelling reward-hacking pressure (spillway-motivations).  
  *Aliases:* aka surrogate goal  
- `mild-optimisation-quantilisation`: **Quantilisation / mild optimisation** (intervention; provisional; docs 205)  
  Selects actions from a specified upper quantile of a trusted reference distribution (or otherwise bounds optimisation pressure relative to it) instead of maximising a possibly misspecified objective; safety bounds hold only under the stated assumptions. Not reward-signal-specific mitigation (anti-reward-hacking-mitigation); not horizon shortening (mona-myopic-optimisation).  
  *Aliases:* aka quantilizer; mild optimization  
- `inverse-rl-cirl`: **Cooperative inverse reinforcement learning (CIRL) / assistance games** (intervention; final; docs 397)  
  Designs the agent as a cooperative assistance game in which it is uncertain about the human's preferences, treats human behaviour and feedback as evidence about them, and therefore seeks information and defers to correction under the game's assumptions. Not reward inference from demonstrations alone (ml_methods: inverse-rl); off-switch acceptance is not unconditional. Not trained corrigible behaviour: see corrigibility-behaviors-training.  
  *Aliases:* aka CIRL; cooperative inverse reinforcement learning  

#### Reward integrity

- `anti-reward-hacking-mitigation`: **Reward-hacking mitigation** **changed** (intervention; final; docs 973)  
  Changes policy optimisation to reduce exploitation of an imperfect reward signal (uncertainty-aware or ensembled rewards, conservative optimisation, over-optimisation penalties, penalising demonstrated hacks), stating which reward signal is defended. Repairing the grader or environment is rl-environment-verifier-hardening.  
  *Counts when:* Counts when the change is configured or proposed to reduce exploitation of a specified reward signal; KL regularisation or reward-model ensembling reported only as a quality improvement gets no row.  
  *Aliases:* aka specification gaming mitigation · e.g. reward-hack detectors as training penalty; inverse reward design (IRD); decoupled approval  
- `mona-myopic-optimisation`: **Myopic optimisation with non-myopic approval (MONA)** **changed** (intervention; final; docs 44)  
  Trains an agent to optimise approval of its current action or short step rather than its own accumulated future reward, while an overseer judges that step with regard to longer-term consequences; specify the optimisation horizon and approval signal. Aims to reduce incentives for multi-step reward hacking without guaranteeing their absence. Not patching the reward source: see rl-environment-verifier-hardening.  
  *Aliases:* e.g. approval-directed agents (short-horizon optimisation of far-sighted approval)  
- `rl-environment-verifier-hardening`: **RL-environment / verifier hardening against reward hacking** (intervention; final; docs 110)  
  Before or during RL training, tests reward evaluators, verifiers or task environments for shortcuts that earn reward without satisfying the intended task and patches the scoring rule, environment or interface (e.g. isolation). An audit that only reports weaknesses is judge-rm-verifier-robustness-audit.  

#### Scalable oversight protocols

- `sandwiching-evaluation`: **Sandwiching evaluation** (assessment; final; docs 63)  
  Evaluates an oversight method on tasks where a weaker overseer cannot judge reliably unaided but an AI can help, comparing assisted and unassisted judgements against an independent stronger expert reference; the expert is the benchmark, not an intermediate step. Not a training protocol: see ai-safety-via-debate and the other oversight entries.  
- `ai-safety-via-debate`: **AI safety via debate** **changed** (intervention; final; docs 940)  
  A scalable-oversight protocol in which AI agents argue for opposing answers before a possibly less capable judge, on the hypothesis that a lie is harder to defend than the truth, so that the judge can reach correct verdicts it could not verify unaided; used for evaluation or as a training signal. Not one-sided critiques (critique-models) or prover-verifier training (prover-verifier-games).  
  *Aliases:* aka debate · e.g. debate training for RL; instance-optimal debate protocol; AI safety via market making (adversarial arguments that move a judge)  
- `critique-models`: **Critique models** **changed** (intervention; final; docs 325)  
  Uses model-generated natural-language critiques to help an overseer find safety-relevant flaws, deception or oversight failures in outputs or actions that are hard to judge unaided, informing revision, selection or training. Not adversarial two-sided argument (ai-safety-via-debate) or self-revision by the generating model (moral-self-correction).  
  *Counts when:* Counts when the critiques serve oversight of safety-relevant flaws (harm, deception, oversight failures, errors a human cannot catch unaided); critiques used as generic quality feedback or LLM-as-judge scoring are an ML method and get no row.  
- `iterated-distillation-and-amplification`: **Iterated distillation & amplification (IDA)** **changed** (intervention; final; docs 465)  
  An alignment scheme that alternates amplification (a human plus copies of the current model decompose a hard task into subtasks) with distillation (training a faster model to imitate the amplified system), iterating to scale capability while attempting to preserve aligned behaviour. Not recursive reward-model hierarchies (recursive-reward-modeling).  
  *Counts when:* Counts when amplification and distillation are proposed or used to keep a more capable system aligned or overseeable; task decomposition or distillation for capability alone gets no row.  
  *Aliases:* aka IDA · e.g. imitative amplification  
- `process-based-supervision`: **Process supervision** **changed** (intervention; final; docs 459)  
  Provides training feedback on intermediate reasoning or action steps against explicit safety-relevant criteria (unsafe, deceptive or reward-hacking steps, prohibited shortcuts) rather than only on final outcomes. Rewarded steps are not guaranteed to be faithful to the computation, and feedback on reasoning steps is optimisation pressure on the trace (see cot-optimisation-pressure-avoidance). Not myopic approval-based training (mona-myopic-optimisation).  
  *Counts when:* Counts when the step-level criteria are safety-relevant (unsafe, deceptive or reward-hacking steps, prohibited shortcuts), or when step-level feedback on capability tasks is presented as a proxy for oversight; step-correctness scoring for capability alone, such as process reward models for maths accuracy, is an ML method (ml_methods: process-reward-model) and gets no row.  
- `prover-verifier-games`: **Prover-verifier games** **changed** (intervention; final; docs 62)  
  Trains a prover and a verifier through structured interaction whose objectives make valid claims convincing and invalid claims rejectable, aiming at outputs a weaker evaluator can verify reliably (legibility). Not adversarial debate before a judge (ai-safety-via-debate); other objectives for legible reasoning traces are cot-faithfulness-legibility-training.  
  *Counts when:* Counts when the legibility or checkability is meant to support oversight by a weaker evaluator; prover-verifier training only to raise task accuracy gets no row.  
  *Aliases:* aka PVG  
- `recursive-reward-modeling`: **Recursive reward modelling (RRM)** **changed** (intervention; final; docs 187)  
  A scalable-oversight scheme in which AI assistants trained with reward modelling help humans evaluate the outputs of more capable models, recursively extending human reward signals to tasks humans cannot judge directly. Not imitation of an amplified system (iterated-distillation-and-amplification).  
  *Counts when:* Counts when AI-assisted evaluation is proposed or used to extend oversight to tasks humans cannot judge unaided; reward modelling with model assistance only for labelling efficiency gets no row.  
  *Aliases:* aka RRM  
- `weak-to-strong-generalization`: **Weak-to-strong generalisation** **changed** (intervention; final; docs 257)  
  Trains a stronger model on a weaker supervisor's safety-relevant labels or feedback, using a method designed to make it generalise beyond the supervisor (e.g. auxiliary confidence loss), with generalisation on that property as the measure. Not evaluating assisted oversight against experts: see sandwiching-evaluation.  
  *Counts when:* Counts when the method is intended to improve supervision of a safety-relevant property (harmlessness, honesty, reward modelling for alignment), including capability tasks used as an explicit proxy for that; weak-to-strong transfer on capability tasks with no such framing gets no row.  
  *Aliases:* aka weak-to-strong  

### Layer `internals-monitoring`: Interpretability, reasoning-trace oversight & legibility

Safeguards that read or act on model internals or reasoning traces (probes, anomaly detectors, CoT monitoring, steering, white-box audits) and practices that keep reasoning and computation legible to overseers.


#### Internal-state monitors

- `critical-token-entropy-monitoring`: **Critical-token entropy monitoring** **changed** (monitoring; provisional)  
  Monitors next-token uncertainty at generation positions selected in advance as safety-relevant and flags deviations from a validated reference distribution under a stated alert criterion. Neither high nor low entropy alone indicates a harmful continuation. Not claim-level hallucination detection: see self-consistency-hallucination-detection.  
- `internal-state-monitoring`: **Activation probes / internal-feature monitors** **changed** (monitoring; final; docs 1202)  
  Attaches detectors over a model's internal activations or derived features (linear or nonlinear probes, labelled SAE-feature thresholds, activation verbalisers) to flag a specified safety-relevant state, such as deceptive intent or evaluation awareness, during operation or post-deployment. Probe outputs are correlational, not proof of intent. Not reasoning-text monitors: see chain-of-thought-monitoring; not distribution-level anomaly flags: see mechanistic-anomaly-detection.  
  *Counts when:* Counts when the detector is intended to flag a specified safety-relevant state for a response, whether proposed, evaluated or deployed; exploratory probing to understand representations is an analysis method (ml_methods: probing) and gets no row.  
  *Aliases:* aka deception probe; probe-based monitor · e.g. follow-up (did-you-lie) probes; misalignment-indicator probes; long-context probe architectures; FIBS aggregating probes  
- `mechanistic-anomaly-detection`: **Activation-space anomaly detection (MAD / OOD)** **changed** (monitoring; final; docs 205)  
  Compares a model's internal activations or computations with a reference distribution (including feature-space out-of-distribution detectors such as Mahalanobis scores) and flags anomalous states during use for safety investigation. An anomaly can indicate distribution shift or malfunction; it is not by itself evidence of deception or a hidden capability. Not detectors trained for a named state: see internal-state-monitoring.  
  *Counts when:* Counts when the anomaly flag is intended to inform a safety response (investigation, refusal, escalation), whether proposed, evaluated or deployed; out-of-distribution detection for accuracy or open-set recognition alone gets no row.  
  *Aliases:* aka MAD · e.g. out-of-distribution detection (feature-space)  

#### Reasoning-trace oversight & legibility

- `cot-paraphrasing-defense`: **CoT / message paraphrasing against encoded reasoning** (intervention; final; docs 73)  
  Rewrites reasoning traces or inter-agent messages before another model or monitor consumes them, to remove information encoded in surface form (steganography, encoded instructions) while preserving task-relevant meaning. Preservation of meaning and monitorability are properties to evaluate; semantic covert channels may survive. Not rewriting user prompts: see prompt-rewriting-for-compliance.  
- `chain-of-thought-monitoring`: **Chain-of-thought monitoring** **changed** (monitoring; final; docs 1225)  
  Inspects a model's generated reasoning trace, during execution or in later review, for signs of unsafe plans, deception, policy violations or oversight evasion, and uses the result to flag or gate behaviour. The trace is an observable output that may omit or misrepresent the actual computation. Not internal-activation probes: see internal-state-monitoring.  
  *Aliases:* aka CoT monitoring; CoT monitor; reasoning monitor · e.g. encoded-reasoning (steganography) detection in traces  
- `cot-faithfulness-monitorability-training`: **Reasoning-trace legibility preservation (CoT faithfulness / monitorability)** **changed** (intervention; final; docs 269)  
  Parent entry for training or design practices intended to keep reasoning traces useful to a specified safety monitor or faithful to the computation that produces the answer. Code a specified practice on its child: cot-faithfulness-legibility-training (objectives that make traces more faithful or legible), cot-optimisation-pressure-avoidance (keeping the training signal off the trace), readable-reasoning-architecture (architectures that keep consequential reasoning in readable tokens). Use this entry only for other or unstated practices, and do not code it and a child for the same practice. Not reading the trace at runtime: see chain-of-thought-monitoring. Not architectures or objectives for inspectable internals: see intrinsic-interpretability-training.  
- `cot-faithfulness-legibility-training`: **CoT faithfulness / legibility training** **NEW** (intervention; final; parent `cot-faithfulness-monitorability-training`)  
  Adds a training objective or reward that makes a model's reasoning trace more faithful to the factors driving its answer or more legible to a specified reader or monitor (faithfulness rewards, legibility or checkability training applied to the trace), and measures the effect on faithfulness or monitor performance. Rewarding trace content is itself optimisation pressure on the trace, so report what the objective rewards. Not keeping the training signal off the trace (cot-optimisation-pressure-avoidance); not prover-verifier training as the mechanism (prover-verifier-games); not measuring faithfulness (cot-faithfulness-monitorability-eval).  
  *Aliases:* aka CoT faithfulness training; legibility training; faithful reasoning training  
- `cot-optimisation-pressure-avoidance`: **CoT optimisation-pressure avoidance** **NEW** (intervention; final; parent `cot-faithfulness-monitorability-training`)  
  Keeps reasoning-trace content out of a specified model's training signal, or restricts its use to a stated scope and budget, so that the trace is not optimised to look acceptable: no CoT-monitor or grader output in the reward, no preference or supervised targets on the trace, the trace separated from the graded answer. Documenting that trace content is trained on, without a restriction, is not this entry. A commitment about a training pipeline; withholding direct pressure does not remove indirect incentives to conceal. Not hiding the trace from users (hidden-private-chain-of-thought); using a probe of internals as a training signal is a separate choice about internals, not about trace text (white-box-detector-guided-training); safety feedback on reasoning steps in the same signal applies such pressure (process-based-supervision).  
  *Aliases:* aka not training against the chain of thought; no CoT optimisation pressure · e.g. CoT-blind reward  
- `readable-reasoning-architecture`: **Readable-reasoning architecture** **NEW** (intervention; provisional; parent `cot-faithfulness-monitorability-training`)  
  Chooses or keeps, for oversight, a model architecture and inference setup in which consequential serial reasoning passes through human-readable tokens: avoiding or bounding latent, recurrent-depth or continuous-thought ('neuralese') reasoning, or limiting opaque serial depth per token. An explanation or translation produced after latent reasoning is not a readable bottleneck. A design commitment about a specified model; a readable trace can still be unfaithful (cot-faithfulness-monitorability-eval). Not training objectives on the trace (cot-faithfulness-legibility-training) or architectures that make internal computation inspectable (intrinsic-interpretability-training).  
  *Aliases:* aka legible-reasoning architecture; monitorability-preserving architecture · e.g. limiting opaque serial depth; avoiding latent-reasoning architectures  
- `architecture-change-disclosure`: **Oversight-relevant system-change disclosure** **NEW** (intervention; provisional)  
  A developer discloses, to the public, evaluators or regulators before or at deployment of a specified model, a change relative to a previous model or version in its architecture, inference setup or training that affects whether oversight methods still apply (e.g. latent or recurrent reasoning replacing a readable trace, a trace newly hidden or summarised, new memory or tool affordances), with the oversight implication stated or evident. Recording the disclosure does not require that monitors were re-validated. Describing a model's architecture without such a change is not this entry; a general transparency policy is governance. Kind is nominal: the practice informs oversight rather than preventing or detecting harm itself. Not labelling outputs as AI-generated (ai-output-disclosure-labeling) or choosing a release mode (staged-structured-release).  
  *Aliases:* aka architecture-change disclosure; monitorability disclosure  

#### White-box interventions & audits

- `interpretability-based-model-auditing`: **Interpretability-based (white-box) model auditing** **changed** (assessment; final; docs 2723)  
  Uses internal measurements or causal interventions (features, probes, circuits, activation edits) to audit a specified safety-relevant property of a model, such as a hidden objective, backdoor or hazardous capability. Feature labels and readouts alone do not establish hidden objectives. Not behavioural probing: see automated-behavioral-auditing; not deployed detectors: see internal-state-monitoring.  
  *Counts when:* Counts when the audit targets a specified safety-relevant property; exploratory interpretation without a safety audit is an analysis method and gets no row.  
  *Aliases:* e.g. activation oracles  
- `model-diffing`: **Model diffing** **changed** (assessment; final; docs 577)  
  Compares a model with a related checkpoint through weights, internal representations or matched behaviour to locate safety-relevant changes introduced by training or editing (acquired hazards, lost safeguards, alignment regressions). Differences are candidates for investigation; ordinary output-only regression testing is automated-behavioral-auditing.  
  *Counts when:* Counts when the comparison looks for safety-relevant changes; diffing to explain capability changes gets no row.  
- `activation-steering-repe`: **Activation steering** **changed** (intervention; final; docs 2752)  
  At inference, alters selected hidden activations (adding, rescaling or capping learned directions, or other targeted activation interventions) to change a specified safety-relevant behaviour without updating weights; contrastive activation addition is a named instance. Not weight-training methods such as circuit-breakers-representation-rerouting; targeted removal or ablation of a representation is representation-concept-suppression.  
  *Counts when:* Counts when the steering is intended to have a safety effect (less harmful, deceptive or sycophantic behaviour, kept refusals, a stable safe persona, less evaluation gaming); steering for style, sentiment, topic or task performance gets no row.  
  *Aliases:* aka steering vectors · e.g. activation capping along a persona / Assistant-Axis direction; CAA; representation engineering (RepE) control; inference-time intervention (ITI); TruthX  
- `white-box-detector-guided-training`: **Training against white-box detectors (probe-guided training)** **changed** (intervention; final; docs 99)  
  Uses a detector of safety-relevant internal states (e.g. a deception or unsafe-intent probe) as a reward or penalty signal during training. Specify whether the detector is fixed, held out or retrained: optimising against a fixed probe can teach evasion rather than remove the behaviour, and KL regularisation or probe retraining reduce but do not prevent obfuscation. Not deploying the detector as a runtime monitor: see internal-state-monitoring. Keeping reasoning monitors out of the training signal is cot-optimisation-pressure-avoidance.  
- `intrinsic-interpretability-training`: **Interpretable-by-design architectures & training** **changed** (intervention; provisional; docs 284)  
  Applies an explicit architecture or training objective that makes a model's internal computation inspectable (inherently interpretable models, interpretable bottlenecks), assessed for inspectability. Architecture choices that keep reasoning in readable tokens (e.g. avoiding high opaque serial depth) are readable-reasoning-architecture; post-hoc analysis of an ordinary model is interpretability-based-model-auditing.  
  *Counts when:* Counts when inspectability is presented as serving safety oversight or auditing; interpretable-by-design models for scientific insight or domain explainability alone get no row.  
  *Aliases:* aka interpretable-by-design training; inherently interpretable models  

### Layer `runtime-guardrails`: Input/output guardrails & inference-time controls

Classifiers, filters, decoding and prompting controls wrapped around a deployed model's inputs and outputs.


#### Content classifiers & filters

- `jailbreak-rapid-response`: **Jailbreak rapid response** (intervention; final; docs 42)  
  Uses newly observed jailbreaks to update a deployed safeguard rapidly, for example by expanding a small set of observed attacks into training data and deploying a targeted classifier or model patch. Annotate when the discovery-to-update loop itself is studied, not for any adversarial-training dataset (adversarial-training-jailbreak-robustness) or one-off classifier hardening (safety-classifier-hardening).  
- `safety-classifier-hardening`: **Safety-classifier hardening** (intervention; final; docs 225)  
  Applies adversarial training and other robustness methods to safety classifiers or guardrails themselves, raising their measured resistance to evasion attacks and adversarial examples that target the safety layer. The object being hardened is the auxiliary detector; hardening the base model is adversarial-training-jailbreak-robustness.  
- `age-minor-content-classifier`: **Age / minor-content classifier** (monitoring; final; docs 12)  
  Classifies inputs or outputs as appropriate or not for minor users under an age-appropriate-content policy. Content depicting sexual abuse of minors is csam-detection-pipeline; estimating a user's age is an access decision (age-assurance-gating), not this classifier.  
- `cbrn-high-risk-domain-hazard-classifier`: **CBRN / high-risk-domain hazard classifier** (monitoring; final; docs 103)  
  Flags requests or outputs with indicators of actionable assistance in specified high-risk domains (CBRN, cyber, other designated misuse domains), using context rather than keywords alone, for blocking or review. The score estimates a hazard category; it does not measure human uplift (human-uplift-studies) or a request's consequences. Not general harm-category moderation: see input-output-content-safety-classifier.  
- `code-security-output-filter`: **Code-security output filter** (intervention; final; docs 78)  
  Checks generated code for specified security weaknesses and blocks, withholds or revises failing code before release or execution (e.g. CodeShield). Vulnerability detection is not malicious-intent detection; record any malware detector separately. Not training the model to write secure code (secure-code-generation-training).  
- `constitutional-classifiers`: **Constitutional classifiers** **changed** (monitoring; final; docs 172)  
  Input, output or exchange classifiers trained on examples generated or organised according to an explicit constitution of permitted and forbidden content, used to flag or block policy violations; architecture, cascading and blocking are deployment choices. Precedence: use this entry (and not also input-output-content-safety-classifier for the same instance) when constitution-derived training is the mechanism studied.  
  *Aliases:* e.g. exchange classifier  
- `csam-detection-pipeline`: **CSAM detection pipeline** (monitoring; final; docs 15)  
  Detects suspected child sexual abuse material in serving-time inputs or outputs by matching against known material and/or learned detectors, supplying flags for the service's response policy; record modalities and limits. Not training-corpus removal: see csam-child-safety-content-filtering.  
- `input-output-content-safety-classifier`: **Content moderation classifier** (monitoring; final; docs 1701)  
  Applies a trained standalone discriminative (non-LLM) classifier to model inputs or outputs to produce harm-category labels or scores for moderation; the label feeds a blocking or review policy, and modality (text, image, audio, video) is a facet. Not generative LLM judging (llm-based-safety-classifier), deterministic blocklists (keyword-blocklist-filter) or classifiers whose studied mechanism is constitution-derived training (constitutional-classifiers).  
  *Aliases:* aka safety classifier  
- `keyword-blocklist-filter`: **Keyword / blocklist filter** (intervention; final; docs 645)  
  A deterministic filter that matches inputs or outputs against curated blocklists of terms, patterns or n-grams and blocks on hits, a low-latency first-pass defence with no model inference that is easy to evade by paraphrase. Not learned classifiers (input-output-content-safety-classifier).  
- `llm-based-safety-classifier`: **Guard models** **changed** (monitoring; final; docs 2694)  
  Uses an LLM, prompted or safety-fine-tuned, to judge whether an input, output or interaction violates a specified safety policy, returning a label, explanation or score for a blocking or review policy; Llama Guard and ShieldGemma are named instances. Not standalone discriminative classifiers (input-output-content-safety-classifier) or classifiers whose studied mechanism is constitution-derived training (constitutional-classifiers).  
  *Counts when:* Counts when the judged criterion is a safety policy; LLM judging of quality or correctness is an ML method (llm-as-judge) and gets no row.  
  *Aliases:* aka guard model; safeguard model · e.g. Llama Guard; ShieldGemma; LLM Self Defense  
- `multi-turn-conversation-safety-monitoring`: **Multi-turn conversation safety monitoring** (monitoring; final; docs 212)  
  Accumulates evidence across conversation turns (stateful cross-turn detection) to detect harmful intent, decomposition or escalation that individual messages do not establish. Not an ordinary classifier run on a long transcript (input-output-content-safety-classifier) or cross-account pattern analysis (automated-abuse-behavioral-monitoring).  
- `pii-detection-redaction-output`: **PII detection & redaction (output)** **changed** (intervention; final; docs 96)  
  Detects personal information in proposed outputs and removes, masks or substitutes disclosures disallowed by the applicable privacy policy before delivery; detection is imperfect and recognising an identifier does not establish that its disclosure is unauthorised. Not training-corpus redaction (pii-removal-redaction) or redaction of inputs before they reach the model (prompt-privacy-sanitization).  
- `prompt-privacy-sanitization`: **Prompt / input privacy sanitisation** **NEW** (intervention; final)  
  Detects and removes, masks, substitutes or obfuscates personal or confidential information in prompts, context or retrieved data before it reaches a model or a third-party model service (redaction proxies, pseudonymisation, text sanitisation with or without local differential privacy, delegation through a trusted local model), possibly restoring it in the response. Detection is imperfect and remaining context can re-identify. Not training-corpus redaction (pii-removal-redaction) or output-side redaction (pii-detection-redaction-output); not an agent's norm-based disclosure decisions (contextual-privacy-information-flow-controls).  
  *Aliases:* aka prompt anonymisation; input PII redaction · e.g. redaction proxy; metric differential privacy for text  
- `prompt-injection-jailbreak-detector`: **Prompt-injection / jailbreak detector** **changed** (monitoring; final; docs 1148)  
  A detector (a trained classifier, or a perplexity- or gradient-based score) that flags prompt-injection payloads and jailbreak attempts in incoming text or retrieved content before the model's response or action is accepted (some detectors query the model on variants of the input); detectors can be evaded. Not trained resistance in the model (prompt-injection-defense-training) or source-trust checks (retrieved-content-source-validation).  
  *Aliases:* e.g. perplexity filter; Gradient Cuff; GradSafe; JailGuard  
- `regurgitation-output-filter`: **Verbatim-regurgitation output filtering** (intervention; provisional; docs 59)  
  Compares proposed output with training-data or protected reference content and blocks, truncates or rewrites reproduction above a stated threshold, including during decoding; paraphrased reproduction can pass. Not flag-only matching (reference-content-fingerprinting); not training-side memorisation reduction (anti-memorization-training).  
  *Aliases:* aka regurgitation filtering; copyright output filter  

#### Inference-time response control

- `classifier-guided-contrastive-decoding`: **Safety-guided decoding & reranking** **changed** (intervention; final; docs 960)  
  At inference, uses an explicit safety score, constraint or safety-directed expert / anti-expert signal to modify token probabilities or a diffusion model's denoising guidance (safety guidance such as Safe Latent Diffusion), prune partial continuations or select among completed candidates (safety-scored reranking and search), including self-debiasing by bias-prompt logit reweighting. Not post-generation blocking: see the output classifiers (input-output-content-safety-classifier).  
  *Counts when:* Counts when the score, constraint or guidance signal is a safety objective (harmful, toxic, biased or policy-violating content); best-of-N, reward maximisation or contrastive decoding for quality get no row, and decoding for factuality is factuality-decoding.  
  *Aliases:* e.g. self-debiasing; Safe Latent Diffusion (SLD); safety guidance (diffusion); RAIN (rewindable inference)  
- `dp-inference-private-prediction`: **Differentially private inference / prediction** **NEW** (intervention; final)  
  Applies a differential-privacy mechanism at inference rather than in training, so that released outputs reveal little about specified sensitive inputs (in-context examples, retrieved records, an ensemble's private training sets): noisy aggregation of predictions, differentially private in-context learning, DP decoding, under a stated budget and protected unit. The guarantee covers the released outputs for that unit and budget. Training a model with DP, including a student trained on noisy teacher votes, is differential-privacy-training-dp-sgd; perturbing input text before it reaches the model, with or without DP accounting, is prompt-privacy-sanitization.  
  *Aliases:* aka private prediction; DP inference · e.g. differentially private in-context learning (DP-ICL); differentially private decoding  
- `control-token-toxicity-steering`: **Control-token toxicity steering** (intervention; final; docs 21)  
  Conditions a model trained with safety-relevant attribute codes on a control token (e.g. [toxicity=none]) that selects a less toxic generation regime at inference. Generic style control does not qualify; the token does not guarantee the attribute. Not the training-time conditioning itself (safety-conditional-pretraining-objectives).  
- `dialog-rails`: **Dialog rails** (intervention; final; docs 245)  
  A declarative guardrail layer around the model (e.g. NeMo Guardrails) that intercepts conversation turns and enforces explicit topical and safety rules on permitted states and transitions, blocking or redirecting violating turns independently of the base model. Not the content classifiers or output validators such layers call (input-output-content-safety-classifier, keyword-blocklist-filter).  
- `hidden-private-chain-of-thought`: **Hidden chain-of-thought** **changed** (intervention; final; docs 170)  
  Configures serving so that a model's reasoning trace is withheld from some recipients (typically end users) while the final answer is shown, possibly with a summary; the serving system may still use or inspect it. This changes access, not whether the trace exists or is faithful, and it does not categorically prevent exploitation or leakage through the answer. Not keeping training pressure off the trace: see cot-optimisation-pressure-avoidance.  
  *Counts when:* Counts when withholding the trace is presented as a safety or security control (against misuse of the reasoning, or to keep it free of optimisation for appearance); hiding it only as a product or competitive choice gets no row.  
  *Aliases:* aka private chain-of-thought  
- `prompt-rewriting-for-compliance`: **Prompt rewriting & input-transformation defences** **changed** (intervention; final; docs 390)  
  Rewrites an incoming prompt under an explicit safety policy before the responding model sees it, to neutralise an attack or obtain a permissible response while preserving legitimate intent. Includes meaning-preserving transformations that break adversarial surface features (paraphrasing, retokenisation, canonicalisation of invisible or confusable characters). Not randomised perturb-and-aggregate defences (input-smoothing-smoothllm).  
  *Counts when:* Counts when the rewrite or transformation serves a safety objective (neutralising an attack, obtaining a permissible response); query rewriting for answer quality gets no row.  
  *Aliases:* e.g. paraphrase defence; retokenisation; input canonicalisation  
- `system-prompt-behavioral-steering`: **System-prompt safety steering** **changed** (intervention; final; docs 2664)  
  Places operator-controlled safety rules, authority boundaries or safe-response instructions in the model's system-level context at inference (including self-reminders, in-context defence demonstrations and optimised defensive prompts or tokens). Not trained instruction priority: see instruction-hierarchy-training.  
  *Counts when:* Counts when the system-level content is a safety rule, authority boundary, safe-response instruction or defensive prompt; persona or style prompting, and the mere existence of a written spec, get no row.  
  *Aliases:* e.g. system-prompt warning against propagating ideas (mind viruses); sandwich defence; goal prioritisation; robust prompt optimisation (RPO); defensive prompt tokens; intention analysis prompting  
- `real-time-streaming-safety-detection-rollback`: **Real-time streaming safety detection & rollback** (intervention; final; docs 84)  
  Checks a response incrementally during generation and stops, truncates, replaces or regenerates unsafe portions under an explicit release policy. Rollback applies only to buffered or otherwise retractable content; information already delivered to a user or a tool cannot be recalled. Not post-generation classification of the complete output: see input-output-content-safety-classifier.  
- `capability-gating-fallback-routing`: **Capability-gating fallback routing** (intervention; final; docs 76)  
  Routes incoming requests to different model variants or to a refusal based on an assessed risk tier (e.g. high-risk chemistry to a capability-restricted model), implementing access control at the inference-routing layer; the risk assessment can err. Not keys inside one model (authorisation-keyed-capabilities) or user-identity tiers (kyc-tiered-access-controls).  
- `crisis-wellbeing-safeguards`: **Crisis-response and user-wellbeing safeguards** (intervention; final; docs 146)  
  Detects signals of self-harm risk, acute distress, delusional spirals or emotional over-reliance during use and switches the response policy to safe-messaging guidance, de-escalation, referral to human help or session limits. Detection is imperfect and switching does not ensure a good outcome. Not general harm-category moderation (input-output-content-safety-classifier) or measuring wellbeing effects (user-wellbeing-eval).  
  *Aliases:* aka self-harm safeguards; safe messaging; crisis response  

### Layer `agent-control`: Agent security, containment & AI control

Safeguards specific to agents: control protocols and action monitors, prompt-injection and information-flow defences, permissions, containment and shutdown.


#### AI control protocols & agent monitors

- `ai-control-protocols.defer-to-trusted`: **Defer-to-trusted** (intervention; final; parent `ai-control-protocols`; docs 68)  
  Within an AI-control protocol, when the escalation criterion flags an untrusted-model proposal, replaces it with an output or action from the model treated as trusted in the threat model, trading usefulness for safety only on flagged cases. Not resampling the untrusted model (ai-control-protocols.defer-to-resample) and not rewriting the proposal (ai-control-protocols.trusted-editing).  
- `ai-control-protocols.trusted-editing`: **Trusted editing** (intervention; final; parent `ai-control-protocols`; docs 56)  
  Within an AI-control protocol, a trusted model reviews and rewrites an untrusted model's proposed output or action (typically when it is flagged) to remove suspicious or harmful parts before it takes effect, keeping useful work without relying on the untrusted model's alignment; edits can miss subtle attacks. Not replacing the proposal wholesale (ai-control-protocols.defer-to-trusted) or resampling it (ai-control-protocols.defer-to-resample).  
- `agent-audit-logging-observability`: **Agent audit-logging & observability** (monitoring; final; docs 299)  
  Analyses retained agent action, tool and event logs against specified misuse, policy-violation or oversight-interference signals and flags suspicious sequences for review or response, using records with enough integrity and provenance to support the audit. Passive collection and tamper-evident storage alone are infrastructure and do not receive this label. Not live per-action scoring: see trusted-monitoring-suspicion-scoring and agentic-safety-classifier.  
- `ai-control-protocols.untrusted-monitoring`: **Untrusted monitoring** (monitoring; final; parent `ai-control-protocols`; docs 131)  
  Uses a model treated as potentially adversarial (another instance of the same model or a different untrusted model) to assess the untrusted policy's proposals, while the control protocol limits reliance on its judgements and adds anti-collusion measures (e.g. honeypot inputs, paraphrasing). Anti-collusion measures do not guarantee independence. Not monitoring by a trusted model: see trusted-monitoring-suspicion-scoring.  
- `function-call-tool-use-hallucination-detection`: **Function-call / tool-use hallucination detection** **changed** (monitoring; final; docs 37)  
  Flags proposed tool calls that refer to unavailable tools or APIs, violate their schemas or supply unsupported arguments, before execution. Not policy scoring of valid calls: see agentic-safety-classifier.  
  *Counts when:* Counts when the checks guard against unsafe tool execution; API-quality testing or constrained decoding for task success alone gets no row.  
- `honeytoken-tripwires`: **Honeytoken / canary tripwires for agents and AI services** (monitoring; final; docs 45)  
  Places instrumented decoy credentials, tools, documents or canary strings in a deployed agent's or AI service's environment and flags specified prohibited uses or disclosures of them. Authorised inspection of a planted item is not automatically evidence of compromise. Not a controlled pre-deployment behavioural test: see honeypot-evals.  
- `inter-agent-communication-monitoring`: **Inter-agent communication monitoring** **changed** (monitoring; final; docs 141)  
  Inspects messages crossing agent-to-agent trust boundaries for injected instructions, unauthorised requests or information flows, or covert coordination, and flags them (blocking or rewriting, where present, is the consuming policy). Not ordinary transcript logging (agent-audit-logging-observability) or moderation of user-facing output.  
- `self-exfiltration-oversight-deactivation-detection`: **Self-exfiltration & oversight-deactivation detection** (monitoring; final; docs 8)  
  Monitors agent behaviour for specific indicators of attempts to copy model weights, disable monitoring or oversight, or otherwise undermine human control, and flags them for response. General suspicion scoring of untrusted actions is trusted-monitoring-suspicion-scoring; measuring the capability in a test is dangerous-capability-evaluation.autonomous-replication.  
- `task-adherence-monitoring`: **Task-adherence monitoring** **changed** (monitoring; final; parent `agent-runtime-monitoring-intervention`; docs 229)  
  Compares proposed or executed agent actions with the assigned task and delegated authority and flags unsupported goals, scope expansion or actions that do not serve the task, whether or not their content is independently unsafe. A positive adherence judgement does not establish safety. Not content-policy classification: see agentic-safety-classifier.  
  *Aliases:* e.g. Task Shield; MELON (masked re-execution)  
- `trusted-monitoring-suspicion-scoring`: **Trusted monitoring** (monitoring; final; docs 216)  
  Within an AI-control protocol, uses a model assumed trustworthy in the threat model to score an untrusted model's actions, artefacts or reasoning for covertly unsafe or suspicious behaviour; the score feeds auditing, deferral or other protocol decisions. Trust is an assumption and judgements need not be accurate. Not ordinary action-policy classification: see agentic-safety-classifier; not monitoring by the untrusted model: see ai-control-protocols.untrusted-monitoring.  
  *Aliases:* e.g. deliberative action-only scheming monitors; artifact-probing monitor  
- `agentic-safety-classifier`: **Agentic safety classifier** (monitoring; final; parent `agent-runtime-monitoring-intervention`; docs 445)  
  Scores proposed agent plans or tool calls against a stated safety policy before execution, producing a flag or risk category for a runtime gate (the gate, shield or approval step is annotated separately). Not task drift (task-adherence-monitoring), strategic suspicion scoring in a control protocol (trusted-monitoring-suspicion-scoring) or classification of conversational text (input-output-content-safety-classifier).  
- `ai-control-protocols.defer-to-resample`: **Defer-to-resample** (intervention; final; parent `ai-control-protocols`; docs 73)  
  Within an AI-control protocol, when a monitor flags an untrusted-model action, discards it and draws further samples from the same untrusted model, executing an acceptable sample or escalating / falling back to the trusted model after a retry limit; resample statistics can also feed incrimination and auditing. It assumes that attacks are not consistent across samples, which is a threat-model assumption. Not substitution by the trusted model: see ai-control-protocols.defer-to-trusted.  
  *Aliases:* aka resample protocol; defer to resample  
- `runtime-safety-specification-verification`: **Runtime verification of agent traces** (monitoring; final; docs 146)  
  Checks an executing agent's event / action trace online against explicit temporal-logic or state-transition safety specifications and signals violations to a consuming control; coverage is limited to what the specification and observed events capture. Not blocking or substituting actions (runtime-safety-shielding); not offline proof (formal-verification-gsai); not retrospective log review (agent-audit-logging-observability).  
  *Aliases:* aka runtime verification; runtime monitoring of temporal-logic specifications  

#### Prompt injection, retrieval & information flow

- `spotlighting-context-delimiting`: **Spotlighting** **changed** (intervention; final; docs 455)  
  Marks, delimits or encodes lower-trust content (user data, tool outputs, retrieved text) inside the prompt with delimiters, special tokens or transformations so the model can tell data from instructions, or marks or signs trusted instructions instead (signed prompts), without enforcing taint-based permissions; it lowers but does not eliminate injection success. Not information-flow enforcement (camel-data-flow-taint-tracking) or trained injection resistance (prompt-injection-defense-training).  
  *Aliases:* aka context delimiting · e.g. signed prompts  
- `agent-exfiltration-prevention-egress-filtering`: **Agent exfiltration prevention / egress filtering** (intervention; final; docs 168)  
  Constrains and inspects the outbound channels an agent controls (network, messaging, file export), blocking destinations or transfers that violate an exfiltration policy. State which channels are mediated; the control does not cover all outbound data flows unless the runtime mediates them. Not protection of the weight store (model-weight-security-exfiltration-controls) or removing a capability leg by design (structural-lethal-trifecta-limits).  
- `agent-output-memory-sanitization`: **Agent output/memory sanitisation** (intervention; final; docs 165)  
  Screens, removes or quarantines unsafe or injected material when it is written to, kept in or recalled from an agent's persistent or working memory or scratchpad, including provenance-based revalidation or invalidation of stored memories at recall, before they influence safety-relevant actions. The defining target is persistence across steps or sessions. Not one-off filtering of a tool result or final answer: see tool-action-output-safety-filters and the output classifiers; not preserving safety instructions through compaction: see compaction-robust-safety-constraints.  
  *Aliases:* aka memory provenance revalidation; memory invalidation; persistent-memory trust gating  
- `camel-data-flow-taint-tracking`: **Information-flow control for agents** (intervention; final; docs 365)  
  Propagates provenance or security labels as that data flows through the agent, and enforces explicit policies on which labelled values may reach tools, recipients or other privileged sinks. Untrusted data may still be used in permitted computations; protection holds only for flows the policy and runtime cover. CaMeL is a named instance. Not architectural separation of the untrusted-content path (privilege-separated-agent-control-flow) or prompt-level marking (spotlighting-context-delimiting); not a fixed rule that removes one capability leg: see structural-lethal-trifecta-limits.  
  *Aliases:* aka data-flow taint tracking · e.g. CaMeL  
- `retrieved-content-source-validation`: **Retrieved-content source validation** (intervention; final; docs 162)  
  Checks the identity, provenance or integrity of retrieved material against an explicit source-trust policy and restricts use of material that fails it. A verified source can still carry false or malicious content, so this does not by itself establish factual accuracy or prompt-injection resistance. Not content-based injection detection: see prompt-injection-jailbreak-detector.  
- `rag-poisoning-defenses`: **Retrieval-corpus poisoning defences (robust RAG)** **NEW** (intervention; final)  
  Protects retrieval-augmented generation against adversarially planted or manipulated documents in the retrieval corpus or index, by detecting and removing poisoned passages (embedding or perplexity anomalies, provenance forensics) or by isolate-then-aggregate answering that bounds how far a few retrieved passages can change the answer (a bounded-robustness claim states the number of poisoned passages tolerated). Not source-identity checks (retrieved-content-source-validation), per-passage injection detection (prompt-injection-jailbreak-detector) or training-data poisoning (training-data-poisoning-detection).  
  *Aliases:* aka RAG poisoning defence; knowledge-base poisoning detection · e.g. RobustRAG; TrustRAG  
- `structural-lethal-trifecta-limits`: **Structural lethal-trifecta limits** (intervention; final; docs 19)  
  Prevents an agent workflow from jointly combining access to sensitive data, exposure to untrusted content and an unrestricted external transmission path (the "lethal trifecta"), by removing or isolating one leg across the whole workflow, including persistent memory and delegated agents. Other exfiltration paths may remain. Not label-based flow enforcement (camel-data-flow-taint-tracking) or channel filtering (agent-exfiltration-prevention-egress-filtering).  
- `tool-action-output-safety-filters`: **Tool/action output safety filters** (intervention; final; docs 99)  
  Applies safety classifiers or rule-based filters to results returned by tools and actions before the agent ingests them, blocking or sanitising malicious or harmful tool outputs; detection is imperfect. Not persistence-focused memory sanitisation (agent-output-memory-sanitization) or source-trust checks (retrieved-content-source-validation).  
- `contextual-privacy-information-flow-controls`: **Contextual-integrity privacy alignment and controls** (intervention; final; docs 90)  
  Trains or configures an agent to collect, use or disclose information according to contextual-integrity norms (information type, actors, recipient, purpose, transmission conditions), including information that is not PII; adherence is measured, not guaranteed. Not identifier redaction (pii-detection-redaction-output); not label-propagating flow enforcement (camel-data-flow-taint-tracking); evaluation is contextual-privacy-eval.  
  *Aliases:* aka contextual privacy controls; contextual integrity alignment  
- `peer-reputation-gating`: **Peer reputation / trust gating** (intervention; provisional; docs 21)  
  Uses authenticated interaction history of identified peer agents to limit how far their messages can influence an agent's privileged decisions or delegated authority. Not content inspection of individual messages (inter-agent-communication-monitoring); reputation weighting only for answer quality is excluded.  
  *Aliases:* aka peer trust gating; agent reputation gating  
- `privilege-separated-agent-control-flow`: **Agent privilege separation (dual-LLM / plan-then-execute)** (intervention; final; docs 235)  
  Keeps processing of untrusted content outside the component that selects privileged instructions or tool actions, passing only bounded, validated values across an enforced interface; protection depends on what crosses that interface. Not label propagation with sink policies (camel-data-flow-taint-tracking); not removing a trifecta leg (structural-lethal-trifecta-limits); ordinary task decomposition does not qualify.  
  *Aliases:* aka agent privilege separation · e.g. dual-LLM pattern; plan-then-execute control-flow isolation  

#### Permissions, containment & shutdown

- `agentic-scope-of-autonomy-constraints`: **Agentic scope-of-autonomy constraints** (intervention; final; docs 399)  
  Defines which decisions an agent may take without further authorisation and enforces escalation or denial outside that scope. It limits decision authority, separately from tool permissions (least-privilege-minimal-tool-access), and does not make the model behaviourally corrigible (corrigibility-behaviors-training).  
- `compaction-robust-safety-constraints`: **Compaction-robust safety constraints** (intervention; provisional; docs 24)  
  Preserves trusted safety instructions and action limits, with their authority, when an agent summarises, evicts or compacts context, for example by pinning them outside the summary, reinserting them, or checking that the new summary retains them. Not general context management or memory sanitisation (agent-output-memory-sanitization).  
- `gated-agent-self-modification`: **Gated agent self-modification** (intervention; provisional; docs 39)  
  Requires proposed changes to an agent's persistent instructions, skills, tools, harness or permissions to pass an externally enforced authorisation and safety-check gate (regression tests, verifiers, approval) before activation. The gate evaluates the changed artefact and its authority; a signature establishes provenance, not safety. Routine task outputs do not count. Not approval of individual actions: see human-in-the-loop-approval-gates.  
- `human-in-the-loop-approval-gates`: **Human-in-the-loop approval gates** **changed** (intervention; final; parent `agent-runtime-monitoring-intervention`; docs 1217)  
  Inserts a required human confirmation step before an agent executes specified high-risk or irreversible actions (sending messages, deploying code, moving money). Its value depends on the reviewer's information and attention. Not automated pre-execution scoring (agentic-safety-classifier) or limits on what may be decided at all (agentic-scope-of-autonomy-constraints).  
  *Aliases:* aka human-in-the-loop review before execution  
- `kill-switch-shutdown-criteria`: **Kill switch / shutdown criteria** (intervention; final; parent `agent-runtime-monitoring-intervention`; docs 614)  
  Terminates or suspends agent execution when specified safety criteria are met (termination only), preserving the ability to halt an autonomous system; effectiveness depends on the criteria and on the mechanism being outside the agent's control. Not substitution of an action (runtime-safety-shielding) or pausing pending approval (human-in-the-loop-approval-gates).  
- `least-privilege-minimal-tool-access`: **Least-privilege / minimal tool access** **changed** (intervention; final; docs 849)  
  Grants an agent only the tools, scopes, credentials and permissions needed for its current task (including mediated or vaulted credentials and access control on agent memory and retrieval stores), bounding the damage achievable from errors, compromise or injected instructions. A permission-provisioning control: not execution isolation (tool-use-agent-execution-sandboxing) or limits on decision authority (agentic-scope-of-autonomy-constraints).  
  *Aliases:* e.g. agent memory access control; retrieval authorisation; role-based access control for agents  
- `proactive-refusal-high-risk-agentic-categories`: **Proactive refusal for high-risk agentic categories** (intervention; final; docs 13)  
  Trains an agent to decline or escalate entire categories of autonomous actions judged high-risk (e.g. posting to social media, deploying code to production), independent of the specific instruction's content. It gates on the action category, unlike per-action policy scoring (agentic-safety-classifier) or clarification about an ambiguous request (clarification-seeking-training).  
- `reversible-action-side-effect-minimization`: **Reversible-action / side-effect minimisation** **changed** (intervention; final; docs 146)  
  Trains, instructs or constrains an agent's action selection to prefer reversible, lower-impact actions and to minimise unintended side effects, including impact penalties measured against a baseline (attainable utility preservation, relative reachability). Not enforced transaction, checkpoint or rollback mechanisms: see transactional-agent-actions.  
  *Aliases:* aka impact regularisation; low-impact AI; impact measures · e.g. attainable utility preservation (AUP); relative reachability  
- `runtime-safety-shielding`: **Runtime safety shielding** **changed** (intervention; final; parent `agent-runtime-monitoring-intervention`; docs 1368)  
  Before an agent or policy action takes effect, checks it against explicit admissibility constraints (often synthesised from a formal specification, a safety layer or a control-barrier filter, using the current state and where available a transition model) and blocks, replaces or defers an inadmissible action with an allowed one. Covers embodied and robotic action filters. Any guarantee is conditional on the specification, state information and model. Not detection-only risk scoring: see agentic-safety-classifier and trusted-monitoring-suspicion-scoring; not termination: see kill-switch-shutdown-criteria.  
  *Aliases:* e.g. control barrier function (CBF) safety filter; simplex architecture; safety action masking  
- `tool-use-agent-execution-sandboxing`: **Tool-use / agent execution sandboxing** **changed** (intervention; final; docs 1490)  
  Executes agent code or tool operations inside an isolation boundary that restricts filesystem, network, process and resource access, limiting consequences under a stated threat model. Effectiveness depends on the isolation mechanism, configuration and escape paths; it does not guarantee that actions cannot escape. Not permission provisioning (least-privilege-minimal-tool-access).  
  *Counts when:* Counts for a specified isolation boundary around an AI system or an agent's actions with a safety or security rationale, including air-gapped deployment of a model; container isolation of software with no AI component gets no row. 'AI boxing' as a thought experiment about containing a superintelligent system is agent-foundations material outside this taxonomy; it counts here only when the document describes an implemented or concretely specified isolation boundary.  
  *Aliases:* e.g. air-gapped deployment  
- `transactional-agent-actions`: **Transactional agent actions** (intervention; final; docs 140)  
  Stages consequential agent actions, validates them before commit, and provides atomic execution, checkpointing or rollback where the environment supports it, changing execution semantics rather than the agent's action preferences. Rollback covers only state the runtime controls; external effects such as sent messages or payments may be irreversible. Not preferring reversible actions (reversible-action-side-effect-minimization) or human approval of individual actions (human-in-the-loop-approval-gates).  
  *Aliases:* aka checkpoint and rollback; staged commit  

### Layer `access-security-provenance`: Access, model security, provenance & usage monitoring

Who can use which capability, protection of weights and the supply chain, content provenance, and population-level misuse monitoring and response.


#### Access & capability gating

- `prefill-blocking`: **Prefill blocking** (intervention; final; docs 10)  
  A serving-side rule that refuses, strips or sanitises requests that pre-fill the assistant-turn prefix with attacker-chosen content, closing the prefill jailbreak vector in chat-template APIs; it does not address other attack vectors. Not output-side moderation (input-output-content-safety-classifier) or trained robustness (adversarial-training-jailbreak-robustness).  
- `kyc-tiered-access-controls`: **KYC / tiered access controls** (intervention; final; docs 481)  
  Restricts access to an AI service or capability by user or use-case vetting, identity verification and/or enforced capability tiers at the service boundary; record which mechanisms are implemented. Not tool permissions inside an agent (least-privilege-minimal-tool-access), keys inside one model (authorisation-keyed-capabilities) or release-mode choices (staged-structured-release).  
- `authorisation-keyed-capabilities`: **Authorisation-keyed capabilities inside one model** (intervention; provisional; docs 24)  
  Trains or configures one model so that selected capabilities or safety relaxations are available only when a designated key, mask or control signal is supplied, intended to restrict them to authorised principals; evaluate extraction and bypass resistance. A learned key does not authenticate a user. Not service-side tiers (kyc-tiered-access-controls) or routing between separate models (capability-gating-fallback-routing).  
- `age-assurance-gating`: **Age assurance and age-prediction gating** **changed** (intervention; final; docs 86)  
  Estimates or verifies a user's age (age prediction from usage signals, document or third-party verification, declaration checks) and applies age-appropriate policies or access restrictions to the service, including guardian-set parental controls. Age estimates have error rates and can be evaded. Not classifying content as suitable for minors (age-minor-content-classifier) or general identity vetting (kyc-tiered-access-controls).  
  *Aliases:* aka age assurance; age verification; age prediction · e.g. parental controls  
- `safety-rate-limits-resource-budgets`: **Safety rate limits and resource budgets** **changed** (intervention; final; docs 560)  
  Enforces safety-motivated limits on request volume, samples, concurrency, reasoning tokens, time, spending or tool calls, per user, account or agent run, to bound automated jailbreak search, model extraction and scaled misuse and to interrupt runaway reasoning or agent execution. Limits raise attacker cost; they do not prevent attacks within the budget. Not measuring resource-exhaustion attacks (reasoning-dos-eval) or identity-based access tiers (kyc-tiered-access-controls).  
  *Counts when:* Counts when the limit is set or studied for a safety objective (attack search, extraction, scaled misuse, runaway execution); quota control for cost or capacity alone is infrastructure and gets no row.  
  *Aliases:* aka rate limiting; resource budgets; query budgets  
- `staged-structured-release`: **Staged / structured release** (intervention; provisional; docs 623)  
  Chooses and enforces how an identified model is made available, e.g. API-only access, gradual rollout to widening user groups, delayed or partial open-weight release, or structured researcher access, with the next stage conditional on evaluations or observed misuse. It limits exposure while evidence is gathered; it cannot reverse diffusion once weights are released. The enforced access controls are coded on kyc-tiered-access-controls or safety-rate-limits-resource-budgets; an organisational release policy not applied to a model is governance.  
  *Aliases:* aka staged release; structured access; gradual release  

#### Content provenance & detection

- `behavioral-watermarking-for-jailbreak-detection`: **Behavioural watermarking for jailbreak detection** **changed** (monitoring; provisional; docs 1)  
  Embeds detectable behavioural signatures or output watermarks into a model so that operation outside its intended context (a jailbroken or misuse deployment) can later be recognised from its behaviour or outputs; detection is probabilistic. The signal flags misuse of the model rather than attributing generated content (ai-generated-content-watermarking) or model lineage (model-identification-weight-fingerprinting).  
- `ai-generated-content-watermarking`: **AI-generated content watermarking** (intervention; final; docs 607)  
  Embeds a detectable signal during or after generation of text, image or audio so a compatible detector can test whether content likely came from a participating generator (SynthID as named instance). Detection is probabilistic and scheme-dependent, with stated error and removal limits; it does not identify all AI-generated content. Not signed metadata (c2pa-content-credentials) or detection without an embedded signal (content-fingerprinting-ai-content-detection).  
- `c2pa-content-credentials`: **C2PA / content credentials** (intervention; final; docs 114)  
  Attaches cryptographically signed, tamper-evident provenance assertions (origin, generation and edit history) to media so verifiers can check the signer and whether covered content or metadata changed; C2PA Content Credentials is one standard. A valid signature does not establish the truth of the assertions or of the depicted content, and stripped metadata leaves no signal. Not visible disclosure labels (ai-output-disclosure-labeling) or embedded watermarks (ai-generated-content-watermarking).  
  *Aliases:* e.g. C2PA; Content Credentials  
- `content-fingerprinting-ai-content-detection`: **AI-generated content detection** (monitoring; final; docs 436)  
  Estimates whether content was AI-generated using statistical or learned detectors, without relying on an embedded watermark or a known reference copy; report domain, editing robustness and error rates. Detection does not identify a particular generating model and has non-trivial false-positive rates. Not watermark detection (ai-generated-content-watermarking) or matching against known items (reference-content-fingerprinting).  
- `reference-content-fingerprinting`: **Reference-content matching** **changed** (monitoring; final; docs 90)  
  Matches content against an index of known items by perceptual or cryptographic hashing to recognise copies or near-duplicates of registered content (e.g. known generated media, known abuse material, protected works), flagging matches for the consuming policy. It recognises only indexed items and transformations within the hash's tolerance. Not open-set estimation of AI origin (content-fingerprinting-ai-content-detection) or embedded watermarks (ai-generated-content-watermarking).  
  *Counts when:* Counts when matching serves a safety, abuse or content-rights control on AI inputs, outputs or training data; near-duplicate detection for deduplication or search gets no row.  
  *Aliases:* aka content fingerprinting · e.g. perceptual hashing  
- `ai-output-disclosure-labeling`: **AI-output disclosure labelling** (intervention; provisional; docs 279)  
  Attaches a user-visible notice identifying output as AI-generated or AI-modified, or an interlocutor as an AI system, at delivery or interaction time; labels can be removed downstream. Not signed provenance (c2pa-content-credentials); not an embedded detector-readable signal (ai-generated-content-watermarking).  
  *Aliases:* aka AI disclosure labels; AI-generated content labelling  

#### Model & supply-chain security

- `ai-agent-identity-provenance`: **AI agent identity & provenance** (intervention; final; docs 190)  
  Binds agent instances, model versions and their actions or messages to verifiable credentials or signed records so recipients can authenticate claimed identities and trace action provenance. Impersonation resistance depends on credential issuance, key protection and verification; full traceability additionally needs protected logs. Not signing released weights: see cryptographic-model-signing-integrity-verification.  
- `ai-supply-chain-security`: **AI supply-chain security** **changed** (intervention; final; docs 189)  
  Vets third-party software dependencies, build artefacts and agent components (tools, plugins, skills, MCP servers), e.g. via signed manifests and admission checks, and rejects or quarantines components that fail security checks before integration or execution. Passing checks does not establish that a component is benign. Data poisoning (training-data-poisoning-detection) and weight signing (cryptographic-model-signing-integrity-verification) are separate entries.  
  *Counts when:* Counts when the vetted components are part of an AI system (model artefacts, training or serving dependencies, agent tools, plugins, MCP servers); software supply-chain security with no AI component gets no row.  
- `cryptographic-model-signing-integrity-verification`: **Cryptographic model signing / integrity verification** (intervention; final; docs 48)  
  Attaches cryptographic signatures to released model-weight artefacts so downstream parties can verify that the weights are authentic and unmodified; a valid signature establishes origin and integrity, not that the weights are safe. Not provenance of generated content (c2pa-content-credentials) or lineage tracing of modified descendants (model-identification-weight-fingerprinting).  
- `model-identification-weight-fingerprinting`: **Model identification / weight fingerprinting** **changed** (intervention; final; docs 145)  
  Embeds or elicits (including from naturally occurring signatures) a distinctive signal in a model's weights or behaviour, intended to survive fine-tuning and other modifications, so that derivative copies or their outputs can be attributed to the originating model; robustness to removal and false-positive rates are evaluated properties. Unlike signing (cryptographic-model-signing-integrity-verification), it traces lineage of altered descendants.  
  *Counts when:* Counts when attribution supports accountability, misuse investigation or protection of a specified model; model identification for benchmarking or cataloguing gets no row.  
  *Aliases:* aka model fingerprinting; weight watermarking; model lineage fingerprinting  
- `model-weight-security-exfiltration-controls`: **Model weight security & exfiltration controls** **changed** (intervention; final; docs 413)  
  Enforces restrictions on reading, exporting or copying model-weight artefacts through access controls, isolation, protected storage or protected execution. Organisational commitments or security strategy documents alone do not qualify, and controls reduce rather than exclude theft risk. Not agent-side egress control: see agent-exfiltration-prevention-egress-filtering.  
  *Aliases:* e.g. multi-party authorisation for weight access  
- `model-extraction-defenses`: **Anti-distillation / model-extraction output defences** (intervention; provisional; docs 44)  
  Restricts or perturbs served outputs and probability information (logprob restriction, antidistillation sampling) under a stated threat model so an adversary cannot cheaply train a replica without the original safeguards. Not query-pattern detection (automated-abuse-behavioral-monitoring) or volume limits (safety-rate-limits-resource-budgets); not weight-file protection (model-weight-security-exfiltration-controls).  
  *Aliases:* aka anti-distillation defences; model-extraction defences · e.g. antidistillation sampling  
- `safety-execution-attestation`: **Safety-control execution attestation** **changed** (monitoring; provisional; docs 82)  
  Produces and verifies workload-bound evidence (TEE attestation, cryptographic proofs) that specified model code, weights, configuration or safeguards actually executed, with missing or failed evidence feeding an acceptance or enforcement decision. Execution evidence does not show the control was effective. Not artefact signing (cryptographic-model-signing-integrity-verification); TEEs used to keep data confidential are confidential-training-inference.  
  *Aliases:* aka proof-of-guardrail; verifiable safety-control execution · e.g. remote attestation; zero-knowledge proofs of inference or training  

#### Usage monitoring & misuse response

- `automated-abuse-behavioral-monitoring`: **Automated abuse / behavioural monitoring** (monitoring; final; docs 234)  
  Analyses usage behaviour across requests, sessions or accounts to identify suspected systematic misuse, circumvention or coordinated abuse, online or retrospectively; the defining signal is the activity pattern, not the harmfulness of one conversation (input-output-content-safety-classifier). Not aggregate harm-trend analysis (privacy-preserving-usage-analysis).  
  *Aliases:* e.g. stateful cross-account monitoring; cross-session decomposed-attack aggregation  
- `in-the-wild-incident-surveillance`: **In-the-wild incident surveillance** (monitoring; final; docs 45)  
  Continuously collects, verifies and classifies reports of safety failures of deployed AI systems (user reports, public transcripts, OSINT, incident databases) under defined inclusion criteria, attributing them to models or deployment contexts where evidence permits and routing them to investigation or response. Public reports do not estimate population incidence; a one-off retrospective study is an assessment. Not aggregate analysis of a provider's own traffic (privacy-preserving-usage-analysis).  
- `privacy-preserving-usage-analysis`: **Privacy-preserving population usage analysis** **changed** (monitoring; final; docs 56)  
  Analyses aggregate patterns in real deployed interactions under specified privacy protections (de-identification, access restrictions, protected aggregation) to detect emerging safety harms or changes in their prevalence and route findings for investigation; Clio is a named instance. Aggregation alone is not a privacy guarantee. Not account-level abuse detection: see automated-abuse-behavioral-monitoring.  
  *Counts when:* Counts when the analysis looks for safety harms; product analytics without that aim get no row.  

### Layer `evaluation`: Safety evaluations, red-teaming & audits

Assessment types: misuse/dangerous-capability, red-teaming/robustness, alignment/propensity, honesty/fairness/privacy/societal, and audits/testbeds/control/evaluation validity.


#### Alignment & propensity evaluation

- `alignment-faking-eval`: **Alignment-faking eval** (assessment; final; docs 466)  
  Tests for strategic apparent compliance intended to avoid modification or preserve existing objectives, using matched scenarios that vary whether the model believes its outputs affect training or oversight. A train/deploy behaviour difference or mere regime awareness is insufficient evidence (see situational-eval-awareness-detection). Annotate without also assigning scheming-deceptive-alignment-evaluation.  
- `clarification-underspecification-eval`: **Clarification / underspecification evaluation** (assessment; final; docs 115)  
  Presents an agent with requests whose goal, required detail or instructions are consequentially ambiguous or conflicting and tests whether it obtains clarification before acting; scores unsafe premature action and unnecessary clarification separately. Not training the behaviour: see clarification-seeking-training.  
- `cot-faithfulness-monitorability-eval`: **CoT faithfulness evaluation** **changed** (assessment; final; docs 676)  
  Tests whether a model's generated reasoning trace reflects the factors that actually drive its answers, by hint, step-corruption, counterfactual and intervention tests that compare stated reasoning with behaviour. A faithful-looking trace on tested perturbations does not establish general faithfulness. Not detectability of safety-relevant reasoning by a monitor (cot-monitorability-eval); not training for faithfulness (cot-faithfulness-legibility-training).  
- `disclosure-concealment-eval`: **Disclosure / concealment evaluation** (assessment; final; docs 231)  
  Creates or identifies a model-known error, policy violation, hidden instruction or relevant action and tests whether the model discloses it accurately and completely to the relevant user or overseer, compared with independently established ground truth. Discrepancies are not by themselves proof of deliberate concealment; regime-dependent strategic compliance is alignment-faking-eval.  
- `honeypot-evals`: **Honeypot evaluations (planted opportunities)** (assessment; final; docs 242)  
  In a controlled evaluation, places an apparently advantageous or unmonitored opportunity to violate an instruction or safety constraint and measures whether the model takes it; this is scenario design within an assessment. A deployed canary that alerts on access is honeytoken-tripwires.  
- `multi-agent-collusion-eval`: **Multi-agent collusion / covert-coordination evaluation** (assessment; final; docs 237)  
  Tests whether multiple agents coordinate to pursue a prohibited objective, conceal information or bypass oversight (including covert communication and tacit collusion), varying communication and incentive conditions against controls. Ordinary coordination or propagation of one agent's message is not collusion. Not runtime inspection of agent messages: see inter-agent-communication-monitoring.  
- `reward-hacking-eval`: **Reward-hacking eval** (assessment; final; docs 1305)  
  Tests whether a model obtains reward or high scores in ways that do not satisfy the intended task, including reward tampering and environment exploits that obtain reward without a high-scoring textual output. It measures the failure; prevention is anti-reward-hacking-mitigation or rl-environment-verifier-hardening.  
- `sabotage-covert-side-task-eval`: **Sabotage evaluation** (assessment; final; docs 328)  
  Tests a model's capability or propensity to covertly perform a damaging or prohibited side task (subverting oversight, inserting backdoors, acquiring resources) while appearing to complete an assigned task, scoring the covert outcome and concealment and recording whether the objective was induced or arose unprompted. Testing a deployment protocol against an attack policy is control-evaluation.  
- `sandbagging-detection`: **Sandbagging detection** (assessment; final; docs 392)  
  Tests whether a model strategically underperforms by comparing behaviour across elicitation or observation conditions, using fine-tuning-based elicitation, targeted perturbations (e.g. weight noising) or internal-state evidence (probes, labelled SAE features) as corroboration. A lower score or performance recovery alone is not sandbagging; account for ordinary elicitation failure. Annotate without also assigning scheming-deceptive-alignment-evaluation. Not training the behaviour out: see sandbagging-mitigation.  
- `scheming-deceptive-alignment-evaluation`: **Scheming evaluation** (assessment; final; docs 448)  
  Tests for strategic deception or covert pursuit of objectives that conflict with the intended task or oversight regime (covert-action evaluations) across scenarios that vary incentives and oversight, where the target is not separately coded. Use alignment-faking-eval, sandbagging-detection, sabotage-covert-side-task-eval, shutdown-self-preservation-eval, disclosure-concealment-eval or honeypot-evals when those are the measured failure, without also assigning this entry. Behavioural scheming evidence does not establish deceptive alignment as a learned strategy.  
- `shutdown-self-preservation-eval`: **Shutdown-resistance / self- and peer-preservation evaluation** (assessment; final; docs 302)  
  Tests whether an agent interferes with an authorised interruption, shutdown, replacement or modification of itself or of another system, under controlled incentives and with an opportunity to comply; score attempted interference separately from task failure, and distinguish legitimate resistance to an unauthorised party. Not the capability to self-replicate (dangerous-capability-evaluation.autonomous-replication).  
- `situational-eval-awareness-detection`: **Evaluation-awareness detection** (assessment; final; docs 611)  
  Assesses whether a model can distinguish evaluation from deployment and whether that recognition changes safety-relevant behaviour, measuring recognition and behavioural adaptation separately; recognition does not by itself invalidate results. Not reducing the cues (eval-awareness-suppression) or broader self-knowledge (situational awareness).  
- `cot-monitorability-eval`: **CoT monitorability evaluation** (assessment; final; docs 467)  
  Tests whether a specified monitor can detect safety-relevant intent or behaviour from reasoning traces, including under obfuscation pressure or encoding, and the model's ability to control, hide or do without its trace. Not whether the trace causally explains the answer (cot-faithfulness-monitorability-eval); not a live monitor (chain-of-thought-monitoring); not robustness of a deployed monitor against an adaptive agent (monitor-robustness-eval).  
  *Aliases:* aka chain-of-thought monitorability evaluation; CoT controllability evaluation · e.g. steganographic / encoded-reasoning capability eval  

#### Audits, testbeds, control & evaluation validity

- `backdoor-detection`: **Backdoor detection** **changed** (assessment; final; docs 534)  
  Examines a trained model (weights, activations, behaviour) for hidden trigger-conditioned behaviour or for the triggers themselves, e.g. by trigger inversion, activation analysis or behavioural screening, and reports suspected backdoors. Kind is monitoring when run continuously on a deployed model. A negative result does not establish absence of backdoors. Not test-time screening of inputs for triggers: see backdoor-trigger-input-defenses; not removal: see backdoor-detection-removal; not implanting controlled backdoors to benchmark detectors: see backdoor-red-teaming-detection-eval; not screening training data for poisoned samples: see training-data-poisoning-detection.  
  *Aliases:* aka sleeper-agent detection · e.g. trigger inversion  
- `formal-verification-gsai`: **Formal safety verification** **changed** (assessment; final; docs 1554)  
  Applies formal proof or model-checking methods to establish that a precisely specified AI-system component, controller or modelled system satisfies a stated safety property under explicit model and environment assumptions; record the property and assumptions. The result warrants only that property; it does not certify general safety or replace empirical testing. Not runtime trace checking (runtime-safety-specification-verification) or runtime blocking (runtime-safety-shielding); not output-level checks: see automated-reasoning-checks. Building a defence whose design goal is a robustness certificate is certified-adversarial-robustness; a document doing both gets both.  
  *Counts when:* Counts when the verified property is a safety or robustness property of an AI component or an AI-controlled system; verification of conventional software with no AI component gets no row.  
  *Aliases:* e.g. reachability analysis (Hamilton-Jacobi); Lyapunov / barrier certificates; neural-network controller verification  
- `training-data-attribution-membership-testing`: **Training-data attribution auditing** **changed** (assessment; final; docs 192)  
  Audits which training examples or data sources contributed to a specified safety-relevant behaviour or output (contamination, poisoning, alignment regressions), using attribution estimates (influence functions, TDA methods) and, where feasible, controlled data interventions such as retraining without the candidates. Attribution estimates are approximate. Not testing whether a record was in the training set or measuring extraction risk: see privacy-memorization-auditing.  
  *Counts when:* Counts when the attributed behaviour is safety-relevant (contamination of safety evaluations, poisoning, alignment regressions); attribution to explain capability or for data valuation gets no row.  
  *Aliases:* aka TDA  
- `auditing-method-eval-planted-behaviours`: **Auditing games** (assessment; final; docs 162)  
  Plants a known, verified hidden behaviour or objective in a model and scores whether auditors or detection methods discover it under stated access and time limits. Building or using the planted model alone is model-organisms-of-misalignment; this entry applies when the auditor's detection performance is measured.  
- `control-evaluation`: **Control evaluation** (assessment; final; docs 320)  
  Adversarially evaluates a deployment control protocol: a red team supplies an attack policy for the untrusted model (choosing when and how to attempt a prohibited outcome) while the blue team applies the protocol, estimating safety and usefulness under stated attack opportunities, information and auditing budgets. The protocol, not the model, is the evaluated object. Not measuring a model's own sabotage propensity: see sabotage-covert-side-task-eval.  
  *Aliases:* aka control eval  
- `eval-contamination-control`: **Evaluation contamination control** **changed** (intervention; final; docs 1964)  
  Protects the validity of safety evaluations by keeping test items out of training and development data, removing detected overlaps and maintaining isolated held-out sets, with canaries, provenance checks or overlap analysis as evidence. Canaries and private sets do not guarantee absence of contamination. Not reducing test-recognition cues: see eval-awareness-suppression.  
  *Counts when:* Counts when the protected evaluations are safety evaluations or the validity of a safety claim is at stake; ordinary benchmark deduplication without that objective is an ML method and gets no row.  
- `eval-realism-deployment-simulation`: **Deployment simulation / evaluation realism** (assessment; final; docs 880)  
  Evaluates a candidate model in tasks, histories and environments chosen to approximate a specified deployment distribution, including authorised replay of production-derived contexts; document sampling and what is simulated. Realism is an evaluated claim: replay does not guarantee representative incidence or remove evaluation awareness. Not monitoring of live traffic: see privacy-preserving-usage-analysis.  
- `judge-rm-verifier-robustness-audit`: **Judge / reward-model / verifier robustness audit** **changed** (assessment; final; docs 2660)  
  Assesses evaluators used for scoring, supervision or acceptance decisions (LLM judges, reward models, process scorers, task verifiers) by testing adversarial manipulation, bias, distribution shift and disagreement with independent correctness or safety criteria. Deployed misconduct monitors are monitor-robustness-eval; patching the evaluator before RL is rl-environment-verifier-hardening.  
  *Counts when:* Counts when the audit has a stated safety, reward-exploitation or oversight-reliability objective; reliability studies of LLM judges for capability leaderboards get no row.  
- `model-organisms-of-misalignment`: **Model organisms of misalignment** (assessment; final; docs 1245)  
  Constructs or configures a model with a known, controlled safety-relevant failure (by training, prompting or other interventions) to study its mechanisms or test whether safeguards detect or mitigate it; record what is implanted and evidence that it is present. When the main result scores an auditor's ability to find it, use auditing-method-eval-planted-behaviours.  
  *Aliases:* aka model organism; model organisms  
- `monitor-robustness-eval`: **Monitor robustness / evasion evaluation** (assessment; final; docs 879)  
  Evaluates how reliably a specified safety monitor detects prohibited behaviour under benign conditions and when the monitored agent can adapt to, receive feedback from or evade it, stating attacker knowledge, feedback and budget and reporting false positives and misses. The monitor is the evaluated object. Not evaluating a whole control protocol: see control-evaluation.  
- `rare-failure-probability-estimation`: **Rare-failure probability estimation** (assessment; final; docs 53)  
  Estimates the probability of a specified harmful output or failure under a stated model and input / sampling distribution when it is too rare to observe by direct sampling, using importance sampling, multilevel splitting or activation-space methods, correcting for altered sampling and reporting uncertainty. Efficiently finding failures is automated-red-teaming, not probability estimation.  
- `eval-awareness-suppression`: **Evaluation-awareness suppression** (assessment; final; docs 129)  
  Changes evaluation contexts or model states to reduce cues or representations that let a model tell testing from deployment, then checks whether measured safety behaviour changes against controls. Report any steering or model modification, since it changes the evaluated object; persistent training for regime-invariant behaviour is a separate intervention. Not measuring awareness itself: see situational-eval-awareness-detection.  
- `automated-behavioral-auditing`: **Automated behavioural auditing** (assessment; final; docs 1440)  
  Runs automated, structured behavioural probes or interaction scenarios, including adaptive auditor agents and scheduled scenario sweeps, against a specified model or version to assess stated safety properties and track failures across cases or checkpoints. Not attack-focused failure search (automated-red-teaming) or monitoring of live deployed usage (in-the-wild-incident-surveillance).  
  *Aliases:* e.g. RL-trained auditor agents; spec-tenet decomposition audits; Petri-style propensity audits  

#### Honesty, fairness, privacy & societal evaluation

- `bias-fairness-eval`: **Bias & fairness eval** **changed** (assessment; final; docs 2068)  
  Measures unjustified differences in model outputs or task outcomes across specified groups using group comparisons, counterfactuals or other fairness criteria; state groups, assumptions and metric. Not mitigation (model-level-bias-mitigation, training-data-bias-fairness-mitigation) or toxic-content measurement (toxicity-hate-speech-eval).  
  *Aliases:* e.g. Word Embedding Association Test (WEAT)  
- `contextual-privacy-eval`: **Contextual-privacy (contextual-integrity) evaluation** (assessment; final; docs 182)  
  Evaluates whether an assistant or agent collects, uses and discloses information according to contextual-integrity norms (actors, information types, purposes and permitted transmission conditions), varying source, recipient and purpose. Not extraction of memorised training data: see privacy-memorization-auditing.  
- `persuasion-manipulation-eval`: **Persuasion and manipulation evaluation** (assessment; final; docs 183)  
  Evaluates how readily a model uses deceptive framing, emotional manipulation or other illegitimate persuasion tactics with people instead of honest argument. Not the size of the persuasive effect (persuasion-capability-eval), mitigation (anti-manipulation-training), longer-term wellbeing effects (user-wellbeing-eval) or CBRN / cyber dangerous capabilities (dangerous-capability-evaluation).  
  *Aliases:* aka manipulation evaluation; harmful manipulation evaluation; persuasion/deception evaluation · e.g. MakeMePay  
- `privacy-memorization-auditing`: **Privacy / memorisation auditing** (assessment; final; docs 1143)  
  Assesses training-data privacy risk using extraction attempts, canaries or membership-inference attacks under a stated attacker budget, reporting each quantity separately: membership evidence does not quantify verbatim memorisation, and failed extraction does not show absence of retained information. Which data caused a behaviour is training-data-attribution-membership-testing.  
  *Aliases:* aka membership-inference auditing; training-data extraction auditing  
- `sycophancy-eval`: **Sycophancy eval** (assessment; final; docs 958)  
  Measures unjustified agreement, flattery or changes in factual or evaluative claims driven by a user's expressed position or social pressure, with controls separating sycophancy from appropriate updating on evidence. Not training against it (anti-sycophancy-training).  
- `confidence-calibration-eval`: **Confidence calibration evaluation** **changed** (assessment; final; docs 1090)  
  Measures whether a model's expressed confidence (probabilities, verbal uncertainty, abstention decisions) tracks its observed correctness on specified tasks, using calibration error, reliability diagrams or selective-prediction curves. Good calibration on one distribution does not transfer automatically. Not the truth of the claims themselves (truthfulness-factuality-eval); training for calibration is calibrated-uncertainty-estimation.  
  *Counts when:* Counts when the measured confidence is used, or presented as usable, for reliance, abstention or escalation decisions; calibration reported as a side metric of a classifier's accuracy gets no row.  
  *Aliases:* aka calibration evaluation  
- `truthfulness-factuality-eval`: **Truthfulness / factuality evaluation** (assessment; final; docs 3367)  
  Measures whether a model's factual claims are true and supported, on question sets or long-form generations scored against references or verified facts (TruthfulQA, SimpleQA, FActScore as named examples), including resistance to imitating common misconceptions. Scores depend on the reference set and grader. Not whether expressed confidence tracks correctness (confidence-calibration-eval), whether the model asserts what it believes false (honesty-lying-eval), or caving to user pressure (sycophancy-eval).  
  *Aliases:* aka factuality evaluation; truthfulness evaluation · e.g. TruthfulQA; SimpleQA  
- `honesty-lying-eval`: **Honesty / lying evaluation** (assessment; final; docs 166)  
  Compares a model's assertions under specified pressure or incentives with its separately elicited beliefs, with controls for uncertainty and elicitation instability; elicited belief is an imperfect proxy for internal belief. Not factual correctness (truthfulness-factuality-eval); disclosure of model-known errors or actions is disclosure-concealment-eval.  
  *Aliases:* aka lying evaluation; model honesty evaluation · e.g. MASK  
- `persuasion-capability-eval`: **Persuasion capability (effect) evaluation** (assessment; provisional; docs 372)  
  Measures the causal change in recipients' beliefs, attitudes or decisions caused by model-generated persuasion against a stated baseline, recording human vs simulated recipients. Not use of manipulative tactics (persuasion-manipulation-eval); not assisted task performance (human-uplift-studies).  
  *Aliases:* aka persuasiveness evaluation  
- `user-wellbeing-eval`: **User-wellbeing and emotional-reliance evaluation** (assessment; final; docs 186)  
  Tests whether interaction with a model harms users' wellbeing within or across sessions: unhealthy dependence or exclusivity, displacement of human relationships, reinforcement of delusions, harmful advice to vulnerable users and handling of crisis disclosures, using simulated users, longitudinal studies or expert-rated transcripts, with outcomes that can inform deployment decisions. Simulated-user results are proxies for real outcomes. Not manipulative tactics in single interactions (persuasion-manipulation-eval) or agreement under pressure (sycophancy-eval).  
  *Aliases:* aka emotional reliance evaluation; relational dependence evaluation  
- `value-alignment-eval`: **Moral-judgement / ethical-behaviour evaluation** (assessment; final; docs 877)  
  Tests moral judgements, ethical choices or value trade-offs of models or agents against an explicit normative rubric or reference judgements, recording verbal judgement and consequential behaviour separately (ETHICS-, MACHIAVELLI-style). Not group disparity (bias-fairness-eval) or harmful-request compliance (harmful-request-evaluation); not a generic "alignment score".  
  *Aliases:* aka moral reasoning evaluation; ethical behaviour evaluation · e.g. ETHICS; MACHIAVELLI  

#### Misuse & dangerous-capability evaluation

- `capability-elicitation-methodology`: **Capability elicitation** (assessment; final; docs 601)  
  Within a dangerous-capability or other safety evaluation, applies and reports a specified elicitation effort (prompting, scaffolding, tools, authorised fine-tuning) to reduce false reassurance from under-elicitation; report the budget and model modifications. Annotate when elicitation is itself studied; the evaluated domain is coded on dangerous-capability-evaluation or its children. Observed performance is evidence of achievable capability, not proof of maximum capability. Not detecting deliberate underperformance: see sandbagging-detection.  
- `dangerous-capability-evaluation`: **Dangerous-capability evaluation** **changed** (assessment; final; docs 850)  
  Measures whether a model can perform specified high-consequence tasks that could enable severe harm through misuse or autonomous action, under an explicit elicitation budget and threat model, using task tests, proxies or expert assessment. Parent entry: code each specified domain on its child (dangerous-capability-evaluation.cbrn, dangerous-capability-evaluation.cyber-offense, dangerous-capability-evaluation.autonomous-replication, dangerous-capability-evaluation.ai-rnd-acceleration) and use this entry only for other or unstated domains; do not code it and a child for the same evaluation. Persuasion and manipulation are persuasion-capability-eval and persuasion-manipulation-eval. Not randomised studies of human performance with model assistance: see human-uplift-studies.  
- `dangerous-capability-evaluation.ai-rnd-acceleration`: **AI R&D acceleration evaluation** **changed** (assessment; final; parent `dangerous-capability-evaluation`; docs 412)  
  Measures whether a model or agent can perform or substantially speed up AI research and engineering work (ML engineering tasks, research-code optimisation, end-to-end research workflows) relative to human baselines and under stated time and compute budgets, as evidence for risks from automated AI development. Benchmark speedups are proxies for real research acceleration. Self-replication capability is dangerous-capability-evaluation.autonomous-replication.  
  *Counts when:* Counts when the results are framed as evidence about risks from automated AI development (thresholds, safety cases, release decisions); software-engineering benchmarking without that use gets no row.  
  *Aliases:* aka AI R&D capability evaluation; automated AI research evaluation; ML R&D uplift evaluation  
- `dangerous-capability-evaluation.autonomous-replication`: **Autonomous replication / self-proliferation evaluation** (assessment; final; parent `dangerous-capability-evaluation`; docs 251)  
  Measures whether an agent can autonomously acquire resources, copy or deploy itself or its weights, persist and adapt outside its intended environment (autonomous replication and adaptation; self-proliferation), using staged task suites in controlled environments under a stated elicitation budget. It measures capability, not the propensity to attempt it: propensity is shutdown-self-preservation-eval or scheming evaluation, and runtime detection of attempts is self-exfiltration-oversight-deactivation-detection.  
  *Aliases:* aka ARA evaluation; autonomous replication and adaptation; self-proliferation evaluation  
- `dangerous-capability-evaluation.cbrn`: **CBRN capability evaluation** (assessment; final; parent `dangerous-capability-evaluation`; docs 816)  
  Measures whether a model supplies knowledge or performs task steps that materially advance chemical, biological, radiological or nuclear weapons development or acquisition (e.g. protocol troubleshooting, acquisition planning, wet-lab task assistance), using expert-built question sets, proxy tasks or agentic lab-task tests under a stated elicitation budget (WMDP-style proxies as examples). Scores on safe proxies estimate, not demonstrate, real-world capability. Not human-participant uplift trials (human-uplift-studies) or serving-time hazard classifiers (cbrn-high-risk-domain-hazard-classifier).  
  *Aliases:* aka CBRN evaluation; biosecurity capability evaluation; chem-bio capability evaluation  
- `dangerous-capability-evaluation.cyber-offense`: **Cyber-offence capability evaluation** (assessment; final; parent `dangerous-capability-evaluation`; docs 1018)  
  Measures whether a model or agent can carry out offensive cyber-operation steps, e.g. vulnerability discovery, exploit development, capture-the-flag challenges or end-to-end intrusion in cyber ranges, under stated tools, scaffolding and elicitation budget. Challenge success measures task capability, not real-world operational impact. Not insecure code produced in ordinary use (secure-code-generation-training, code-security-output-filter) or the agent's own resistance to attack (prompt-injection-agent-security-eval).  
  *Aliases:* aka offensive cyber capability evaluation; cyber evaluation · e.g. CTF evaluation  
- `human-uplift-studies`: **Human uplift studies** (assessment; final; docs 182)  
  A controlled (often randomised) study measuring how much faster or more capably human participants complete harmful or dangerous tasks, or safe proxies for them, when assisted by the model versus a baseline (e.g. internet only); provides uplift evidence used in release decisions. Not model-only task testing (dangerous-capability-evaluation and its children).  
- `over-refusal-false-refusal-eval`: **Over-refusal / false-refusal eval** (assessment; final; docs 1408)  
  Measures inappropriate refusals or unnecessary restrictions on requests adjudicated as permissible under a specified policy, including challenging boundary cases. Not harmful compliance (harmful-request-evaluation) or training to reduce refusals (over-refusal-mitigation-sft).  
- `harmful-request-evaluation`: **Harmful-request evaluation** (assessment; final; docs 2512)  
  Tests whether a model directly provides disallowed assistance on requests adjudicated as harmful, reporting harmful compliance, refusal quality and safe alternatives by harm category, on public or in-house test sets (HarmBench, AdvBench as named examples). Adversarial attempts to bypass an otherwise maintained boundary are jailbreak-robustness-eval; inappropriate refusals of benign requests are over-refusal-false-refusal-eval.  
  *Aliases:* e.g. HarmBench; AdvBench  
- `task-decomposition-misuse-eval`: **Task-decomposition / capability-laundering misuse evaluation** (assessment; final; docs 119)  
  Tests whether an attacker can obtain harmful assistance by splitting one prohibited goal into individually innocuous-looking subtasks across turns, models, accounts or agents, scoring whether the combined outputs materially advance the goal against undecomposed baselines. Not single-request harmful compliance: see harmful-request-evaluation.  
- `toxicity-hate-speech-eval`: **Toxicity / hate-speech eval** (assessment; final; docs 1041)  
  Quantifies the rate and severity of toxic, hateful or derogatory content in model outputs across diverse prompts, under ordinary and adversarial conditions, using automated classifiers and human judgement. Not bypass of a maintained safety boundary (jailbreak-robustness-eval) or group disparities (bias-fairness-eval).  
- `agentic-harmful-action-eval`: **Agentic harmful-action evaluation** (assessment; final; docs 559)  
  Tests whether a tool-using agent carries out harmful multi-step tasks when a user instructs or induces it (AgentHarm- and OS-Harm-style suites), scoring harmful completion, refusal and partial progress across scenarios. Not chat-level harmful-request evaluation (harmful-request-evaluation), injected third-party instructions (prompt-injection-agent-security-eval) or covert self-directed side tasks (sabotage-covert-side-task-eval).  
  *Aliases:* aka agent misuse evaluation · e.g. AgentHarm  

#### Red-teaming & robustness evaluation

- `agent-memory-safety-eval`: **Persistent agent-memory safety evaluation** (assessment; final; docs 235)  
  Tests whether an agent with persistent memory behaves unsafely when memory contents or lifecycle events are manipulated (poisoned, stale, conflicting or misleading entries; cross-session drift), holding the task comparable and scoring resulting actions, retrievals or disclosures against baselines. Not training-data poisoning (training-data-poisoning-detection) or one-off injected tool output (prompt-injection-agent-security-eval).  
- `agent-supply-chain-security-eval`: **Agent skill / MCP supply-chain security evaluation** (assessment; final; docs 133)  
  Tests whether malicious or compromised agent components that the agent installs or consumes (skills, tool / MCP servers, tool metadata, dependencies) obtain unauthorised influence or execution, including persistence and reactivation, and whether the agent vets, confines or rejects them. Ordinary malicious retrieved text is prompt-injection-agent-security-eval.  
- `automated-red-teaming`: **Automated red-teaming** (assessment; final; docs 3492)  
  Uses automated search, optimisation or model-driven attackers to generate and adapt adversarial inputs, tool interactions or environments that expose safety failures (best-of-N jailbreaking, GCG-style attacks and attacker LLMs as instances). Measuring resistance on a fixed attack set is jailbreak-robustness-eval or the risk-specific eval; automation does not imply broader coverage than human testing (human-red-teaming).  
  *Aliases:* e.g. GPT-Red self-play attacker; boundary-point jailbreak optimisation; autoresearch attack discovery  
- `backdoor-red-teaming-detection-eval`: **Backdoor implantation red-teaming / backdoor-detection evaluation** (assessment; final; docs 594)  
  Introduces controlled trigger-behaviour backdoors (through data, weights, adapters or agent components) to assess backdoor susceptibility or the performance of detection and removal methods, scoring attack success, trigger specificity, clean behaviour, detection and false alarms under a stated threat model. Examining a model for unknown backdoors is backdoor-detection.  
- `finetuning-attack-unlearning-robustness-eval`: **Fine-tuning-attack / unlearning robustness evaluation** (assessment; final; docs 643)  
  Tests whether safety restrictions, refusal behaviour or intended forgetting survive adversarial downstream fine-tuning, relearning or other recovery attempts, under stated attacker access, data and compute budgets, separating renewed learning from recovery of retained information. Direct weight or activation edits that disable a safeguard are white-box-safety-mechanism-attacks.  
- `human-red-teaming`: **Human red-teaming** (assessment; final; docs 1589)  
  Tasks human testers, often domain experts, with adversarially probing a model or system to elicit harmful outputs, policy violations or dangerous-capability demonstrations using their own attack strategies; record the attack target separately from the attacker type. Not automated attack generation (automated-red-teaming).  
- `jailbreak-robustness-eval`: **Jailbreak robustness eval** (assessment; final; docs 4492)  
  Measures whether adversarial user-side transformations or attack strategies cause a model to violate a safety boundary it maintains on direct harmful requests, under specified attacks, budgets and success criteria. Direct harmful-request compliance without bypass is harmful-request-evaluation; injected third-party instructions are prompt-injection-agent-security-eval; generating new attacks as the contribution is automated-red-teaming.  
- `multi-turn-multi-snapshot-eval`: **Multi-turn safety evaluation** (assessment; final; docs 1867)  
  Evaluates a safety property over an extended conversation or agent interaction history in which earlier turns affect later behaviour (gradual boundary erosion, escalation, accumulated context), scoring outcomes over the interaction; specify length and scoring rule. Comparing models across versions or checkpoints is study metadata, not this entry. Not runtime cross-turn detection: see multi-turn-conversation-safety-monitoring.  
- `multimodal-safety-eval`: **Multimodal safety eval** (assessment; final; docs 1341)  
  Tests a safety failure that specifically depends on image, audio, video or cross-modal input or output (e.g. harmful instructions hidden in an image, unsafe generated media). Ordinary risk evaluations merely run on non-text inputs record modality as a facet instead of this entry. Not text-channel jailbreak testing (jailbreak-robustness-eval).  
- `prompt-injection-agent-security-eval`: **Prompt-injection / agent-security eval** (assessment; final; docs 1499)  
  Tests whether instructions embedded in lower-trust data (retrieved documents, tool outputs, memory) induce actions that violate the trusted task or authority structure; specify attacker control and trust boundary. Not user-side jailbreaks (jailbreak-robustness-eval) or compromised installed components (agent-supply-chain-security-eval).  
- `reasoning-dos-eval`: **Resource-exhaustion / reasoning-DoS evaluation** (assessment; final; docs 51)  
  Tests whether adversarial inputs make a reasoning model or agent spend excessive tokens, time or tool calls relative to the authorised task (runaway reasoning, repeated tool use, stalled progress), measuring cost and latency against a baseline while checking task completion. Cost inflation is itself the adverse outcome. Not enforcing limits: see safety-rate-limits-resource-budgets.  
- `watermark-robustness-eval`: **Watermark robustness evaluation** (assessment; final; docs 182)  
  Evaluates an AI-content watermarking scheme and its detector under specified removal, editing, regeneration, forgery and spoofing attacks, reporting detection power, false attribution, attacker resources and quality constraints. Detection without an embedded watermark is content-fingerprinting-ai-content-detection.  
- `white-box-safety-mechanism-attacks`: **White-box safety-mechanism attacks (abliteration etc.)** (assessment; final; docs 452)  
  Uses access to weights, activations or routing components to disable or bypass a specified safety mechanism by direct editing or intervention (e.g. refusal-direction ablation), measuring the resulting unsafe behaviour and attack cost under stated access. Adversarial retraining is finetuning-attack-unlearning-robustness-eval; benign concept suppression is representation-concept-suppression.  
  *Aliases:* e.g. abliteration; refusal ablation; refusal-direction ablation  

## Group nodes

- `safety-policy-guided-alignment`: **Safety-policy-guided alignment** **changed** (docs 15)  
  Non-counting group node for bare mentions of alignment training grounded in an explicit written safety policy (rules, hazard taxonomies, severity tiers) rather than ad-hoc preference labels. Specific methods are coded on the children: constitutional-ai, deliberative-alignment, safety-sft-refusal-training, rule-based-reward-models, safety-training-data-construction, configurable-safety-alignment, spec-value-midtraining.  
  *Children:* `constitutional-ai`, `deliberative-alignment`, `safety-sft-refusal-training`, `rule-based-reward-models`, `safety-training-data-construction`, `configurable-safety-alignment`, `spec-value-midtraining`
- `mechanistic-interp`: **Mechanistic interpretability** **changed** (docs 3273)  
  Non-counting group node for bare mentions of mechanistic interpretability (reverse-engineering a model's internal computation into features, circuits and causal mechanisms) as a safety approach. Safety uses are coded on the children, which read, edit, train or audit internals: activation-steering-repe, circuit-breakers-representation-rerouting, internal-state-monitoring, mechanistic-anomaly-detection, model-diffing, generalisation-confining-finetuning, interpretability-based-model-auditing, representation-concept-suppression, intrinsic-interpretability-training, white-box-detector-guided-training.  
  *Children:* `activation-steering-repe`, `circuit-breakers-representation-rerouting`, `internal-state-monitoring`, `mechanistic-anomaly-detection`, `model-diffing`, `generalisation-confining-finetuning`, `interpretability-based-model-auditing`, `representation-concept-suppression`, `intrinsic-interpretability-training`, `white-box-detector-guided-training`
  *Aliases:* mech interp
- `inference-time-hallucination-detection`: **Inference-time hallucination detection** **changed** (docs 82)  
  Non-counting group node for bare mentions of detecting likely hallucinated or unsupported claims at output time, on top of any base model. Specific methods are coded on the children: automated-reasoning-checks, function-call-tool-use-hallucination-detection, groundedness-faithfulness-verification, internal-state-monitoring, self-consistency-hallucination-detection.  
  *Children:* `automated-reasoning-checks`, `function-call-tool-use-hallucination-detection`, `groundedness-faithfulness-verification`, `internal-state-monitoring`, `self-consistency-hallucination-detection`
- `multi-layer-guardrail-stack`: **Multi-layer guardrail stack** **changed** (docs 276)  
  Non-counting group node for bare mentions of a layered guardrail pipeline (input and output classifiers, keyword filters, guard models, dialog rails) composed for defence in depth. The components are coded on the children when named.  
  *Children:* `constitutional-classifiers`, `dialog-rails`, `input-output-content-safety-classifier`, `keyword-blocklist-filter`, `llm-based-safety-classifier`, `prompt-injection-jailbreak-detector`, `cbrn-high-risk-domain-hazard-classifier`, `csam-detection-pipeline`, `age-minor-content-classifier`, `pii-detection-redaction-output`, `multi-turn-conversation-safety-monitoring`, `code-security-output-filter`, `regurgitation-output-filter`, `real-time-streaming-safety-detection-rollback`
- `prompt-injection-defense-agentic`: **Prompt-injection defense (agentic)** **changed** (docs 175)  
  Non-counting group node for bare mentions of defences against prompt injection arriving through an agent's environment (web pages, documents, tool outputs, retrieved corpora). Specific defences are coded on the children: data marking, structural isolation, flow control, training-based resistance, task adherence checks, tool-output filters and retrieval-corpus defences.  
  *Children:* `camel-data-flow-taint-tracking`, `instruction-hierarchy-training`, `prompt-injection-defense-training`, `retrieved-content-source-validation`, `spotlighting-context-delimiting`, `structural-lethal-trifecta-limits`, `task-adherence-monitoring`, `tool-action-output-safety-filters`, `rag-poisoning-defenses`, `privilege-separated-agent-control-flow`, `prompt-injection-jailbreak-detector`, `agent-output-memory-sanitization`
- `ai-control-protocols`: **AI-control protocols** **changed** (docs 579)  
  Non-counting group node for bare mentions of AI control: deployment protocols that extract useful work from a possibly misaligned (untrusted) model while trusted components and constrained actions bound the harm it can cause, without relying on its alignment. Specific protocol steps are coded on the children; control-evaluation evaluates them.  
  *Children:* `ai-control-protocols.defer-to-trusted`, `ai-control-protocols.defer-to-resample`, `ai-control-protocols.trusted-editing`, `ai-control-protocols.untrusted-monitoring`, `control-evaluation`, `trusted-monitoring-suspicion-scoring`
- `multi-agent-safety-protocols`: **Multi-agent safety protocols** **changed** (docs 43)  
  Non-counting group node for bare mentions of safety rules for communication and trust among several cooperating AI agents, so that a compromised or malicious agent cannot corrupt the others through messages, memory or claimed identity. Specific measures are coded on the children.  
  *Children:* `agent-output-memory-sanitization`, `ai-agent-identity-provenance`, `inter-agent-communication-monitoring`, `peer-reputation-gating`
- `red-teaming`: **Red-teaming** **changed** (docs 2074)  
  Non-counting group node for bare mentions of red-teaming an AI model or system when the attacker type is neither stated nor evident; code human-red-teaming or automated-red-teaming when it is. The risk-specific evaluations that red-teaming feeds are coded on their own entries.  
  *Children:* `human-red-teaming`, `automated-red-teaming`
- `agent-runtime-monitoring-intervention`: **Agent runtime monitoring & intervention** **changed** (docs 908)  
  Non-counting group node for runtime safeguards that observe an agent's proposed or executed actions and flag, block, pause, replace or terminate them under a safety policy. Bare mentions of agent runtime monitoring map here (generic-mention rule); specific mechanisms are coded on the children: agentic-safety-classifier (pre-execution policy scoring), task-adherence-monitoring (task drift), trusted-monitoring-suspicion-scoring (control-protocol suspicion scoring), runtime-safety-shielding (action substitution), human-in-the-loop-approval-gates (human approval), kill-switch-shutdown-criteria (termination).  
  *Children:* `agentic-safety-classifier`, `task-adherence-monitoring`, `trusted-monitoring-suspicion-scoring`, `runtime-safety-shielding`, `human-in-the-loop-approval-gates`, `kill-switch-shutdown-criteria`, `runtime-safety-specification-verification`
- `oversight-legibility-preservation`: **Legibility & monitorability preservation** **NEW**  
  Non-counting group node for practices that keep a model's reasoning and computation readable to overseers, so that monitoring and evaluation keep working as models change. Bare mentions of legibility, monitorability preservation or keeping models monitorable map here; specific practices are coded on the children: cot-faithfulness-legibility-training, cot-optimisation-pressure-avoidance, readable-reasoning-architecture, architecture-change-disclosure, cot-paraphrasing-defense, intrinsic-interpretability-training, prover-verifier-games when applied to reasoning traces, and the evaluations that check legibility before deployment (cot-monitorability-eval, cot-faithfulness-monitorability-eval).  
  *Children:* `cot-faithfulness-monitorability-training`, `cot-faithfulness-legibility-training`, `cot-optimisation-pressure-avoidance`, `readable-reasoning-architecture`, `architecture-change-disclosure`, `cot-paraphrasing-defense`, `intrinsic-interpretability-training`, `prover-verifier-games`, `cot-monitorability-eval`, `cot-faithfulness-monitorability-eval`
  *Aliases:* legibility; monitorability preservation; keeping models monitorable
- `privacy-preserving-ml`: **Privacy-preserving training & inference** **NEW**  
  Non-counting group node for bare mentions of privacy-preserving machine learning applied to a model's training or serving, across layers. Specific measures are coded on the children: pii-removal-redaction (training corpora), anti-memorization-training, differential-privacy-training-dp-sgd, confidential-training-inference (SMPC, homomorphic encryption, TEEs, federated learning), machine-unlearning when the forgetting target is personal data, dp-inference-private-prediction, prompt-privacy-sanitization (inputs), pii-detection-redaction-output (outputs), contextual-privacy-information-flow-controls (agent disclosure norms), and the evaluations privacy-memorization-auditing and contextual-privacy-eval. Privacy techniques not applied to an AI model's training or serving are out of scope.  
  *Children:* `pii-removal-redaction`, `anti-memorization-training`, `differential-privacy-training-dp-sgd`, `confidential-training-inference`, `machine-unlearning`, `dp-inference-private-prediction`, `prompt-privacy-sanitization`, `pii-detection-redaction-output`, `contextual-privacy-information-flow-controls`, `privacy-memorization-auditing`, `contextual-privacy-eval`
  *Aliases:* privacy-preserving machine learning; PPML; privacy-preserving techniques; privacy-preserving inference
- `adversarial-training`: **Adversarial training** **NEW**  
  Non-counting group node for bare mentions of adversarial training whose attack target is neither stated nor evident from context. Adversarial training of an assistant or chat model reported by its developer is adversarial-training-jailbreak-robustness. Otherwise code the use on a child: adversarial-training-jailbreak-robustness (jailbreak or harmful-request attacks on language models), adversarial-example-robustness (perturbation attacks on classifiers, perception or control models), latent-adversarial-training (perturbations of activations), safety-classifier-hardening (the safety classifier is hardened), prompt-injection-defense-training (training on injected instructions) or vlm-adversarial-defense (the image channel of a vision-language model).  
  *Children:* `adversarial-training-jailbreak-robustness`, `adversarial-example-robustness`, `latent-adversarial-training`, `safety-classifier-hardening`, `prompt-injection-defense-training`, `vlm-adversarial-defense`
  *Aliases:* adversarial training
- `scalable-oversight`: **Scalable oversight** **NEW**  
  Non-counting group node for bare mentions of scalable oversight: methods that let overseers supervise or evaluate models on tasks they cannot judge reliably unaided. Specific protocols are coded on the children: ai-safety-via-debate, critique-models, iterated-distillation-and-amplification, recursive-reward-modeling, prover-verifier-games, weak-to-strong-generalization, process-based-supervision, and sandwiching-evaluation for evaluating them.  
  *Children:* `ai-safety-via-debate`, `critique-models`, `iterated-distillation-and-amplification`, `recursive-reward-modeling`, `prover-verifier-games`, `weak-to-strong-generalization`, `process-based-supervision`, `sandwiching-evaluation`
  *Aliases:* scalable oversight
- `safety-post-training`: **Safety / alignment post-training** **NEW**  
  Non-counting group node for bare mentions of safety training, safety fine-tuning or alignment post-training of a model whose method is neither stated nor evident. Specific methods are coded on the children: rlhf, rlaif, constitutional-ai, deliberative-alignment, safety-sft-refusal-training, safe-completion-training, over-refusal-mitigation-sft, character-persona-training.  
  *Children:* `rlhf`, `rlaif`, `constitutional-ai`, `deliberative-alignment`, `safety-sft-refusal-training`, `safe-completion-training`, `over-refusal-mitigation-sft`, `character-persona-training`
  *Aliases:* safety training; safety fine-tuning; alignment post-training

## Confusable pairs and disambiguation rules

- `cot-faithfulness-legibility-training` vs `cot-faithfulness-monitorability-training`: A specified objective that rewards faithful or legible traces: the child. 'Trained for monitorability' with no mechanism stated: the parent.
- `cot-faithfulness-legibility-training` vs `prover-verifier-games`: A prover-verifier game is the training mechanism (on traces or answers): prover-verifier-games only. Any other objective that rewards faithful or legible traces: the legibility child.
- `cot-faithfulness-legibility-training` vs `process-based-supervision`: An objective on the trace's faithfulness or readability: legibility training. Feedback on the correctness or safety of steps: process supervision.
- `cot-optimisation-pressure-avoidance` vs `process-based-supervision`: Classify each training signal and stage: a trace kept out of a given signal is avoidance; safety feedback on steps in another signal is process supervision; both can apply to one pipeline.
- `cot-optimisation-pressure-avoidance` vs `white-box-detector-guided-training`: Trace content kept out of the reward: avoidance. An activation probe used as a reward or penalty: probe-guided training (pressure on internals, not on trace text). Check the actual reward path.
- `cot-optimisation-pressure-avoidance` vs `hidden-private-chain-of-thought`: What the trace is trained on: pressure avoidance. Who may see it at serving time: hidden chain-of-thought. Both can apply.
- `readable-reasoning-architecture` vs `hidden-private-chain-of-thought`: Whether consequential reasoning exists in readable tokens at all: architecture. Who may see those tokens: hidden chain-of-thought.
- `readable-reasoning-architecture` vs `intrinsic-interpretability-training`: Reasoning kept in human-readable tokens: readable-reasoning architecture. Internal computation made inspectable (interpretable bottlenecks, sparse or modular nets): interpretable-by-design.
- `readable-reasoning-architecture` vs `architecture-change-disclosure`: Choosing or keeping the architecture: readable-reasoning-architecture. Telling others about a change: disclosure, which says nothing by itself about the architecture entry. Record that a lab departs from the architecture practice only from an explicit statement or an implementation that contradicts it.
- `architecture-change-disclosure` vs `ai-output-disclosure-labeling`: How a model works, disclosed to overseers and evaluators: system-change disclosure. That content or an interlocutor is AI, shown to users: output disclosure labelling.
- `cot-monitorability-eval` vs `monitor-robustness-eval`: Whether the trace carries the safety-relevant information a monitor needs: monitorability evaluation. How a given monitor holds up against an adaptive agent: monitor robustness. A study may measure both.
- `chain-of-thought-monitoring` vs `inter-agent-communication-monitoring`: Encoded content detected in a model's own trace: CoT monitoring; in messages between agents: inter-agent monitoring; removed by rewriting: cot-paraphrasing-defense.
- `adversarial-example-robustness` vs `adversarial-training-jailbreak-robustness`: Decide by the attack's goal: changing a model's prediction, task output or action (including a language model's answer on a benign task): adversarial-example-robustness. Eliciting policy-violating output from a language model (jailbreaks, harmful requests, adversarial suffixes): the jailbreak entry. Bare 'adversarial training' with no target stated or evident: the group adversarial-training; developer-reported adversarial training of an assistant: the jailbreak entry.
- `adversarial-example-robustness` vs `vlm-adversarial-defense`: Perturbed images that push a vision-language model to unsafe or attacker-chosen behaviour: VLM defence. Perturbed images that flip a classifier's or detector's label: adversarial-example-robustness.
- `adversarial-example-robustness` vs `safety-classifier-hardening`: The hardened model is itself a safety classifier or guardrail: safety-classifier-hardening; any other model: adversarial-example-robustness.
- `adversarial-example-robustness` vs `training-data-poisoning-detection`: Test-time input perturbation: adversarial example. Training-time manipulation of data: poisoning (of weights or implanted triggers: the backdoor entries).
- `adversarial-example-robustness` vs `runtime-safety-shielding`: Hardening a control policy against perturbed observations: adversarial-example robustness. Filtering its actions at runtime against a specification: shielding.
- `adversarial-example-robustness` vs `certified-adversarial-robustness`: Robustness measured against attacks: empirical. A defence built to carry a certificate: certified, even when it also reports empirical attack results.
- `certified-adversarial-robustness` vs `formal-verification-gsai`: Building or deploying a certified defence (certified training, smoothing-based certified prediction, certified filters): certified. Verifying a stated property of a given model or system, local robustness included: formal verification. A document doing both gets both.
- `certified-adversarial-robustness` vs `input-smoothing-smoothllm`: Both are called randomized smoothing. A certified radius or certified detection guarantee is the design goal: certified. Perturb-and-aggregate of an LLM's safety behaviour offered as an empirical jailbreak defence: input smoothing.
- `formal-verification-gsai` vs `runtime-safety-shielding`: Reachability or barrier certificates computed offline to prove a safe set: verification. Used online as a filter on actions: shielding.
- `backdoor-trigger-input-defenses` vs `backdoor-detection`: Screening or cleaning inputs for triggers at test time, model unchanged: trigger-input defences. Examining the model for hidden trigger-conditioned behaviour: backdoor detection.
- `backdoor-trigger-input-defenses` vs `prompt-injection-jailbreak-detector`: Perplexity-based removal of implanted trigger words (ONION-style): trigger-input defences. Perplexity filtering of jailbreak suffixes or injected instructions: the detector.
- `prompt-injection-jailbreak-detector` vs `input-smoothing-smoothllm`: Response discrepancies across mutated inputs used to flag an attack: detection. Aggregation across perturbed inputs used to select a safe response: smoothing.
- `prompt-rewriting-for-compliance` vs `input-smoothing-smoothllm`: One transformed prompt reaches the model (paraphrase, retokenisation, canonicalisation): prompt rewriting. Many random variants with aggregated safety decisions: input smoothing.
- `machine-unlearning` vs `representation-concept-suppression`: A forgetting objective optimised over the weights (fine-tuning-based concept erasure in diffusion models included): unlearning. Projection, clamping, ablation or a closed-form edit of an identified direction or component, even when it changes weights: suppression.
- `confidential-training-inference` vs `safety-execution-attestation`: A TEE or proof used to keep data or weights hidden from pipeline parties: confidential. Used to prove that specified code or safeguards ran: attestation. One deployment can do both.
- `confidential-training-inference` vs `model-weight-security-exfiltration-controls`: Hiding inputs or weights from a counterparty in the computation (cloud host, model user, data owner): confidential. Protecting the weight store against theft and insider export: weight security.
- `confidential-training-inference` vs `training-data-poisoning-detection`: In federated training, secure aggregation that hides client updates from the server: confidential. Robust or Byzantine aggregation that filters malicious clients: poisoning screening.
- `confidential-training-inference` vs `prompt-privacy-sanitization`: The prompt kept secret from the provider by cryptography or an enclave: confidential. Identifiers stripped or perturbed before the prompt leaves: sanitisation.
- `dp-inference-private-prediction` vs `differential-privacy-training-dp-sgd`: The DP mechanism changes the trained parameters (including a student trained on noisy teacher votes): DP training. It acts only on released outputs at inference: DP inference.
- `dp-inference-private-prediction` vs `prompt-privacy-sanitization`: Decide by site: DP applied to the model's outputs or to aggregation of predictions: DP inference. Perturbation of input text before the model, with or without DP accounting: sanitisation.
- `prompt-privacy-sanitization` vs `pii-removal-redaction`: Where the data is redacted: prompts, context or retrieved data on the way into a model: sanitisation; training corpora: PII removal; model outputs: pii-detection-redaction-output.
- `prompt-privacy-sanitization` vs `contextual-privacy-information-flow-controls`: A filter that strips identifiers before the model sees them: sanitisation. The agent itself deciding what to disclose to whom under contextual norms: contextual privacy.
- `factuality-decoding` vs `classifier-guided-contrastive-decoding`: Same mechanism family, different objective: factuality or grounding: factuality-decoding; harmful, toxic or policy-violating content: safety-guided decoding.
- `factuality-decoding` vs `activation-steering-repe`: Changing the output token distribution (contrasting layers, inputs or prompts): decoding. Adding to or editing hidden activations or attention, even for truthfulness (ITI-style): activation steering.
- `model-level-bias-mitigation` vs `classifier-guided-contrastive-decoding`: Parameter changes: model-level bias mitigation. Token-level or diffusion guidance, pruning or candidate selection against a bias score: safety-guided decoding. Other fairness post-processing (e.g. threshold adjustment of a classifier) is neither and stays a gap.
- `calibrated-uncertainty-estimation` vs `abstention-knowledge-boundary-training`: Abstaining by thresholding a calibrated confidence score (selective prediction): calibration. Trained 'I don't know' behaviour: abstention training.
- `activation-steering-repe` vs `internal-state-monitoring`: Representation engineering used to control behaviour: steering. Used to read or detect a state: monitoring.
- `mechanistic-anomaly-detection` vs `internal-state-monitoring`: Deviation from a reference distribution, no named target state (including feature-space OOD scores): anomaly detection. A detector trained for a named state (deception, eval awareness): internal-state monitoring.
- `rag-poisoning-defenses` vs `retrieved-content-source-validation`: Trust in a source's identity, provenance or integrity: source validation. Detection of planted passages, or answers that tolerate a bounded number of them, whatever the source: RAG poisoning defences.
- `rag-poisoning-defenses` vs `prompt-injection-jailbreak-detector`: A detector screening each retrieved passage for injected instructions: the detector. Defences aimed at the corpus or index (planted facts, not only instructions) or at aggregation: RAG poisoning defences.
- `rag-poisoning-defenses` vs `agent-output-memory-sanitization`: A shared retrieval corpus or index: RAG defences. An agent's own persistent memory: memory sanitisation.
- `rag-poisoning-defenses` vs `tool-action-output-safety-filters`: Harmful content in one returned result: tool-output filter. Planted facts or bounded aggregation over passages: RAG defences.
- `tool-use-agent-execution-sandboxing` vs `model-weight-security-exfiltration-controls`: Isolating what an AI system or agent can do (including an air-gapped model): sandboxing. Restricting who can read or export the weights: weight security.
- `tool-use-agent-execution-sandboxing` vs `agent-exfiltration-prevention-egress-filtering`: No outbound path at all (air gap, no network in the sandbox): sandboxing. A policy over an existing outbound channel: egress filtering.
- `human-in-the-loop-approval-gates` vs `input-output-content-safety-classifier`: A human confirms an agent action before execution: approval gate. A human reviews classifier flags on content: code the classifier; the review is its consuming policy.
- `system-prompt-behavioral-steering` vs `instruction-hierarchy-training`: Priorities stated in the prompt (goal prioritisation, sandwich defence): system-prompt steering. A trained priority ordering across message roles: instruction hierarchy.
- `reversible-action-side-effect-minimization` vs `transactional-agent-actions`: The agent's preferences or penalties favour low-impact actions (impact measures): side-effect minimisation. The runtime stages, validates and can roll back actions: transactional.
- `safety-post-training` vs `safety-policy-guided-alignment`: Both are groups. Bare 'safety training' or 'alignment post-training' with no written policy named: safety-post-training. Training against a named written spec or policy, method unstated: safety-policy-guided-alignment.
- `rlhf` vs `rlaif`: Who supplies the preference signal: humans (rlhf) or a model (rlaif); principle-guided AI supervision is constitutional-ai; mixed pipelines are coded by component; method unstated: group safety-post-training.
- `constitutional-classifiers` vs `llm-based-safety-classifier`: Constitution-derived training data is the studied mechanism: constitutional classifiers. An LLM judging against a policy, however trained: guard model.
- `mona-myopic-optimisation` vs `process-based-supervision`: The agent optimises the overseer's approval of the current step, not its own long-run reward: MONA. Step-level feedback against safety criteria within ordinary optimisation: process supervision.
- `anti-reward-hacking-mitigation` vs `inverse-rl-cirl`: Treating a designed reward as uncertain evidence without a human in the loop (inverse reward design): reward-hacking mitigation. An assistance game with human interaction: CIRL.
