import traceback

from app.core.orchestrator import EireneOrchestrator


print("\n==============================")
print("EIRENE SYSTEM VALIDATION")
print("==============================\n")


try:

    orchestrator = EireneOrchestrator()

    print("[OK] Orchestrator initialized")

except Exception as e:

    print("[INIT ERROR]")
    traceback.print_exc()

    exit()


test_message = "I feel emotionally overwhelmed lately"


try:

    result = orchestrator.process_message(
        test_message
    )

    print("\n[PROCESS SUCCESS]\n")

    print(result)

except Exception as e:

    print("\n[PROCESS ERROR]\n")

    traceback.print_exc()


print("\n==============================")
print("VALIDATION COMPLETE")
print("==============================")
