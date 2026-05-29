class EmotionVoiceAdapter:

    def adapt_voice(
        self,
        emotion
    ):

        settings = {

            "tone": "calm",

            "speed": "normal",

            "intensity": "moderate"
        }

        if emotion in [
            "sad",
            "burnout",
            "fear"
        ]:

            settings["tone"] = "soft"

            settings["speed"] = "slow"

        if emotion == "angry":

            settings["tone"] = "stable"

            settings["speed"] = "controlled"

        return settings
