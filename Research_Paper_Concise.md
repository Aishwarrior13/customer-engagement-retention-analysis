# Customer Engagement & Product Utilization Analytics for Retention Strategy
**Concise Research Paper | European Bank Customer Dataset**  
**Unified Mentor | Business Analytics Project**

## 1. Abstract
This project examines customer churn through engagement, banking product utilization and relationship strength. Using 10,000 customer records, the analysis applies data validation, exploratory data analysis, segmentation and KPI calculations to identify retention patterns. Overall churn was 20.37%. Inactive customers had higher churn than active customers, customers holding exactly two products had comparatively strong retention, and customers holding three or four products showed very high churn. The findings support targeted re-engagement, product-fit reviews and proactive attention to high-balance inactive customers.

## 2. Background, problem and objectives
Banks need to understand more than customer demographics and financial balances to design effective retention initiatives. Customers with substantial balances may still be disengaged, and owning more products does not automatically imply loyalty. This project evaluates the relationship between engagement and churn, measures product-count patterns, and identifies disengaged high-balance customers. Secondary aims are to support engagement-led retention and improve product-bundling decisions.

## 3. Dataset and validation
The supplied European Bank dataset contains 10,000 rows and 14 original columns, including customer geography, tenure, balance, estimated salary, number of products, activity status, credit-card ownership and the churn target `Exited` (1 = churned; 0 = retained). Validation found no missing values or duplicate rows. The `Year` field had one unique value (2025) and was not useful for comparative analysis.

| Validation item | Result |
|---|---:|
| Records | 10,000 |
| Original columns | 14 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Churned customers | 2,037 |
| Retained customers | 7,963 |
| Overall churn | 20.37% |

## 4. Methodology
The analysis used Python and Pandas for data preparation and calculations, and Matplotlib/Seaborn for charts. Customers were compared by activity status and product count. Balance was classified as high at or above the 75th percentile (127,644.24). A descriptive Relationship Strength Index assigned 50 points for active status and 50 points for holding exactly two products; tiers were Weak (0), Moderate (50) and Strong (100). Retention priority groups were assigned mutually exclusively in this order: 3–4 products; inactive single-product; high-balance inactive; active two-product; other customers.

## 5. Key findings

### 5.1 Engagement and product count

| Segment | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| Active | 5,151 | 735 | 14.27% |
| Inactive | 4,849 | 1,302 | 26.85% |
| 1 product | 5,084 | 1,409 | 27.71% |
| 2 products | 4,590 | 348 | 7.58% |
| 3 products | 266 | 220 | 82.71% |
| 4 products | 60 | 60 | 100.00% |

Inactive customers had 12.58 percentage points higher churn than active customers. Customers with exactly two products had the lowest observed churn. The three- and four-product groups were much smaller, so their high rates should be interpreted cautiously and investigated rather than assumed to reflect a general product-count effect.

### 5.2 Financial commitment and disengagement

| Balance/activity segment | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| Low balance, active | 3,898 | 523 | 13.42% |
| Low balance, inactive | 3,602 | 922 | 25.60% |
| High balance, active | 1,253 | 212 | 16.92% |
| High balance, inactive | 1,247 | 380 | 30.47% |

The high-balance threshold was 127,644.24. Among 2,500 high-balance customers, 1,247 (49.88%) were inactive. The high-balance inactive group had a 30.47% churn rate. This supports proactive engagement review; it does not prove why customers are inactive or whether funds have moved elsewhere.

### 5.3 Relationship strength and retention priority

| Relationship tier | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| Weak | 2,705 | 1,090 | 40.30% |
| Moderate | 4,849 | 811 | 16.73% |
| Strong | 2,446 | 136 | 5.56% |

| Priority segment | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| High Product Count (3–4) | 326 | 280 | 85.89% |
| Inactive Single-Product | 2,521 | 924 | 36.65% |
| High-Balance Inactive | 370 | 54 | 14.59% |
| Active Two-Product | 2,446 | 136 | 5.56% |
| Other Customers | 4,337 | 643 | 14.83% |

The Weak relationship tier had 40.30% churn, compared with 5.56% in the Strong tier. The high-balance inactive population (1,247 customers) overlaps with other groups. In the mutually exclusive priority table, only 370 customers appear in the High-Balance Inactive category because customers with 3–4 products and inactive single-product customers are assigned earlier in the priority order.

## 6. KPI results

| KPI | Operational definition | Result |
|---|---|---:|
| Engagement Retention Ratio | Active retention ÷ inactive retention | 1.17 : 1 |
| Product Depth Index | Mean number of products per customer | 1.53 |
| High-Balance Disengagement Rate | Inactive high-balance ÷ all high-balance customers | 49.88% |
| Credit Card Stickiness Score | Cardholder retention minus non-cardholder retention | +0.63 pp |
| Relationship Strength Index | Mean customer-level descriptive score | 48.71 / 100 |

The project brief named the KPIs but did not specify formulas; the definitions above are operational definitions adopted for this analysis. Credit-card ownership is not evidence of card usage. Product count is not a measure of usage frequency.

## 7. Recommendations
1. Prioritize re-engagement for inactive customers, especially inactive single-product customers.
2. Investigate the 3–4 product segment for product suitability, service complexity and customer experience; the sample sizes are small.
3. Offer proactive relationship reviews to high-balance inactive customers.
4. Study the active two-product segment to understand which product combinations and engagement practices may be worth testing.
5. Use the Relationship Strength Index as a descriptive monitoring aid only; validate it before operational or automated use.

## 8. Dashboard, limitations and conclusion
A Streamlit dashboard was built with engagement, product-count, minimum-balance and minimum-salary filters. It presents customer KPIs, engagement/product analysis, relationship tiers, high-value disengaged customer records and retention-priority segments.

Limitations: the dataset is historical and observational; it does not establish causation. The activity field does not show transaction frequency, product count does not identify product types or usage intensity, estimated salary is not verified income, and credit-card ownership does not show card usage. The Relationship Strength Index is a simplified descriptive score, not a validated predictive model.

The analysis indicates that engagement and product utilization are useful dimensions for customer-retention segmentation. Inactive customers, high-balance inactive customers and customers with 3–4 products warrant different forms of investigation and intervention. The results can support more targeted retention planning, subject to validation with richer behavioral and customer-feedback data.

**Source:** European Bank Customer Dataset supplied for this project; calculations reproduced from the supplied data.
