from app.automation.approvals.approval_manager import ApprovalManager

manager = ApprovalManager()

request = manager.create_approval(
    approval_id="APP001",
    workflow_id="WF001",
    workflow_name="Lead Qualification"
)

print("Initial:", request.status)

manager.approve(
    approval_id="APP001",
    approved_by="Admin"
)

print("Final:", manager.get_status("APP001"))
