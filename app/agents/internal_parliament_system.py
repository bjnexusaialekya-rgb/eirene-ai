class InternalParliamentSystem:

    def __init__(self):

        self.active_agents = [

            "empathy_agent",

            "logic_agent",

            "protective_agent",

            "reflective_agent"
        ]

    def run_parliament(

        self,

        user_input,

        emotional_state=None
    ):

        return {

            "active_agents": self.active_agents,

            "dominant_voice": "empathy_agent",

            "emotional_context": emotional_state,

            "processed_input": str(user_input)
        }
