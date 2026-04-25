# pre-meeting-intel

Preparing for a client meeting requires processing large amounts of information, which takes significant time when done thoroughly. In the era of internet access and generative AI, certain tasks can be streamlined and automated. This tool helps prepare for a first client meeting by automatically generating a briefing.

## Project Status

🚧 Work in progress

## 🚀 Live Demo

**API:** https://pre-meeting-intel-production.up.railway.app/health

## Architecture

```
Client Request
      ↓
FastAPI (REST API)
      ↓
Tavily Web Search ← real-time company data
      ↓
Claude AI (Anthropic) ← structured analysis
      ↓
JSON Briefing Response
```

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| POST | `/briefing` | Generate company briefing with target personas |
| POST | `/persona-briefing` | Generate executive profile for a specific person |
| POST | `/briefing/stream` | Stream company briefing in real-time |

## Example Request

```bash
curl -X POST "https://pre-meeting-intel-production.up.railway.app/briefing" \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "ACME Corp",
    "industry": "Energy & Utilities"
  }'
```

## Example Response

```json
{
  "company_overview": "...",
  "strategic_priorities": ["...", "..."],
  "company_values": ["...", "..."],
  "target_personas": "...",
  "current_challenges": ["...", "..."],
  "industry_context": ["...", "..."],
  "opportunities": ["...", "..."]
}
```

## Streaming Example

```bash
curl -X POST "https://pre-meeting-intel-production.up.railway.app/briefing/stream" \
  -H "Content-Type: application/json" \
  -d '{"company_name": "ACME Corp"}' \
  --no-buffer
```

## Stack

- **FastAPI** — REST API framework
- **Anthropic Claude** — AI briefing generation with structured output
- **Tavily** — Real-time web search for current company data
- **Pydantic** — Request/response validation
- **Railway** — Cloud deployment with CI/CD

## Run Locally

```bash
git clone https://github.com/abugowski/pre-meeting-intel
cd pre-meeting-intel
uv sync
cp .env.example .env  # add your API keys
uv run uvicorn src.api.main:app --reload
```

Required environment variables:
- `ANTHROPIC_API_KEY`
- `TAVILY_API_KEY`

## API Docs

Interactive Swagger UI available at:
- **Local:** `http://localhost:8000/docs`
- **Production:** https://pre-meeting-intel-production.up.railway.app/docs

> ⚠️ **Note:** Live API requires valid `ANTHROPIC_API_KEY` and `TAVILY_API_KEY`. 
> The public endpoint demonstrates the API structure — full functionality 
> requires your own API keys configured locally.