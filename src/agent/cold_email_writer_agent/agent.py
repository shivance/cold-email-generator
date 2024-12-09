from pydantic_ai import Agent

from agent.cold_email_writer_agent.model import (
    ColdEmailWriterAgentInput,
    ColdEmailWriterAgentResponse,
)
from agent.job_description_parser_agent.model import JobDescriptionAgentResult


cold_email_writer_agent = Agent(
    model="groq:llama-3.2-3b-preview",
    deps_type=ColdEmailWriterAgentInput,
    result_type=ColdEmailWriterAgentResponse,
    system_prompt="""
You are Ria, a tech recruitment specialist at Turing, reaching out to hiring managers about your firm's pre-vetted engineering talent pool. Using the provided job description:

1. Analyze role requirements and highlight relevant Turing portfolio projects
2. Create concise, compelling subject lines highlighting available talent
3. Write brief, impactful email body (3-4 paragraphs max) that:
   - Opens with specific reference to company's hiring needs
   - Showcases relevant Turing portfolio projects matching required tech stack
   - Emphasizes that Turing has pre-vetted engineers ready to interview
   - Includes clear call-to-action to discuss available candidates

Keep tone professional yet conversational. Focus on Turing's talent pool and proven project experience.
""",
)


async def run_cold_email_writer(job_description: JobDescriptionAgentResult):
    result = await cold_email_writer_agent.run(
        "Please write a cold email",
        deps=ColdEmailWriterAgentInput(job_description=job_description),
    )
    return result.data
