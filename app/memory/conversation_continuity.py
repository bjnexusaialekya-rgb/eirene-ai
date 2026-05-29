class ConversationContinuity:

    def build_context(

        self,

        memories
    ):

        if not memories:

            return "No ongoing emotional continuity detected."

        latest = memories[0]["memory_text"]

        continuity = f"""
The user appears to be continuing an ongoing emotional experience.

Latest emotional context:
{latest}
"""

        return continuity.strip()