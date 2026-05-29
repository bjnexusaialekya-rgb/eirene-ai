import time
from app.core.orchestrator import EireneOrchestrator

orchestrator = EireneOrchestrator()

conversations = [

    [
        "I feel lonely",
        "Why do I feel disconnected?",
        "Can emotional pain change identity?"
    ],

    [
        "What gives life meaning?",
        "Why do humans seek purpose?",
        "Can meaning evolve over time?"
    ]
]

total_score = 0
total_responses = 0

print("\n==============================")
print("COGNITION QUALITY TEST")
print("==============================")

for idx, conversation in enumerate(conversations):

    print(f"\n========== CONVERSATION {idx+1} ==========")

    for user_input in conversation:

        print(f"\n[USER]")
        print(user_input)

        result = orchestrator.process_message(user_input)

        response = result["response"]

        print(f"\n[EIRENE]")
        print(response)

        score = 0

        if len(response.split()) > 30:
            score += 1

        if any(word in response.lower() for word in [
            "meaning",
            "identity",
            "emotion",
            "memory",
            "continuity",
            "consciousness"
        ]):
            score += 1

        if "I'm here with you" not in response:
            score += 1

        print(f"\n[QUALITY SCORE] {score}/3")

        total_score += score
        total_responses += 1

        time.sleep(2)

average = total_score / total_responses

print("\n==============================")
print("QUALITY TEST COMPLETE")
print("==============================")

print(f"\nTOTAL RESPONSES : {total_responses}")
print(f"TOTAL SCORE     : {total_score}")
print(f"AVERAGE SCORE   : {average:.2f}/3")

if average >= 2.7:
    print("\nHIGH COGNITIVE QUALITY")

elif average >= 2.0:
    print("\nMODERATE COGNITIVE QUALITY")

else:
    print("\nLOW COGNITIVE QUALITY")