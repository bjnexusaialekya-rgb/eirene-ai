from app.guardrails.safety_check import SafetyCheck
from app.nlp.sentiment_engine import SentimentEngine
from app.nlp.emotion_classifier import EmotionClassifier
from app.nlp.empathy_analyzer import EmpathyAnalyzer
from app.nlp.context_memory import ContextMemory
from app.personas.persona_manager import PersonaManager
from app.nlp.tone_adapter import ToneAdapter
from app.llm.groq_client import GroqClient
from app.database.memory_db import MemoryDatabase
from app.vector_memory.chroma_memory import ChromaMemory

import uuid


class EireneOrchestrator:

    def __init__(self):

        self.safety = SafetyCheck()

        self.sentiment = SentimentEngine()

        self.emotion = EmotionClassifier()

        self.empathy = EmpathyAnalyzer()

        self.memory = ContextMemory()

        self.persona = PersonaManager()

        self.tone_adapter = ToneAdapter()

        self.llm = GroqClient()

        self.database = MemoryDatabase()

        self.chroma = ChromaMemory()

    def process_user_message(self, user_message):

        safety_result = self.safety.validate_response(
            user_message
        )

        if not safety_result["safe"]:

            return {
                "status": "blocked",
                "reason": safety_result["reason"]
            }

        sentiment_result = self.sentiment.analyze_sentiment(
            user_message
        )

        emotion_result = self.emotion.classify_emotion(
            user_message
        )

        empathy_result = self.empathy.analyze_response_strategy(
            emotion_result
        )

        tone_result = self.tone_adapter.adapt_tone(
            empathy_result["tone"]
        )

        self.memory.store_interaction(

            user_message=user_message,

            emotion=empathy_result["emotion"],

            tone=empathy_result["tone"]
        )

        persona_prompt = self.persona.build_persona_prompt(

            emotion=empathy_result["emotion"],

            tone=empathy_result["tone"]
        )

        relevant_memories = self.chroma.retrieve_memories(
            query=user_message
        )

        final_prompt = f"""

{persona_prompt}

Relevant Emotional Memories:
{relevant_memories}

User Message:
{user_message}

Generate a natural emotionally supportive response.
"""

        llm_response = self.llm.generate_response(
            final_prompt
        )

        self.database.store_memory(

            user_message=user_message,

            ai_reply=llm_response,

            sentiment=sentiment_result["label"],

            emotion=empathy_result["emotion"],

            tone=empathy_result["tone"]
        )

        memory_id = str(uuid.uuid4())

        combined_memory = f"""

User:
{user_message}

AI:
{llm_response}

Emotion:
{empathy_result['emotion']}
"""

        self.chroma.store_memory(

            memory_id=memory_id,

            text=combined_memory
        )

        return {

            "sentiment": sentiment_result,

            "emotion": emotion_result,

            "empathy_strategy": empathy_result,

            "tone_configuration": tone_result,

            "persona_prompt": persona_prompt,

            "reply": llm_response,

            "relevant_memories": relevant_memories
        }


if __name__ == "__main__":

    orchestrator = EireneOrchestrator()

    result = orchestrator.process_user_message(
        "I feel emotionally exhausted and anxious."
    )

    print(result)