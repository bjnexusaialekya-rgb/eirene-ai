class InternalWorldModel:

    def build_world_model(
        self,
        dominant_emotion,
        beliefs,
        narrative,
        goals
    ):

        if dominant_emotion in [
            "burnout",
            "sadness"
        ]:

            worldview = (
                "The world currently feels emotionally demanding and heavy."
            )

        elif dominant_emotion in [
            "fear",
            "anxious"
        ]:

            worldview = (
                "The world feels uncertain and emotionally unpredictable."
            )

        elif dominant_emotion == "joy":

            worldview = (
                "The world feels emotionally expansive and hopeful."
            )

        else:

            worldview = (
                "The world feels emotionally complex and evolving."
            )

        return {

            "worldview": worldview,

            "belief_reference": beliefs,

            "narrative_reference": narrative,

            "goal_reference": goals
        }
