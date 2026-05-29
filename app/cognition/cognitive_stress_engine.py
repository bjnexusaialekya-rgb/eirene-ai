class CognitiveStressEngine:

    def analyze(
        self,
        recursion_depth,
        dominant_emotion
    ):

        stress = "low"

        if recursion_depth > 5:

            stress = "high"

        elif recursion_depth > 3:

            stress = "moderate"

        return {

            "stress_level":
            stress,

            "dominant_emotion":
            dominant_emotion
        }
