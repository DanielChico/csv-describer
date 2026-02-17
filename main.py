"""Chart Description Generator — demo script.

Fires off all 18 chart descriptions concurrently via asyncio,
then prints results in order.
"""

import asyncio
from pathlib import Path

from src.chart_describer import describe_chart

MOCK_DATA_DIR = Path(__file__).parent / "mock_data"

CHARTS: list[tuple[str, str]] = [
    (
        "01_summary_kpis.csv",
        "Summary KPIs showing total projects, total clients, total suppliers, and total sales, "
        "each with their change versus the previous period. Used to assess overall business health at a glance.",
    ),
    (
        "02_projects_by_year_month.csv",
        "Monthly project counts across 2023, 2024, and 2025, used to compare year-over-year "
        "sales performance and identify seasonal trends. 2025 data is only available through May.",
    ),
    (
        "03_sales_funnel.csv",
        "Sales funnel showing the number of projects at each pipeline stage: Ofertado (Offered), "
        "No es posible ofertar (Not possible to offer), Cerrado y perdido (Closed & lost), "
        "Informativo (Informational), Cancelado (Cancelled), Ganado (Won), and Cerrado y ganado "
        "(Closed & won). Used to evaluate pipeline health and conversion efficiency.",
    ),
    (
        "04_invoiced_sales_by_month.csv",
        "Invoiced sales in EUR by month for 2025, showing actual revenue billed to clients. "
        "Used to track revenue realization versus pipeline value.",
    ),
    (
        "05_value_by_client.csv",
        "Total project value in USD by client, ranked from highest to lowest. Shows the "
        "concentration of revenue across the client portfolio and identifies key accounts.",
    ),
    (
        "06_value_by_representative.csv",
        "Total project value in USD by sales representative, ranked from highest to lowest. "
        "Used to evaluate individual sales performance and identify top performers.",
    ),
    (
        "07_pct_by_project_status.csv",
        "Percentage distribution of all projects by status. Shows what proportion of the "
        "total pipeline is at each stage (offered, lost, won, informational, etc.).",
    ),
    (
        "08_client_distribution_by_status.csv",
        "Distribution of projects by status for each sales representative. Shows how each "
        "representative's portfolio breaks down across won, lost, offered, informational, "
        "cancelled, and other statuses.",
    ),
    (
        "09_project_status_and_value.csv",
        "Number of projects and their total monetary value by status. Compares project count "
        "versus actual revenue generated at each pipeline stage.",
    ),
    (
        "10_project_trend_by_month.csv",
        "Monthly project count trend for 2025, showing the number of new projects initiated "
        "each month throughout the year. Used to identify seasonal patterns and momentum.",
    ),
    (
        "11_geographic_distribution.csv",
        "Geographic distribution of project value by country. Shows how the business "
        "is spread across its operating markets.",
    ),
    (
        "12_project_success_rate.csv",
        "Overall project success rate KPI (percentage of projects won or closed & won out of "
        "total resolved projects), with change versus the previous period.",
    ),
    (
        "13_project_failure_rate.csv",
        "Overall project failure rate KPI (percentage of projects lost, cancelled, or not "
        "possible to offer out of total resolved projects), with change versus the previous period.",
    ),
    (
        "14_success_failure_trend.csv",
        "Year-over-year trend of project success and failure percentages. Compares the "
        "proportion of successful versus failed projects across years.",
    ),
    (
        "15_pct_success_failure.csv",
        "Pie chart data showing the overall split between successful (Exitosos) and failed "
        "(Fallidos) projects, including absolute counts and percentages.",
    ),
    (
        "16_failure_rate_by_category.csv",
        "Project failure rate broken down by product/service category (e.g., Paper, Oil and Gas, "
        "Containers, Automotive). Shows which business lines have the highest loss rates.",
    ),
    (
        "17_success_rate_by_category.csv",
        "Project success rate broken down by product/service category. Shows which business "
        "lines are most effective at converting opportunities into wins.",
    ),
    (
        "18_success_failure_by_category.csv",
        "Combined success and failure rates by product/service category, allowing direct "
        "comparison of win/loss performance across all business lines.",
    ),
]


async def main() -> None:
    tasks = [
        describe_chart(MOCK_DATA_DIR / filename, description)
        for filename, description in CHARTS
    ]
    results = await asyncio.gather(*tasks)

    for (filename, _), result in zip(CHARTS, results):
        chart_name = filename.replace(".csv", "").split("_", 1)[1].replace("_", " ").title()
        print(f"\n{'='*80}")
        print(f"  {chart_name}")
        print(f"{'='*80}\n")
        print(result)
        print()


if __name__ == "__main__":
    asyncio.run(main())
