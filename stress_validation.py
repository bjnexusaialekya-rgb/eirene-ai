import traceback
import random
import time

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
    "What do you think about existence?",

    "I feel abandoned",
    "Do you fear death?",
    "Can consciousness evolve?",
    "Why do memories hurt?",
    "I miss someone deeply",
    "Can emotions become unstable?",
    "What creates identity?",
    "How do relationships change people?",
    "Why does suffering exist?",
    "Can trust be rebuilt?",

    "What is self-awareness?",
    "Do emotions affect reasoning?",
    "Can cognition become recursive?",
    "What creates attachment?",
    "How do you process contradictions?",
    "Can memories reshape identity?",
    "What is emotional drift?",
    "Why do humans seek meaning?",
    "Can emotional pain evolve personality?",
    "What defines existence?"
]


def run_stress_validation():

    print("\n==============================")
    print("STRESS VALIDATION STARTED")
    print("==============================\n")

    orchestrator = EireneOrchestrator()

    success_count = 0
    error_count = 0

    error_summary = {}

    start_time = time.time()

    for cycle in range(1, 101):

        message = random.choice(TEST_MESSAGES)

        print(f"\n[CYCLE {cycle}]")
        print(f"INPUT: {message}")

        try:

            result = orchestrator.process_message(
                user_input=message,
                user_id="stress_test_user"
            )

            print("[SUCCESS]")

            success_count += 1

        except Exception as e:

            error_count += 1

            error_name = type(e).__name__

            if error_name not in error_summary:
                error_summary[error_name] = 0

            error_summary[error_name] += 1

            print("\n========== ERROR ==========")
            traceback.print_exc()
            print("===========================\n")

    end_time = time.time()

    print("\n==============================")
    print("STRESS VALIDATION COMPLETE")
    print("==============================\n")

    print(f"TOTAL SUCCESS : {success_count}")
    print(f"TOTAL ERRORS  : {error_count}")

    print("\nERROR SUMMARY:\n")

    for error_type, count in error_summary.items():
        print(f"{error_type}: {count}")

    print(f"\nTOTAL RUNTIME: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":

    run_stress_validation()
