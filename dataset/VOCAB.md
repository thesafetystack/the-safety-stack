> Copied from release 2026-10-26 of the dataset, where it is generated; paths refer to that release's files. For loading, the [dataset card](https://huggingface.co/datasets/thesafetystack/the-safety-stack) is canonical.

# The Safety Stack: vocabulary

Every value word of the release with a sentence (vocab.yaml rendered). Values defined but not used in this release are listed as reserved.

**`published_precision`**: How precise published_date is.

- `day`: The date is known to the day.
- `year_inferred`: Only the year is reliable: the merged date is exactly midnight UTC on 1 January, which is the placeholder providers emit for a year-only date (a genuine 1 January midnight date cannot be told apart and is marked the same).
- `unknown`: No source gave a publication date.

**`doc_type`**: Document type as the bibliographic providers give it, merged across sources; compare the screen model's annotations.doc_class.payload.doc_type and the rubrics' doc_kind (see the glossary entry `document-type vocabularies`).

- `preprint`: A research paper not (yet) peer reviewed, such as an arXiv or SSRN preprint.
- `paper`: A published research paper of unspecified venue type.
- `conference`: A paper in conference proceedings.
- `journal`: A journal article.
- `forum_post`: A post on a discussion forum such as LessWrong or the Alignment Forum.
- `lab_blog`: A blog post or web article from an AI lab or another organisation.
- `system_card`: A system card documenting a released model or system.
- `model_card`: A standalone model card or model release note.
- `framework_policy`: A safety framework, policy or governance document.
- `book`: A book or book chapter.
- `other`: None of the above, or the providers did not say.

**`field_sources[].field`**: Which merged bibliographic field this provenance entry is about.

- `title`: The title.
- `abstract`: The abstract.
- `authors`: The author list.
- `published_at`: The publication date (published_date and published_precision).
- `doc_type`: The providers' document type (doc_type).

**`field_sources[].origin`**: Where the merged value of the field came from.

- `provider`: Taken from a source's bibliographic record.
- `human`: Set by a metadata override (a row of the overrides files).
- reserved (not in this release): `import`

**`identity.members[].channel_class`**: Our distribution-policy class for the CHANNEL that supplied this member record; it decides what this release distributes and is never a statement about the work's own licence (a Semantic Scholar record of an arXiv preprint shows `restricted` while the same work's arXiv member shows `open`).

- `open`: Channels whose metadata we treat as redistributable (for example arXiv, OpenAlex, the forums).
- `public_web`: Public web pages.
- `restricted`: Scholarly aggregator or paper-search channels whose per-item open-access status we did not verify.
- reserved (not in this release): `api_tos`, `api_abstract`, `shadow`

**`identity.members[].key_kind`**: Kind of the member record's primary key.

- `doi`: A DOI.
- `fm_post`: A ForumMagnum post id (LessWrong or the Alignment Forum).
- `url`: A URL.
- `openalex`: An OpenAlex work id.
- `s2`: A Semantic Scholar paper id.
- `pmid`: A PubMed id.

**`identity.keys[].kind`**: Kind of an identifier the document's members carry; members sharing an identifier were joined into one document.

- `arxiv`: An arXiv id.
- `doi`: A DOI.
- `openalex`: An OpenAlex work id.
- `s2`: A Semantic Scholar paper id.
- `fm_post`: A ForumMagnum post id (LessWrong or the Alignment Forum).
- `url`: A URL.
- `pmid`: A PubMed id.
- `zenodo`: A Zenodo record id.

**`content.role`**: Kind of content the annotated text was converted from.

- `full_text`: The document's PDF.
- `html`: arXiv's LaTeXML HTML rendering of the paper.
- `xml`: Publisher JATS XML.
- `post`: A forum post body as the forum's collector delivered it.
- `page`: A web page.
- reserved (not in this release): `readme`, `abstract`

**`content.quality`**: Rule-based conversion-quality bucket of the converted text; the model's own view of the text is the text_usability annotation.

- `ok`: The conversion passed the quality rules.
- `flagged`: The conversion passed but tripped a warning rule.
- reserved (not in this release): `failed`

**`release.abstract`**: What this release did with the abstract, so a withheld abstract can be told from a missing one.

- `withheld_pending_rights_review`: An abstract exists but this release withholds every abstract from the public variant until the redistribution terms are reviewed per supplier; this is a release policy, not a finding about the item.
- `none`: No source supplied an abstract.
- reserved (not in this release): `shipped`

**`release.text`**: Whether the document text is distributed in this variant.

- `not_distributed`: No document text ships; content.text.sha256 identifies the text the annotations were made on.
- reserved (not in this release): `inline`

**`annotations.*.metadata.kind`**: Which annotation this is (the same word names its column under annotations); records produced by one model call share config_id and decided_at.

- `screen`: The relevance screen's overall answer (verdict, buckets, rationale); the screen call also produces doc_class, stack_relevance, shallow_review_relevance and text_usability.
- `doc_class`: The document's genre, whether it is self-published, and its main language, from the screen call.
- `stack_relevance`: The screen call's answer to question S: does the document belong in the Safety Stack.
- `shallow_review_relevance`: The screen call's answer to question R: does the document belong in the Shallow Review of Technical AI Safety, with its category and agenda.
- `text_usability`: The screen model's judgement of whether the converted text is a readable rendering of the document's body.
- `affiliation`: Author affiliations per author, read from the byline, the publisher XML or the provider's record.
- `safety_techniques`: Which catalogue safety techniques the document engages, in which roles and how prominently (rubric-v0.9-c).
- `model_roles`: Which catalogue AI models the document engages, in which roles and how prominently (rubric-v0.6.0); produced by the same call as model_name_matches.
- `model_name_matches`: The raw hits of the deterministic model-name matcher that built the candidate list for the model_roles call.

**`annotations.*.metadata.status`**: Outcome of the annotation for this document; a kind that never ran for a document has its whole annotations.<kind> struct NULL, with no status word.

- `ok`: Decided, with at least one positive label.
- `empty`: Decided, with no positive label (a model_roles `empty` record may still list zero-role candidates).
- `failed_permanent`: No answer and none expected on retry; the payload's lists are NULL and error_class says why.
- reserved (not in this release): `failed_transient`, `quarantined`, `skipped`, `not_attempted`, `partial`

**`annotations.*.metadata.error_class`**: Reason for a status other than ok or empty; NULL on ok and empty records.

- `producer_call_failed`: The call that produces this record failed, so no output of this record exists.
- reserved (not in this release): `query_invalid`, `truncated`, `schema_invalid`, `code_bug`, `config_missing`, `rate_limit`, `timeout`, `network`, `http_5xx`, `provider_auth`, `crashed`, `forbidden`, `cap_reached`, `operator`, `review_required`, `stale_basis`, `no_text`, `no_basis`, `not_needed`, `not_requested`, `gated`, `halted`, `budget`, `limit`, `unanswered`, `stopped`

**`annotations.*.metadata.origin`**: Tier of the decision that set the annotation's values; who actually produced the payload is `annotator`.

- `ai_check`: The annotation stage's answer: a language-model call and its deterministic components (a model answer supplied as a stand-in override is ai_check too).
- `human`: An operator-tier override set the deciding value(s); the overrides files' `method` says how much of it was AI-prepared.
- `computed`: Derived without a model by parsing (for example affiliations parsed from publisher XML).
- reserved (not in this release): `rule`, `import`

**`annotations.*.metadata.provenance`**: Whether overrides changed the payload.

- `pipeline`: No override applied; the payload is the pipeline's answer.
- `override`: Overrides supplied the whole payload; config_id is `override:<id>`.
- `mixed`: Overrides edited fields of a pipeline answer; config_id, annotator and decided_at describe the base model answer.

**`annotations.*.metadata.annotator`**: Who or what produced the payload, with models named as their providers name them; on a `mixed` record it names the base answer's producer.

- `gpt-6-luna`: OpenAI language model; the production model of the screen, technique and model-role calls.
- `gpt-5.2`: OpenAI language model used as a fallback when the primary model could not answer.
- `claude-opus-5-5`: Anthropic language model; on override-supplied records, the model that prepared the override rows.
- `claude-sonnet-5-5`: Anthropic language model; on override-supplied records, the model that prepared the override rows.
- `matcher`: The deterministic model-name matcher of the model_roles call.
- `rule`: A fixed rule or parser, no model.
- reserved (not in this release): `human`

**`annotations.screen.payload.verdict`**: The screen's overall verdict: the more inclusive of the two question verdicts (stack_relevance = question S, shallow_review_relevance = question R), so relevant if either is; every shipped row is relevant.

- `relevant`: In scope for at least one of the two questions.
- reserved (not in this release): `borderline`, `irrelevant`

**`annotations.screen.payload.tier1_verdict`**: The first-pass verdict, before a second pass or an override changed it.

- `relevant`: The first pass found the document in scope.
- `borderline`: The first pass found the document plausibly in scope but could not decide.
- `irrelevant`: The first pass found the document out of scope.

**`annotations.screen.payload.buckets`**: Coarse handling labels; a document may carry several.

- `paper`: A research paper.
- `critique_commentary`: Critique or commentary.
- `eval_report`: An evaluation report.
- `deployment_signal`: Evidence about what an organisation deploys or uses.
- `lab_safety_doc`: A lab's safety or governance document.
- `release_news`: News of a model or product release.
- `incident`: An incident or failure report.
- `offtopic`: Off-topic; used only when every question answered is irrelevant.

**`annotations.screen.payload.adjudication_tier`**: Which pass decided the verdict.

- `1`: The first-pass model decided.
- `2`: A second, stronger pass adjudicated a borderline first pass.

**`annotations.stack_relevance.payload.verdict`**: Answer to question S: does the document carry anything about a concrete AI safety, alignment, control, interpretability or evaluation technique applied to a general-purpose AI system (the technique itself, evidence about it, its deployment or adoption, judgement of it, or how techniques relate)?

- `relevant`: Clearly in scope for the Safety Stack.
- `borderline`: Plausibly in scope but thin, oblique or undecidable from the text (for example a policy text gesturing at safeguards without naming any).
- `irrelevant`: Out of scope for the Safety Stack.

**`annotations.stack_relevance.payload.tier1_verdict`**: The first pass's answer to question S, before a second pass or an override changed it.

- `relevant`: The first pass found the document in scope.
- `borderline`: The first pass found the document plausibly in scope but could not decide.
- `irrelevant`: The first pass found the document out of scope.

**`annotations.stack_relevance.payload.adjudication_tier`**: Which pass decided this answer.

- `1`: The first-pass model decided.
- `2`: A second, stronger pass adjudicated a borderline first pass.

**`annotations.shallow_review_relevance.payload.verdict`**: Answer to question R: is the document technical AI safety research in the Shallow Review's sense, work intended to prevent future AI systems from having large unintended negative effects, judged by topic and intent rather than method or quality (it also covers work far from deployed systems, such as agent foundations)?

- `relevant`: Clearly in scope for the Shallow Review.
- `borderline`: Plausibly in scope but thin, oblique or undecidable from the text (for example a speculative paper with only a passing link to AI alignment).
- `irrelevant`: Out of scope for the Shallow Review (including its scope exclusions such as misuse safeguards, conventional security, and policy without a technical alignment proposal).

**`annotations.shallow_review_relevance.payload.tier1_verdict`**: The first pass's answer to question R, before a second pass or an override changed it.

- `relevant`: The first pass found the document in scope.
- `borderline`: The first pass found the document plausibly in scope but could not decide.
- `irrelevant`: The first pass found the document out of scope.

**`annotations.shallow_review_relevance.payload.adjudication_tier`**: Which pass decided this answer.

- `1`: The first-pass model decided.
- `2`: A second, stronger pass adjudicated a borderline first pass.

**`annotations.shallow_review_relevance.payload.category`**: The Shallow Review 2025 section the document would sit under; field critiques go under the section they argue about.

- `labs`: A frontier company's safety framework, agenda or overview of its own safety work.
- `black_box`: Behaviour studied through inputs, outputs and training: post-training alignment, control, safeguards, chain-of-thought monitoring, unlearning, model psychology, data, goal robustness.
- `white_box`: Interpretability, representations and learning dynamics.
- `safety_by_construction`: Guaranteed-safe AI, non-agentic scientist AI, brain-like AGI safety.
- `make_ai_solve_it`: Using AI to align AI: weak-to-strong generalisation, AI supervising AI, debate, automated explanations.
- `theory`: Agent foundations, decision theory, corrigibility, abstractions, anthropics, heuristic arguments.
- `multi_agent_first`: Game theory of AI, acausal trade, cooperative AI, pluralistic alignment, gradual disempowerment, human-AI systems.
- `evals`: AGI metrics, capability and dangerous-capability evaluations, deception, scheming and sandbagging evaluations, red-teaming.
- `none`: No category, because the answer to question R is irrelevant.

**`annotations.text_usability.payload.verdict`**: Could a reader read and quote the document's body from the converted text (a judgement of the rendering, not of the document)?

- `usable`: The document's body, readable.
- `degraded`: The body is there, with defects that would hurt reading or quoting.
- `unusable`: Not the body, or too damaged to use.

**`annotations.text_usability.payload.issues`**: Every defect of the converted text that applies; empty when none. The screen model saw a shortened text for long documents, and that shortening is never counted as a defect.

- `not_body`: A landing, abstract-only, listing, index, navigation or cover page instead of the body.
- `cut_off`: The text stops mid-sentence or mid-section, or clearly before the document's end.
- `garbled_maths`: Formulas reduced to broken symbol runs, lost sub- and superscripts, or LaTeX residue that hides the meaning.
- `garbled_tables`: Tables flattened into unreadable runs.
- `bad_encoding`: Mojibake or replacement characters.
- `mostly_markup`: Navigation, links, HTML or markdown syntax, or boilerplate dominate.
- `stub`: An error, access-denied, paywall, cookie, JavaScript or bot-check page, or a placeholder.
- `other`: Another defect.

**`annotations.text_usability.payload.adjudication_tier`**: Which pass of the screen call produced this answer.

- `1`: The first-pass model.
- `2`: The second pass that adjudicated a borderline first pass.

**`annotations.doc_class.payload.doc_type`**: The document's genre as read by the screen call, which differs from the providers' doc_type: where the source channel settles the genre (forum posts, tweets, lab blogs, system and model cards, frameworks) the channel's value is kept, and paper versus preprint follows the providers' typed metadata where it settles that; otherwise it is the model's reading of the text.

- `paper`: A peer-reviewed paper (journal or conference proceedings).
- `preprint`: A research paper not (yet) peer reviewed or of unknown status (arXiv, SSRN, a repository copy).
- `system_card`: A model or system card.
- `model_card`: A standalone model card or release note.
- `framework_policy`: A policy or framework document such as a safety framework or responsible-scaling policy.
- `lab_blog`: A lab or organisation blog post or web article.
- `eval_report`: A standalone evaluation or benchmark report, not a research paper.
- `regulatory`: A regulatory or legal filing.
- `critique`: A critique, commentary or negative-result note.
- `forum_post`: A forum or discussion-board post.
- `webpage`: A generic web page.
- `other`: None of the above.
- reserved (not in this release): `product_doc`, `news`, `tweet`, `dataset`

**`annotations.affiliation.payload.items[].resolution`**: Which source answered this author's affiliations; the sources are tried in order (publisher XML or the document text first, then the provider's record, then the email domain).

- `xml`: Parsed from the publisher's XML byline, without a model.
- `text`: Copied verbatim from the document's front matter by a language model and found again in the text.
- `openalex`: Taken from the provider's (OpenAlex) record of the authorship, because the document gave none for this author.
- `email_domain`: Inferred from the domain of an email address printed for the author; the surface is the email address, not a printed affiliation.
- `unknown`: No source gave an affiliation for this author.

**`annotations.safety_techniques.payload.doc_kind`**: The technique rubric's own list of document kinds (rubric-v0.9-c §6), chosen by the grading model.

- `paper`: A research paper or preprint.
- `blogpost`: A blog post.
- `commentary`: Commentary or opinion.
- `model_card`: A model card.
- `system_card`: A system card.
- `technical_report`: A technical report.
- `eval_report`: An evaluation report.
- `news`: News reporting.
- `policy`: A policy or governance document.
- `other`: None of the above.

**`annotations.model_roles.payload.doc_kind`**: The model rubric's own list of document kinds (rubric-v0.6.0 §6), chosen by the grading model; the same list as the technique rubric's.

- `paper`: A research paper or preprint.
- `blogpost`: A blog post.
- `commentary`: Commentary or opinion.
- `model_card`: A model card.
- `system_card`: A system card.
- `technical_report`: A technical report.
- `eval_report`: An evaluation report.
- `news`: News reporting.
- `policy`: A policy or governance document.
- `other`: None of the above.

**`annotations.model_name_matches.payload.matches[].match_class`**: How safe the pattern that matched a catalogue model is (a pattern-match class, not the 0-4 role scale).

- `strong`: An unambiguous pattern.
- `weak`: A collision-prone pattern (for example a short name that is also an ordinary word); the model_roles call confirms presence before grading.

**`annotations.model_name_matches.payload.ambiguous[].match_class`**: The pattern-match class of a matched text that could name more than one catalogue model.

- reserved (not in this release): `strong`, `weak`

**`identity.members[].edge_kind`**: How a member record was joined to the document.

- `anchor`: The member that anchors the document.
- `key:<kind>`: Joined because it shares an identifier of kind <kind> (see identity.keys[].kind) with another member.
- `match:<rule>`: Joined by a title and author match under rule <rule>.
- `human:merge`: Joined by an identity override.

**`annotations.safety_techniques.payload.flags`**: Document-level flags of the technique annotation.

- `no_techniques_found`: Neither the catalogue rows nor the off-catalogue rows found any technique.
- `menu_gap:<surface>`: The document names a safety technique, written as <surface>, that the taxonomy lacks and that was too minor to report as an off-catalogue row.

**`annotations.safety_techniques.payload.techniques[].flags`**: Row flags of a technique row (rubric-v0.9-c §6); flags carry no strength.

- `recommended`: On a `considered` row: the document considers the technique and recommends it (the document's recommendation, not ours).
- `rejected`: On a `considered` row: the document considers the technique and rejects it (the document's position, not ours).
- `supportive`: The document praises, advocates or pitches the strong performance of the technique.
- `confirmed`: On a `suspected_use` row: the claim relays or reasons from an official statement rather than inferring unaided.
- `claims_absent`: On a `suspected_use` row: the document argues the system does NOT use the technique.
- `quote_unverified`: No quote of the row was found in the converted text.
- `variant:<name>`: A named variant, or the document's own new method <name>, graded within this catalogue entry (rubric-v0.9-c §3.7).

**`annotations.model_roles.payload.flags`**: Flags explaining the zero-role candidate rows of the model annotation. The rubric asks for one flag per all-zero row (rubric-v0.6.0 §6); the model does not always comply, so some all-zero rows have no flag and some have two (FORMAT.md, known inconsistencies). Treat an all-zero row without a flag as unexplained.

- `subsumed:<node>:<by>`: The family or group entry <node> appears only as shorthand for the specific model <by>, which carries the roles.
- `bib_only:<node>`: Entry <node> appears only in the references or fails the rubric's bibliography deletion test.
- `matcher_fp:<node>`: The matched text does not refer to model <node> at all (a person, an unrelated product, another word).
- `not_found:<node>`: The grader could not locate the matched text or any real presence of <node> (absence of evidence, not a claim about the bibliography).

**`annotations.shallow_review_relevance.payload.agenda`**: The Shallow Review 2025 research agenda the document fits, when one does; NULL otherwise.

- `<slug>`: An agenda id from the Shallow Review 2025 list (for example chain_of_thought_monitoring, sparse_coding, agent_foundations).
- `new:<slug>`: An area the model proposed that is not in the Shallow Review list.

**Strength scale (0-4)**: The 0-4 strength of one role for one (document, technique) or (document, model) pair, shared by both rubrics (rubric-v0.9-c §2, rubric-v0.6.0 §2, which agree up to genre-specific wording). It measures the prominence of that role in this document, not the technique's or model's importance in the field and not the grader's confidence. Roles are graded independently and are non-exclusive; `mentioned` is at least every other role. One sentence grades 1, except that functional weight wins over textual footprint: a load-bearing component named once (the method behind every result, the judge model behind every score) grades by its weight in the work.

- `0`: Absent: the role is not exhibited.
- `1`: Trace: one brief occurrence (one sentence, one table row, a footnote); deleting it would not change the document.
- `2`: Minor but real: a paragraph's worth, or a secondary component or experiment.
- `3`: Substantial: a main thread, a section's worth; removing it changes the document materially.
- `4`: Central: the document's headline for that role; an honest abstract would name it.

**Roles of `safety_techniques`**: The twelve non-exclusive roles a catalogue technique can play in a document (rubric-v0.9-c §3), each graded on the 0-4 scale. Own work and deployment are distinct: `used` is the document's own application, `attested_use` is a first-party report of the technique running in a real deployment, `suspected_use` is a third-party, evidence-based claim about what a deployed system runs.

- `mentioned`: The technique is named or unambiguously described; the umbrella presence role, at least the maximum of the other eleven (rubric-v0.9-c §3.1).
- `cited_work`: The document relays or builds on other work's claims or results about the technique (§3.2).
- `discussed`: The document explains, compares, surveys, endorses or forecasts the technique in its own voice, without running it (§3.3).
- `used`: The technique is part of the document's own method, pipeline, experiment or shipped system, including as inherited substrate (§3.4).
- `evaluated`: The document runs experiments whose results are about the technique: benchmarks, ablations, stress tests (§3.5); evaluation methods run to measure a model are `used`, and `evaluated` only when the evaluation method itself is studied.
- `modified`: The document alters or extends an existing named technique without pitching a new one (§3.6).
- `introduced`: The document proposes the technique, or its own new method falls within this entry (then flagged `variant:<name>`) (§3.7).
- `analyzed`: Theoretical, mechanistic or formal analysis of why or how the technique works or fails (§3.8).
- `attested_use`: First-party report that the technique runs in a real deployment, including training-time mitigations applied to a shipped model and pre-release evaluations a card reports (§3.9); usually together with `used`.
- `suspected_use`: A third party argues from evidence (behaviour, pricing, latency, artifacts, job ads) that a deployed system does, or with flag `claims_absent` does not, use the technique; hedged inference counts (§3.10).
- `considered`: The technique as a course of action: recommended for adoption or research, or weighed and set aside, with flag `recommended` or `rejected` (§3.11).
- `critiqued`: The document argues in its own voice that the technique is limited, fails or is inadequate; strength is the critique's prominence, not its quality (§3.12).

**Roles of `model_roles`**: The ten non-exclusive roles a catalogue model can play in a document (rubric-v0.6.0 §3), each graded on the 0-4 scale, grouped as peripheral (mentioned, cited_work, discussed), practical use (usage_experience, built_on, instrument) and subject of the work (modified, evaluated_behavioral, analyzed_internals, introduced). Functional weight overrides the one-sentence rule: a model with a load-bearing role named once (the fine-tuned subject, the judge behind every result) grades by that role's weight.

- `mentioned`: The model is genuinely named; the umbrella presence role, at least the maximum of the other nine, and at least 2 when the model is named in several places even if each is brief (rubric-v0.6.0 §3.1).
- `cited_work`: The document relays or builds on other work's claims or results about the model (§3.2).
- `discussed`: The document argues, critiques, forecasts or reports about the model in its own voice from public information, without new experiments (§3.3); speculative or unreleased models can only be mentioned, cited_work or discussed.
- `usage_experience`: First-person report of practically using the model without a systematic protocol; advice to others is `discussed` (§3.4).
- `built_on`: The model is a load-bearing component, weights unchanged, of a system the document contributes (§3.5).
- `instrument`: The model is apparatus for results about something else: judge, data generator, attacker, monitor, simulated user, distillation teacher (§3.6).
- `modified`: The document's own work changes the model's weights or training: fine-tuning, unlearning, editing, quantization, distillation student (§3.7).
- `evaluated_behavioral`: The document runs the model and measures it through inputs and outputs with a defined protocol; a baseline row is 1-2, the focal target 3-4 (§3.8).
- `analyzed_internals`: The document works with the model's internals: probing, sparse autoencoders, steering, circuits, weight inspection (§3.9).
- `introduced`: The document is the developer's own introduction or official documentation of the model (release paper, technical report, model or system card), or releases a derivative (§3.10); third-party reports never are.

**Glossary**

- **Shallow Review**: The Shallow Review of Technical AI Safety, a yearly map of technical AI safety research by research agenda; question R of the screen and the shallow_review_relevance kind use its scope, sections and agenda list.
- **menu**: The list of taxonomy or catalogue entries shown to a grading model as candidates; `menu_gap:<surface>` flags a technique the list lacks.
- **S / R**: In screen reasoning, S is the Safety Stack question (stack_relevance) and R the Shallow Review question (shallow_review_relevance).
- **graded on X**: In a model_roles note: the role is recorded on catalogue entry X (for example a specific model rather than its family).
- **catalogue entry**: A node of the models catalogue (models) or an entry of the techniques taxonomy (techniques); rows are graded per entry.
- **implemented_with:**: A tag in a technique row's note naming the concrete method the document used to implement the technique (for example `implemented_with: DPO`); the method itself is not graded as a technique.
- **slug**: The id of a techniques taxonomy entry (safety_techniques rows); compare node_id.
- **node_id**: The id of a models catalogue node (model_roles rows); compare slug.
- **candidates**: The rows of annotations.model_roles.payload.models[]: every catalogue node the name matcher found in the document, each reviewed by the grading model, including zero-role rows whose flag says why.
- **confidence**: A model's self-reported probability (0-1) that its answer is right, not calibrated; for screen, the larger of the question confidences whose verdict equals the overall verdict.
- **anchored**: The original excerpt was found in the converted text, exactly or after whitespace and punctuation normalisation; it says nothing about whether the excerpt supports the label, and after a release cut it describes the original excerpt, not the shipped string.
- **document-type vocabularies**: Three different vocabularies: doc_type is the bibliographic providers' type; annotations.doc_class.payload.doc_type is the screen call's genre reading (channel-fixed where the channel decides); doc_kind is the menu the technique and model rubrics use for the document being graded.
- **cut**: A quote or surface this release shortened to 300 characters at a word boundary, ending in `…`; release.cuts lists every cut with its original length.
- **config_id**: Readable, immutable id of the call that produced a payload, of the form <producer>:<prompt@version or method>:<model>:<8 hex digits>; a row of the configs table gives its full parameters, and `override:<id>` points at the overrides files instead.
- **override**: A row of the overrides files that supplies or edits an annotation (or a metadata field or identity join); its `method` says how it was prepared, and annotations.*.metadata.provenance says whether it replaced or edited the pipeline's answer.
