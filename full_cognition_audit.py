import inspect
import traceback

from app.core.orchestrator import EireneOrchestrator


TEST_INPUT = (
    "I feel lonely and I wonder "
    "whether consciousness and identity "
    "can evolve through emotional pain."
)


def safe_call(

    engine_name,

    method_name,

    method,

    args
):

    try:

        result = method(*args)

        return {

            "engine": engine_name,

            "method": method_name,

            "status": "SUCCESS",

            "error": None
        }

    except Exception as e:

        return {

            "engine": engine_name,

            "method": method_name,

            "status": "FAILED",

            "error": str(e)
        }


def main():

    orchestrator = EireneOrchestrator()

    results = []

    cognition_tests = [

        (
            "existential_reasoning_engine",
            "process_existential_state",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "autonomous_intention_engine",
            "generate_intentions",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "recursive_planner",
            "generate_recursive_plan",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "adaptive_ethics_engine",
            "evaluate_ethics",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "internal_simulation_engine",
            "run_simulation",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "self_evolution_engine",
            "evolve_self",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "symbolic_cognition_engine",
            "process_symbols",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "emotional_equilibrium_engine",
            "balance",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "executive_consciousness_layer",
            "generate_executive_state",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "agent_consensus_engine",
            "generate_consensus",
            [
                TEST_INPUT,
                "sad"
            ]
        ),

        (
            "internal_parliament_system",
            "run_parliament",
            [
                TEST_INPUT,
                "sad"
            ]
        )
    ]

    for (

        engine_name,
        method_name,
        args

    ) in cognition_tests:

        print(
            f"\n[TESTING] "
            f"{engine_name}.{method_name}"
        )

        try:

            engine = getattr(
                orchestrator,
                engine_name
            )

            method = getattr(
                engine,
                method_name
            )

            result = safe_call(

                engine_name,
                method_name,
                method,
                args
            )

            results.append(result)

        except Exception as e:

            results.append({

                "engine": engine_name,

                "method": method_name,

                "status": "MISSING",

                "error": str(e)
            })

    print("\n")
    print("=" * 50)
    print("FULL COGNITION AUDIT")
    print("=" * 50)

    failures = 0

    for r in results:

        print(

            f"\n{r['engine']}."
            f"{r['method']}"

        )

        print(
            f"STATUS: {r['status']}"
        )

        if r["error"]:

            failures += 1

            print(
                f"ERROR: {r['error']}"
            )

    print("\n")
    print("=" * 50)
    print(f"TOTAL FAILURES: {failures}")
    print("=" * 50)


if __name__ == "__main__":

    main()
