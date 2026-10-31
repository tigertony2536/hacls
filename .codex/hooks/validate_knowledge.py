#!/usr/bin/env python3
"""Run the KNOTE validator after Codex tools that may edit knowledge files."""

from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_knowledge.py"


def should_validate(event: dict) -> bool:
    tool_name = event.get("tool_name", "")
    tool_input = event.get("tool_input", {})
    if tool_name == "apply_patch":
        return True
    if tool_name == "Bash" and isinstance(tool_input, dict):
        command = tool_input.get("command", "")
        return "knowledge/" in command or "validate_knowledge.py" in command
    return False


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    if not should_validate(event):
        return 0

    spec = importlib.util.spec_from_file_location("validate_knowledge", VALIDATOR)
    if spec is None or spec.loader is None:
        print(json.dumps({"decision": "block", "reason": "โหลด KNOTE validator ไม่สำเร็จ"}))
        return 0

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = io.StringIO()
    with redirect_stdout(output):
        result = module.main()

    if result != 0:
        print(json.dumps({"decision": "block", "reason": output.getvalue().strip()}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
