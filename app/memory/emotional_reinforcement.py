from collections import Counter


class EmotionalReinforcement:

    def reinforce(

        self,

        memories
    ):

        emotions = [

            memory["emotional_state"]

            for memory in memories
        ]

        counter = Counter(emotions)

        reinforced = {}

        for emotion, count in counter.items():

            reinforced[emotion] = round(
                count / len(memories),
                2
            )

        return reinforced