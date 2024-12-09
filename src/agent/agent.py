from agent.cold_email_writer_agent.agent import run_cold_email_writer
from agent.job_description_parser_agent.agent import run_job_description_parser
from agent.cold_email_writer_agent.model import ColdEmailWriterAgentResponse


async def get_cold_email_for_job_url(url: str) -> ColdEmailWriterAgentResponse:
    job_description = await run_job_description_parser(job_posting_url=url)
    cold_email = await run_cold_email_writer(job_description=job_description)

    return cold_email


async def entrypoint(url: str) -> str:
    agent_output = await get_cold_email_for_job_url(url=url)

    return f"Subject: {agent_output.subject}\n\n{agent_output.body}"
