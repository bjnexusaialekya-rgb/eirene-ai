class FailsafeController:

    def protect(self, state):

        if state is None:
            return {
                "failsafe": True
            }

        return {
            "failsafe": False
        }
