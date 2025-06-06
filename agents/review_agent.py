import os
from openai import OpenAI


class ReviewAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
        )
        self.model = "llama3-8b-8192"

    def review_post(self, draft_post):
        print("\n=== Post Review ===")
        print(f"\nCurrent draft post:\n{draft_post}")

        is_perfect = input("\nIs this post perfect? (yes/no): ").lower().strip()

        if is_perfect == "yes":
            print("\nGreat! Keeping the post as is.")
            return draft_post

        print("\nWhat would you like to do?")
        print("1. Add new points")
        print("2. Remove points")
        print("3. Provide general suggestions")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            new_points = input(
                "\nPlease enter the new points to add (one per line, press Enter twice to finish):\n"
            )
            points = []
            while new_points:
                points.append(new_points)
                new_points = input()
            draft_post += "\n\n" + "\n".join(points)

        elif choice == "2":
            print("\nCurrent points:")
            points = draft_post.split("\n")
            for i, point in enumerate(points, 1):
                print(f"{i}. {point}")

            to_remove = input(
                "\nEnter the numbers of points to remove (comma-separated): "
            ).strip()
            indices = [int(x.strip()) - 1 for x in to_remove.split(",")]
            points = [p for i, p in enumerate(points) if i not in indices]
            draft_post = "\n".join(points)

        elif choice == "3":
            suggestions = input("\nPlease provide your suggestions for improvement:\n")
            prompt = self.generate_polish_prompt(draft_post, suggestions)

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500,
            )

            draft_post = response.choices[0].message.content

        print("\n=== Updated Post ===")
        print(draft_post)

        final_ok = input("\nIs this version good to go? (yes/no): ").lower().strip()
        if final_ok != "yes":
            return self.review_post(draft_post)  # Recursively review again

        return draft_post

    def generate_polish_prompt(self, draft_post: str, suggestions: str) -> str:
        prompt = f"""
        You are a professional LinkedIn content editor. Your task is to polish and improve a LinkedIn post based on specific suggestions while maintaining its core message and professional tone.

        Current post:
        {draft_post}

        Improvement suggestions:
        {suggestions}

        Please polish the post by:
        1. Incorporating the suggested improvements
        2. Maintaining a professional and clear tone
        3. Keeping the post concise and focused
        4. Ensuring proper grammar and formatting
        5. Preserving the original message and key points

        Return only the polished post without any explanations or additional text.
        """
        return prompt.strip()
