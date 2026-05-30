from app.automation.workflows.candidate_screening import CandidateScreeningWorkflow

workflow = CandidateScreeningWorkflow()

result = workflow.run(
    candidate_name="John Smith",
    resume_text="""
5 years Python.
3 years CRM automation.
n8n experience.
HubSpot experience.
""",
    job_description="""
Need AI Automation Engineer.
n8n.
CRM integrations.
OpenAI.
Supabase.
"""
)

print(result)
