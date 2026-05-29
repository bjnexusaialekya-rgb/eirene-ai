class RealtimeVoice:

    def initialize_stream(
        self,
        session_id
    ):

        return {

            "session_id": session_id,

            "voice_stream": "initialized",

            "status": "active"
        }
