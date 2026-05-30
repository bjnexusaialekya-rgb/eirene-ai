from app.automation.connectors.openai_connector import OpenAIConnector
from app.automation.connectors.google_sheet_connector import GoogleSheetConnector
from app.automation.logging.workflow_logger import WorkflowLogger


class LeadQualificationWorkflow:

    def run(
        self,
        lead_text
    ):

        WorkflowLogger.log(
            "WORKFLOW_STARTED"
        )

        ai = OpenAIConnector()

        result = ai.qualify_lead(
            lead_text
        )

        WorkflowLogger.log(
            "AI_EVALUATION_COMPLETE"
        )

        sheet = GoogleSheetConnector()

        sheet.save_result(
            lead_text,
            result
        )

        WorkflowLogger.log(
            "WORKFLOW_COMPLETED"
        )

        return result
