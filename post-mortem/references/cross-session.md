# Cross-session mode: read many sessions instead of one

Load this only for cross-session mode, never for a review of one session. Read it completely before the first step.

Steps 1 to 6 of `SKILL.md` read ONE session. This mode reads MANY, in one of two forms; pick by the question the user asks:

| Form | The question | Steps |
|---|---|---|
| **Recurring work** | What do I keep doing by hand, what should become a skill or a script? | C1 to C6 below |
| **Comparison** | My sessions of one kind (every run of one skill, every deploy, every migration step): where does the effort go, and which problems keep coming back? | CP1 to CP5 in the section *Comparison form* |

The two do not substitute for each other: recurring work treats a job that already has a skill as covered, which is exactly the job a comparison is about.

## Recurring work

This form reads many sessions for the same kind of request done by hand again and again, and asks which of those jobs should become an artefact. Steps are ordered: clustering before extraction produces keyword buckets, and proposing before the gap-fit check produces duplicates.

**C1 - Scope.** Fix the window (a date range or a count of sessions), the transcript roots (`~/.claude/projects/<slugged-cwd>/`, plus any second config root or other CLI's logs the user names), and the privacy rule: transcripts can hold client and employer material, so evidence is cited by session id and turn rather than by quote, and the confidentiality rules and the place for the candidate list are the ones `local.md` names (by default: quote nothing, keep the list in an untracked local file). Read `transcripts.md` first: it names the enumeration and narrative tools and the schema fact, and no raw `.jsonl` is read whole. For a window larger than one context, one fresh-context subagent per slice of sessions, each writing its instances to a file. **Done when:** the window, the roots and the n of sessions in it are stated, and every session in it is either read or listed as skipped with its reason.

**C2 - Extract task instances, not keywords.** Per session, one row per job the user asked for: the request in a neutral paraphrase, the steps actually taken (tools, files, corrections), the output, and whether the user steered mid-way. A request that recurs as the same words is not the unit; the same JOB under different words is. A subagent prompt or a compaction summary is not a request (`SKILL.md` Step 1). **Done when:** every read session has at least one row or an explicit none, and each row carries its session id and turn.

**C3 - Cluster by job, count distinct sessions.** Group rows by what the user wanted done, not by vocabulary or tool. Count occurrences across DISTINCT sessions, never raw rows: one long session doing the job nine times is one occurrence. **Done when:** every row sits in exactly one cluster or in a named singles bucket, and each cluster states its distinct-session count.

**C4 - Pick the artefact on the ladder, cheapest that closes it.** Per cluster with two or more distinct sessions: nothing (the variation is the work); a written rule in the instruction file (only when no mechanism exists, Step 4's ordering); a script or check (the steps are deterministic, or the same code gets regenerated each time); a template (the structure of the output repeats, the judgement does not); a skill (only when the job is repeatable, context-sensitive, step-by-step, needs a human in the loop, and wants consistent output); an automation platform (stable, predictable, no judgement). `local.md` says where each rung lives. Name the rung you rejected directly below the chosen one and why. **Done when:** every counted cluster has one rung and one rejected-rung line.

**C5 - Gap-fit before proposing.** Per candidate, check what the setup already holds, with the catalogues and searches `local.md` lists, for the job's own terms; read the owning file's headings before calling anything absent, because a concept that exists usually exists under a name you did not search for. Where an artefact exists, the finding is that it was not reached or not good enough, and the candidate names it. **Done when:** every candidate reads either NEW with the checks run, or EXISTS with the file path.

**C6 - Deliver a ranked list.** Rank by distinct-session count, then by cost per occurrence. Per candidate: job (one line), occurrences and the evidence session ids, rung plus rejected rung, gap-fit verdict, and for any new check or gate its class and displacement answer (`SKILL.md` Step 5). Then the residue: singles and clusters decided as nothing. Approval rules are Step 4's: propose, never build. **Done when:** every cluster from C3 appears either ranked or in the residue.

### Anti-patterns

A candidate resting on one session (that is a finding for Steps 1 to 6, not a pattern). A skill where a script does it: deterministic steps in a SKILL.md buy variance for nothing. Mining keywords or tool-call frequencies instead of jobs: the built-in permission-allowlist scan already counts recurring tool calls, and a frequent `grep` says nothing about a recurring job. Counting rows instead of sessions. Quoting a transcript into a tracked file.

### Where it stops

It finds jobs the user brought to the agent, so work done outside these sessions and jobs the user stopped asking for because they failed are invisible to it; it degrades on a window of a handful of sessions, where every count is noise. For the first, interview the user about the week; for a single rough session, use Steps 1 to 6; to build the skill a candidate names, hand off to a skill-building method with the evidence sessions as its real run, because a skill built from a real run beats one built from theory (if `local.md` names a method for either, use it).

## Comparison form

Lays several sessions of ONE kind of work side by side, so that cost can be compared and a problem that keeps coming back shows up as one finding instead of as a fresh surprise in every session. The user names the kind (my source-fold sessions, every deploy this month, the last six migration steps) or the sessions themselves.

**CP1 - Select, and show the selection.** Turn the description into a rule a transcript can be tested against: a skill or command invoked, a phrase in the first request, a path the work touched. `local.md` may say how a kind of session is recognised here. List the matching sessions with id, date and first request, and let the user confirm or strike before anything is read; confidentiality and transcript reading are as in C1. Fewer than three sessions is not a comparison: run Steps 1 to 6 on each instead. **Done when:** the user confirmed the list and its n is stated.

**CP2 - Measure every session the same way.** One row per session, the same columns for all: user turns, tool calls, corrections (the agent's concessions plus refused tool calls, `transcripts.md`), outcome (delivered, partial, abandoned), active time where timestamps allow it, and the SIZE of the input (pages, files, candidates, whatever the work scales with). One counting tool and one definition per column for every session, or the table compares the tools. **Done when:** every session has every column, or `unknown` with the reason.

**CP3 - Causes per session.** Per session, a light pass of Steps 1 to 3: each correction and stall with its trace and a cause that names an artefact. When the sessions do not fit in one context, one fresh-context subagent per session, each writing its rows to a file. **Done when:** every session has its cause rows, or an explicit none.

**CP4 - Count causes across sessions.** Group the cause rows by the artefact they name plus what went wrong there, and count DISTINCT sessions. A cause in two or more sessions is a recurring problem and becomes a finding under Steps 4 to 6 (destination, mechanism before rule, class and displacement for a new check), ranked by its distinct-session count. Then compare cost per unit of input from CP2: what did the cheapest session do that the dearest did not? That difference, with its trace, is the what-worked finding to make repeatable. **Done when:** every cause row sits in a cluster or in the singles bucket.

**CP5 - Deliver.** The CP2 table, at most seven findings in the Step 6 format with each finding's session count in its Recurrence line, then the residue: singles, and any column left `unknown`. Propose, never build.

**Anti-patterns.** Ranking sessions on raw turns or tool calls while their inputs differ in size. A recurring cause counted from rows of one session. Changing a column's definition halfway through the table. Reading the selection rule loosely, so that sessions of another kind dilute the counts.
