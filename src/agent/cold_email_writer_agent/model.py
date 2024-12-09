from pydantic import BaseModel, Field

from agent.job_description_parser_agent.model import JobDescriptionAgentResult


class ColdEmailWriterAgentInput(BaseModel):
    job_description: JobDescriptionAgentResult = Field(
        description="Parsed job posting details including role, company, required experience, skills, and full description"
    )


class ColdEmailWriterAgentResponse(BaseModel):
    subject: str = Field(
        description="Email subject line that captures attention and highlights key value proposition (e.g., 'Experienced Python/ML Engineers Available for Anthropic's AI Initiative')"
    )
    body: str = Field(
        description="Professional email body that matches job requirements with portfolio expertise, includes introduction, value proposition, relevant project examples, and call-to-action"
    )
