#!/usr/bin/env python3
"""Validate public truth-surface tags and artifact boundaries."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_TAGS = {"Lean-proved", "Computed here", "Imported theorem", "Interpretation"}
BOUNDARY_RE = re.compile(
    r"(light-cone|light rays|horizon|redshift|arrow of time|shared sign|shared-sign|"
    r"t\s*>\s*0|c\s*>\s*0|PHYS-01)",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    print(f"truth-surface check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: str) -> str:
    target = ROOT / path
    if not target.exists():
      fail(f"missing {path}")
    return target.read_text(encoding="utf-8")


def load_yaml(path: str) -> dict:
    target = ROOT / path
    if not target.exists():
        fail(f"missing {path}")
    with target.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def check_manifest() -> None:
    target = ROOT / "results/manifest.json"
    if not target.exists():
        fail("missing results/manifest.json")
    manifest = json.loads(target.read_text(encoding="utf-8"))
    if manifest.get("schema") != "ii-logos-spacetime-derivation-results-manifest-v2":
        fail("results/manifest.json must use schema v2")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail("results/manifest.json has no artifacts list")

    for index, entry in enumerate(artifacts):
        if not isinstance(entry, dict):
            fail(f"artifact entry {index} must be an object")
        path = entry.get("path")
        if not path:
            fail(f"artifact entry {index} is missing path")
        if not (ROOT / path).exists():
            fail(f"artifact path does not exist: {path}")
        producer = entry.get("producer")
        if producer and not (ROOT / producer).exists():
            fail(f"artifact producer does not exist: {producer}")
        tag = entry.get("truth_tag")
        if tag not in ALLOWED_TAGS:
            fail(f"artifact {path} has invalid truth_tag {tag!r}")


def lean_text() -> str:
    paths = [ROOT / "Spacetime.lean", ROOT / "SpacetimeFull.lean", *sorted((ROOT / "Spacetime").glob("*.lean"))]
    return "\n".join(path.read_text(encoding="utf-8") for path in paths if path.exists())


def declaration_exists(name: str, text: str) -> bool:
    needle = name.split(".")[-1]
    return re.search(rf"\b(def|theorem|lemma|structure|inductive)\s+{re.escape(needle)}\b", text) is not None


def check_specs() -> None:
    claims = load_yaml("spec/claims.yaml").get("claims", [])
    equations = load_yaml("spec/equations.yaml").get("equations", [])
    source = lean_text()

    for claim in claims:
        claim_id = claim.get("id", "<missing id>")
        status = claim.get("status")
        if status not in ALLOWED_TAGS:
            fail(f"claim {claim_id} has invalid status {status!r}")
        statement = claim.get("statement", "")
        if status == "Lean-proved" and (claim_id == "PHYS-01" or BOUNDARY_RE.search(statement)):
            fail(f"claim {claim_id} crosses the physical boundary as Lean-proved")
        for declaration in claim.get("lean_declarations", []) or []:
            if not declaration_exists(str(declaration), source):
                fail(f"claim {claim_id} references missing Lean declaration {declaration}")

    for equation in equations:
        eq_id = equation.get("id", "<missing id>")
        status = equation.get("status")
        if status not in ALLOWED_TAGS:
            fail(f"equation {eq_id} has invalid status {status!r}")
        expression = equation.get("expression", "")
        if status == "Lean-proved" and BOUNDARY_RE.search(expression):
            fail(f"equation {eq_id} crosses the physical boundary as Lean-proved")
        declaration = equation.get("lean_declaration")
        if declaration and not declaration_exists(str(declaration), source):
            fail(f"equation {eq_id} references missing Lean declaration {declaration}")


def check_docs() -> None:
    expected = {
        "README.md": "v1.0",
        "docs/claim-status.md": "Current v1.0 Status",
        "docs/build-status.md": "v1.0",
        "docs/repo-operating-system.md": "v1.0",
        "PLANS.md": "v1.0",
    }
    for path, needle in expected.items():
        if needle not in read_text(path):
            fail(f"{path} is missing {needle!r}")

    pyproject = read_text("pyproject.toml")
    citation = read_text("CITATION.cff")
    if 'version = "1.0.0"' not in pyproject:
        fail("pyproject.toml version must be 1.0.0")
    if "version: 1.0.0" not in citation:
        fail("CITATION.cff version must be 1.0.0")

    doc_paths = [
        "README.md",
        "PLANS.md",
        "docs/claim-status.md",
        "docs/theorem-ledger.md",
        "docs/paper-lean-notebook-crosswalk.md",
        "docs/public-reader-preview.md",
        "docs/build-status.md",
        "docs/repo-operating-system.md",
    ]
    for path in doc_paths:
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            if "Lean-proved" in line and BOUNDARY_RE.search(line):
                fail(f"{path}:{line_no} marks a physical-boundary line as Lean-proved")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifacts-only", action="store_true")
    args = parser.parse_args()

    check_manifest()
    if not args.artifacts_only:
        check_specs()
        check_docs()
    print("truth-surface check passed")


if __name__ == "__main__":
    main()
