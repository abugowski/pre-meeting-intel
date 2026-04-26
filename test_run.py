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
# import asyncio
# from src.intelligence.search import search_company


# async def main():
#     results = await search_company("Orlen")
#     # content = results["results"][0]["content"]
#     print(results)


# asyncio.run(main())

# # Voyageai

# from src.intelligence.embeddings import embed_text

# result = embed_text("Orlen is a Polish energy company")
# print(type(result))
# print(len(result))
# print(result[:5])

# Tests ChromaDb
from src.intelligence.vector_store import add_documents, search

# Przykładowe tickety z systemu zgłoszeń
tickets = [
    "Ticket #001: System SAP nie uruchamia się po aktualizacji. Użytkownik zgłasza błąd 500. Rozwiązanie: restart serwisu aplikacyjnego i wyczyszczenie cache.",
    "Ticket #002: Użytkownik nie może zalogować się do portalu klienta. Hasło wygasło. Rozwiązanie: reset hasła przez administratora AD.",
    "Ticket #003: Drukarka w dziale finansowym nie drukuje. Brak papieru i zacięcie. Rozwiązanie: uzupełnienie papieru i usunięcie zacięcia.",
    "Ticket #004: Email nie działa od rana. Serwer Exchange niedostępny. Rozwiązanie: restart serwisu Exchange i sprawdzenie certyfikatów.",
    "Ticket #005: Baza danych Oracle bardzo wolno odpowiada. Problem z indeksami. Rozwiązanie: przebudowanie indeksów i analiza query execution plan.",
    "Ticket #006: VPN nie łączy się z biurem. Certyfikat wygasł. Rozwiązanie: odnowienie certyfikatu VPN i restart klienta.",
    "Ticket #007: Aplikacja CRM zawiesza się przy exporcie raportu. Problem z pamięcią. Rozwiązanie: zwiększenie heap size JVM do 4GB.",
    "Ticket #008: Backup nie wykonał się w nocy. Dysk zapasowy pełny. Rozwiązanie: usunięcie starych backupów i rozszerzenie przestrzeni dyskowej.",
]

ids = [f"ticket_{i:03d}" for i in range(1, len(tickets) + 1)]

print("Dodawanie ticketów do ChromaDB...")
add_documents(tickets, ids)
print(f"Dodano {len(tickets)} ticketów.\n")

# Testowe zapytania
queries = [
    "problem z logowaniem użytkownika",
    "serwer nie działa",
    "brak miejsca na dysku",
]

for query in queries:
    print(f"Zapytanie: '{query}'")
    results = search(query, n_results=2)
    for i, result in enumerate(results, 1):
        print(f"  Wynik {i}: {result[:80]}...")
    print()
