import streamlit as st

st.title("6️⃣ Dynamic Tables")

st.markdown("**Duration:** ~20 minutes")

st.markdown("---")

st.header("Objectives")

st.markdown("""
By the end of this section, you will be able to:

- Understand declarative data pipelines with Dynamic Tables
- Create a Dynamic Table that auto-refreshes as source data changes
- Chain Dynamic Tables to build a multi-step pipeline
- Visualize the pipeline DAG in Snowsight
""")

st.markdown("---")

st.header("Part A: What Are Dynamic Tables?")

st.markdown("""
Dynamic Tables let you define a transformation **declaratively** — you write a `SELECT` statement 
describing the desired result, and Snowflake automatically keeps the table up-to-date as source 
data changes. No scheduling, no stored procedures, no orchestration tools needed.
""")

st.info("""
**Key Concept:** You specify a `TARGET_LAG` — the maximum staleness you'll tolerate. Snowflake 
determines the optimal refresh strategy (incremental when possible, full when needed) automatically.
""")

st.markdown("---")

st.header("Part B: Create Your First Dynamic Table")

st.markdown("#### Exercise 6.1 — Set context")

st.code("""
USE ROLE SYSADMIN;
USE WAREHOUSE COMPUTE_WH;
USE DATABASE TU30_CORTEX_ANALYST_LAB;
USE SCHEMA RETAIL_BANKING;
""", language="sql")

st.markdown("#### Exercise 6.2 — Create a summary Dynamic Table")

st.markdown("""
Let's create a Dynamic Table that maintains a real-time summary of transactions by product and channel:
""")

st.code("""
CREATE OR REPLACE DYNAMIC TABLE TRANSACTION_SUMMARY
    TARGET_LAG = '1 minute'
    WAREHOUSE = COMPUTE_WH
AS
SELECT
    p.PRODUCT_NAME,
    p.PRODUCT_CATEGORY,
    t.CHANNEL,
    COUNT(*) AS transaction_count,
    SUM(t.AMOUNT) AS total_amount,
    AVG(t.AMOUNT) AS avg_amount,
    MIN(t.TRANSACTION_DATE) AS earliest_txn,
    MAX(t.TRANSACTION_DATE) AS latest_txn
FROM TRANSACTIONS t
JOIN PRODUCTS p ON t.PRODUCT_ID = p.PRODUCT_ID
GROUP BY p.PRODUCT_NAME, p.PRODUCT_CATEGORY, t.CHANNEL;
""", language="sql")

st.markdown("#### Exercise 6.3 — Query the Dynamic Table")

st.code("""
SELECT * FROM TRANSACTION_SUMMARY
ORDER BY total_amount DESC;
""", language="sql")

st.success("""
**What happened?** Snowflake materialized the query results into a table. If the source 
`TRANSACTIONS` or `PRODUCTS` tables change, this summary will auto-refresh within 1 minute.
""")

st.markdown("---")

st.header("Part C: Chain Dynamic Tables")

st.markdown("""
Dynamic Tables can read from other Dynamic Tables, creating a pipeline (DAG). Let's build 
a second table that ranks products by total revenue:
""")

st.markdown("#### Exercise 6.4 — Create a downstream Dynamic Table")

st.code("""
CREATE OR REPLACE DYNAMIC TABLE PRODUCT_RANKINGS
    TARGET_LAG = '2 minutes'
    WAREHOUSE = COMPUTE_WH
AS
SELECT
    PRODUCT_NAME,
    PRODUCT_CATEGORY,
    SUM(total_amount) AS revenue,
    SUM(transaction_count) AS total_transactions,
    RANK() OVER (ORDER BY SUM(total_amount) DESC) AS revenue_rank
FROM TRANSACTION_SUMMARY
GROUP BY PRODUCT_NAME, PRODUCT_CATEGORY;
""", language="sql")

st.markdown("#### Exercise 6.5 — Query the rankings")

st.code("""
SELECT * FROM PRODUCT_RANKINGS
ORDER BY revenue_rank;
""", language="sql")

st.markdown("---")

st.header("Part D: Simulate a Data Change")

st.markdown("#### Exercise 6.6 — Insert new transactions")

st.code("""
-- Insert some new high-value transactions
INSERT INTO TRANSACTIONS (TRANSACTION_ID, CUSTOMER_ID, PRODUCT_ID, AMOUNT, TRANSACTION_DATE, CHANNEL, TRANSACTION_TYPE)
SELECT
    MAX(TRANSACTION_ID) + SEQ4() + 1,
    1,  -- first customer
    1,  -- first product
    5000.00,
    CURRENT_DATE(),
    'Online',
    'Deposit'
FROM TRANSACTIONS, TABLE(GENERATOR(ROWCOUNT => 3));
""", language="sql")

st.markdown("#### Exercise 6.7 — Watch the pipeline refresh")

st.code("""
-- Wait ~1 minute, then check the summary updated
SELECT * FROM TRANSACTION_SUMMARY
WHERE PRODUCT_NAME = (SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_ID = 1)
ORDER BY total_amount DESC;

-- Check rankings also updated (~2 minutes)
SELECT * FROM PRODUCT_RANKINGS
ORDER BY revenue_rank
LIMIT 5;
""", language="sql")

st.markdown("---")

st.header("Part E: Visualize the DAG")

st.markdown("""
To see your pipeline graph in Snowsight:

1. Navigate to **Data → Databases**
2. Expand `TU30_CORTEX_ANALYST_LAB` → `RETAIL_BANKING` → **Dynamic Tables**
3. Click on `PRODUCT_RANKINGS`
4. Select the **Graph** tab

You'll see the dependency chain: `TRANSACTIONS` → `TRANSACTION_SUMMARY` → `PRODUCT_RANKINGS`
""")

st.markdown("---")

st.header("Part F: Clean up")

st.code("""
DROP DYNAMIC TABLE IF EXISTS PRODUCT_RANKINGS;
DROP DYNAMIC TABLE IF EXISTS TRANSACTION_SUMMARY;

-- Remove the test transactions
DELETE FROM TRANSACTIONS WHERE AMOUNT = 5000.00 AND TRANSACTION_DATE = CURRENT_DATE();
""", language="sql")

st.markdown("---")

st.header("Key Concepts")

st.markdown("""
| Feature | Description |
|---------|-------------|
| `TARGET_LAG` | Maximum allowed staleness (e.g., '1 minute', '1 hour') |
| Incremental refresh | Snowflake processes only changed data when possible |
| DAG visualization | See pipeline dependencies in Snowsight Graph tab |
| No orchestration | No Tasks, no cron — Snowflake handles scheduling |
| Chaining | Dynamic Tables can read from other Dynamic Tables |
""")
