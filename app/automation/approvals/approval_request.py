from dataclasses import dataclass
from datetime import datetime


@dataclass
class ApprovalRequest:

    approval_id: str

    workflow_id: str

    workflow_name: str

    status: str = "PENDING"

    created_at: datetime = datetime.utcnow()

    approved_by: str | None = None

    notes: str | None = None
