import traceback

from app.nlp.sentiment_engine import SentimentEngine
from app.vector_memory.chroma_memory import ChromaMemory
from app.llm.groq_client import GroqClient

from app.memory.memory_manager import MemoryManager
from app.memory.profile_manager import ProfileManager
from app.memory.reflection_engine import ReflectionEngine
from app.memory.memory_decay import MemoryDecayEngine
from app.memory.emotional_reinforcement import EmotionalReinforcement
from app.memory.cognitive_state import CognitiveState
from app.memory.trigger_detector import TriggerDetector
from app.memory.episodic_cluster import EpisodicCluster
from app.memory.conversation_continuity import ConversationContinuity
from app.memory.self_reflection import SelfReflection
from app.memory.consolidation_engine import ConsolidationEngine

from app.personas.adaptive_tone import AdaptiveTone

from app.cognition.emotional_reasoning_engine import EmotionalReasoningEngine
from app.cognition.emotional_forecasting import EmotionalForecasting
from app.cognition.intervention_engine import InterventionEngine
from app.cognition.attachment_model import AttachmentModel
from app.cognition.self_model_engine import SelfModelEngine
from app.cognition.narrative_engine import NarrativeEngine
from app.cognition.meta_awareness_engine import MetaAwarenessEngine
from app.cognition.emotional_drift import EmotionalDrift
from app.cognition.proactive_support import ProactiveSupport
from app.cognition.personality_evolution import PersonalityEvolution
from app.cognition.recursive_awareness import RecursiveAwareness
from app.cognition.identity_engine import IdentityEngine
from app.cognition.goal_engine import GoalEngine
from app.cognition.planning_engine import PlanningEngine
from app.cognition.priority_engine import PriorityEngine

from app.cognition.strategic_reasoning import StrategicReasoning
from app.cognition.meta_cognition import MetaCognition
from app.cognition.decision_engine import DecisionEngine


class EireneOrchestrator:

    def __init__(self):

        self.sentiment_engine = SentimentEngine()

        self.vector_store = ChromaMemory()

        self.groq_client = GroqClient()

        self.memory_manager = MemoryManager()

        self.profile_manager = ProfileManager()

        self.reflection_engine = ReflectionEngine()

        self.memory_decay = MemoryDecayEngine()

        self.emotional_reinforcement = EmotionalReinforcement()

        self.cognitive_state = CognitiveState()

        self.trigger_detector = TriggerDetector()

        self.episodic_cluster = EpisodicCluster()

        self.conversation_continuity = ConversationContinuity()

        self.self_reflection = SelfReflection()

        self.consolidation_engine = ConsolidationEngine()

        self.adaptive_tone = AdaptiveTone()

        self.reasoning_engine = EmotionalReasoningEngine()

        self.forecasting_engine = EmotionalForecasting()

        self.intervention_engine = InterventionEngine()

        self.attachment_model = AttachmentModel()

        self.self_model_engine = SelfModelEngine()

        self.narrative_engine = NarrativeEngine()

        self.meta_awareness_engine = MetaAwarenessEngine()

        self.emotional_drift = EmotionalDrift()

        self.proactive_support = ProactiveSupport()

        self.personality_evolution = PersonalityEvolution()

        self.recursive_awareness = RecursiveAwareness()

        self.identity_engine = IdentityEngine()

        self.goal_engine = GoalEngine()

        self.planning_engine = PlanningEngine()

        self.priority_engine = PriorityEngine()

        self.strategic_reasoning = StrategicReasoning()

        self.meta_cognition = MetaCognition()

        self.decision_engine = DecisionEngine()

    def process_message(
        self,
        user_input,
        user_id="user_1"
    ):

        try:

            # -----------------------------------
            # Emotion detection
            # -----------------------------------

            emotion = self.sentiment_engine.detect_emotion(
                user_input
            )

            print(f"[DEBUG] Emotion: {emotion}")

            # -----------------------------------
            # Store memory
            # -----------------------------------

            self.memory_manager.store_memory(
                user_id=user_id,
                message=user_input,
                emotional_state=emotion
            )

            print("[DEBUG] Memory stored")

            # -----------------------------------
            # Retrieve memories
            # -----------------------------------

            recent_memories = self.memory_manager.get_recent_memories(
                user_id
            )

            postgres_context = "\n".join(
                [
                    memory["memory_text"]
                    for memory in recent_memories
                ]
            )

            print("[DEBUG] PostgreSQL memories retrieved")

            # -----------------------------------
            # Vector memory
            # -----------------------------------

            try:

                vector_memories = self.vector_store.retrieve_memories(
                    user_input
                )

                vector_context = str(
                    vector_memories
                )

                print("[DEBUG] Vector memories retrieved")

            except Exception as e:

                print(f"[VECTOR MEMORY ERROR] {e}")

                traceback.print_exc()

                vector_context = ""

            # -----------------------------------
            # Emotional profile
            # -----------------------------------

            profile = self.profile_manager.build_emotional_profile(
                user_id
            )

            dominant_emotion = profile["dominant_emotion"]

            emotion_distribution = profile["emotion_distribution"]

            print("[DEBUG] Emotional profile built")

            # -----------------------------------
            # Reflection engine
            # -----------------------------------

            reflection = self.reflection_engine.generate_reflection(
                user_id
            )

            print("[DEBUG] Reflection generated")

            # -----------------------------------
            # Reinforcement patterns
            # -----------------------------------

            reinforcement = self.emotional_reinforcement.reinforce(
                recent_memories
            )

            print("[DEBUG] Reinforcement generated")

            # -----------------------------------
            # Trigger detection
            # -----------------------------------

            triggers = self.trigger_detector.detect_triggers(
                recent_memories
            )

            print("[DEBUG] Triggers detected")

            # -----------------------------------
            # Cognitive state
            # -----------------------------------

            cognitive_state = self.cognitive_state.determine_state(
                dominant_emotion
            )

            print(f"[DEBUG] Cognitive state: {cognitive_state}")

            # -----------------------------------
            # Memory decay
            # -----------------------------------

            decay_scores = []

            for memory in recent_memories:

                decay = self.memory_decay.calculate_decay(
                    memory["created_at"]
                )

                decay_scores.append(decay)

            print("[DEBUG] Memory decay calculated")

            # -----------------------------------
            # Episodic clustering
            # -----------------------------------

            episodic_clusters = self.episodic_cluster.cluster_memories(
                recent_memories
            )

            print("[DEBUG] Episodic clustering complete")

            # -----------------------------------
            # Adaptive tone
            # -----------------------------------

            tone_profile = self.adaptive_tone.generate_tone(
                emotion,
                cognitive_state
            )

            print("[DEBUG] Adaptive tone generated")

            # -----------------------------------
            # Continuity engine
            # -----------------------------------

            continuity = self.conversation_continuity.build_context(
                recent_memories
            )

            print("[DEBUG] Continuity built")

            # -----------------------------------
            # Self reflection
            # -----------------------------------

            internal_reflection = self.self_reflection.generate_internal_state(
                dominant_emotion,
                triggers
            )

            print("[DEBUG] Internal reflection generated")

            # -----------------------------------
            # Emotional reasoning
            # -----------------------------------

            reasoning = self.reasoning_engine.analyze(
                dominant_emotion,
                triggers,
                reinforcement
            )

            print("[DEBUG] Emotional reasoning generated")

            # -----------------------------------
            # Forecasting
            # -----------------------------------

            forecast = self.forecasting_engine.predict(
                dominant_emotion,
                reinforcement
            )

            print("[DEBUG] Forecast generated")

            # -----------------------------------
            # Intervention engine
            # -----------------------------------

            intervention = self.intervention_engine.generate_intervention(
                dominant_emotion
            )

            print("[DEBUG] Intervention generated")

            # -----------------------------------
            # Attachment modeling
            # -----------------------------------

            attachment = self.attachment_model.infer_attachment(
                recent_memories
            )

            print("[DEBUG] Attachment modeling complete")

            # -----------------------------------
            # Self model
            # -----------------------------------

            self_model = self.self_model_engine.build_self_model(
                profile,
                triggers,
                reinforcement
            )

            print("[DEBUG] Self model generated")

            # -----------------------------------
            # Narrative engine
            # -----------------------------------

            narrative = self.narrative_engine.build_narrative(
                recent_memories
            )

            print("[DEBUG] Narrative generated")

            # -----------------------------------
            # Meta awareness
            # -----------------------------------

            meta_awareness = self.meta_awareness_engine.generate_meta_awareness(
                dominant_emotion,
                reinforcement
            )

            print("[DEBUG] Meta awareness generated")

            # -----------------------------------
            # Consolidation engine
            # -----------------------------------

            consolidation = self.consolidation_engine.consolidate_memories(
                recent_memories
            )

            print("[DEBUG] Consolidation complete")

            # -----------------------------------
            # Emotional drift
            # -----------------------------------

            drift_analysis = self.emotional_drift.calculate_drift(
                emotion,
                dominant_emotion
            )

            print("[DEBUG] Emotional drift calculated")

            # -----------------------------------
            # Proactive support
            # -----------------------------------

            proactive_support = self.proactive_support.generate_support(
                drift_analysis
            )

            print("[DEBUG] Proactive support generated")

            # -----------------------------------
            # Personality evolution
            # -----------------------------------

            personality_evolution = self.personality_evolution.evolve_personality(
                dominant_emotion,
                reinforcement
            )

            print("[DEBUG] Personality evolution generated")

            # -----------------------------------
            # Recursive awareness
            # -----------------------------------

            recursive_state = self.recursive_awareness.generate_recursive_state(
                reflection,
                narrative,
                meta_awareness
            )

            print("[DEBUG] Recursive awareness generated")

            # -----------------------------------
            # Identity engine
            # -----------------------------------

            identity_state = self.identity_engine.build_identity_state(
                personality_evolution,
                attachment,
                self_model
            )

            print("[DEBUG] Identity state generated")

            # -----------------------------------
            # Goal engine
            # -----------------------------------

            goals = self.goal_engine.generate_goals(
                dominant_emotion,
                reinforcement
            )

            print("[DEBUG] Goal generation complete")

            # -----------------------------------
            # Planning engine
            # -----------------------------------

            planning = self.planning_engine.create_plan(
                goals,
                cognitive_state
            )

            print("[DEBUG] Planning engine complete")

            # -----------------------------------
            # Priority engine
            # -----------------------------------

            priorities = self.priority_engine.prioritize(
                emotion,
                triggers,
                goals
            )

            print("[DEBUG] Priority engine complete")

            # -----------------------------------
            # Strategic reasoning
            # -----------------------------------

            strategy = self.strategic_reasoning.generate_strategy(
                goals,
                priorities,
                cognitive_state
            )

            print("[DEBUG] Strategic reasoning complete")

            # -----------------------------------
            # Meta cognition
            # -----------------------------------

            meta_cognition = self.meta_cognition.analyze_internal_state(
                strategy,
                recursive_state,
                identity_state
            )

            print("[DEBUG] Meta cognition complete")

            # -----------------------------------
            # Decision engine
            # -----------------------------------

            decisions = self.decision_engine.make_decision(
                emotion,
                priorities,
                strategy
            )

            print("[DEBUG] Decision engine complete")

            # -----------------------------------
            # Prompt generation
            # -----------------------------------

            prompt = f"""
You are Eirene, an emotionally intelligent AI companion.

Current detected emotion:
{emotion}

Dominant long-term emotional pattern:
{dominant_emotion}

Emotional distribution:
{emotion_distribution}

Current cognitive state:
{cognitive_state}

Adaptive tone profile:
{tone_profile}

Detected emotional triggers:
{triggers}

Emotional reinforcement patterns:
{reinforcement}

Memory decay analysis:
{decay_scores}

Episodic emotional clusters:
{episodic_clusters}

Persistent emotional memories:
{postgres_context}

Relevant semantic memories:
{vector_context}

Conversation continuity:
{continuity}

Reflection summary:
{reflection}

Internal reflection:
{internal_reflection}

Emotional reasoning:
{reasoning}

Forecasting analysis:
{forecast}

Suggested emotional intervention:
{intervention}

Attachment analysis:
{attachment}

Self-model beliefs:
{self_model}

Narrative understanding:
{narrative}

Meta-awareness analysis:
{meta_awareness}

Memory consolidation:
{consolidation}

Emotional drift analysis:
{drift_analysis}

Proactive support guidance:
{proactive_support}

Personality evolution:
{personality_evolution}

Recursive awareness state:
{recursive_state}

Identity state:
{identity_state}

Emotional goals:
{goals}

Support planning:
{planning}

Cognitive priorities:
{priorities}

Strategic emotional reasoning:
{strategy}

Meta cognition:
{meta_cognition}

Autonomous decisions:
{decisions}

Current user message:
{user_input}

Respond empathetically, intelligently, naturally, and with emotional continuity.
"""

            print("[DEBUG] Prompt built")

            # -----------------------------------
            # Generate response
            # -----------------------------------

            response = self.groq_client.generate_response(
                prompt
            )

            print("[DEBUG] Response generated")

            # -----------------------------------
            # Store semantic memory
            # -----------------------------------

            try:

                self.vector_store.store_memory(
                    user_input
                )

                print("[DEBUG] Semantic memory stored")

            except Exception as e:

                print(f"[VECTOR STORE ERROR] {e}")

                traceback.print_exc()

            return {
                "emotion": emotion,
                "response": response
            }

        except Exception as e:

            print("\n========== ORCHESTRATOR ERROR ==========")

            traceback.print_exc()

            print("========================================\n")

            return {
                "emotion": "unknown",
                "response": "I'm here with you. Something went wrong internally, but I still want to support you."
            }