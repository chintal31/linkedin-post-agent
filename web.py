from flask import Flask, render_template, request, jsonify
from linkedin_post_crew import LinkedInPostCrew
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
crew = LinkedInPostCrew()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_post():
    data = request.get_json()
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    try:
        final_post = crew.run(topic, is_browser=True)
        return jsonify({"post": final_post})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/review", methods=["POST"])
def review_post():
    data = request.get_json()
    draft_post = data.get("draft_post")
    edited_content = data.get("edited_content")
    suggestions = data.get("suggestions")

    if not draft_post:
        return jsonify({"error": "Draft post is required"}), 400

    try:
        final_post = crew.review_agent.review_post(
            draft_post,
            is_browser=True,
            edited_content=edited_content,
            suggestions=suggestions,
        )
        return jsonify({"post": final_post})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
