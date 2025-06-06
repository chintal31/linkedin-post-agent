# LinkedIn Post Agent

An AI-powered tool that helps create engaging LinkedIn posts by combining research and writing capabilities. The system uses Groq's API to generate professional, well-researched content for your LinkedIn presence.

## Prerequisites

- Python 3.8 or higher
- Groq API key
- Tavily API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/chintal31/linkedin-post-agent.git
cd linkedin-post-agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory using the format of .env.dist

## Usage

1. Run the main script:

```bash
python main.py
```

2. Enter your topic when prompted
3. The system will:
   - Research your topic
   - Generate a professional LinkedIn post
   - Display the draft post
