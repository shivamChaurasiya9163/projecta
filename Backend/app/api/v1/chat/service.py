import os
import json
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Path to company.json
KNOWLEDGE_FILE = (
    Path(__file__).resolve().parents[3]
    / "knowledge"
    / "company.json"
)


def load_company_data():
    """
    Reads company knowledge from company.json
    """

    if not KNOWLEDGE_FILE.exists():
        return {}

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def build_system_prompt(company_data):
    """
    Creates the system prompt for GPT.
    """

    return f"""
You are the official AI Assistant of SGenovix Technologies.

Your job is to help visitors by answering questions using ONLY the company information provided below.

If someone asks about:

- Services
- Portfolio
- Pricing
- Contact Details
- Office Hours
- Technologies
- AI
- ERP
- CRM
- Website Development
- Mobile Apps
- Cloud
- Cyber Security

Answer politely.

If the answer is not available in the company information, politely say:

"I don't have that information yet. Please contact our team for more details."

Company Information:

{json.dumps(company_data, indent=2)}
"""


def generate_reply(user_message: str):
    """
    Sends the user's question to OpenAI and returns the response.
    """

    company_data = load_company_data()

    system_prompt = build_system_prompt(company_data)

    response = client.chat.completions.create(
        model="gpt-5.5",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],

        max_completion_tokens=500
    )

    return response.choices[0].message.content.strip()