from app.automation.connectors.openai_connector import OpenAIConnector


class CandidateScreeningWorkflow:

    def run(
        self,
        candidate_name: str,
        resume_text: str,
        job_description: str
    ):

        ai = OpenAIConnector()

        prompt = f"""
You are an AI recruitment specialist.

Evaluate this candidate.

Candidate:
{candidate_name}

Resume:
{resume_text}

Job Description:
{job_description}

Return:

Fit Score (0-100)

Strengths

Weaknesses

Concerns

Suggested Interview Questions
"""

        result = ai.ask(
            prompt,
            "You are a senior recruitment consultant."
        )

        return result
