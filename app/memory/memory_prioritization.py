class MemoryPrioritization:

    def prioritize(self, memories):

        prioritized = sorted(
            memories,
            key=lambda x: len(str(x)),
            reverse=True
        )

        return prioritized
