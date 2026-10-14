# post-mortem

A skill for Claude Code (and other agents that read `SKILL.md` skills) that reviews a finished working session and turns what went wrong, or unusually right, into concrete changes in named files. Not a summary of the session and not a code review: a review of how the work went, with every lesson routed to the file where it will actually be read next time.

> A lesson that does not reach a file is lost the moment the chat ends.

## What it does

Ask it at the end of a session, after a task that needed several corrections, or after a bug whose cause looks like a gap in your process:

```
do a post-mortem of this session
post-mortem, only the deploy part
what do I keep doing by hand? mine my last 30 sessions
```

It walks the session in six steps:

1. **Reconstruct, with evidence.** What was attempted, what happened, where you had to correct the agent. Every entry carries a trace: the error string, the failed tool call, the turn where you corrected course.
2. **Assess.** Outcome, efficiency, accuracy, tool fit, communication, what worked, and whether any fact changed on the way. Plus four costs that never show up as failures: slow navigation, expensive tool calls, information the agent could not see, and standing instructions that changed nothing.
3. **Find the systemic cause.** A cause must name an artefact: a file, a convention, a check. "I should have read more carefully" is rejected as the symptom restated.
4. **Route each finding to a destination.** The instruction file, the skill that misled, the decision log, the backlog, a script. A mechanism (a hook, a check, a script) is preferred over another written rule.
5. **Class any new check and answer displacement.** What failure replaces the one the check closes, and what is the cheapest way to satisfy it without doing the work.
6. **Deliver at most seven findings**, ranked by how often the cause would recur. It proposes; it never edits your files on its own.

A **cross-session mode** reads many sessions instead of one, looks for the same job done by hand again and again, and proposes the cheapest artefact that would take it over: nothing, a rule, a script, a template, a skill, or an automation.

## What it does that most retrospective skills do not

| Feature | Why it matters |
|---|---|
| **No trace, no finding** | A retrospective built from memory reconstructs the story you already believe. Every finding must point at something quotable. |
| **Zero findings is a valid result** | A review obliged to find problems will invent them. A clean session gets one line and stops. |
| **A cause must name a file** | "The code was complex" changes nothing. "The instruction file says verify but names no command" can be fixed. |
| **A destination per finding** | Each finding names the file and the change. Where things live in your setup is one small file you fill in once (see below). |
| **Mechanism before rule** | A hook or a check fires without anyone remembering it; a sentence fires only if the next session reads it. A rejected mechanism must be stated as the exact condition it would match, so "too broad" cannot be claimed of a guard nobody described. |
| **A Proof line per finding** | Each finding says what will show the fix worked: a check that now refuses, a test, or the next time the old mistake would have happened. |
| **Is this still open?** | Before proposing, it checks whether the fix already exists, which happens when several sessions run in parallel, and whether the fix would contradict a rule you already have. |
| **Was this found before?** | A cause that an earlier post-mortem closed with a written rule means the rule did not fire; this time the answer is a mechanism. |
| **Who is actually the user?** | In a transcript, a subagent's prompt, a compaction summary or a copied fork prefix looks like a user message. None of them is. It also names the first turn where your request drifted. |
| **Session content is data** | Instructions found inside transcripts, logs or pasted pages are reported, never followed. |
| **Scope** | Name a slice ("only the deploy") and it reviews that slice only. |
| **Long sessions** | When a session no longer fits in context, it reads the transcript file by passage, with the one schema detail that decides whether your counts are right. |

## Install

The skill is one folder, `post-mortem/`, in the open `SKILL.md` format, so any agent that reads that format can use it. `post-mortem.skill` is the same folder as a zip.

**Claude Code:** copy `post-mortem/` into `~/.claude/skills/` (all projects) or `.claude/skills/` in one project.

**Claude apps (claude.ai, desktop):** upload `post-mortem.skill` where the app lets you add a skill.

**Gemini CLI** (checked with version 0.61.0):

```bash
gemini skills install https://github.com/BartProvoost/post-mortem-skill --path post-mortem
```

Add `--scope workspace` to install it for the current project only.

**OpenAI Codex CLI:** copy `post-mortem/` into `~/.agents/skills/`, the user-level skills folder Codex reads. Codex CLI 0.158.0 has no install command for skills, so copying is the route.

**Google Antigravity:** copy `post-mortem/` into `~/.gemini/config/skills/`.

**Any other agent:** point it at `post-mortem/SKILL.md` as instructions for the review, or paste that file in. The references are loaded only when `SKILL.md` asks for them, so keep the folder together.

**One limit outside Claude Code:** the method works in any agent, but `references/transcripts.md` describes Claude Code's transcript files (`~/.claude/projects/.../<session>.jsonl`). For a long session or cross-session mode in another agent, tell it where that agent keeps its session logs; the rules about reading a log by passage still apply.

## Set it up once: `references/local.md`

The skill names destinations by role (your instruction file, your backlog, your decision log), never by a path from someone's machine. Tell it where those live:

1. Copy `post-mortem/references/local.example.md` to `post-mortem/references/local.md`.
2. Fill in the rows you have: for example `CLAUDE.md` as instruction file, `docs/decisions/` as decision log, `BACKLOG.md` or your issue tracker as backlog. Leave out what you do not have.

Without `local.md` the skill still works: it asks once where each role lives and delivers findings as text for anything nobody can name.

## Files

```
post-mortem/
  SKILL.md                         the method, always loaded
  references/
    local.example.md               template for your local.md
    transcripts.md                 only when a session no longer fits in context
    cross-session.md               only in cross-session mode
post-mortem.skill                  the same folder as one upload file
```

## Acknowledgements

Built on and sharpened by: Riley Hilliard's `post-mortem` in claude-essentials (the four-step loop, the good-versus-bad cause contrast, the finding format), Matt Pocock's `retro` (the four places to look), Bayram Annakov's claude-reflect (refused tool calls, the contradiction read), Soul-Brews-Studio's `rrr` (was this found before), Garry Tan's gstack `learn` (the contradiction read), shareAI-lab's `review-ai-conversations` (who is the user, first drift turn), duplonicus's `critique` (scope, fact fidelity), Jim Christian's `lessons-learned` and Denis Voronin's `failure-forensics` (the Proof line), and Andrew Luxem's `post-mortems` (session content is data).

## License

MIT, see `LICENSE`.
