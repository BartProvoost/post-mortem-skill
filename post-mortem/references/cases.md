# The measurements behind the rules

`SKILL.md` and `gates.md` state each rule with its tell; the incident or count that produced it is here, under the number in brackets after the rule. Open this file when you want the evidence, or before you change or drop a rule. All counts come from one user's sessions on two machines, so they show that a failure happens, not how often it will happen elsewhere.

**A new measurement about this skill goes here, as a new case or as a line under an existing one. `SKILL.md` changes by at most one sentence per finding.**

## Case 1 - corrections and mid-turn messages left out (Step 1, Done when)

Over 101 post-mortem reports, 18 left out a correction that was in the session. Messages the user sent while a turn ran, 294 in 57 of those sessions, were invisible to the tool that listed the turns, and some of them were corrections aimed at a running post-mortem.

## Case 2 - a guard that keeps refusing is not a guard that works (Step 2, read 9)

Over 19 sessions, one guard on piped commands refused 74 times, while each session's report called it working. Refusals had been recalled, not counted.

## Case 3 - a mechanism named from its summary (Step 4, quote the line)

One proposal named a sync script as the mechanism from its row in an index; the script skips exactly the dirty working tree it was proposed for. Another said a brief asks for a label that the brief forbids.

## Case 4 - a search for your own words (Step 4, still open)

A search for the finding's own wording missed a rule that was written in other words. The existing rule was proposed again and the user approved a finding that was already closed.

## Case 5 - a fix tested on a look-alike (Step 4, prove on the exact trace)

A fix tested on a sentence that resembled the original still failed on the reply it came from. In another session, one file's fix left two sibling scripts with the same bug.

## Case 6 - findings summarised (Step 6, show every finding in full)

2026-10-19: a report's findings were summarised in four lines under a standing instruction to answer briefly. The user asked why the report was no longer shown.

## Case 7 - findings carried out without a go (Step 6, pre-authorised runs)

Reports written while the findings were being carried out carried a Proof line 1 time in 6, against 3 in 3 when proposing. On a second machine, 26 of 26 such reports were built first and summarised afterwards inside the run's closing message, where the user answered the run's question and never saw the findings. This is why the format is checked by `scripts/check_report.py` instead of described.

## Case 8 - the cost of a gate on a clean run (gates.md, the gate's own cost)

A refusal whose bypass had been named correctly moved about thirty hand-written rows into every later run. That cost, not the bypass, was the one that recurred.

## Case 9 - the skill grew by reviewing itself (Step 4, a new instance is a case)

2026-11-17: after some three months of post-mortems on post-mortems, `SKILL.md` held 4.118 words, 1.100 of them in Step 4, with eight measurements inline. The rule that an instruction file may not grow net applied to every file except this one. The measurements moved here and the material on checks to `gates.md`. The same review found that the report check refused a finding from a chat with no project files, which the fallback promised to support; the check now accepts *no destination: delivered as text*.
