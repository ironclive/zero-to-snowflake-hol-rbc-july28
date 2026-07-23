import streamlit as st

st.title("🚀 Getting Started")

st.markdown("Complete these steps before beginning the lab exercises.")

st.markdown("---")

st.header("Step 1: Log in to Snowflake")

st.info("""
Your instructor will provide you with:
- A **Snowflake account URL** (either the AWS or Azure sandbox)
- Your **username** and **password**

Open the account URL in your browser and log in with the credentials provided.
""")

st.markdown("---")

st.header("Step 2: Pick your seat number")

st.markdown("""
Each participant gets their own isolated workspace. Look at the **seat number** displayed at your 
workstation (01–30). This is your number for the entire lab.
""")

st.warning("Remember your number! You'll use it in every section.")

st.markdown("---")

st.header("Step 3: Set your context")

st.markdown("""
Open a **SQL Worksheet** (Projects → Worksheets → + Worksheet) and run the following, replacing 
`XX` with your two-digit seat number (e.g., `03`, `14`, `27`):
""")

st.code("""
USE ROLE HOL_USER_XX;              -- e.g., HOL_USER_03
USE WAREHOUSE ZERO_TO_SNOWFLAKE_HOL_WH;
USE DATABASE ZERO_TO_SNOWFLAKE_HOL;
USE SCHEMA RETAIL_BANKING_XX;      -- e.g., RETAIL_BANKING_03
""", language="sql")

st.info("""
**What this does:**
- **Role** — Your dedicated role with full access to your workspace
- **Warehouse** — Shared compute engine (auto-starts when you run a query)
- **Database** — The lab database containing all participant schemas
- **Schema** — Your isolated copy of the banking data (500 customers, 15 products, 1,000 transactions)
""")

st.markdown("---")

st.header("Step 4: Verify your setup")

st.markdown("Run this quick check to confirm everything is working:")

st.code("""
SELECT CURRENT_ROLE() AS my_role,
       CURRENT_WAREHOUSE() AS my_warehouse,
       CURRENT_DATABASE() AS my_database,
       CURRENT_SCHEMA() AS my_schema;
""", language="sql")

st.success("""
**Expected result:**

| my_role | my_warehouse | my_database | my_schema |
|---------|-------------|-------------|-----------|
| HOL_USER_XX | ZERO_TO_SNOWFLAKE_HOL_WH | ZERO_TO_SNOWFLAKE_HOL | RETAIL_BANKING_XX |
""")

st.markdown("Run a quick data check:")

st.code("""
SELECT 'CUSTOMERS' AS table_name, COUNT(*) AS rows FROM CUSTOMERS
UNION ALL
SELECT 'PRODUCTS', COUNT(*) FROM PRODUCTS
UNION ALL
SELECT 'TRANSACTIONS', COUNT(*) FROM TRANSACTIONS;
""", language="sql")

st.success("""
**Expected result:** CUSTOMERS = 500, PRODUCTS = 15, TRANSACTIONS = 1,000
""")

st.markdown("---")

st.header("Step 5: Keep this guide open")

st.markdown("""
Keep this browser tab open throughout the lab:

👉 **https://zero-to-sf-hol-rbc-july28.streamlit.app**

Use the sidebar to navigate between sections. Each section has:
- A **concept intro** explaining what you'll learn
- **Numbered exercises** with SQL to copy and run
- A **CoCo Sneak Peek** showing how Cortex Code could do it for you
""")

st.markdown("---")

st.success("""
## ✅ You're ready!

Head to **Section 1: Snowflake UI Tour** to begin the lab.
""")
