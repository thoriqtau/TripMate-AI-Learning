from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def tavily_search(query):
    response = client.search(
        query,
        max_results=5,
        country="Indonesia"
    )

    results = []
    for index,item in enumerate(response['results'], 1):
        title = item.get("title", "Unknown")
        url = item.get("url", "")
        snippet = item.get("content", "").strip()
        # keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{index}. **{title}**\n {url}\n {snippet}\n")
    return "\n\n".join(results)