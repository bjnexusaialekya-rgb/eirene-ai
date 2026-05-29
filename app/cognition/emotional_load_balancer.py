class EmotionalLoadBalancer:

    def balance(
        self,
        dominant_emotion,
        recursion_depth
    ):

        stabilization = "stable"

        if recursion_depth > 5:

            stabilization = (
                "Reducing recursive emotional overload."
            )

        return {

            "stabilization":
            stabilization,

            "dominant_emotion":
            dominant_emotion
        }
