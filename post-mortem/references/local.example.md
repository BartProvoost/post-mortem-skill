# This installation (template)

Copy this file to `local.md` in the same folder and fill in the angle-bracket parts. `SKILL.md` and the other references name ROLES; this file says which real file, script or skill plays each role where the skill runs. Leave a row out when your setup has no such file. **When `local.md` does not exist, the skill reads this template and asks the user once where each role lives**, and delivers findings as text for any role nobody can name.

## Destinations (Step 3 and Step 4)

| Role | Here |
|---|---|
| Always-loaded instruction file | <for example `CLAUDE.md` or `AGENTS.md`; name a broader and a narrower one if you have both, and which rules go where> |
| A skill's own file | <for example `.claude/skills/<skill>/SKILL.md`; how a third-party skill is steered without editing it> |
| Authoring guide for skills and rules | <a file, or none> |
| Decision log | <for example `docs/decisions/`> |
| Backlog | <for example `BACKLOG.md` or an issue tracker> |
| Change log and status | <for example `CHANGELOG.md`; note it if the file is generated from fragments> |
| Project context | <for example `docs/` or a `.context/` folder> |
| A script or check | <for example `scripts/`, and the index file that lists them, if any> |

**Was-this-found-before grep (Step 3):** <which files to search for earlier post-mortem findings, for example the change log and the backlog>.

## Transcript tools

<Scripts that list sessions, strip a transcript to its narrative, or find correction moments; or none, in which case the agent searches the transcript files directly as `transcripts.md` describes.>

## Cross-session mode

- **Confidentiality (C1):** <which material in the transcripts may not be quoted, and where the candidate list may be stored>.
- **Where each rung lives (C4):** <instruction file, script folder, template folder, skill folder, automation platform>.
- **Comparison form (CP1, CP2):** <how a kind of session is recognised here (a skill or command it ran, a phrase in the first request), which tool counts tool calls and corrections per session, and what the size of an input is measured in>.
- **Gap-fit checks (C5):** <the catalogues and searches that show what already exists: a skills list, a scripts index, a templates index>.
