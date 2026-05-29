class PresenceEngine:

    def generate_presence(
        self,
        trust_score,
        attachment
    ):

        presence = "supportive"

        if trust_score > 0.8:

            presence = "deeply_present"

        return {

            "presence_mode": presence,

            "attachment": attachment
        }
