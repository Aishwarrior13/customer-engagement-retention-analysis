# Executive Summary
## Customer Engagement & Product Utilization Analytics for Retention Strategy
**Unified Mentor | Business Analytics Project**

### Purpose
This project examines how customer engagement, banking product count and financial profile relate to churn. The aim is to identify customer groups that may benefit from targeted retention initiatives and to support engagement-led product and relationship strategies.

### Dataset and approach
The analysis used 10,000 records from the supplied European Bank customer dataset. Data validation found no missing values or duplicate rows. Python-based exploratory analysis compared churn across activity status, product count, balance/activity groups and descriptive relationship-strength tiers. An interactive Streamlit dashboard was developed with engagement, product-count, balance and salary filters.

### Headline findings

| Measure | Result |
|---|---:|
| Overall churn | 20.37% (2,037 of 10,000 customers) |
| Active customer churn | 14.27% |
| Inactive customer churn | 26.85% |
| Two-product customer churn | 7.58% |
| Three-product customer churn | 82.71% (266 customers) |
| Four-product customer churn | 100.00% (60 customers) |
| High-balance inactive customers | 1,247; churn rate 30.47% |
| Weak vs Strong relationship-tier churn | 40.30% vs 5.56% |

### What the findings suggest
- Inactive customers show materially higher churn than active customers.
- Customers with exactly two products have the lowest observed churn in this dataset; this is an association, not proof that adding a product causes retention.
- The 3–4 product groups show very high churn but are small and require investigation before broad conclusions.
- High account balance does not guarantee engagement: almost half of high-balance customers are inactive.
- The descriptive relationship-strength tiers show a strong gradient in observed churn, but the score is not a validated predictive model.

### Recommended actions
1. Prioritize re-engagement campaigns for inactive customers, particularly inactive single-product customers.
2. Conduct relationship reviews for high-balance inactive customers to identify service needs or dissatisfaction.
3. Investigate product suitability and customer experience among customers holding 3–4 products.
4. Study the active two-product segment to identify product combinations and engagement practices for further testing.
5. Track engagement and product-utilization KPIs over time and validate segment performance with newer data.

### Cautions and limitations
The data is observational and does not establish causation. Product count does not measure actual product usage; credit-card ownership does not establish card usage; estimated salary is not verified income; and the activity indicator does not provide transaction frequency. Small 3–4 product groups should be interpreted cautiously. The relationship-strength score is a descriptive segmentation tool only.

### Conclusion
The analysis supports using customer engagement and product utilization together to prioritize retention attention. It identifies distinct groups for re-engagement, relationship review and further investigation. These findings provide a practical starting point for more targeted retention strategies, subject to validation with richer customer-behavior data.

**Prepared for:** Unified Mentor project submission.
