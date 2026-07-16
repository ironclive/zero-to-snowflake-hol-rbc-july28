import streamlit as st

st.title("5️⃣ Time Travel & UNDROP")

st.markdown("**Duration:** ~15 minutes")

st.markdown("---")

st.header("Objectives")

st.markdown("""
By the end of this section, you will be able to:

- Understand Snowflake's Time Travel capability
- Query historical data using `AT` and `BEFORE` clauses
- Recover a dropped table instantly with `UNDROP`
- Appreciate how Time Travel supports data recovery without backups
""")

st.markdown("---")

st.header("Part A: Understanding Time Travel")

st.markdown("""
Snowflake automatically retains historical versions of your data for a configurable retention period 
(default: 1 day for Standard, up to 90 days for Enterprise+). This means you can query data **as it existed 
at any point** within that window — no snapshots or backups required.
""")

st.info("""
**Key Concept:** Time Travel operates at the micro-partition level. When data changes, Snowflake 
preserves the old micro-partitions for the retention period, enabling point-in-time queries at no 
additional configuration cost.
""")

st.markdown("---")

st.header("Part B: Querying Historical Data")

st.markdown("#### Exercise 5.1 — Check current row count")

st.code("""
USE ROLE SYSADMIN;
USE WAREHOUSE COMPUTE_WH;
USE DATABASE TU30_CORTEX_ANALYST_LAB;
USE SCHEMA RETAIL_BANKING;

SELECT COUNT(*) AS current_count FROM CUSTOMERS;
""", language="sql")

st.markdown("#### Exercise 5.2 — Delete some rows")

st.code("""
-- Delete customers in a specific segment
DELETE FROM CUSTOMERS
WHERE SEGMENT = 'Youth';

-- Confirm the delete
SELECT COUNT(*) AS after_delete FROM CUSTOMERS;
""", language="sql")

st.markdown("#### Exercise 5.3 — Query the table BEFORE the delete")

st.code("""
-- Query the table as it was 5 minutes ago
SELECT COUNT(*) AS before_delete
FROM CUSTOMERS AT(OFFSET => -60*5);
""", language="sql")

st.success("""
**What happened?** Even though we deleted rows, Snowflake still has the previous version of the data. 
The `AT(OFFSET => -300)` clause queries the table as it existed 300 seconds (5 minutes) ago.
""")

st.markdown("#### Exercise 5.4 — Restore the deleted data")

st.code("""
-- Re-insert the deleted rows from the historical version
INSERT INTO CUSTOMERS
SELECT * FROM CUSTOMERS AT(OFFSET => -60*5)
WHERE SEGMENT = 'Youth';

-- Verify restoration
SELECT COUNT(*) AS restored_count FROM CUSTOMERS;
""", language="sql")

st.markdown("---")

st.header("Part C: UNDROP a Table")

st.markdown("#### Exercise 5.5 — Accidentally drop a table")

st.code("""
-- Create a clone to experiment with safely
CREATE TABLE CUSTOMERS_BACKUP CLONE CUSTOMERS;

-- Oops! Drop the backup
DROP TABLE CUSTOMERS_BACKUP;

-- Verify it's gone
SHOW TABLES LIKE 'CUSTOMERS_BACKUP';
""", language="sql")

st.markdown("#### Exercise 5.6 — Recover with UNDROP")

st.code("""
-- Instantly restore the dropped table
UNDROP TABLE CUSTOMERS_BACKUP;

-- Verify it's back
SELECT COUNT(*) FROM CUSTOMERS_BACKUP;
""", language="sql")

st.success("""
**Key Takeaway:** `UNDROP` restores a dropped table to its exact state before deletion — instantly, 
with no restore-from-backup process. This works for tables, schemas, and entire databases.
""")

st.markdown("#### Exercise 5.7 — Clean up")

st.code("""
DROP TABLE CUSTOMERS_BACKUP;
""", language="sql")

st.markdown("---")

st.header("Key Concepts")

st.markdown("""
| Feature | Description |
|---------|-------------|
| `AT(OFFSET => -N)` | Query data as it was N seconds ago |
| `AT(TIMESTAMP => '...')` | Query data at a specific timestamp |
| `BEFORE(STATEMENT => 'id')` | Query data before a specific query ran |
| `UNDROP TABLE/SCHEMA/DATABASE` | Instantly recover dropped objects |
| Retention period | 1 day (Standard) / up to 90 days (Enterprise+) |
""")
