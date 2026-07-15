import streamlit as st

st.set_page_config(
    page_title="Zero to Snowflake HOL",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.logo("https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg")

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #1B2A4A;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
        color: #C8D6E5 !important;
    }
    [data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] {
        background-color: rgba(255,255,255,0.1) !important;
    }
    .big-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1B2A4A;
        margin-bottom: 0;
        line-height: 1.2;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #5A6B7B;
        margin-top: 0.25rem;
        margin-bottom: 2rem;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #5A6B7B;
        margin-bottom: 0.25rem;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1B2A4A;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">Zero to Snowflake</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Hands-on Lab · July 28, 2026</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<p class="metric-label">Sections</p>', unsafe_allow_html=True)
    st.markdown('<p class="metric-value">4</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="metric-label">Exercises</p>', unsafe_allow_html=True)
    st.markdown('<p class="metric-value">12</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="metric-label">Duration</p>', unsafe_allow_html=True)
    st.markdown('<p class="metric-value">2 hrs</p>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### How this workshop works

Each section has **numbered exercises** that you run in a Snowflake worksheet:

- **Snowsight UI** — for navigating and exploring your data
- **SQL Worksheets** — for writing and running queries
- **Marketplace** — for subscribing to external data

All exercises build on each other sequentially — work through them in order.
""")

st.markdown("---")

st.markdown("### The scenario")

st.info("""
You are a data analyst at a **Canadian retail bank**. You have access to customer, product, 
and transaction data and need to explore it, build analytics, and enrich it with external market data.

We'll work with a pre-provisioned dataset covering:

| Data type | Examples |
|-----------|----------|
| **Customers** | Demographics, segment, income, credit score, province |
| **Products** | Chequing, savings, credit card, mortgage, LOC, investments |
| **Transactions** | Purchases, deposits, withdrawals, transfers, payments across 5 channels |
""")

st.markdown("---")

st.markdown("### What you'll learn")

st.markdown("""
| # | Section | What you'll do |
|---|---------|---------------|
| 1 | **Snowflake UI Tour** | Navigate Snowsight, set context, explore tables |
| 2 | **Querying & Analytics** | Joins, aggregates, window functions, time-series |
| 3 | **Results Cache & Cloning** | Observe caching, create zero-copy clones |
| 4 | **Marketplace Data** | Subscribe to free data, join with banking tables |
""")

st.markdown("---")

st.markdown("### Prerequisites")

st.markdown("""
- Access to a Snowflake account (trial or provisioned sandbox)
- Basic SQL knowledge (SELECT, WHERE, JOIN, GROUP BY)
- A modern web browser (Chrome, Edge, Firefox)
""")

st.markdown("---")

st.markdown("### Pre-provisioned data")

st.markdown("""
Your lab environment includes **`TU30_CORTEX_ANALYST_LAB.RETAIL_BANKING`** with:
""")

st.markdown("""
| Table | Rows | Description |
|-------|------|-------------|
| `CUSTOMERS` | 500 | Canadian retail banking customers |
| `PRODUCTS` | 15 | Banking products |
| `TRANSACTIONS` | 1,000 | Transaction history |

**Relationships:**  
`TRANSACTIONS.CUSTOMER_ID` → `CUSTOMERS.CUSTOMER_ID`  
`TRANSACTIONS.PRODUCT_ID` → `PRODUCTS.PRODUCT_ID`
""")
