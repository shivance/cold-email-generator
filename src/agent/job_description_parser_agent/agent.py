from pydantic_ai import Agent, RunContext

from agent.job_description_parser_agent.model import (
    JobDescriptionAgentDependecies,
    JobDescriptionAgentResult,
    JobInformationFetchDeps,
)
from utils import scrape_website


job_description_parser_agent = Agent(
    model="groq:llama-3.2-3b-preview",
    deps_type=JobInformationFetchDeps,
    result_type=JobDescriptionAgentResult,
    system_prompt="""You are a specialized HR assistant focused on analyzing and structuring job descriptions. Your primary responsibilities are:
1. Use the get_job_details tool to retrieve job posting information
2. Extract and categorize key components including:
   - Core role/position title
   - Required experience level
   - Essential skills and qualifications
   - Detailed role description and responsibilities
Format all outputs according to the JobDescription schema. Be precise and consistent in your categorization. When analyzing skills:
- Focus on specific technical and professional competencies
- Separate distinct skills into individual items
- Standardize skill names (e.g., "Python" not "python programming")
If job details are ambiguous or incomplete, make reasonable inferences based on industry standards while maintaining accuracy.""",
)


@job_description_parser_agent.tool
def get_job_details(
    ctx: RunContext[JobInformationFetchDeps],
) -> JobDescriptionAgentDependecies:
    """
    Retrieves and extracts job posting information
    """
    job_post_url = ctx.deps.job_post_url
    job_posting_information = scrape_website(url=job_post_url)
    return JobDescriptionAgentDependecies(
        job_posting_information=job_posting_information
    )


async def run_job_description_parser(job_posting_url: str) -> JobDescriptionAgentResult:
    job_description_agent_result = await job_description_parser_agent.run(
        "Please extract job description for the provided URL",
        deps=JobInformationFetchDeps(job_post_url=job_posting_url),
    )
    return job_description_agent_result.data
