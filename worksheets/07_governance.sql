/*
=============================================================================
  SECTION 7: GOVERNANCE WITH HORIZON
  Zero to Snowflake HOL — July 28, 2026
=============================================================================
*/

-- ============================================================
-- PART B: Column-Level Masking
-- ============================================================

-- Exercise 6.1: View sensitive data (before masking)
SELECT
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    ANNUAL_INCOME
FROM CUSTOMERS
LIMIT 10;

-- Exercise 6.2: Create a masking policy for email
CREATE OR REPLACE MASKING POLICY EMAIL_MASK AS (val STRING)
RETURNS STRING ->
    CASE
        WHEN CURRENT_ROLE() LIKE 'TU30_ZERO_TO_SNOWFLAKE_LAB_USER_%'
            THEN val
        ELSE REGEXP_REPLACE(val, '.+@', '****@')
    END;

-- Exercise 6.3: Apply the masking policy
ALTER TABLE CUSTOMERS
    MODIFY COLUMN EMAIL
    SET MASKING POLICY EMAIL_MASK;

-- Exercise 6.4: Create a masking policy for income
CREATE OR REPLACE MASKING POLICY INCOME_MASK AS (val NUMBER)
RETURNS NUMBER ->
    CASE
        WHEN CURRENT_ROLE() LIKE 'TU30_ZERO_TO_SNOWFLAKE_LAB_USER_%'
            THEN val
        ELSE NULL
    END;

ALTER TABLE CUSTOMERS
    MODIFY COLUMN ANNUAL_INCOME
    SET MASKING POLICY INCOME_MASK;

-- Exercise 6.5: Test the masking (your role sees full data)
SELECT CUSTOMER_ID, EMAIL, ANNUAL_INCOME
FROM CUSTOMERS LIMIT 5;

-- ============================================================
-- PART C: Row Access Policies
-- ============================================================

-- Exercise 6.6: Create a row access policy
CREATE OR REPLACE ROW ACCESS POLICY PROVINCE_ACCESS AS (province_val VARCHAR)
RETURNS BOOLEAN ->
    CASE
        WHEN CURRENT_ROLE() LIKE 'TU30_ZERO_TO_SNOWFLAKE_LAB_USER_%'
            THEN TRUE
        ELSE province_val = 'Ontario'
    END;

-- Exercise 6.7: Apply the row access policy
ALTER TABLE CUSTOMERS
    ADD ROW ACCESS POLICY PROVINCE_ACCESS ON (PROVINCE);

-- Exercise 6.8: Verify (your role sees all rows)
SELECT PROVINCE, COUNT(*) AS customer_count
FROM CUSTOMERS
GROUP BY PROVINCE
ORDER BY customer_count DESC;

-- ============================================================
-- PART D: Clean up
-- ============================================================

-- Remove policies
ALTER TABLE CUSTOMERS MODIFY COLUMN EMAIL UNSET MASKING POLICY;
ALTER TABLE CUSTOMERS MODIFY COLUMN ANNUAL_INCOME UNSET MASKING POLICY;
ALTER TABLE CUSTOMERS DROP ROW ACCESS POLICY PROVINCE_ACCESS;

-- Drop policy objects
DROP MASKING POLICY IF EXISTS EMAIL_MASK;
DROP MASKING POLICY IF EXISTS INCOME_MASK;
DROP ROW ACCESS POLICY IF EXISTS PROVINCE_ACCESS;
