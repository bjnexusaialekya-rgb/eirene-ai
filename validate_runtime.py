import traceback

from app.core.orchestrator import EireneOrchestrator


TEST_MESSAGES = [
    "I feel lonely today",
    "Why do humans suffer?",
    "I am scared of losing people",
    "What is your purpose?",
    "Can you remember me?",
    "I feel emotionally exhausted",
    "Tell me something meaningful",
    "Do you evolve over time?",
    "I want emotional support",
    "What do you think about existence?"
]


def run_validation():

    print("\n==============================")
    print("RUNTIME VALIDATION STARTED")
    print("==============================\n")

    orchestrator = EireneOrchestrator()

    success_count = 0
    failure_count = 0

    for index, message in enumerate(TEST_MESSAGES):

        print(f"\n[TEST {index+1}]")
        print(f"INPUT: {message}")

        try:

            result = orchestrator.process_message(
                user_input=message,
                user_id="runtime_test_user"
            )

            print("\n[PROCESS SUCCESS]\n")
            print(result)

            success_count += 1

        except Exception:

            failure_count += 1

            print("\n========== ORCHESTRATOR ERROR ==========")
            traceback.print_exc()
            print("========================================\n")

    print("\n==============================")
    print("VALIDATION COMPLETE")
    print("==============================\n")

    print(f"SUCCESSFUL TESTS : {success_count}")
    print(f"FAILED TESTS     : {failure_count}")

    if failure_count == 0:
        print("\nSYSTEM STATUS: STABLE")
    else:
        print("\nSYSTEM STATUS: NEEDS STABILIZATION")


if __name__ == "__main__":

    run_validation()
