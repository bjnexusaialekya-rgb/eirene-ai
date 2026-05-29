class AttachmentEvolution:

    def evolve_attachment(
        self,
        attachment_style,
        reinforcement
    ):

        evolution = "stable"

        if reinforcement > 0.8:

            evolution = "deepening"

        return {

            "attachment_style": attachment_style,

            "evolution_state": evolution
        }
