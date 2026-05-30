from app.automation.logging.workflow_logger import WorkflowLogger

WorkflowLogger.log(
    workflow_id="lead_001",
    workflow_name="Lead Qualification",
    event="WORKFLOW_STARTED",
    status="RUNNING",
    details={
        "lead_name": "Gym Owner"
    }
)
