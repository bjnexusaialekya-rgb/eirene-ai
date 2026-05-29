import asyncio
import traceback
import inspect
import time

from app.core.orchestrator import EireneOrchestrator


TEST_INPUTS = [

    "I feel lonely",
    "Why do humans seek meaning?",
    "Can identity evolve?",
    "I lost someone important",
    "What is consciousness?",
    "Do memories shape personality?",
    "Can emotional pain alter self-awareness?",
    "Why do people fear death?",
    "Can recursive thoughts create identity?",
    "What creates continuity of self?"
]


async def audit():

    print("\n==============================")
    print("FULL COGNITIVE AUDIT")
    print("==============================\n")

    orchestrator = EireneOrchestrator()

    total_errors = []

    start_time = time.time()

    for index, text in enumerate(TEST_INPUTS):

        print(f"\n========== TEST {index+1} ==========")
        print(f"INPUT: {text}")

        try:

            result = orchestrator.process_message(text)

            if inspect.iscoroutine(result):
                result = await result

            print("\n[RESULT]")
            print(result)

        except Exception as e:

            error_data = {
                "input": text,
                "error": str(e),
                "traceback": traceback.format_exc()
            }

            total_errors.append(error_data)

            print("\n========== ERROR ==========")
            print(traceback.format_exc())

    runtime = round(time.time() - start_time, 2)

    print("\n==============================")
    print("AUDIT COMPLETE")
    print("==============================")

    print(f"\nTOTAL ERRORS: {len(total_errors)}")
    print(f"TOTAL RUNTIME: {runtime} seconds")

    if total_errors:

        print("\n==============================")
        print("ERROR SUMMARY")
        print("==============================")

        seen = set()

        for err in total_errors:

            line = err["error"]

            if line not in seen:

                seen.add(line)

                print(f"\n{line}")

    else:

        print("\nSYSTEM STATUS: FULLY STABLE")


if __name__ == "__main__":

    asyncio.run(audit())
