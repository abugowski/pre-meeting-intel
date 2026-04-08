from fastapi import FastAPI, HTTPException
from src.api.schemas import CompanyRequest, CompanyResponse
from src.intelligence.models import CompanyProfile
from loguru import logger
from src.intelligence.exceptions import APIConnectionError
from src.api.config import Settings

# Logur and log configuration

logger.add("logs/app.log", rotation="1 MB", retention="10 days")


settings = Settings()
app = FastAPI()


@app.get("/health")
async def health():
    """Check the health of the API."""
    return {"status": "ok"}


@app.post("/company")
async def post_company(request: CompanyRequest) -> CompanyResponse:
    """Get information about a company by name."""
    if request.name == "":
        raise HTTPException(status_code=400, detail="Company name cannot be empty")

    try:
        profile = await CompanyProfile.create(
            name=request.name, industry=request.industry, country=request.country
        )
    except APIConnectionError:
        raise HTTPException(status_code=503, detail="External API is unavailable")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return CompanyResponse(
        name=profile.name,
        country=profile.country,
        industry=profile.industry,
        notes=profile.notes,
        summary=profile.summary(),
    )
