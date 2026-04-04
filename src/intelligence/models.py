from pydantic import BaseModel, Field, field_validator
from src.intelligence.utils import clean_text
from src.intelligence.fetcher import fetch_country_data
from loguru import logger


class CompanyProfile(BaseModel):
    """Represents a company profile with relevant information."""

    name: str = Field(min_length=1)
    industry: str
    country: str = Field(min_length=2, max_length=2)
    notes: str

    def model_post_init(self, __context):
        """Log the creation of a new company profile."""
        logger.info(f"Company Profile created: {self.name}")

    @field_validator("name", "industry", "country", "notes")
    @classmethod
    def strip_whitespace(cls, value: str) -> str:
        """Clean whitespace from all string fields."""
        return clean_text(value)

    def to_dict(self) -> dict:
        """Convert the company profile to a dictionary."""
        logger.info(f"Converting CompanyProfile to dictionary: {self.name}")
        return {
            "name": self.name,
            "industry": self.industry,
            "country": self.country,
            "notes": self.notes,
        }

    def summary(self) -> str:
        """Generate a summary of the company profile."""
        logger.info(f"Generating summary for CompanyProfile: {self.name}")
        return (
            f"Company: {self.name}\n"
            f"Industry: {self.industry}\n"
            f"Country: {self.country}\n"
            f"Notes: {self.notes}\n"
        )

    @classmethod
    async def create(cls, name: str, industry: str, country: str) -> "CompanyProfile":
        """Create a new company profile with notes"""
        logger.info(f"Creating CompanyProfile for {name} in {country}.")
        notes = await fetch_country_data(country)
        logger.info(f"Successfully created CompanyProfile for {name}")
        return cls(name=name, industry=industry, country=country, notes=notes)
