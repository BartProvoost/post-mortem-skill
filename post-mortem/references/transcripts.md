# Reading a session from its transcript file

Load this only when the session does not fit in context (an unattended or multi-day run), or in cross-session mode. Within context, walk the session in order instead.

## Where transcripts live and how not to read them

Claude Code writes one file per session at `~/.claude/projects/<slugged-cwd>/<session-id>.jsonl`, one JSON entry per line; a second account has its own config root. **Never read one whole: a four-day loop is tens of megabytes.** Find the passages that matter first, then open only those.

## The schema fact that decides whether your numbers are right

The bulk of a transcript sits in the ENTRY-LEVEL `toolUseResult` key, not in the `tool_result` blocks inside `message.content`, which are stubs. Summing the stubs undercounts tool output by roughly half and can return a clean zero for a file that was read back dozens of times. Measured on a 26 MB transcript: 1.526.192 characters and zero mentions of a term on the wrong key, against 2.652.280 characters and 44 mentions on the right one.

## Refused tool calls

A refused tool call with feedback sits in the entry-level `toolUseResult` as the text after `user said:`; an empty one is a refusal without feedback. Search for these separately: a tool that counts the agent's own concessions does not see them.

## Who wrote an entry

A user-role entry can be a subagent prompt (delegated work written by the agent), a compaction summary (the agent's paraphrase) or the copied prefix of a forked or resumed session. Step 1 of `SKILL.md` says how to treat each.

## Tools

Before writing a parser, check `local.md` for scripts that already list sessions, strip a transcript to its narrative or find its correction moments, and start from those. Without any, search the file for the passages first (an error string, a file name, `user said:`) and open only those lines.
