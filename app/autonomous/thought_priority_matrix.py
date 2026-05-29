class ThoughtPriorityMatrix:

    def prioritize(
        self,
        thoughts
    ):

        return sorted(
            thoughts,
            key=lambda x: len(str(x)),
            reverse=True
        )
