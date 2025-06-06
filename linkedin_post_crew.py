from agents.writing_agent import WritingAgent
from agents.research_agent import ResearchAgent
from agents.review_agent import ReviewAgent


class LinkedInPostCrew:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
        self.review_agent = ReviewAgent()
        # self.posting_agent = PostingAgent()

    def run(self, topic, is_browser=False):
        print("Step 1: Researching topic...")
        research = self.research_agent.research_topic(topic)

        print("Step 2: Generating draft post...")
        draft_post = self.writing_agent.generate_post(topic, research)

        print("Step 3: Reviewing post...")
        final_post = self.review_agent.review_post(draft_post, is_browser)

        print("Final post: ", final_post)

        return final_post
