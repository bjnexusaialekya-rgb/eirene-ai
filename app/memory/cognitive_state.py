class CognitiveState:

    def determine_state(

        self,

        dominant_emotion
    ):

        mapping = {

            "sad": "supportive",

            "angry": "calm",

            "fear": "protective",

            "happy": "encouraging",

            "neutral": "balanced"
        }

        return mapping.get(
            dominant_emotion,
            "balanced"
        )