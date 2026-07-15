import streamlit as st

st.set_page_config(page_title="3. Results Cache & Cloning", page_icon="❄️", layout="wide")

st.title("3️⃣ Results Cache & Cloning")
st.markdown("**Duration:** ~20 minutes")
st.markdown("---")

st.markdown("""
## Objectives

By the end of this section, you will be able to:
- Understand Snowflake's multi-layer caching architecture
- Observe the results cache in action (sub-second repeat queries)
- Create a zero-copy clone of a schema
- Demonstrate that clones are independent from the source
""")

st.markdown("---")

st.header("Part A: The Results Cache")

st.markdown("""
### How Snowflake Caching Works

Snowflake has **three layers** of caching:

| Cache Layer | Scope | Duration | Cost |
|-------------|-------|----------|------|
| **Metadata Cache** | COUNT, MIN, MAX on columns | Indefinite | Free (no warehouse) |
| **Results Cache** | Exact same query, same data | 24 hours | Free (no warehouse) |
| **Warehouse Cache** | Data loaded into local SSD | Until warehouse suspends | Warehouse running |

### Exercise: Observe the Results Cache
""")

st.markdown("**Step 1:** Run this query and note the execution time in the **Query Profile**:")

st.code("""
SELECT C.SEGMENT,
       COUNT(DISTINCT T.CUSTOMER_ID) AS active_customers,
       SUM(T.AMOUNT) AS total_volume
FROM TRANSACTIONS T
JOIN CUSTOMERS C ON T.CUSTOMER_ID = C.CUSTOMER_ID
GROUP BY C.SEGMENT
ORDER BY total_volume DESC;
""", language="sql")

st.markdown("**Step 2:** Run the **exact same query** again immediately.")

st.info("""
💡 **What to observe:**
- The second run should complete in **milliseconds** (vs. seconds for the first)
- In the Query Profile, you'll see: `QUERY_RESULT_REUSE = true`
- No warehouse compute was consumed for the repeat query!
""")

st.markdown("**Step 3:** Now modify the query slightly (e.g., change the ORDER BY) and run again:")

st.code("""
SELECT C.SEGMENT,
       COUNT(DISTINCT T.CUSTOMER_ID) AS active_customers,
       SUM(T.AMOUNT) AS total_volume
FROM TRANSACTIONS T
JOIN CUSTOMERS C ON T.CUSTOMER_ID = C.CUSTOMER_ID
GROUP BY C.SEGMENT
ORDER BY active_customers DESC;  -- Changed!
""", language="sql")

st.warning("⚠️ The cache is **not reused** — even a minor change creates a different query hash.")

st.markdown("---")

st.markdown("""
### Exercise: Metadata Cache

Some queries don't need a warehouse at all. Try these with your warehouse **suspended**:
""")

st.code("""
-- Suspend your warehouse first
ALTER WAREHOUSE COMPUTE_WH SUSPEND;

-- These still work (metadata cache)!
SELECT COUNT(*) FROM CUSTOMERS;
SELECT MIN(TRANSACTION_DATE) FROM TRANSACTIONS;
SELECT MAX(AMOUNT) FROM TRANSACTIONS;
""", language="sql")

st.success("These queries return instantly because Snowflake stores metadata (row counts, min/max) automatically.")

st.code("""
-- Resume the warehouse for the next exercises
ALTER WAREHOUSE COMPUTE_WH RESUME;
""", language="sql")

st.markdown("---")

st.header("Part B: Zero-Copy Cloning")

st.markdown("""
### What is Zero-Copy Cloning?

Cloning creates a **copy** of a database, schema, or table that:
- Is **instant** (regardless of data size)
- Consumes **no additional storage** (until changes are made)
- Is **fully independent** — changes to the clone don't affect the original

This is incredibly powerful for:
- Development & testing
- Experimentation without risk
- Point-in-time snapshots
""")

st.markdown("### Exercise: Clone and Modify")

st.markdown("**Step 1:** Clone the entire RETAIL_BANKING schema:")

st.code("""
CREATE SCHEMA TU30_CORTEX_ANALYST_LAB.RETAIL_BANKING_CLONE
  CLONE TU30_CORTEX_ANALYST_LAB.RETAIL_BANKING;
""", language="sql")

st.markdown("**Step 2:** Verify the clone has the same data:")

st.code("""
SELECT COUNT(*) FROM RETAIL_BANKING_CLONE.CUSTOMERS;
-- Should return 500

SELECT COUNT(*) FROM RETAIL_BANKING_CLONE.TRANSACTIONS;
-- Should return 1000
""", language="sql")

st.markdown("**Step 3:** Make a change in the clone (delete some rows):")

st.code("""
DELETE FROM RETAIL_BANKING_CLONE.CUSTOMERS
WHERE PROVINCE = 'Alberta';

-- Check the count
SELECT COUNT(*) FROM RETAIL_BANKING_CLONE.CUSTOMERS;
""", language="sql")

st.markdown("**Step 4:** Confirm the original is **unaffected**:")

st.code("""
SELECT COUNT(*) FROM RETAIL_BANKING.CUSTOMERS;
-- Still 500!
""", language="sql")

st.success("The original data is completely untouched. This is the power of zero-copy cloning.")

st.markdown("**Step 5:** Clean up — drop the clone:")

st.code("""
DROP SCHEMA TU30_CORTEX_ANALYST_LAB.RETAIL_BANKING_CLONE;
""", language="sql")

st.markdown("---")

st.success("""
## ✅ Section Complete!

You've learned:
- Snowflake's 3-layer caching automatically accelerates repeated queries
- The results cache saves compute costs on identical queries
- Zero-copy cloning creates instant, independent copies of data
- Clones are perfect for safe experimentation

**Next →** Head to **Section 4: Marketplace Data** to bring in external data.
""")
