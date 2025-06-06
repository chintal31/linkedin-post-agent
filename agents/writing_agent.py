import os
from openai import OpenAI


class WritingAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
        )
        self.model = "llama3-8b-8192"

    def generate_post(self, topic, research=""):
        prompt = self.generate_linkedin_prompt(topic, research)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content

    def generate_linkedin_prompt(self, topic: str, research: str = "") -> str:
        prompt = f"""
            You are a professional LinkedIn content writer. Your task is to write a short, clear, and precise LinkedIn post explaining a software or technical concept in a simple and straightforward way.

            The post should:
            - Be short and to the point (3-4 sentences, max 100-120 words)
            - Use simple language suitable for a broad technical audience, including beginners
            - Include a concise, factual definition or explanation of the concept
            - Highlight up to 3 key practical points or use cases, stated clearly and directly
            - Avoid flowery language, marketing phrases, or vague advice
            - Focus on delivering concrete facts and explanations only
            - Use the given top 3 posts as reference to ensure accuracy and relevance, but write in your own clear style

            Topic: {topic}

            Top 3 posts: {research}

            Write the LinkedIn post accordingly.
        """

        return prompt.strip()
