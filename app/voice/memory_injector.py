class VoiceMemoryInjector:

    def inject_memory_context(
        self,
        memories
    ):

        return {

            "memory_context_size": len(memories),

            "context_status": "injected"
        }
