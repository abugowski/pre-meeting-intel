import re
from pydantic import BaseModel, Field


class CompanyRequest(BaseModel):
    """Represents a request to create or retrieve a company profile."""

    name: str
    industry: str
    country: str = Field(min_length=2, max_length=2, default="PL")


class CompanyResponse(BaseModel):
    """Represents a response containing company profile information."""

    name: str
    country: str
    industry: str
    notes: str
    summary: str


class BriefingRequest(BaseModel):
    """Represents a request to generate a pre-meeting briefing for a company."""

    company_name: str
    industry: str | None = None
    technology_focus: str | None = None


class PersonaBreifingRequest(BaseModel):
    """Represents a request to generate a pre-meeting briefing for a person."""

    name: str
    position: str | None = None
    bio: str | None = None


class KnowledgeAddRequest(BaseModel):
    """Represents a request to add documents to the knowledge base."""

    documents: list[str]
    ids: list[str]


class KnowledgeQueryRequest(BaseModel):
    """Represents a request to search the knowledge base."""

    query: str
    n_results: int = 3
    max_distance: float = 1.5
