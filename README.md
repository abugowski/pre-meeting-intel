# Pre-discovery and Discovery AI Supported Tool

Preparing for a client meeting requires processing large amounts of information,
which takes significant time when done thoroughly. In the era of internet access
and generative AI, certain tasks can be streamlined and automated. This tool
helps prepare for a first client meeting by automatically generating a briefing.

## Project Status

🚧 Work in progress

## How to Run Locally

1. Clone the repository: `git clone https://github.com/abugowski/fde-portfolio`
2. Navigate to the folder: `cd fde-portfolio`
3. Install dependencies: `uv sync`
4. Copy `.env.example` to `.env` and add your API key
5. Run tests: `uv run pytest tests/ -v`

## GitHub

github.com/abugowski/fde-portfolio

## Live Demo

API is deployed and available at:

🚀 **Production URL:** https://pre-meeting-intel.railway.app/

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Check API status |
| `/company` | POST | Generate company profile |

### Test the API

```bash
curl https://https://pre-meeting-intel.railway.app/health
```