import streamlit as st

st.title("🏪 Marketplace Data")
st.markdown("**Duration:** ~20 minutes")
st.markdown("---")

st.markdown("""
## Objectives

By the end of this section, you will be able to:
- Navigate the Snowflake Marketplace
- Subscribe to a free data listing
- Explore shared data without any ETL or data loading
- Join Marketplace data with your banking tables for enriched analytics
""")

st.markdown("---")

st.header("Part A: The Snowflake Marketplace")

st.markdown("""
### What is the Snowflake Marketplace?

The Snowflake Marketplace provides access to **thousands of data listings** from third-party providers — 
directly in your Snowflake account. Key benefits:

- **No ETL required** — data appears as a shared database in your account
- **Always up-to-date** — providers maintain and refresh their data
- **Governed** — access controlled by Snowflake's security model
- **Free and paid listings** — many high-value datasets are free

### Use Cases in Banking
- Economic indicators for risk modeling
- Market data for portfolio analytics
- Geographic/demographic data for customer segmentation
- Financial benchmarks and indices
""")

st.markdown("---")

st.header("Part B: Subscribe to Snowflake Public Data (Free)")

st.markdown("""
### Step 1: Navigate to the Marketplace

1. In Snowsight, click **Data Products → Marketplace** in the left nav.
2. You'll see featured and recommended listings.
""")

st.markdown("""
### Step 2: Find the Listing

1. In the search bar, type: **`Snowflake Public Data`**
2. Look for the listing: **"Snowflake Public Data (Free)"** by Snowflake Public Data
3. Click on the listing to view details.
""")

st.markdown("""
### Step 3: Get the Data

1. Click the **Get** button.
2. Review the information in the dialog.
3. Accept the terms and click **Get** again.
4. Optionally rename the database (default: `SNOWFLAKE_PUBLIC_DATA_FREE`).
5. Click **Done**.
""")

st.success("""
🎉 **That's it!** A new database now appears in your account with live financial and economic data.
No loading, no ETL, no pipelines. The data is instantly queryable.
""")

st.markdown("---")

st.header("Part C: Explore the Marketplace Data")

st.markdown("**Step 1:** Explore what's available:")

st.code("""
-- See what schemas are available
SHOW SCHEMAS IN DATABASE SNOWFLAKE_PUBLIC_DATA_FREE;
""", language="sql")

st.code("""
-- Explore the FINANCE schema (if available)
SHOW TABLES IN SCHEMA SNOWFLAKE_PUBLIC_DATA_FREE.FINANCE;

-- Or explore all schemas
SHOW TABLES IN DATABASE SNOWFLAKE_PUBLIC_DATA_FREE;
""", language="sql")

st.markdown("**Step 2:** Preview some data:")

st.code("""
-- Example: Look at available financial data
SELECT *
FROM SNOWFLAKE_PUBLIC_DATA_FREE.FINANCE.SEI_DAILY_STOCK_PRICING_WITH_ANALYTICS
LIMIT 20;
""", language="sql")

st.info("""
💡 **Note:** The exact tables and schemas available may vary. Use `SHOW TABLES` 
and `SHOW SCHEMAS` to explore what's in your version of the listing.
""")

st.markdown("---")

st.header("Part D: Enrich Your Banking Data")

st.markdown("""
Now for the powerful part — **join Marketplace data with your banking tables** to create 
enriched analytics without any data movement.

### Example: Cross-reference with economic data

The concept here is simple: external datasets can add context to your internal data. 
In a real-world scenario, you might join:
- Customer locations with economic indicators (unemployment rate, GDP by province)
- Transaction dates with market data (what was the market doing when customers transacted?)
- Product categories with industry benchmarks
""")

st.markdown("**Example query** (adjust based on available Marketplace tables):")

st.code("""
-- Pattern: Enrich internal banking data with external context
-- This is a template — adjust table/column names based on what's in your Marketplace listing

-- Example: Customer distribution by province (internal) 
-- ready to join with provincial economic indicators (external)
SELECT C.PROVINCE,
       COUNT(*) AS customer_count,
       AVG(C.ANNUAL_INCOME) AS avg_income,
       AVG(C.CREDIT_SCORE) AS avg_credit_score,
       SUM(T.AMOUNT) AS total_transaction_volume
FROM RETAIL_BANKING.CUSTOMERS C
JOIN RETAIL_BANKING.TRANSACTIONS T ON C.CUSTOMER_ID = T.CUSTOMER_ID
GROUP BY C.PROVINCE
ORDER BY total_transaction_volume DESC;
""", language="sql")

st.markdown("""
> 💡 **Key Insight:** In production, you would JOIN this with provincial economic data from the 
> Marketplace (e.g., unemployment rates, housing starts, GDP growth) to build richer risk 
> and segmentation models — all without any data loading or ETL.
""")

st.markdown("---")

with st.expander("🤖 CoCo Sneak Peek — Do this with Cortex Code"):
    st.markdown("""
CoCo can help you discover and use Marketplace data:

| What you did | CoCo prompt |
|-------------|-------------|
| Explore listing | `What schemas and tables are in SNOWFLAKE_PUBLIC_DATA_FREE?` |
| Preview data | `Show me sample rows from the finance tables in the public data listing` |
| Enrich banking data | `Join our customer province data with any economic indicators from the marketplace listing` |
| Find relevant data | `What marketplace tables could I join with our CUSTOMERS table by province?` |

CoCo can also help you discover new listings: `Search the Snowflake Marketplace for Canadian economic data`
""")

st.markdown("---")

st.success("""
## ✅ Section Complete!

You've learned:
- The Snowflake Marketplace provides instant access to third-party data
- Subscribing is a click — no ETL, no pipelines, no data loading
- Marketplace data can be joined directly with your internal tables
- This pattern enables enriched analytics without data movement

**Next →** Head to **Section 7: Governance** to secure your data with masking and row access policies.
""")
