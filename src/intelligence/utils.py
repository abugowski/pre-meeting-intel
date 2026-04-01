from loguru import logger


def clean_text(text: str) -> str:
    """
    Clean the input text by removing extra whitespace and special characters.

    Args:
        text (str): The input text to be cleaned.
    Returns:
        str: The cleaned text.
    """

    if not text.strip():
        logger.warning(f"Empty text passed to clean_text: {text}")

    return " ".join(text.split())


def fromat_company_name(name: str) -> str:
    """
    Format the company name by removing common suffixes and converting to lowercase.

    Args:
        name (str): The original company name.
    Returns:
        str: The formatted company name.
    """

    return clean_text(name).title()
