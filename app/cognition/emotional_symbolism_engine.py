class EmotionalSymbolismEngine:

    def generate(
        self,
        dominant_emotion
    ):

        symbolism = {

            "sadness": "rain",

            "fear": "storm",

            "joy": "sunlight",

            "burnout": "ashes"
        }

        return {

            "symbolism":
            symbolism.get(
                dominant_emotion,
                "ocean"
            )
        }
