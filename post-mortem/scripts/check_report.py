#!/usr/bin/env python3
"""Check a post-mortem report file against the finding format of Step 6, before it is delivered.

Why it exists: across 101 post-mortems on one machine, every report written while the findings were
being carried out without a go (26 of 26) dropped the per-finding fields, including the six written
after the Proof line had become required; and 9 reports numbered a finding that had no action or was
already closed. A rule in prose had already failed in that mode, so the format is checked instead.

    python check_report.py <report.md>

A finding is a block under a heading that names it, `### Finding 3: ...` (or `Bevinding 3`). Each block
needs the five field labels (What happened, Root cause, Action, Proof, Recurrence; Dutch forms accepted),
each with text. The check refuses a block when:
  - a field is missing or empty;
  - the Proof line holds no command in backticks, no turn or entry reference (`#123`) and no plain
    statement that no proof can be named (the skill allows that statement, not silence);
  - the Action says none or already closed (those belong in the residue or the closed list);
  - the Action adds, loosens or changes a guard, gate, check, lint, hook or refusal and the block has no
    Class line naming CONTRACT, TIER or QUIRK (or n.a. with a reason).
It also refuses more than seven findings, and a file with no finding block and no zero-findings line.

What stays judgement: whether the Proof was actually run, whether the cause is systemic, whether the
Class is right. Exit 0 when every block passes, 1 when one fails, 2 on a usage error.
"""
import io
import re
import sys

# `### Finding 3: ...`, or the bold line the skill's worked example uses (`> **Finding 1: ...**`)
HEAD = re.compile(r"(?im)^(?:#{2,4}\s+|>?\s*(?=\*\*))(?:\*\*)?(?:finding|bevinding)\s*(\d+)\b.*$")
FIELDS = {
    "what happened": r"what happened|wat (?:er )?gebeurde",
    "root cause": r"root cause|oorzaak",
    "action": r"action|actie",
    "proof": r"proof|bewijs",
    "recurrence": r"recurrence|herhaling",
}
NO_ACTION = re.compile(r"(?i)^\W*(?:none|geen|n\.?a\.?|no action|already closed|al gesloten|al opgelost)\b")
GATE = re.compile(r"(?i)\b(?:guard|gate|check|lint|hook|refus\w*|weiger\w*|warn\w*|waarschuw\w*|block\w*)\b")
CLASS = re.compile(r"(?i)\*{0,2}class\b[^\n]*?(?:\b(?:CONTRACT|TIER|QUIRK)\b|n\.?a\.?\W+\w+\s+\w+)")
PROOF_OK = re.compile(r"`[^`]+`|#\d+|(?i:\bcannot be (?:named|proven|shown)\b|\bkan niet\b|\bno proof\b|\bgeen bewijs\b)")
ZERO = re.compile(r"(?i)zero findings|geen bevindingen|nothing to change")


def field(block, name):
    """The text after a field label, up to the next label or the end of the line's paragraph; None if absent."""
    m = re.search(r"(?im)(?:^|\*\*|\s-\s|^\s*-\s*)\s*(?:\*\*)?(?:%s)(?:\*\*)?\s*[:.]\s*(?:\*\*)?(.*)" % FIELDS[name], block)
    return None if m is None else m.group(1).strip().strip("*").strip()


def blocks(text):
    heads = list(HEAD.finditer(text))
    out = []
    for k, h in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(text)
        body = text[h.end():end]
        cut = re.search(r"(?m)^#{1,3}\s+(?!.*(?:finding|bevinding)\s*\d)", body)   # a later section ends the block
        out.append((h.group(1), body[:cut.start()] if cut else body))
    return out


def problems(block):
    out = []
    got = {n: field(block, n) for n in FIELDS}
    for n, v in got.items():
        if v is None:
            out.append("no %s line" % n)
        elif not v:
            out.append("empty %s line" % n)
    if got["proof"] and not PROOF_OK.search(got["proof"]):
        out.append("Proof names no command in backticks, no #entry and no statement that it cannot be named")
    if got["action"] and NO_ACTION.search(got["action"]):
        out.append("Action is none or already closed: move it to the residue or the closed list")
    if got["action"] and GATE.search(got["action"]) and not CLASS.search(block):
        out.append("Action touches a check or gate and the block has no Class line (CONTRACT, TIER, QUIRK, or n.a. with a reason)")
    return out


def check(text):
    """(n_blocks, [(finding number, [problems])], [file-level problems])."""
    bl = blocks(text)
    per = [(num, problems(body)) for num, body in bl]
    top = []
    if not bl and not ZERO.search(text):
        top.append("no finding block (### Finding N) and no zero-findings line")
    if len(bl) > 7:
        top.append("%d findings, the cap is seven" % len(bl))
    return len(bl), per, top


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    try:
        text = io.open(argv[1], encoding="utf-8").read()
    except OSError as e:
        print("check_report: %s" % e)
        return 2
    n, per, top = check(text)
    bad = 0
    for num, probs in per:
        for p in probs:
            print("finding %s: %s" % (num, p))
        bad += bool(probs)
    for p in top:
        print("report: %s" % p)
    print("check_report: %d of %d findings pass%s" % (n - bad, n, "" if not top else ", %d report problem(s)" % len(top)))
    return 0 if not bad and not top else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
