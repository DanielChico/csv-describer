import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
COMPANY_NAME = os.getenv("COMPANY_NAME", "the company")
COMPANY_CONTEXT = os.getenv("COMPANY_CONTEXT", "")
MODEL = "google/gemini-3-flash-preview"
BASE_URL = "https://openrouter.ai/api/v1"


def _build_system_prompt() -> str:
    audience = f"the executive team at {COMPANY_NAME}"
    context_line = f" {COMPANY_CONTEXT}" if COMPANY_CONTEXT else ""

    return (
        f"You are a business analyst writing narrative descriptions for a sales dashboard report. "
        f"Your audience is {audience}.{context_line}\n\n"
        "When given CSV data and a description of what it represents, write an English narrative that:\n"
        "- Highlights key trends, patterns, and comparisons visible in the data\n"
        "- Explains the business implications of what the numbers show\n"
        "- Uses specific numbers from the data to support your observations\n"
        "- Maintains a professional yet accessible tone, similar to a monthly sales report\n"
        "- Avoids simply restating the data — instead, interpret and contextualize it\n\n"
        "Match your length to the complexity of the data. Simple KPIs or single-metric data need only 1-2 sentences. "
        "Richer datasets with multiple dimensions deserve 2-3 paragraphs.\n\n"
        "Do NOT use markdown headers (no #, ##, etc.). Write in prose."
    )


_client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL,
)


async def describe_chart(csv_input: str | Path, description: str) -> str:
    """Generate a narrative description of chart data using an LLM.

    Args:
        csv_input: File path to a CSV or a raw CSV string.
        description: What the data represents (context for the LLM).

    Returns:
        English narrative description of trends and business implications.
    """
    csv_path = Path(csv_input)
    if csv_path.is_file():
        csv_content = csv_path.read_text(encoding="utf-8")
    else:
        csv_content = str(csv_input)

    user_prompt = (
        f"Data description: {description}\n\n"
        f"CSV data:\n```\n{csv_content}\n```\n\n"
        "Write a narrative analysis of this data."
    )

    response = await _client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": _build_system_prompt()},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=1024,
    )

    return response.choices[0].message.content or ""
