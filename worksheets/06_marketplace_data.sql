/*
=============================================================================
  SECTION 6: MARKETPLACE DATA
  Zero to Snowflake HOL — July 28, 2026
  
  NOTE: The Marketplace subscription is done through the Snowsight UI,
  not via SQL. Follow the steps in the HOL guide to subscribe first.
=============================================================================
*/

-- ============================================================
-- PART C: Explore the Marketplace Data
-- (Run AFTER subscribing to "Snowflake Public Data (Free)")
-- ============================================================

-- Step 1: See what schemas are available
SHOW SCHEMAS IN DATABASE SNOWFLAKE_PUBLIC_DATA_FREE;

-- Explore the FINANCE schema (if available)
SHOW TABLES IN SCHEMA SNOWFLAKE_PUBLIC_DATA_FREE.FINANCE;

-- Or explore all schemas
SHOW TABLES IN DATABASE SNOWFLAKE_PUBLIC_DATA_FREE;

-- Step 2: Preview some data
SELECT *
FROM SNOWFLAKE_PUBLIC_DATA_FREE.FINANCE.SEI_DAILY_STOCK_PRICING_WITH_ANALYTICS
LIMIT 20;

-- ============================================================
-- PART D: Enrich Your Banking Data
-- ============================================================

-- Customer distribution by province (internal)
-- Ready to join with provincial economic indicators (external)
SELECT C.PROVINCE,
       COUNT(*) AS customer_count,
       AVG(C.ANNUAL_INCOME) AS avg_income,
       AVG(C.CREDIT_SCORE) AS avg_credit_score,
       SUM(T.AMOUNT) AS total_transaction_volume
FROM RETAIL_BANKING.CUSTOMERS C
JOIN RETAIL_BANKING.TRANSACTIONS T ON C.CUSTOMER_ID = T.CUSTOMER_ID
GROUP BY C.PROVINCE
ORDER BY total_transaction_volume DESC;
