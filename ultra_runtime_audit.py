import asyncio
import traceback
import inspect

from app.core.orchestrator import EireneOrchestrator

TEST_INPUTS = [

    "I feel lonely",
    "Why do humans seek meaning?",
    "Can emotional pain change identity?",
    "Do memories shape personality?",
    "What is consciousness?",
    "Can recursive thoughts evolve self-awareness?",
    "Why does grief persist?",
    "Can attachment survive loss?",
    "What creates continuity of self?",
    "Do you remember previous conversations?"
]


async def run_audit():

    orchestrator = EireneOrchestrator()

    failures = []

    print("\n==============================")
    print("ULTRA RUNTIME AUDIT")
    print("==============================\n")

    for idx, text in enumerate(TEST_INPUTS):

        print(f"\n========== TEST {idx+1} ==========")
        print(f"INPUT: {text}")

        try:

            result = orchestrator.process_message(text)

            if inspect.iscoroutine(result):

                result = await result

            print("\n[RESULT]")
            print(result)

        except Exception as e:

            print("\n========== FAILURE ==========")

            tb = traceback.extract_tb(e.__traceback__)

            final_frame = tb[-1]

            failure = {

                "test": idx + 1,
                "input": text,
                "error_type": type(e).__name__,
                "error": str(e),
                "file": final_frame.filename,
                "line": final_frame.lineno,
                "function": final_frame.name

            }

            failures.append(failure)

            print(f"TYPE: {failure['error_type']}")
            print(f"ERROR: {failure['error']}")
            print(f"FILE: {failure['file']}")
            print(f"LINE: {failure['line']}")
            print(f"FUNCTION: {failure['function']}")

    print("\n==============================")
    print("FINAL FAILURE SUMMARY")
    print("==============================\n")

    if not failures:

        print("NO FAILURES DETECTED")
        print("\nSYSTEM STATUS: ORCHESTRATION STABLE")

    else:

        for f in failures:

            print("--------------------------------")
            print(f"TEST      : {f['test']}")
            print(f"FUNCTION  : {f['function']}")
            print(f"LINE      : {f['line']}")
            print(f"TYPE      : {f['error_type']}")
            print(f"ERROR     : {f['error']}")

        print("\nTOTAL FAILURES:", len(failures))

asyncio.run(run_audit())
