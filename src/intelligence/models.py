from pydantic import BaseModel, Field, field_validator
from src.intelligence.utils import clean_text


class CompanyProfile(BaseModel):
    name: str = Field(min_length=1)
    industry: str
    country: str = Field(min_length=2, max_length=2)
    notes: str

    @field_validator("name", "industry", "country", "notes")
    @classmethod
    def stripe_whitespace(cls, value: str) -> str:
        return clean_text(value)

    def to_dict(self):
        return {
            "name": self.name,
            "industry": self.industry,
            "country": self.country,
            "notes": self.notes,
        }

    def summary(self):
        return (
            f"Company: {self.name}\n"
            f"Industry: {self.industry}\n"
            f"Country: {self.country}\n"
            f"Notes: {self.notes}\n"
        )
