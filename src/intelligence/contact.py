from pydantic import BaseModel, field_validator
from src.intelligence.utils import clean_text


class Contact(BaseModel):
    first_name: str
    last_name: str
    role: str
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value

    @field_validator("first_name", "last_name", "role", "email")
    @classmethod
    def validate_whitespace(cls, value: str) -> str:
        return clean_text(value)

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
