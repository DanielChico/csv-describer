# csv-describer

Takes CSV data + a description of what the data represents and uses an LLM to generate English narrative descriptions of trends and their business implications.

Built for dashboard reporting — feed it the CSV behind any chart and get back prose you can drop into a monthly report.

## How it works

The core function `describe_chart` accepts a CSV file (or raw CSV string) and a plain-English description of what the data represents. It sends both to Gemini 3 Flash via OpenRouter and returns a narrative analysis.

All calls are async, so when processing multiple charts (like the included demo with 18 dashboard panels), they run concurrently.

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/DanielChico/csv-describer.git
cd csv-describer
uv sync
```

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

```
OPENROUTER_API_KEY=sk-or-v1-your-key-here
COMPANY_NAME=Acme Corp
COMPANY_CONTEXT=A trading company operating in international markets.
```

- **OPENROUTER_API_KEY** — get one at [openrouter.ai](https://openrouter.ai/)
- **COMPANY_NAME** — used in the LLM prompt to tailor the narrative audience
- **COMPANY_CONTEXT** — optional extra context about what the company does

## Usage

### Run the demo

The included `main.py` processes 18 sample CSV files concurrently and prints the generated descriptions:

```bash
uv run python main.py
```

### Use in your own code

```python
import asyncio
from src.chart_describer import describe_chart

result = asyncio.run(
    describe_chart(
        "data/sales.csv",
        "Monthly sales in EUR for 2025, used to track revenue trends."
    )
)
print(result)
```

You can also pass a raw CSV string instead of a file path:

```python
csv_data = "month,revenue\nJan,10000\nFeb,15000\nMar,12000"

result = asyncio.run(
    describe_chart(
        csv_data,
        "Quarterly revenue figures showing early-year performance."
    )
)
```

## Project structure

```
csv-describer/
├── pyproject.toml
├── .env.example
├── src/
│   └── chart_describer.py   # describe_chart(csv_input, description) -> str
├── mock_data/               # 18 sample CSV files
└── main.py                  # Demo script
```
