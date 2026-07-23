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

st.header("Step 2: Find your assigned number")

st.markdown("""
Each participant has a pre-assigned number and workspace. Find your name below and note your **number** — 
you'll use it throughout the entire lab.
""")

st.dataframe(
    {
        "#": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
              "21", "22", "23"],
        "Name": [
            "Azer, David",
            "Das, Asesh",
            "Deng, Yuhan",
            "Guo, Charlie",
            "He, Shuntian",
            "Kichler, Aaron",
            "Lakshminarayanan, Prithvi",
            "Liu, Shally S",
            "Malik, Jamshed",
            "Rehal, Manisha",
            "Chellappan, Dinesh",
            "Shaikh, Anaan",
            "Kundu, Sujoy",
            "Villar, Cesar",
            "Lingaratnam, Anojan",
            "Karbasi, Payam",
            "Terlecky, Stephen",
            "Yadav, Sachinkumar",
            "Chen, Yan",
            "Walimbe, Sharwari",
            "Braga, Antony",
            "Mohanan, Sukanya",
            "Wong, Sam",
        ],
        "Role": [
            "HOL_USER_01", "HOL_USER_02", "HOL_USER_03", "HOL_USER_04",
            "HOL_USER_05", "HOL_USER_06", "HOL_USER_07", "HOL_USER_08",
            "HOL_USER_09", "HOL_USER_10", "HOL_USER_11", "HOL_USER_12",
            "HOL_USER_13", "HOL_USER_14", "HOL_USER_15", "HOL_USER_16",
            "HOL_USER_17", "HOL_USER_18", "HOL_USER_19", "HOL_USER_20",
            "HOL_USER_21", "HOL_USER_22", "HOL_USER_23",
        ],
        "Schema": [
            "RETAIL_BANKING_01", "RETAIL_BANKING_02", "RETAIL_BANKING_03",
            "RETAIL_BANKING_04", "RETAIL_BANKING_05", "RETAIL_BANKING_06",
            "RETAIL_BANKING_07", "RETAIL_BANKING_08", "RETAIL_BANKING_09",
            "RETAIL_BANKING_10", "RETAIL_BANKING_11", "RETAIL_BANKING_12",
            "RETAIL_BANKING_13", "RETAIL_BANKING_14", "RETAIL_BANKING_15",
            "RETAIL_BANKING_16", "RETAIL_BANKING_17", "RETAIL_BANKING_18",
            "RETAIL_BANKING_19", "RETAIL_BANKING_20", "RETAIL_BANKING_21",
            "RETAIL_BANKING_22", "RETAIL_BANKING_23",
        ],
    },
    use_container_width=True,
    hide_index=True,
)

st.warning("Use **your assigned number** in every `USE ROLE` and `USE SCHEMA` command throughout the lab.")

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
