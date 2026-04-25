# from src.intelligence.contact import Contact
# import src.intelligence.config as config  # noqa: F401


# c = Contact(
#     first_name="Jan", last_name="Kowalski", role="TCO", email="jan.kowalski@example.com"


# import intelligence.config_orig  # noqa: F401
# import asyncio
# # from src.intelligence.fetcher import fetch_country_data
# # from src.intelligence.models import CompanyProfile

# # result = asyncio.run(
# #     CompanyProfile.create(name="Example Corp", industry="Technology", country="LT")
# # )
# # print(result)

# from src.intelligence.briefing import generate_briefing

# result = asyncio.run(generate_briefing("Orlen"))
# print(result)

# search.py test
import asyncio
from src.intelligence.search import search_company


async def main():
    results = await search_company("Orlen")
    # content = results["results"][0]["content"]
    print(results)


asyncio.run(main())
