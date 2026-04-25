from fastapi import FastAPI, HTTPException
from starlette.responses import StreamingResponse
from src.api.schemas import (
    BriefingRequest,
    CompanyRequest,
    CompanyResponse,
    PersonaBreifingRequest,
)
from src.intelligence.models import CompanyProfile
from src.intelligence.briefing import (
    generate_briefing,
    generate_persona_briefing,
    stream_briefing,
    BriefingResponse,
    PersonaBriefingResponse,
)
from loguru import logger
from src.intelligence.exceptions import APIConnectionError
from src.api.config import settings
from dotenv import load_dotenv

load_dotenv()
# Logur and log configuration

logger.add("logs/app.log", rotation="1 MB", retention="10 days")

app = FastAPI(docs_url="/docs", redoc_url="/redoc")


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


@app.post("/briefing")
async def post_briefing(request: BriefingRequest) -> BriefingResponse:
    """Generate a pre-meeting briefing for a company."""
    if request.company_name == "":
        raise HTTPException(status_code=400, detail="Company name cannot be empty")
    try:
        briefing = await generate_briefing(
            company_name=request.company_name,
            industry=request.industry,
            technology_focus=request.technology_focus,
        )
    except APIConnectionError:
        raise HTTPException(status_code=503, detail="External API is unavailable")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return BriefingResponse(
        company_overview=briefing.company_overview,
        strategic_priorities=briefing.strategic_priorities,
        company_values=briefing.company_values,
        target_personas=briefing.target_personas,
        current_challenges=briefing.current_challenges,
        industry_context=briefing.industry_context,
        opportunities=briefing.opportunities,
    )


@app.post("/persona-briefing")
async def post_persona_briefing(
    request: PersonaBreifingRequest,
) -> PersonaBriefingResponse:
    """
    Generate a persona-based briefing for the given persona.
    Args:
        request (PersonaBreifingRequest): The request object containing the persona details.
    Returns:
        PersonaBreifingResponse: The response object containing the generated persona-based briefing.
    """

    if request.name == "":
        raise HTTPException(status_code=400, detail="Persona name cannot be empty")
    try:
        persona = await generate_persona_briefing(
            name=request.name,
            position=request.position,
            bio=request.bio,
        )
    except APIConnectionError:
        raise HTTPException(status_code=503, detail="External API is unavailable")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

    return PersonaBriefingResponse(
        persona_overview=persona.persona_overview,
        strategic_priorities=persona.strategic_priorities,
        talking_points=persona.talking_points,
        risk_flags=persona.risk_flags,
    )


@app.post("/briefing/stream")
async def post_stream_briefing(request: BriefingRequest) -> StreamingResponse:
    """
    Stream a briefing based on the provided request.
    """
    if request.company_name == "":
        raise HTTPException(status_code=400, detail="Company name cannot be empty")
    try:
        return StreamingResponse(
            stream_briefing(
                company_name=request.company_name,
                industry=request.industry,
                technology_focus=request.technology_focus,
            ),
            media_type="text/plain",
        )
    except APIConnectionError:
        raise HTTPException(status_code=503, detail="External API is unavailable")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
