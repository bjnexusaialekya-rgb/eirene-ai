class InterruptionHandler:

    def process_interruption(
        self,
        interruption_detected
    ):

        return {

            "interruption_detected": interruption_detected,

            "realtime_adjustment": True
        }
