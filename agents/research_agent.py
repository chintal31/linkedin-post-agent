import os
import requests


class ResearchAgent:
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        self.url = "https://api.tavily.com/search"

    def research_topic(self, topic):
        payload = {
            "api_key": self.api_key,
            "query": topic,
            "search_depth": "basic",  # options: "basic", "advanced"
            "include_answer": True,
            "include_images": False,
            "max_results": 5,
        }

        response = requests.post(self.url, json=payload)
        data = response.json()

        # Assemble snippets from results
        snippets = []
        for result in data.get("results", []):
            title = result.get("title", "")
            snippet = result.get("snippet", "")
            snippets.append(f"{title}: {snippet}")

        # Join all snippets into one research text
        research_text = "\n\n".join(snippets)
        return research_text
