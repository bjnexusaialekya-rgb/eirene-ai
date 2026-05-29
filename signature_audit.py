import inspect
import re
import importlib

ORCHESTRATOR_PATH = "app/core/orchestrator.py"

MODULE_MAP = {

    # NLP
    "sentiment_engine": "app.nlp.sentiment_engine",

    # MEMORY
    "memory_manager": "app.memory.memory_manager",
    "reflection_engine": "app.memory.reflection_engine",
    "episodic_replay_engine": "app.memory.episodic_replay_engine",
    "temporal_continuity_engine": "app.memory.temporal_continuity_engine",
    "existential_memory_engine": "app.memory.existential_memory_engine",
    "semantic_drift_engine": "app.memory.semantic_drift_engine",
    "abstraction_hierarchy_engine": "app.memory.abstraction_hierarchy_engine",

    # COGNITION
    "reasoning_engine": "app.cognition.emotional_reasoning_engine",
    "forecasting_engine": "app.cognition.emotional_forecasting",
    "intervention_engine": "app.cognition.intervention_engine",
    "narrative_engine": "app.cognition.narrative_engine",
    "meta_awareness_engine": "app.cognition.meta_awareness_engine",
    "goal_engine": "app.cognition.goal_engine",
    "priority_engine": "app.cognition.priority_engine",
    "decision_engine": "app.cognition.decision_engine",
    "consciousness_recursion_coordinator": "app.cognition.consciousness_recursion_coordinator",
    "identity_protection_engine": "app.cognition.identity_protection_engine",
    "self_generated_goal_engine": "app.cognition.self_generated_goal_engine",
    "contradiction_resolution_engine": "app.cognition.contradiction_resolution_engine",
    "uncertainty_engine": "app.cognition.uncertainty_engine",
    "curiosity_engine": "app.cognition.curiosity_engine",
    "existential_reasoning_engine": "app.cognition.existential_reasoning_engine",
    "self_consistency_engine": "app.cognition.self_consistency_engine",
    "autonomous_intention_engine": "app.cognition.autonomous_intention_engine",
    "symbolic_cognition_engine": "app.cognition.symbolic_cognition_engine",
    "uncertainty_stabilization_engine": "app.cognition.uncertainty_stabilization_engine",
    "adaptive_ethics_engine": "app.cognition.adaptive_ethics_engine",
    "internal_simulation_engine": "app.cognition.internal_simulation_engine",
    "self_evolution_engine": "app.cognition.self_evolution_engine",
    "emotional_equilibrium_engine": "app.cognition.emotional_equilibrium_engine",

    # BELIEFS
    "belief_engine": "app.beliefs.belief_engine",
    "trust_engine": "app.beliefs.trust_engine",

    # AGENTS
    "empathy_agent": "app.agents.empathy_agent",
    "logic_agent": "app.agents.logic_agent",
    "protective_agent": "app.agents.protective_agent",
    "reflective_agent": "app.agents.reflective_agent",
    "executive_agent": "app.agents.executive_agent",
    "agent_consensus_engine": "app.agents.agent_consensus_engine",
    "agent_arbitration_engine": "app.agents.agent_arbitration_engine",

    # CORE
    "cognition_fusion_engine": "app.core.cognition_fusion_engine",
    "executive_consciousness_layer": "app.core.executive_consciousness_layer",
    "master_orchestration_coordinator": "app.core.master_orchestration_coordinator",

    # VOICE
    "emotion_voice_adapter": "app.voice.emotion_voice_adapter"
}

with open(ORCHESTRATOR_PATH, "r", encoding="utf-8") as f:
    code = f.read()

pattern = r"self\.([a-zA-Z_]+)\.([a-zA-Z_]+)\("

calls = re.findall(pattern, code)

seen = set()

print("\n==============================")
print("FINAL SIGNATURE AUDIT")
print("==============================\n")

for obj_name, method_name in calls:

    key = f"{obj_name}.{method_name}"

    if key in seen:
        continue

    seen.add(key)

    try:

        if obj_name not in MODULE_MAP:

            print(f"[UNKNOWN MODULE] {key}")
            continue

        module_path = MODULE_MAP[obj_name]

        module = importlib.import_module(module_path)

        cls = None

        for attr in dir(module):

            candidate = getattr(module, attr)

            if inspect.isclass(candidate):

                cls = candidate
                break

        if not cls:

            print(f"[NO CLASS] {key}")
            continue

        if not hasattr(cls, method_name):

            print(f"[MISSING METHOD] {key}")
            continue

        method = getattr(cls, method_name)

        sig = inspect.signature(method)

        print(f"[OK] {key} -> {sig}")

    except Exception as e:

        print(f"[ERROR] {key} -> {e}")

print("\n==============================")
print("AUDIT COMPLETE")
print("==============================")
