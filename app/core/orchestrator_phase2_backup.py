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

from app.autonomous.emotional_monitor import EmotionalMonitor
from app.autonomous.thought_scheduler import ThoughtScheduler
from app.autonomous.cognition_loop import CognitionLoop
from app.autonomous.background_reflection import BackgroundReflection
from app.autonomous.self_check_engine import SelfCheckEngine
from app.autonomous.internal_dialogue import InternalDialogue
from app.autonomous.reflection_cycle import ReflectionCycle
from app.autonomous.idle_cognition import IdleCognition
from app.autonomous.emotional_stability import EmotionalStability
from app.autonomous.recursive_thought import RecursiveThought
from app.autonomous.self_awareness_loop import SelfAwarenessLoop
from app.autonomous.concern_engine import ConcernEngine
from app.autonomous.autonomous_thoughts import AutonomousThoughts

from app.beliefs.belief_engine import BeliefEngine
from app.beliefs.value_system import ValueSystem
from app.beliefs.trust_engine import TrustEngine
from app.beliefs.relationship_graph import RelationshipGraph
from app.beliefs.attachment_persistence import AttachmentPersistence

from app.relationships.emotional_dependency import EmotionalDependency
from app.relationships.relational_memory import RelationalMemory
from app.relationships.attachment_evolution import AttachmentEvolution
from app.relationships.trust_continuity import TrustContinuity
from app.relationships.emotional_resonance import EmotionalResonance

from app.agents.empathy_agent import EmpathyAgent
from app.agents.logic_agent import LogicAgent
from app.agents.protective_agent import ProtectiveAgent
from app.agents.reflective_agent import ReflectiveAgent
from app.agents.executive_agent import ExecutiveAgent

from app.voice.realtime_voice import RealtimeVoice
from app.voice.emotion_voice_adapter import EmotionVoiceAdapter
from app.voice.stream_manager import StreamManager
from app.voice.memory_injector import VoiceMemoryInjector
from app.voice.speech_modulator import SpeechModulator
from app.voice.presence_engine import PresenceEngine
from app.voice.interruption_handler import InterruptionHandler


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

        self.emotional_monitor = EmotionalMonitor()

        self.thought_scheduler = ThoughtScheduler()

        self.cognition_loop = CognitionLoop()

        self.background_reflection = BackgroundReflection()

        self.self_check_engine = SelfCheckEngine()

        self.internal_dialogue = InternalDialogue()

        self.reflection_cycle = ReflectionCycle()

        self.idle_cognition = IdleCognition()

        self.emotional_stability = EmotionalStability()

        self.recursive_thought = RecursiveThought()

        self.self_awareness_loop = SelfAwarenessLoop()

        self.concern_engine = ConcernEngine()

        self.autonomous_thoughts = AutonomousThoughts()

        self.belief_engine = BeliefEngine()

        self.value_system = ValueSystem()

        self.trust_engine = TrustEngine()

        self.relationship_graph = RelationshipGraph()

        self.attachment_persistence = AttachmentPersistence()

        self.emotional_dependency = EmotionalDependency()

        self.relational_memory = RelationalMemory()

        self.attachment_evolution = AttachmentEvolution()

        self.trust_continuity = TrustContinuity()

        self.emotional_resonance = EmotionalResonance()

        self.empathy_agent = EmpathyAgent()

        self.logic_agent = LogicAgent()

        self.protective_agent = ProtectiveAgent()

        self.reflective_agent = ReflectiveAgent()

        self.executive_agent = ExecutiveAgent()

        self.realtime_voice = RealtimeVoice()

        self.emotion_voice_adapter = EmotionVoiceAdapter()

        self.stream_manager = StreamManager()

        self.memory_injector = VoiceMemoryInjector()

        self.speech_modulator = SpeechModulator()

        self.presence_engine = PresenceEngine()

        self.interruption_handler = InterruptionHandler()