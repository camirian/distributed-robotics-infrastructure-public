#!/usr/bin/env python3
"""Static local-reference checker for this public documentation repo.

Validates that in-repo references resolve to files that actually exist:

  * Markdown links of the form ``[text](relative/path)`` whose target is a
    local path (not an ``http(s)://`` URL, not a ``mailto:``, not a pure
    ``#anchor``). Any ``#fragment`` on the target is stripped before checking.
  * Explicit shell-style local script references of the form ``./path/...``
    found in fenced code or prose.

It deliberately does NOT validate:

  * External URLs (``http://`` / ``https://``) -- network state is out of scope.
  * Bare ``file:line`` evidence citations used in the master-plan prose.
  * The master-plan files themselves, which cite ``file:line`` in prose and
    would otherwise produce false positives.

Exit status: 0 if every checked reference resolves, 1 otherwise.
Standard library only; no third-party dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files excluded from scanning (they cite file:line evidence in prose).
EXCLUDED_FILES = {
    REPO_ROOT / "MASTER_PLAN.md",
    REPO_ROOT / "docs" / "MASTER_PLAN.md",
}

# [text](target)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# ./something or ./a/b.sh  (explicit relative path tokens)
DOT_SLASH_RE = re.compile(r"(?<![\w./])\.\/[\w./-]+")


def is_external(target: str) -> bool:
    target = target.strip()
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def normalize(target: str) -> str:
    # Drop any anchor fragment and surrounding whitespace/quotes.
    target = target.strip().strip("'\"")
    return target.split("#", 1)[0]


def check_file(md_path: Path) -> list[str]:
    """Return a list of human-readable errors for one markdown file."""
    errors: list[str] = []
    text = md_path.read_text(encoding="utf-8")
    base = md_path.parent

    targets: list[str] = []
    targets.extend(MD_LINK_RE.findall(text))
    targets.extend(DOT_SLASH_RE.findall(text))

    for raw in targets:
        if is_external(raw):
            continue
        target = normalize(raw)
        if not target:
            continue
        resolved = (base / target).resolve()
        if not resolved.exists():
            rel = md_path.relative_to(REPO_ROOT)
            errors.append(f"{rel}: dangling local reference -> {raw!r}")
    return errors


def main() -> int:
    md_files = sorted(REPO_ROOT.rglob("*.md"))
    all_errors: list[str] = []
    checked = 0
    for md_path in md_files:
        if ".git" in md_path.parts:
            continue
        if md_path.resolve() in EXCLUDED_FILES:
            continue
        checked += 1
        all_errors.extend(check_file(md_path))

    if all_errors:
        print(f"FAIL: {len(all_errors)} dangling local reference(s) "
              f"across {checked} file(s):")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"OK: all local references resolve across {checked} markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
