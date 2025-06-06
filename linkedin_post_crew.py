from agents.writing_agent import WritingAgent
from agents.research_agent import ResearchAgent


class LinkedInPostCrew:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
        # self.posting_agent = PostingAgent()

    def run(self, topic):
        print("Step 1: Researching topic...")
        research = self.research_agent.research_topic(topic)

        print("Step 2: Generating draft post...")
        draft_post = self.writing_agent.generate_post(topic, research)

        # print("Step 3: Posting to LinkedIn...")
        # status, response = self.posting_agent.post_to_linkedin(final_post)

        # print(f"Post status: {status}")
        print("Draft post: ", draft_post)
