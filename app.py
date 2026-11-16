import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Customer Retention Analytics", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    data_path = Path(__file__).resolve().parent / "bank_retention_dashboard.csv"
    return pd.read_csv(data_path)

df = load_data()

st.title("Customer Engagement & Product Utilization Analytics")
st.markdown("""
Analyze customer engagement, product utilization and
relationship strength to identify churn risks and improve retention.
""")

st.subheader("Customer Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{len(df):,}")
col2.metric("Churned Customers", f"{df['Exited'].sum():,}")
col3.metric("Overall Churn Rate", f"{df['Exited'].mean() * 100:.2f}%")
st.divider()

st.sidebar.header("Customer Filters")
engagement_filter = st.sidebar.selectbox("Engagement Status", ["All", "Active", "Inactive"])
product_filter = st.sidebar.slider(
    "Number of Products",
    min_value=int(df["NumOfProducts"].min()),
    max_value=int(df["NumOfProducts"].max()),
    value=(int(df["NumOfProducts"].min()), int(df["NumOfProducts"].max()))
)
balance_filter = st.sidebar.slider(
    "Minimum Balance", min_value=0, max_value=int(df["Balance"].max()),
    value=0, step=10000
)
salary_filter = st.sidebar.slider(
    "Minimum Estimated Salary", min_value=0, max_value=int(df["EstimatedSalary"].max()),
    value=0, step=10000
)

filtered_df = df.copy()
if engagement_filter == "Active":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 1]
elif engagement_filter == "Inactive":
    filtered_df = filtered_df[filtered_df["IsActiveMember"] == 0]

filtered_df = filtered_df[
    filtered_df["NumOfProducts"].between(product_filter[0], product_filter[1])
    & (filtered_df["Balance"] >= balance_filter)
    & (filtered_df["EstimatedSalary"] >= salary_filter)
]

st.subheader("Filtered Customer Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Customers", f"{len(filtered_df):,}")
col2.metric("Churned Customers", f"{filtered_df['Exited'].sum():,}")
churn_rate = filtered_df["Exited"].mean() * 100 if not filtered_df.empty else 0
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
st.divider()

st.subheader("Key Performance Indicators")
active_df = filtered_df[filtered_df["IsActiveMember"] == 1]
inactive_df = filtered_df[filtered_df["IsActiveMember"] == 0]
active_retention = (1 - active_df["Exited"].mean()) * 100 if not active_df.empty else 0
inactive_retention = (1 - inactive_df["Exited"].mean()) * 100 if not inactive_df.empty else 0
engagement_retention_ratio = active_retention / inactive_retention if inactive_retention > 0 else 0
product_depth_index = filtered_df["NumOfProducts"].mean() if not filtered_df.empty else 0
high_balance_df = filtered_df[filtered_df["HighBalance"] == 1]
high_balance_disengagement = (
    (high_balance_df["IsActiveMember"] == 0).mean() * 100
    if not high_balance_df.empty else 0
)
card_df = filtered_df[filtered_df["HasCrCard"] == 1]
no_card_df = filtered_df[filtered_df["HasCrCard"] == 0]
card_retention = (1 - card_df["Exited"].mean()) * 100 if not card_df.empty else 0
no_card_retention = (1 - no_card_df["Exited"].mean()) * 100 if not no_card_df.empty else 0
credit_card_stickiness = card_retention - no_card_retention
relationship_strength_index = (
    filtered_df["Relationship_Strength_Index"].mean() if not filtered_df.empty else 0
)

col1, col2, col3 = st.columns(3)
col1.metric("Engagement Retention Ratio", f"{engagement_retention_ratio:.2f}")
col2.metric("Product Depth Index", f"{product_depth_index:.2f}")
col3.metric("High-Balance Disengagement Rate", f"{high_balance_disengagement:.2f}%")
col4, col5 = st.columns(2)
col4.metric("Credit Card Stickiness Score", f"{credit_card_stickiness:+.2f} pp")
col5.metric("Relationship Strength Index", f"{relationship_strength_index:.2f}/100")

st.subheader("Engagement and Product Utilization")
if not filtered_df.empty:
    engagement_analysis = (
        filtered_df.groupby(["IsActiveMember", "NumOfProducts"])["Exited"]
        .mean().reset_index()
    )
    engagement_analysis["Churn_Rate"] = engagement_analysis["Exited"] * 100
    engagement_analysis["Engagement"] = engagement_analysis["IsActiveMember"].map(
        {0: "Inactive", 1: "Active"}
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=engagement_analysis, x="NumOfProducts", y="Churn_Rate",
                hue="Engagement", ax=ax)
    ax.set_title("Churn Rate by Engagement and Product Count")
    ax.set_xlabel("Number of Products")
    ax.set_ylabel("Churn Rate (%)")
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Relationship Strength")
if "Relationship_Tier" in filtered_df.columns:
    relationship_analysis = (
        filtered_df.groupby("Relationship_Tier", observed=False)
        .agg(Customer_Count=("Exited", "count"),
             Churned_Customers=("Exited", "sum"),
             Churn_Rate=("Exited", "mean"))
        .reset_index()
    )
    relationship_analysis["Churn_Rate"] *= 100
    st.dataframe(relationship_analysis, use_container_width=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=relationship_analysis, x="Relationship_Tier",
                y="Churn_Rate", ax=ax)
    ax.set_title("Churn Rate by Relationship Strength")
    ax.set_ylabel("Churn Rate (%)")
    st.pyplot(fig)
    plt.close(fig)

st.subheader("High-Value Disengaged Customer Detector")
high_risk = filtered_df[
    (filtered_df["HighBalance"] == 1) & (filtered_df["IsActiveMember"] == 0)
].copy()
col1, col2, col3 = st.columns(3)
col1.metric("At-Risk Customers", f"{len(high_risk):,}")
col2.metric("Churned Customers", f"{high_risk['Exited'].sum():,}")
risk_rate = high_risk["Exited"].mean() * 100 if not high_risk.empty else 0
col3.metric("Churn Rate", f"{risk_rate:.2f}%")
st.markdown("**Customer-Level Details**")
if not high_risk.empty:
    customer_table = high_risk[
        ["CustomerId", "Geography", "Balance", "EstimatedSalary",
         "NumOfProducts", "Exited"]
    ].copy()
    customer_table["Customer Status"] = customer_table["Exited"].map(
        {0: "Retained", 1: "Churned"}
    )
    st.dataframe(customer_table.drop(columns=["Exited"]),
                 use_container_width=True, hide_index=True)
else:
    st.info("No high-balance inactive customers match the selected filters.")

st.subheader("Retention Priority Segments")
if "Retention_Priority_Segment" in filtered_df.columns:
    retention_analysis = (
        filtered_df.groupby("Retention_Priority_Segment", observed=False)
        .agg(Customer_Count=("Exited", "count"),
             Churned_Customers=("Exited", "sum"),
             Churn_Rate=("Exited", "mean"))
        .reset_index()
    )
    retention_analysis["Churn_Rate"] *= 100
    st.dataframe(retention_analysis, use_container_width=True)

st.caption(
    "Historical associations do not establish causation. "
    "Small customer segments should be interpreted cautiously."
)
