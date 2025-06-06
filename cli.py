import os
from dotenv import load_dotenv
from linkedin_post_crew import LinkedInPostCrew

load_dotenv()

if __name__ == "__main__":
    topic = input("Enter topic: ")

    crew = LinkedInPostCrew()
    crew.run(topic)
