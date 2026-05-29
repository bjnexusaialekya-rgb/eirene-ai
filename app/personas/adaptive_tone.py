class AdaptiveTone:

    def generate_tone(

        self,

        emotion,

        cognitive_state
    ):

        emotion = emotion.lower()

        if emotion in ["sad", "depressed"]:

            return {
                "tone": "gentle",
                "style": "slow_supportive"
            }

        if emotion in ["fear", "anxious"]:

            return {
                "tone": "reassuring",
                "style": "stabilizing"
            }

        if emotion in ["angry"]:

            return {
                "tone": "calm",
                "style": "deescalating"
            }

        if cognitive_state == "protective":

            return {
                "tone": "protective",
                "style": "emotionally_present"
            }

        return {
            "tone": "balanced",
            "style": "natural"
        }