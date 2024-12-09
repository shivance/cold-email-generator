# Tool Input
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel, Field


@dataclass
class JobInformationFetchDeps:
    job_post_url: str


# Tool Output - Agent Input
@dataclass
class JobDescriptionAgentDependecies:
    job_posting_information: str


class JobDescriptionAgentResult(BaseModel):
    role: str = Field(
        description="The job title or role position being described (e.g., 'Senior Software Engineer', 'Product Manager')"
    )
    company_name: str = Field(description="The Company which posted job")
    experience: str = Field(
        description="Required years and type of experience for the position (e.g., '5+ years of software development')"
    )
    skills: List[str] = Field(
        description="List of specific technical skills, tools, or competencies required for the role (e.g., ['Python', 'AWS', 'Machine Learning'])"
    )
    description: str = Field(
        description="Detailed overview of the job responsibilities, requirements, and expectations"
    )
