from pydantic import BaseModel, Field, field_validator
from src.intelligence.utils import clean_text
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
        logger.info("Converting CompanyProfile to dictionary: {name}", name=self.name)
        return {
            "name": self.name,
            "industry": self.industry,
            "country": self.country,
            "notes": self.notes,
        }

    def summary(self) -> str:
        """Generate a summary of the company profile."""
        logger.info("Generating summary for CompanyProfile: {name}", name=self.name)
        return (
            f"Company: {self.name}\n"
            f"Industry: {self.industry}\n"
            f"Country: {self.country}\n"
            f"Notes: {self.notes}\n"
        )
