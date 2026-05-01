from anthropic.types import ToolParam
from anthropic import AsyncAnthropic
from src.api.config import settings
from src.intelligence.search import search_company
from src.intelligence.vector_store import search
from src.intelligence.briefing import generate_briefing

search_web_schema = ToolParam(
    {
        "name": "search_company",
        "description": "Search the web for current, publicly available information about a company. Use this tool when you need up-to-date news, financial data, press releases, or general information about a specific company that may not be in the internal knowledge base.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The full name of the company to search for, e.g. 'Orlen S.A.' or 'Ignitis Group'",
                }
            },
            "required": ["company_name"],
        },
    }
)

search_docs_schema = ToolParam(
    {
        "name": "search_docs",
        "description": "Search the internal knowledge base (ChromaDB) for documents relevant to a query. Use this tool when you need information from previously indexed internal documents, client notes, tickets, or proprietary knowledge that would not be available through web search. Returns the most semantically similar documents to the query.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to find relevant documents, e.g. 'Orlen digital transformation strategy' or 'energy sector cybersecurity challenges'",
                },
                "n_results": {
                    "type": "integer",
                    "description": "Maximum number of documents to return. Defaults to 3.",
                    "default": 3,
                },
            },
            "required": ["query"],
        },
    }
)

get_company_profile_schema = ToolParam(
    {
        "name": "generate_briefing",
        "description": "Generate a comprehensive pre-meeting intelligence briefing for a company. Use this tool when you need a full structured briefing covering company overview, strategic priorities, company values, target personas, current challenges, industry context, and opportunities. This tool combines web search and internal knowledge base to produce an actionable briefing for enterprise sales executives.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The full name of the company to generate a briefing for, e.g. 'Orlen S.A.' or 'Ignitis Group'",
                },
                "industry": {
                    "type": "string",
                    "description": "The industry sector the company operates in, e.g. 'Energy & Utilities' or 'Financial Services'. Optional but improves briefing quality.",
                },
                "technology_focus": {
                    "type": "string",
                    "description": "Specific technology area to focus on in the briefing, e.g. 'AI governance' or 'cloud migration'. Optional.",
                },
            },
            "required": ["company_name"],
        },
    }
)

tools = [search_web_schema, search_docs_schema, get_company_profile_schema]


async def run_agent(query: str, chromadb_client) -> str:
    """Run the specific agent based on the query."""
    client = AsyncAnthropic()
    messages = [{"role": "user", "content": query}]

    while True:
        response = await client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=4000,
            tools=tools,
            messages=messages,
            system=settings.agent_system_prompt,
        )

        if response.stop_reason != "tool_use":
            break

        messages.append({"role": "assistant", "content": response.content})

        tool_requests = [
            block for block in response.content if block.type == "tool_use"
        ]

        for tool_request in tool_requests:
            if tool_request.name == "search_company":
                results = await search_company(tool_request.input["company_name"])
            elif tool_request.name == "search_docs":
                results = search(chromadb_client, tool_request.input["query"])
            elif tool_request.name == "generate_briefing":
                results = await generate_briefing(
                    company_name=tool_request.input["company_name"],
                    chromadb_client=chromadb_client,
                    industry=tool_request.input.get("industry"),
                    technology_focus=tool_request.input.get("technology_focus"),
                )

            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_request.id,
                            "content": str(results)
                            if results
                            else "No relevant documents found",
                            "is_error": False,
                        }
                    ],
                }
            )

    if response.stop_reason == "end_turn":
        for block in response.content:
            if block.type == "text":
                return block.text
