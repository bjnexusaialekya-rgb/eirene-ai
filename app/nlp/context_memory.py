class ContextMemory:

    def __init__(self):

        self.conversation_history = []

    def store_interaction(
        self,
        user_message,
        emotion,
        tone
    ):

        interaction = {

            "user_message": user_message,
            "emotion": emotion,
            "tone": tone
        }

        self.conversation_history.append(interaction)

    def get_last_interaction(self):

        if len(self.conversation_history) == 0:
            return None

        return self.conversation_history[-1]

    def get_full_history(self):

        return self.conversation_history


if __name__ == "__main__":

    memory = ContextMemory()

    memory.store_interaction(
        user_message="I feel emotionally exhausted.",
        emotion="fear",
        tone="reassuring"
    )

    memory.store_interaction(
        user_message="I am struggling to focus.",
        emotion="sadness",
        tone="supportive"
    )

    print(memory.get_last_interaction())

    print()

    print(memory.get_full_history())