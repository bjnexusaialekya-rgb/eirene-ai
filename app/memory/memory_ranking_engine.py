class MemoryRankingEngine:

    def rank(
        self,
        memories
    ):

        ranked = sorted(
            memories,
            key=lambda x: len(str(x)),
            reverse=True
        )

        return ranked
