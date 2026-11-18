# Customer Engagement & Product Utilization Analytics for Retention Strategy

**Unified Mentor | Business Analytics Project**

## Project overview
This project analyzes customer churn through engagement, banking product count, account balance and descriptive relationship strength. It uses 10,000 records from the supplied European Bank customer dataset.

## Objectives
- Evaluate the relationship between customer engagement and churn.
- Measure churn patterns across product counts.
- Identify high-balance inactive customers.
- Develop retention-oriented customer segments and KPIs.
- Present the analysis in an interactive Streamlit dashboard.

## Key findings
- Overall churn: **20.37%** (2,037 of 10,000 customers).
- Active customer churn: **14.27%**; inactive customer churn: **26.85%**.
- Churn by product count: 1 product **27.71%**, 2 products **7.58%**, 3 products **82.71%** (266 customers), 4 products **100%** (60 customers).
- High-balance inactive customers: **1,247**, with **30.47%** churn.
- Relationship-tier churn: Weak **40.30%**, Moderate **16.73%**, Strong **5.56%**.

The 3- and 4-product groups are small and their high churn rates should be interpreted cautiously. These are observed associations, not evidence of causation.

## Dashboard features
- Engagement status filter.
- Product count range slider.
- Minimum balance and estimated salary filters.
- Overall and filtered customer KPIs.
- Engagement and product-utilization analysis.
- Relationship-strength analysis.
- High-value disengaged customer detector.
- Retention-priority segment analysis.

## Live dashboard
The interactive dashboard is deployed on Streamlit Community Cloud: https://customer-engagement-retention-analysis-aishwarrior.streamlit.app/

## Run locally
Keep `app.py` and `bank_retention_dashboard.csv` in the same folder.

Install dependencies:
```bash
pip install -r requirements.txt
```

Run:
```bash
python -m streamlit run app.py
```

## KPI definitions
The project brief named the KPIs but did not specify formulas. This analysis uses the following operational definitions:
- **Engagement Retention Ratio:** active customer retention rate divided by inactive customer retention rate.
- **Product Depth Index:** mean number of products per customer.
- **High-Balance Disengagement Rate:** inactive high-balance customers divided by all high-balance customers.
- **Credit Card Stickiness Score:** cardholder retention rate minus non-cardholder retention rate, in percentage points.
- **Relationship Strength Index:** mean customer-level descriptive score.

The Relationship Strength Index assigns 50 points for active status and 50 points for holding exactly two products. It is a descriptive segmentation measure, not a validated predictive model.

## Repository contents
- `app.py` — Streamlit dashboard source.
- `requirements.txt` — Python dependencies.
- `Research_Paper_Concise.md` — research paper.
- `Executive_Summary.md` — executive summary.
- `Research_Paper_Concise.docx` and `Executive_Summary.docx` — Word versions of the reports.
- `bank_retention_dashboard.csv` — processed dashboard dataset.
- `churn_by_engagement.png`, `churn_by_product_count.png`, `churn_by_relationship_tier.png`, and `churn_by_retention_segment.png` — analysis charts.

`bank_retention_dashboard.csv` — processed dataset used by the dashboard.

## Limitations
The dataset is observational and does not establish causation. Product count does not measure usage frequency; credit-card ownership does not prove card usage; estimated salary is not verified income; and the activity indicator does not provide transaction frequency. The dataset does not include churn reasons. Small 3–4 product groups require cautious interpretation.
