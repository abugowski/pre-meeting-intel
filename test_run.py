# from src.intelligence.contact import Contact
# import src.intelligence.config as config  # noqa: F401


# c = Contact(
#     first_name="Jan", last_name="Kowalski", role="TCO", email="jan.kowalski@example.com"


import src.intelligence.config  # noqa: F401
import asyncio
from src.intelligence.fetcher import fetch_country_data

result = asyncio.run(fetch_country_data("PL"))
print(result)
