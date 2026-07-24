/*
=============================================================================
  SECTION 8: STREAMLIT IN SNOWFLAKE
  Zero to Snowflake HOL — July 28, 2026
  
  NOTE: This section is done through the Snowsight UI.
  Navigate to Projects → Workspaces → + → Streamlit App
  
  Configure:
    - App name: Banking_Dashboard
    - Database: TU30_ZERO_TO_SNOWFLAKE_LAB
    - Schema: RETAIL_BANKING_XX (your participant number)
    
  A compute pool is automatically assigned — no warehouse needed.

  Then paste the Python code below into the app editor.
=============================================================================
*/

-- ============================================================
-- PYTHON CODE TO PASTE INTO STREAMLIT APP EDITOR:
-- (This is Python, not SQL — paste into the Streamlit editor)
-- ============================================================

/*
import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()
session.sql("USE DATABASE TU30_ZERO_TO_SNOWFLAKE_LAB").collect()
session.sql("USE SCHEMA RETAIL_BANKING").collect()

st.title("🏦 Retail Banking Dashboard")
st.markdown("Interactive view of customer and transaction data.")

# --- Filters ---
st.sidebar.header("Filters")

provinces = session.sql("SELECT DISTINCT PROVINCE FROM CUSTOMERS ORDER BY 1").collect()
province_list = ["All"] + [row[0] for row in provinces]
selected_province = st.sidebar.selectbox("Province", province_list)

segments = session.sql("SELECT DISTINCT CUSTOMER_SEGMENT FROM CUSTOMERS ORDER BY 1").collect()
segment_list = ["All"] + [row[0] for row in segments]
selected_segment = st.sidebar.selectbox("Segment", segment_list)

# --- Build query ---
where_clauses = []
if selected_province != "All":
    where_clauses.append(f"c.PROVINCE = '{selected_province}'")
if selected_segment != "All":
    where_clauses.append(f"c.CUSTOMER_SEGMENT = '{selected_segment}'")

where_sql = "WHERE " + " AND ".join(where_clauses) if where_clauses else ""

# --- Metrics ---
metrics_df = session.sql(f"""
    SELECT
        COUNT(DISTINCT c.CUSTOMER_ID) AS customers,
        COUNT(t.TRANSACTION_ID) AS transactions,
        SUM(t.AMOUNT) AS total_volume,
        AVG(t.AMOUNT) AS avg_transaction
    FROM CUSTOMERS c
    LEFT JOIN TRANSACTIONS t ON c.CUSTOMER_ID = t.CUSTOMER_ID
    {where_sql}
""").collect()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Customers", f"{metrics_df[0][0]:,}")
col2.metric("Transactions", f"{metrics_df[0][1]:,}")
col3.metric("Total Volume", f"${metrics_df[0][2]:,.0f}")
col4.metric("Avg Transaction", f"${metrics_df[0][3]:,.2f}")

st.markdown("---")

# --- Transactions by Channel ---
st.subheader("Transactions by Channel")
channel_df = session.sql(f"""
    SELECT t.CHANNEL, COUNT(*) AS count, SUM(t.AMOUNT) AS total
    FROM TRANSACTIONS t
    JOIN CUSTOMERS c ON t.CUSTOMER_ID = c.CUSTOMER_ID
    {where_sql}
    GROUP BY t.CHANNEL
    ORDER BY total DESC
""").to_pandas()

st.bar_chart(channel_df.set_index("CHANNEL")["TOTAL"])

# --- Top Products ---
st.subheader("Top Products by Revenue")
product_df = session.sql(f"""
    SELECT p.PRODUCT_NAME, SUM(t.AMOUNT) AS revenue
    FROM TRANSACTIONS t
    JOIN PRODUCTS p ON t.PRODUCT_ID = p.PRODUCT_ID
    JOIN CUSTOMERS c ON t.CUSTOMER_ID = c.CUSTOMER_ID
    {where_sql}
    GROUP BY p.PRODUCT_NAME
    ORDER BY revenue DESC
    LIMIT 10
""").to_pandas()

st.bar_chart(product_df.set_index("PRODUCT_NAME")["REVENUE"])
*/
