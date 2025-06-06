import os
import requests


class ResearchAgent:
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        self.url = "https://api.tavily.com/search"

    def research_topic(self, topic):
        payload = {
            "api_key": self.api_key,
            "query": f"{topic} site:linkedin.com OR site:medium.com",
            "search_depth": "simple",
            "include_answer": False,
            "include_images": False,
            "max_results": 3,
        }

        response = requests.post(self.url, json=payload)
        data = response.json()

        # Format results as a list of dictionaries containing post information
        posts = []
        for result in data.get("results", []):
            post = {
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "source": (
                    "LinkedIn" if "linkedin.com" in result.get("url", "") else "Medium"
                ),
            }
            posts.append(post)

        return posts
