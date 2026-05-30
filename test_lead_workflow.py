from app.automation.workflows.lead_qualification import (
    LeadQualificationWorkflow
)

workflow = LeadQualificationWorkflow()

lead = """
Owner of a 5-location gym chain.
Interested in AI sales automation.
Budget around $5000.
"""

result = workflow.run(
    lead
)

print(result)
