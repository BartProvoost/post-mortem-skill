# A finding that touches a check, guard, hook, lint or gate

Load this only when a finding proposes, changes, loosens or rejects a check (Step 5 of `SKILL.md`). A waiver, a relaxed pattern and a narrowed guard change what is enforced just as much as a new check does. The measurements behind the rules marked (case N) are in `cases.md`.

## Before proposing a new check

**Look for one that already exists and is unwired or broken.** An existing check that did not run is the finding, not a reason to write a second one. `local.md` names how to list the hooks and checks of this installation.

**Extend rather than add.** If an existing check fires on the same moment, the action is a new pattern or a fixture case in that check, not a second script beside it. A new script is for a cause no existing check names.

**A check that keeps being patched is chasing examples.** When an earlier finding on the same check was closed by widening or narrowing its pattern, the action this time is to measure the check's precision over every run still on disk. That rate with its n decides between another patch, a structured field instead of matched prose, or dropping the check. The flags of one run are not that measurement.

## Rejecting a mechanism

**Reject on the narrowest form you can describe, never on the broadest.** A reason pitched at a whole category is usually true of the category and false of the guard the finding needs. Example: "a guard on backslashes in a `sed` replacement would fire on the legitimate `\/` and `\&`" is true, and says nothing about a refusal on `\d`, `\s`, `\n` or `\u`, which touches neither.

**The test:** state the rejected guard as the exact condition it would match, then ask whether THAT misfires. A rejection you cannot state as a condition is a rejection you have not checked. What this rule cannot catch: describing a narrow form and still calling it too broad, which nothing can judge for a guard that was never built.

## The Class + displacement line

Every finding that adds, loosens or changes a check carries one line with three answers:

- **Class.** CONTRACT (right regardless of who executes it, never expires), TIER (compensates the attention of a cheaper model tier, expires only when that tier is gone) or QUIRK (compensates one model family or version, the only class that genuinely dates).
- **Displacement.** What failure mode replaces the one this closes, and what is the cheapest way to satisfy the new gate without doing the work? Cover it, or record it as the known residual.
- **The gate's own cost.** What does it refuse, or push into hand work elsewhere, on a run where nothing is wrong (case 8)?

## Proving it

**For a guard or check that has a fixture file, the trace goes in as a fixture case**, so the next change to it is tested on what motivated this one. The wider the reach of a check (one wired into a deploy script runs in front of every future deploy), the less a mention in a commit message substitutes for asking first.
