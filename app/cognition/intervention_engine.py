class InterventionEngine:

    def generate_intervention(

        self,

        dominant_emotion
    ):

        if dominant_emotion == "sad":

            return (
                "Encourage emotional grounding, rest, and supportive reflection."
            )

        if dominant_emotion == "anxious":

            return (
                "Encourage stabilization, slowing down, and reassurance."
            )

        if dominant_emotion == "angry":

            return (
                "Encourage emotional decompression and cognitive reframing."
            )

        return (
            "Maintain emotionally supportive conversational continuity."
        )