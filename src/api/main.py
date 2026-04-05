from fastapi import FastAPI
from src.api.schemas import CompanyRequest, CompanyResponse
from src.intelligence.models import CompanyProfile

app = FastAPI()


@app.get("/health")
async def health():
    """Check the health of the API."""
    return {"status": "ok"}


@app.post("/company")
async def post_company(request: CompanyRequest) -> CompanyResponse:
    """Get information about a company by name."""
    profile = await CompanyProfile.create(
        name=request.name, industry=request.industry, country=request.country
    )

    return CompanyResponse(
        name=profile.name,
        country=profile.country,
        industry=profile.industry,
        notes=profile.notes,
        summary=profile.summary(),
    )
