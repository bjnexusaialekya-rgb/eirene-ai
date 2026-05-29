import re
import traceback

from app.core.orchestrator import EireneOrchestrator


print("\n==============================")
print("ORCHESTRATOR METHOD SCANNER")
print("==============================\n")


orch = EireneOrchestrator()


with open(
    "app/core/orchestrator.py",
    "r",
    encoding="utf-8"
) as f:

    code = f.read()


pattern = r"self\.([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)\("

matches = re.findall(pattern, code)

checked = set()

errors = []


for obj_name, method_name in matches:

    key = f"{obj_name}.{method_name}"

    if key in checked:
        continue

    checked.add(key)

    try:

        obj = getattr(
            orch,
            obj_name
        )

        if not hasattr(
            obj,
            method_name
        ):

            errors.append(
                f"{obj_name}.{method_name}"
            )

    except Exception:

        errors.append(
            f"{obj_name}.{method_name}"
        )


print("\n==============================")
print("MISSING METHODS")
print("==============================\n")


for e in errors:

    print(e)


print(f"\nTOTAL ERRORS: {len(errors)}")

print("\n==============================")
