class CognitiveEnergyEngine:

    def calculate(
        self,
        recursion_depth
    ):

        energy = "stable"

        if recursion_depth > 5:

            energy = "depleted"

        return {

            "energy_state":
            energy
        }
