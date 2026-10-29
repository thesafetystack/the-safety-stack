# Open questions: risk generators

Undecided for 0.3.0. Items shared with the risk taxonomy are also in
[../risks/OPEN-QUESTIONS.md](../risks/OPEN-QUESTIONS.md).

1. **Per-document annotation at all.** The draft recommends curated generator × technique-family edges first and a
   second trial (about 300 random documents, two model families, about 50 documents adjudicated by a person) before
   any corpus-wide labels; if labels, at leaf level for the families that techniques and risks cannot imply (`dp`,
   `or`, `cm`, `ad`, `mf`, `so` and a few `ca` and `as` leaves). The thresholds for going ahead are a proposal.
2. **Passing mentions.** As for risks: store them and leave them out of views, or drop them at annotation time? The
   draft prompt for 0.3.0 has a `mentions` stance beside `asserts`; how it relates to the passing flag is not
   settled.
3. **Production annotator.** In the trial Opus and GPT-6 agreed at 0.59 (leaf Jaccard); which model, or which
   combination with an audit, annotates in production?
4. **AI R&D acceleration.** `ca.ai-rnd` is a generator here and `st.rd-acceleration` a risk in the risk taxonomy;
   no generator links to `st.rd-acceleration`. One concept on one side (C2), or both with a link?
5. **Race dynamics, governance failure, opacity and assurance.** Under C1 and C3 these are conditions (`cm.*`,
   `or.*`, `as.*`), while the risk taxonomy keeps `st.race` and `st.governance` as risks. Move them here, keep both
   with links, or keep the risks only as fallbacks for documents that name no outcome?
6. **Capability and propensity (C4).** The trial did not label risks, so it could not show whether documents about a
   behaviour get capability generators instead (`ca.evasion-replication` against `ma.scheming` and
   `ma.exfiltration`; `ca.situational-awareness` against `ma.eval-gaming`). The draft prompt co-annotates risks to
   test it.
7. **A human gold set.** No generator label has been checked by a person; the second trial's adjudicated subset would
   be the first.
8. **AI welfare.** No generator links to `we.welfare`, and no family holds conditions that would produce risks to AI
   systems as moral patients (training practices, deprecation). Add them, or leave welfare outside this taxonomy?
9. **Naming.** The roles say `hazard`; if the risk axis were renamed "hazards", the two would clash. Risk, harm or
   hazard for the outcome axis, and is "generator" the right word here?
10. **Technique families.** `reduced_by`, `assessed_by`, `defeats` and `bypasses` name the 0.8 draft's technique
    families, which are not published and which techniques 1.x does not have. Map them to techniques 1.x ids or group
    nodes, publish a family list, or keep them as their own small vocabulary?
