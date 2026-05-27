class EmpathyAnalyzer:

    def __init__(self):

        self.response_strategies = {

            "fear": {
                "tone": "reassuring",
                "approach": "de-escalation"
            },

            "anger": {
                "tone": "calm",
                "approach": "diffusion"
            },

            "sadness": {
                "tone": "supportive",
                "approach": "comfort"
            },

            "joy": {
                "tone": "enthusiastic",
                "approach": "engagement"
            },

            "neutral": {
                "tone": "professional",
                "approach": "guidance"
            },

            "surprise": {
                "tone": "clarifying",
                "approach": "orientation"
            },

            "disgust": {
                "tone": "careful",
                "approach": "recovery"
            }
        }

    def analyze_response_strategy(self, emotion_result):

        primary_emotion = emotion_result[0]["label"]

        strategy = self.response_strategies.get(
            primary_emotion,
            {
                "tone": "professional",
                "approach": "guidance"
            }
        )

        return {
            "emotion": primary_emotion,
            "tone": strategy["tone"],
            "approach": strategy["approach"]
        }


if __name__ == "__main__":

    sample_emotion = [
        {
            "label": "fear",
            "score": 0.99
        }
    ]

    analyzer = EmpathyAnalyzer()

    result = analyzer.analyze_response_strategy(sample_emotion)

    print(result)