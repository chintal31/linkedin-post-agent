import os
from openai import OpenAI


class WritingAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
        )
        self.model = "llama3-8b-8192"

    def generate_post(self, topic, research):
        prompt = f"""
        You are a professional LinkedIn content writer.

        Topic: {topic}

        Background Research:
        {research}

        Write an engaging, clear, professional LinkedIn post (~200 words). Use short paragraphs and line breaks.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content
