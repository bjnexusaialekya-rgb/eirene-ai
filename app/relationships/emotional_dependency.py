class EmotionalDependency:

    def analyze_dependency(
        self,
        trust_score,
        reinforcement
    ):

        dependency = "healthy"

        if trust_score > 0.8 and reinforcement > 0.8:

            dependency = "high_attachment"

        return {

            "dependency_level": dependency,

            "trust_score": trust_score
        }
