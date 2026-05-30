from app.automation.approvals.approval_request import ApprovalRequest


class ApprovalManager:

    def __init__(self):
        self.requests = {}

    def create_approval(
        self,
        approval_id: str,
        workflow_id: str,
        workflow_name: str
    ):

        request = ApprovalRequest(
            approval_id=approval_id,
            workflow_id=workflow_id,
            workflow_name=workflow_name
        )

        self.requests[approval_id] = request

        return request

    def approve(
        self,
        approval_id: str,
        approved_by: str,
        notes: str = ""
    ):

        request = self.requests.get(approval_id)

        if not request:
            raise ValueError("Approval request not found")

        request.status = "APPROVED"
        request.approved_by = approved_by
        request.notes = notes

        return request

    def reject(
        self,
        approval_id: str,
        approved_by: str,
        notes: str = ""
    ):

        request = self.requests.get(approval_id)

        if not request:
            raise ValueError("Approval request not found")

        request.status = "REJECTED"
        request.approved_by = approved_by
        request.notes = notes

        return request

    def get_status(self, approval_id: str):

        request = self.requests.get(approval_id)

        if not request:
            return None

        return request.status
