import streamlit as st

st.title("🖥️ The Snowflake UI Tour")
st.markdown("**Duration:** ~20 minutes")
st.markdown("---")

st.markdown("""
## Objectives

By the end of this section, you will be able to:
- Log in to Snowsight (Snowflake's web UI)
- Navigate the key areas: Worksheets, Databases, Warehouses, Marketplace
- Create and configure a worksheet
- Set your session context (role, warehouse, database, schema)
- Browse database objects and preview table data
""")

st.markdown("---")

st.markdown("""
## Step 1: Log in to Snowsight

1. Open your Snowflake account URL in a browser.
2. Enter your **username** and **password**.
3. You will land on the **Home** page.

> 💡 **Tip:** Bookmark your Snowflake URL for quick access.
""")

st.markdown("---")

st.markdown("""
## Step 2: Explore the Left Navigation

Take a moment to explore the left sidebar:

| Section | What It Contains |
|---------|-----------------|
| **Projects → Worksheets** | SQL editor — where you'll spend most of your time |
| **Projects → Dashboards** | Visual dashboards built from queries |
| **Data → Databases** | Browse all databases, schemas, tables, views |
| **Data Products → Marketplace** | Free and paid data listings from providers |
| **Monitoring → Query History** | All queries run in your account |
| **Admin → Warehouses** | Compute resources (virtual warehouses) |
| **Admin → Users & Roles** | Identity and access management |
""")

st.markdown("---")

st.markdown("""
## Step 3: Create a New Worksheet

1. Click **Projects → Worksheets** in the left nav.
2. Click the **+ Worksheet** button (top right).
3. A new SQL worksheet opens.

> 📝 **Name your worksheet** by clicking the auto-generated name at the top and renaming it to: `Zero to Snowflake Lab`
""")

st.markdown("---")

st.markdown("""
## Step 4: Set Your Context

In your new worksheet, set the session context by running:
""")

st.code("""
USE ROLE SYSADMIN;
USE WAREHOUSE COMPUTE_WH;
USE DATABASE TU30_CORTEX_ANALYST_LAB;
USE SCHEMA RETAIL_BANKING;
""", language="sql")

st.info("💡 You can also set context using the dropdowns at the top of the worksheet.")

st.markdown("---")

st.markdown("""
## Step 5: Browse the Data

Navigate to **Data → Databases** and drill into:

```
TU30_CORTEX_ANALYST_LAB → RETAIL_BANKING → Tables
```

You should see three tables: **CUSTOMERS**, **PRODUCTS**, **TRANSACTIONS**.

Click on any table to see:
- **Columns** — data types and structure
- **Data Preview** — sample rows (no query required!)
- **Details** — row count, size, owner
""")

st.markdown("---")

st.markdown("""
## Step 6: Quick Preview from the Worksheet

Back in your worksheet, run these quick queries to confirm your data is ready:
""")

st.code("""
-- How many customers?
SELECT COUNT(*) AS customer_count FROM CUSTOMERS;

-- How many products?
SELECT COUNT(*) AS product_count FROM PRODUCTS;

-- How many transactions?
SELECT COUNT(*) AS transaction_count FROM TRANSACTIONS;
""", language="sql")

st.success("""
**Expected Results:**
- Customers: 500
- Products: 15  
- Transactions: 1,000
""")

st.markdown("---")

with st.expander("🤖 CoCo Sneak Peek — Do this with Cortex Code"):
    st.markdown("""
Instead of navigating the UI manually, you could ask **Cortex Code (CoCo)** to do it for you:

| What you did | CoCo prompt |
|-------------|-------------|
| Set context | `Use role SYSADMIN, warehouse COMPUTE_WH, database TU30_CORTEX_ANALYST_LAB, schema RETAIL_BANKING` |
| Browse tables | `What tables are in my current schema?` |
| Preview data | `Show me the first 10 rows of CUSTOMERS` |
| Check row counts | `How many rows are in each table in RETAIL_BANKING?` |
| Explore columns | `Describe the TRANSACTIONS table` |

CoCo executes SQL on your behalf and returns formatted results — no worksheet needed.
""")

st.markdown("---")

st.markdown("""
## ✅ Section Complete!

You've successfully:
- Logged into Snowsight
- Navigated the UI
- Created a worksheet and set your context
- Confirmed access to the retail banking data

**Next →** Head to **Section 2: Querying & Analytics** to start writing real queries.
""")
