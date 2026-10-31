#!/usr/bin/env python3
"""Validate paths and status metadata for HACLS KNOTE documents."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
VALID_STATUSES = {"inbox", "validated", "canonical"}
FRONTMATTER_FIELD = re.compile(r"^(type|status):\s*([^#\s]+)\s*(?:#.*)?$")


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Read simple scalar fields from YAML-style Markdown frontmatter."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        print(f"ERROR {path.relative_to(ROOT)}: อ่านไฟล์ไม่ได้: {error}")
        return None

    if not lines or lines[0].strip() != "---":
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = FRONTMATTER_FIELD.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip("'\"")

    return None


def validate(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    errors: list[str] = []
    fields = parse_frontmatter(path)

    if fields is None:
        return [f"{relative}: frontmatter ไม่สมบูรณ์หรืออ่านไฟล์ไม่ได้"]
    if fields.get("type") != "KNOTE":
        return []

    parts = relative.parts
    if (
        len(parts) < 5
        or parts[0] != "knowledge"
        or parts[1] not in VALID_STATUSES
        or parts[3] != "notes"
        or path.suffix.lower() != ".md"
    ):
        errors.append(
            f"{relative}: KNOTE ต้องอยู่ใน knowledge/<inbox|validated|canonical>/<topic>/notes/*.md"
        )

    status = fields.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"{relative}: status ต้องเป็น inbox, validated หรือ canonical")
    elif len(parts) > 1 and parts[0] == "knowledge" and parts[1] in VALID_STATUSES and status != parts[1]:
        errors.append(f"{relative}: status: {status} ไม่ตรงกับโฟลเดอร์สถานะ {parts[1]}")

    return errors


def main() -> int:
    paths = sorted(
        path for path in KNOWLEDGE.rglob("*.md")
        if "templates" not in path.relative_to(KNOWLEDGE).parts
    )
    errors = [error for path in paths for error in validate(path)]

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"พบปัญหา {len(errors)} รายการ")
        return 1

    print(f"ผ่าน: ตรวจไฟล์ Markdown {len(paths)} ไฟล์ ไม่พบ KNOTE ที่ผิดตำแหน่งหรือสถานะ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
