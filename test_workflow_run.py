from app.automation.models.workflow_run import WorkflowRun

run = WorkflowRun(
    workflow_id="lead_001",
    workflow_name="Lead Qualification"
)

print(run)
