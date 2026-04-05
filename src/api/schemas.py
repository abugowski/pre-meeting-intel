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
