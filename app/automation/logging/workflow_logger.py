
from datetime import datetime
import json


class WorkflowLogger:

    @staticmethod
    def log(
        workflow_id: str,
        workflow_name: str,
        event: str,
        status: str,
        details: dict | None = None
    ):

        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "workflow_id": workflow_id,
            "workflow_name": workflow_name,
            "event": event,
            "status": status,
            "details": details or {}
        }

        print(json.dumps(payload, indent=2))
