from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    """Check the health of the API."""
    return {"status": "ok"}


@app.get("/company/{name}")
async def get_company(name: str):
    """Get information about a company by name."""
    return {"company": name, "status": "placeholder"}
