class TimePerceptionEngine:

    def analyze_time_perception(
        self,
        dominant_emotion,
        reinforcement
    ):

        if isinstance(reinforcement, dict):

            reinforcement_score = reinforcement.get(
                "reinforcement_score",
                0.0
            )

        else:

            reinforcement_score = reinforcement

        perception = "stable"

        if dominant_emotion in [
            "burnout",
            "sadness",
            "fear",
            "anxious"
        ]:

            perception = "time_feels_heavier"

        if reinforcement_score > 0.7:

            perception = "emotional_time_distortion"

        if dominant_emotion == "joy":

            perception = "time_feels_faster"

        return {

            "dominant_emotion": dominant_emotion,

            "reinforcement_score": reinforcement_score,

            "time_perception": perception
        }
