class ToneAdapter:

    def __init__(self):

        self.tone_rules = {

            "reassuring": {
                "sentence_style": "gentle",
                "response_pacing": "slow",
                "emotion_level": "warm"
            },

            "supportive": {
                "sentence_style": "empathetic",
                "response_pacing": "moderate",
                "emotion_level": "caring"
            },

            "calm": {
                "sentence_style": "stable",
                "response_pacing": "controlled",
                "emotion_level": "neutral"
            },

            "enthusiastic": {
                "sentence_style": "energetic",
                "response_pacing": "fast",
                "emotion_level": "high"
            },

            "professional": {
                "sentence_style": "clear",
                "response_pacing": "balanced",
                "emotion_level": "controlled"
            }
        }

    def adapt_tone(self, tone):

        return self.tone_rules.get(
            tone,
            self.tone_rules["professional"]
        )


if __name__ == "__main__":

    adapter = ToneAdapter()

    result = adapter.adapt_tone("reassuring")

    print(result)