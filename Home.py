import streamlit as st

st.set_page_config(
    page_title="Zero to Snowflake HOL",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg", width=200)
st.sidebar.markdown("---")
st.sidebar.markdown("**Zero to Snowflake**")
st.sidebar.markdown("Hands-on Lab · July 28, 2026")

st.title("❄️ Zero to Snowflake")
st.subheader("Hands-on Lab")

st.markdown("---")

st.markdown("""
### Welcome!

This hands-on lab will take you from **zero** to productive in Snowflake in under 2 hours. 
You'll learn the fundamentals of Snowflake by working with a real-world **retail banking** dataset.

### What You'll Learn

| # | Section | Duration |
|---|---------|----------|
| 1 | **Snowflake UI Tour** — Navigate Snowsight, set context, explore data | ~20 min |
| 2 | **Querying & Analytics** — SQL on banking data: joins, aggregates, windows | ~40 min |
| 3 | **Results Cache & Cloning** — Observe caching, zero-copy clone | ~20 min |
| 4 | **Marketplace Data** — Subscribe to free data, join with banking tables | ~20 min |

### Prerequisites

- ✅ Access to a Snowflake account (trial or provisioned sandbox)
- ✅ Basic SQL knowledge (SELECT, WHERE, JOIN, GROUP BY)
- ✅ A modern web browser (Chrome, Edge, Firefox)

### Pre-Provisioned Data

Your lab environment includes the **`TU30_CORTEX_ANALYST_LAB.RETAIL_BANKING`** schema with:

| Table | Rows | Description |
|-------|------|-------------|
| `CUSTOMERS` | 500 | Canadian retail banking customers (segment, income, credit score, city, province) |
| `PRODUCTS` | 15 | Banking products (chequing, savings, credit card, mortgage, LOC, investments) |
| `TRANSACTIONS` | 1,000 | Transaction history (purchases, deposits, withdrawals, transfers, payments) |

**Relationships:**
- `TRANSACTIONS.CUSTOMER_ID` → `CUSTOMERS.CUSTOMER_ID`
- `TRANSACTIONS.PRODUCT_ID` → `PRODUCTS.PRODUCT_ID`

---

👈 **Use the sidebar to navigate through the lab sections.**
""")
