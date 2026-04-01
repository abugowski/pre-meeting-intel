import os
from loguru import logger
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Loguru configuration
logger.add("logs/app.log")
