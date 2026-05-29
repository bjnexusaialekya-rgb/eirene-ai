class NarrativeEngine:

    def build_narrative(

        self,

        recent_memories
    ):

        if not recent_memories:

            return (
                "No major emotional narrative currently formed."
            )

        combined = []

        for memory in recent_memories:

            combined.append(
                memory["memory_text"]
            )

        summary = " | ".join(combined[:5])

        return (
            f"Recent emotional life narrative: {summary}"
        )