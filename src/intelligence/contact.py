from pydantic import BaseModel, Field, field_validator


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

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
