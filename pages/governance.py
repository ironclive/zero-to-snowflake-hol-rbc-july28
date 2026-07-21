import streamlit as st

st.title("7️⃣ Governance with Horizon")

st.markdown("**Duration:** ~20 minutes")

st.markdown("---")

st.header("Objectives")

st.markdown("""
By the end of this section, you will be able to:

- Understand Snowflake's governance framework (Horizon)
- Create and apply a column-level masking policy
- Create and apply a row access policy
- See how policies enforce data protection transparently
""")

st.markdown("---")

st.header("Part A: Governance Overview")

st.markdown("""
Snowflake Horizon provides unified governance across your data estate:

| Capability | Description |
|-----------|-------------|
| **Role-Based Access Control (RBAC)** | Control who can access what objects |
| **Column-Level Masking** | Dynamically mask sensitive columns based on role |
| **Row Access Policies** | Filter rows based on the querying user's role |
| **Data Classification** | Automatically detect PII and sensitive data |
| **Object Tagging** | Label and categorize objects for compliance |
""")

st.info("""
**Banking Relevance:** Financial institutions must comply with regulations like PIPEDA, OSFI guidelines, 
and PCI-DSS. Snowflake's governance features let you enforce data protection rules declaratively — 
without modifying application code or creating separate views for each team.
""")

st.markdown("---")

st.header("Part B: Column-Level Masking")

st.markdown("""
A masking policy dynamically replaces column values at query time based on the role of the user 
running the query. The underlying data is never modified.
""")

st.markdown("#### Exercise 6.1 — Set context")

st.code("""
USE ROLE SYSADMIN;
USE WAREHOUSE COMPUTE_WH;
USE DATABASE TU30_CORTEX_ANALYST_LAB;
USE SCHEMA RETAIL_BANKING;
""", language="sql")

st.markdown("#### Exercise 6.2 — View sensitive data (before masking)")

st.code("""
-- As SYSADMIN, we can see all data
SELECT
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    ANNUAL_INCOME
FROM CUSTOMERS
LIMIT 10;
""", language="sql")

st.markdown("#### Exercise 6.3 — Create a masking policy for email")

st.code("""
CREATE OR REPLACE MASKING POLICY EMAIL_MASK AS (val STRING)
RETURNS STRING ->
    CASE
        WHEN CURRENT_ROLE() IN ('SYSADMIN', 'ACCOUNTADMIN')
            THEN val
        ELSE REGEXP_REPLACE(val, '.+@', '****@')
    END;
""", language="sql")

st.markdown("#### Exercise 6.4 — Apply the masking policy")

st.code("""
ALTER TABLE CUSTOMERS
    MODIFY COLUMN EMAIL
    SET MASKING POLICY EMAIL_MASK;
""", language="sql")

st.markdown("#### Exercise 6.5 — Create a masking policy for income")

st.code("""
CREATE OR REPLACE MASKING POLICY INCOME_MASK AS (val NUMBER)
RETURNS NUMBER ->
    CASE
        WHEN CURRENT_ROLE() IN ('SYSADMIN', 'ACCOUNTADMIN')
            THEN val
        ELSE NULL
    END;

ALTER TABLE CUSTOMERS
    MODIFY COLUMN ANNUAL_INCOME
    SET MASKING POLICY INCOME_MASK;
""", language="sql")

st.markdown("#### Exercise 6.6 — Test the masking (as SYSADMIN)")

st.code("""
-- As SYSADMIN, you still see full data
SELECT CUSTOMER_ID, EMAIL, ANNUAL_INCOME
FROM CUSTOMERS LIMIT 5;
""", language="sql")

st.success("""
**What happened?** As SYSADMIN, you see the real data. If a lower-privilege role queries the same 
table, emails would show as `****@domain.com` and income would show as `NULL` — same table, 
same query, different results based on role.
""")

st.markdown("---")

st.header("Part C: Row Access Policies")

st.markdown("""
Row access policies filter which **rows** a user can see. This is powerful for multi-tenant 
scenarios or restricting access by geography, business unit, or segment.
""")

st.markdown("#### Exercise 6.7 — Create a row access policy")

st.code("""
-- Only allow non-admin roles to see customers in Ontario
CREATE OR REPLACE ROW ACCESS POLICY PROVINCE_ACCESS AS (province_val VARCHAR)
RETURNS BOOLEAN ->
    CASE
        WHEN CURRENT_ROLE() IN ('SYSADMIN', 'ACCOUNTADMIN')
            THEN TRUE
        ELSE province_val = 'Ontario'
    END;
""", language="sql")

st.markdown("#### Exercise 6.8 — Apply the row access policy")

st.code("""
ALTER TABLE CUSTOMERS
    ADD ROW ACCESS POLICY PROVINCE_ACCESS ON (PROVINCE);
""", language="sql")

st.markdown("#### Exercise 6.9 — Verify (as SYSADMIN, all rows visible)")

st.code("""
SELECT PROVINCE, COUNT(*) AS customer_count
FROM CUSTOMERS
GROUP BY PROVINCE
ORDER BY customer_count DESC;
""", language="sql")

st.success("""
**What happened?** As SYSADMIN, you see all provinces. A restricted role would only see Ontario 
customers — the other rows are silently filtered out. No errors, no empty results messaging — 
the user simply never sees data they shouldn't.
""")

st.markdown("---")

st.header("Part D: Clean up")

st.code("""
-- Remove policies
ALTER TABLE CUSTOMERS MODIFY COLUMN EMAIL UNSET MASKING POLICY;
ALTER TABLE CUSTOMERS MODIFY COLUMN ANNUAL_INCOME UNSET MASKING POLICY;
ALTER TABLE CUSTOMERS DROP ROW ACCESS POLICY PROVINCE_ACCESS;

-- Drop policy objects
DROP MASKING POLICY IF EXISTS EMAIL_MASK;
DROP MASKING POLICY IF EXISTS INCOME_MASK;
DROP ROW ACCESS POLICY IF EXISTS PROVINCE_ACCESS;
""", language="sql")

st.markdown("---")

with st.expander("🤖 CoCo Sneak Peek — Do this with Cortex Code"):
    st.markdown("""
CoCo can create governance policies from plain English:

| What you did | CoCo prompt |
|-------------|-------------|
| Create email mask | `Create a masking policy that hides email addresses for non-admin roles` |
| Create income mask | `Mask the ANNUAL_INCOME column so only SYSADMIN and ACCOUNTADMIN can see it` |
| Apply policies | `Apply the email mask to CUSTOMERS.EMAIL` |
| Row access policy | `Create a row access policy so non-admin roles can only see Ontario customers` |
| Test policies | `Query CUSTOMERS as SYSADMIN and show me EMAIL and ANNUAL_INCOME` |
| Clean up | `Remove all masking and row access policies from CUSTOMERS` |

You can also ask: `What governance policies are applied to the CUSTOMERS table?`
""")

st.markdown("---")

st.header("Key Concepts")

st.markdown("""
| Feature | Description |
|---------|-------------|
| Masking Policy | Dynamically redacts column values based on role |
| Row Access Policy | Silently filters rows based on session context |
| Declarative | Policies are applied once, enforced everywhere |
| No data duplication | One table, many access levels |
| Centralized | Policies defined once, applied to any table/column |
""")
