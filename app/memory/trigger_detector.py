class TriggerDetector:

    def detect_triggers(

        self,

        memories
    ):

        triggers = []

        keywords = [

            "work",
            "relationship",
            "lonely",
            "burnout",
            "stress",
            "family",
            "money"
        ]

        for memory in memories:

            text = memory["memory_text"].lower()

            for keyword in keywords:

                if keyword in text:

                    triggers.append(keyword)

        return list(set(triggers))