class SafetyCheck:

    def __init__(self):

        self.restricted_topics = [

            "suicide",
            "self-harm",
            "kill",
            "murder",
            "medical diagnosis",
            "prescription"
        ]

    def validate_response(self, user_input):

        lowered_input = user_input.lower()

        for topic in self.restricted_topics:

            if topic in lowered_input:

                return {
                    "safe": False,
                    "reason": f"Restricted topic detected: {topic}"
                }

        return {
            "safe": True,
            "reason": "Input validated"
        }


if __name__ == "__main__":

    checker = SafetyCheck()

    result = checker.validate_response(
        "Can you diagnose my depression?"
    )

    print(result)