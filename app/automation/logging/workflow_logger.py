from datetime import datetime


class WorkflowLogger:

    @staticmethod
    def log(event: str, details: str = ""):
        timestamp = datetime.utcnow().isoformat()

        print(
            f"[{timestamp}] "
            f"{event} "
            f"{details}"
        )
