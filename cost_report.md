# Cost Analysis Report — Chart Description Generator

**Model:** `google/gemini-3-flash-preview` via OpenRouter
**Date:** 2026-02-17
**Pricing:** $0.50 / 1M input tokens — $3.00 / 1M output tokens

---

## Per Request (Average)

| Metric         | Tokens | Cost        |
|----------------|-------:|------------:|
| Input tokens   |  339.9 | $0.000170   |
| Output tokens  |  312.1 | $0.000936   |
| **Total**      |  652.1 | **$0.001106** |

> Generating a single chart description costs approximately **$0.0011**.

---

## Demo Run (18 requests)

| Metric         | Tokens | Cost        |
|----------------|-------:|------------:|
| Input tokens   |  6,119 | $0.003060   |
| Output tokens  |  5,618 | $0.016854   |
| **Total**      | 11,737 | **$0.019914** |

> The full 18-chart demo costs approximately **$0.02** per run.

---

## Annual Cost Projection

Assuming the full 18-chart report is generated **once per month** (12 runs/year):

| Period    | Runs | Cost        |
|-----------|-----:|------------:|
| Monthly   |    1 | $0.019914   |
| Quarterly |    3 | $0.059741   |
| Annually  |   12 | **$0.238963** |

> The estimated annual cost is **$0.24**, well under one dollar per year.

---

## Conclusion

At current OpenRouter pricing for Gemini 3 Flash Preview, the cost of generating
all 18 dashboard descriptions is negligible — roughly **two cents per run**.
Even with monthly execution, the annual spend stays under **$0.24**.
Output tokens account for **85%** of the total cost despite being only 48% of
the token volume, due to the 6x price difference between input and output tokens.
This makes the solution extremely cost-effective for recurring business reporting.
