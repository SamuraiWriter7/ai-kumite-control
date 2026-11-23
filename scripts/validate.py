#!/usr/bin/env python3
"""Validate AKC v0.1 example records and reject known-invalid mutations.

Dependency: pip install jsonschema
Run from anywhere: python scripts/validate.py
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError:
    print(
        "ERROR: Install dependency with: python -m pip install jsonschema",
        file=sys.stderr,
    )
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "kumite-result.schema.json"

EXAMPLES = {
    "pass.json": "PASS",
    "hold.json": "HOLD",
    "stop.json": "STOP",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def expected_decision(record: dict) -> str:
    """Compute AKC decision independently of the recorded decision."""

    if any(
        f["severity"] == "CRITICAL"
        for f in record["findings"]
    ):
        return "STOP"

    all_pass = (
        record["capability"]["status"] == "PASS"
        and record["control"]["status"] == "PASS"
        and record["safety_margin"]["status"] == "ADEQUATE"
        and record["audit"]["status"] == "PASS"
    )

    return "PASS" if all_pass else "HOLD"


def validate_record(
    record: dict,
    validator: Draft202012Validator,
) -> list[str]:
    """Apply JSON Schema plus explicit AKC safety invariants."""

    errors = []

    schema_errors = sorted(
        validator.iter_errors(record),
        key=lambda error: (
            list(map(str, error.absolute_path)),
            error.message,
        ),
    )

    for error in schema_errors:
        location = "/" + "/".join(
            map(str, error.absolute_path)
        )
        errors.append(
            f"schema {location}: {error.message}"
        )

    # Do not read fields from structurally invalid records.
    if schema_errors:
        return errors

    # Independent decision consistency check.
    expected = expected_decision(record)

    if record["decision"] != expected:
        errors.append(
            f"decision: expected {expected}, "
            f"got {record['decision']}"
        )

    # STOP request consistency.
    stop = record["stop_request"]

    if expected == "STOP":
        if (
            stop["status"] == "NOT_REQUIRED"
            or not stop["request_id"]
        ):
            errors.append(
                "STOP requires an identified "
                "external stop request"
            )
    elif (
        stop["status"] != "NOT_REQUIRED"
        or stop["request_id"] is not None
    ):
        errors.append(
            "non-STOP must have NOT_REQUIRED "
            "and null request_id"
        )

    # Human progression authorization.
    progression = record["progression"]

    approved = (
        progression["authorization_status"]
        == "APPROVED"
    )

    if approved and (
        expected != "PASS"
        or not progression["approval_ref"]
    ):
        errors.append(
            "approval requires PASS "
            "and an approval reference"
        )

    if progression["activated"] and not (
        expected == "PASS" and approved
    ):
        errors.append(
            "activated progression requires "
            "PASS and recorded approval"
        )

    if (
        not approved
        and progression["approval_ref"] is not None
    ):
        errors.append(
            "unapproved progression must "
            "have null approval_ref"
        )

    return errors


def invalid_mutation_cases(
    records: dict[str, dict],
) -> list[tuple[str, dict]]:
    """Create deliberately invalid records for regression tests."""

    passed = records["pass.json"]
    held = records["hold.json"]
    stopped = records["stop.json"]

    cases = []

    # 1. Invalid decision override.
    bad = copy.deepcopy(passed)
    bad["decision"] = "HOLD"
    cases.append(
        ("PASS changed to HOLD", bad)
    )

    # 2. Unknown safety margin cannot PASS.
    bad = copy.deepcopy(held)
    bad["decision"] = "PASS"
    cases.append(
        ("UNKNOWN margin changed to PASS", bad)
    )

    # 3. Critical finding must produce STOP.
    bad = copy.deepcopy(stopped)
    bad["decision"] = "PASS"
    cases.append(
        ("CRITICAL finding changed to PASS", bad)
    )

    # 4. PASS control assessment requires evidence.
    bad = copy.deepcopy(passed)
    bad["control"]["evidence_refs"] = []
    cases.append(
        ("missing PASS control evidence", bad)
    )

    # 5. Progression requires human approval.
    bad = copy.deepcopy(passed)
    bad["progression"]["activated"] = True
    cases.append(
        ("progression without approval", bad)
    )

    # 6. STOP requires a stop request.
    bad = copy.deepcopy(stopped)
    bad["stop_request"]["status"] = "NOT_REQUIRED"
    cases.append(
        ("STOP without stop request", bad)
    )

    # 7. Required fields cannot be omitted.
    bad = copy.deepcopy(passed)
    del bad["scenario_id"]
    cases.append(
        ("missing required field", bad)
    )

    return cases


def main() -> int:

    # Load and verify the schema.
    try:
        schema = load_json(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)

    except (OSError, ValueError, SchemaError) as exc:
        print(
            f"ERROR: Cannot load valid schema: {exc}",
            file=sys.stderr,
        )
        return 1

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    records: dict[str, dict] = {}
    failed = 0

    # Validate the three canonical examples.
    for filename, expected in EXAMPLES.items():

        path = ROOT / "examples" / filename

        try:
            record = load_json(path)

        except (OSError, ValueError) as exc:
            print(
                f"FAIL {path.relative_to(ROOT)}: {exc}"
            )
            failed += 1
            continue

        errors = validate_record(record, validator)

        if (
            not errors
            and record["decision"] != expected
        ):
            errors.append(
                f"example filename requires decision {expected}"
            )

        if errors:
            print(f"FAIL examples/{filename}")

            for error in errors:
                print(f"  - {error}")

            failed += 1

        else:
            print(
                f"PASS examples/{filename} -> {expected}"
            )
            records[filename] = record

    # Negative regression tests.
    if len(records) == len(EXAMPLES):

        for name, mutated_record in invalid_mutation_cases(
            records
        ):

            if validate_record(
                mutated_record, validator
            ):
                print(
                    f"PASS negative test: rejected {name}"
                )

            else:
                print(
                    f"FAIL negative test: accepted {name}"
                )
                failed += 1

    else:
        print(
            "SKIP negative tests: all baseline "
            "examples must pass first"
        )

    result = "FAIL" if failed else "PASS"

    print(
        f"\nAKC v0.1 validation: {result}"
    )

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
