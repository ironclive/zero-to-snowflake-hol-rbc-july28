/*
=============================================================================
  ZERO TO SNOWFLAKE HOL — PARTICIPANT ENVIRONMENT SETUP
  Run as: ACCOUNTADMIN (or SECURITYADMIN + SYSADMIN)
  
  This script creates:
    - 30 roles (HOL_USER_01 .. HOL_USER_30)
    - 30 schemas cloned from RETAIL_BANKING (RETAIL_BANKING_01 .. _30)
    - All necessary grants for every exercise in the HOL
    
  Run this ONCE before the lab starts in each sandbox (AWS / AZ).
=============================================================================
*/

-- ============================================================
-- CONFIGURATION
-- ============================================================
SET DB_NAME       = 'TU30_CORTEX_ANALYST_LAB';
SET SOURCE_SCHEMA = 'RETAIL_BANKING';
SET WAREHOUSE     = 'TU30_CORTEX_ANALYST_LAB_VWH';
SET NUM_USERS     = 30;

USE ROLE ACCOUNTADMIN;

-- ============================================================
-- STEP 1: Create the warehouse (if not exists)
-- ============================================================
CREATE WAREHOUSE IF NOT EXISTS IDENTIFIER($WAREHOUSE)
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND   = 60
    AUTO_RESUME    = TRUE
    INITIALLY_SUSPENDED = TRUE;

-- ============================================================
-- STEP 2: Create roles and schemas in a loop
-- ============================================================

BEGIN
    LET i INTEGER := 1;
    LET role_name VARCHAR;
    LET schema_name VARCHAR;
    LET user_name VARCHAR;
    
    FOR i IN 1 TO $NUM_USERS DO
        role_name   := 'HOL_USER_' || LPAD(i::VARCHAR, 2, '0');
        schema_name := $SOURCE_SCHEMA || '_' || LPAD(i::VARCHAR, 2, '0');
        
        -- Create the role
        EXECUTE IMMEDIATE 'CREATE ROLE IF NOT EXISTS ' || role_name;
        
        -- Grant role to SYSADMIN (so admins can manage)
        EXECUTE IMMEDIATE 'GRANT ROLE ' || role_name || ' TO ROLE SYSADMIN';
        
        -- Clone the schema (instant, zero storage)
        EXECUTE IMMEDIATE 'CREATE SCHEMA IF NOT EXISTS ' || $DB_NAME || '.' || schema_name || ' CLONE ' || $DB_NAME || '.' || $SOURCE_SCHEMA;
        
        -- ============================================================
        -- GRANTS: Database level
        -- ============================================================
        -- USAGE on database
        EXECUTE IMMEDIATE 'GRANT USAGE ON DATABASE ' || $DB_NAME || ' TO ROLE ' || role_name;
        
        -- ============================================================
        -- GRANTS: Schema level (OWNERSHIP of their schema)
        -- ============================================================
        -- Transfer ownership of the cloned schema to the participant role
        -- This covers: CREATE TABLE, CREATE DYNAMIC TABLE, CREATE VIEW,
        --              CREATE MASKING POLICY, CREATE ROW ACCESS POLICY,
        --              CREATE STREAMLIT, ALTER TABLE, DROP TABLE, etc.
        EXECUTE IMMEDIATE 'GRANT OWNERSHIP ON SCHEMA ' || $DB_NAME || '.' || schema_name || ' TO ROLE ' || role_name || ' REVOKE CURRENT GRANTS';
        
        -- Grant ownership on ALL tables in the schema (cloned tables)
        EXECUTE IMMEDIATE 'GRANT OWNERSHIP ON ALL TABLES IN SCHEMA ' || $DB_NAME || '.' || schema_name || ' TO ROLE ' || role_name || ' REVOKE CURRENT GRANTS';
        
        -- ============================================================
        -- GRANTS: Warehouse
        -- ============================================================
        -- USAGE = can run queries; OPERATE = can suspend/resume (Section 3)
        EXECUTE IMMEDIATE 'GRANT USAGE, OPERATE ON WAREHOUSE ' || $WAREHOUSE || ' TO ROLE ' || role_name;
        
        -- ============================================================
        -- GRANTS: Source schema (read-only, for reference)
        -- ============================================================
        EXECUTE IMMEDIATE 'GRANT USAGE ON SCHEMA ' || $DB_NAME || '.' || $SOURCE_SCHEMA || ' TO ROLE ' || role_name;
        EXECUTE IMMEDIATE 'GRANT SELECT ON ALL TABLES IN SCHEMA ' || $DB_NAME || '.' || $SOURCE_SCHEMA || ' TO ROLE ' || role_name;
        
        -- ============================================================
        -- GRANTS: Marketplace data (Section 6)
        -- The marketplace DB is created during the lab via "Get" button.
        -- Once created, run the marketplace grant script below.
        -- ============================================================
        
    END FOR;
END;

-- ============================================================
-- STEP 3: Marketplace grants (run AFTER subscribing to listing)
-- Uncomment and run after "Snowflake Public Data (Free)" is subscribed
-- ============================================================
/*
SET MARKETPLACE_DB = 'SNOWFLAKE_PUBLIC_DATA_FREE';

BEGIN
    LET i INTEGER := 1;
    LET role_name VARCHAR;
    
    FOR i IN 1 TO $NUM_USERS DO
        role_name := 'HOL_USER_' || LPAD(i::VARCHAR, 2, '0');
        EXECUTE IMMEDIATE 'GRANT IMPORTED PRIVILEGES ON DATABASE ' || $MARKETPLACE_DB || ' TO ROLE ' || role_name;
    END FOR;
END;
*/

-- ============================================================
-- STEP 4: Assign roles to users
-- Run this for each participant, mapping their Snowflake username
-- to their assigned role number.
--
-- Example:
--   GRANT ROLE HOL_USER_01 TO USER participant1_username;
--   GRANT ROLE HOL_USER_01 TO USER participant1_username;
--
-- Or bulk assign (if using sequential usernames like HOL_USER1..30):
-- ============================================================
/*
BEGIN
    LET i INTEGER := 1;
    LET role_name VARCHAR;
    LET user_name VARCHAR;
    
    FOR i IN 1 TO $NUM_USERS DO
        role_name := 'HOL_USER_' || LPAD(i::VARCHAR, 2, '0');
        user_name := 'HOL_PARTICIPANT_' || LPAD(i::VARCHAR, 2, '0');
        EXECUTE IMMEDIATE 'GRANT ROLE ' || role_name || ' TO USER ' || user_name;
    END FOR;
END;
*/

-- ============================================================
-- VERIFICATION: Check that everything was created
-- ============================================================
SHOW ROLES LIKE 'HOL_USER_%';
SHOW SCHEMAS IN DATABASE TU30_CORTEX_ANALYST_LAB STARTS WITH 'RETAIL_BANKING_';

-- ============================================================
-- SUMMARY OF GRANTS PER ROLE
-- ============================================================
-- Each HOL_USER_XX role has:
--
-- DATABASE LEVEL:
--   ✅ USAGE on TU30_CORTEX_ANALYST_LAB
--
-- THEIR SCHEMA (RETAIL_BANKING_XX):
--   ✅ OWNERSHIP — full control of all objects within
--      Covers: SELECT, INSERT, UPDATE, DELETE on tables
--              CREATE/DROP TABLE, VIEW, DYNAMIC TABLE
--              CREATE/DROP MASKING POLICY, ROW ACCESS POLICY
--              CREATE STREAMLIT
--              ALTER TABLE (apply/remove policies)
--              DROP TABLE + UNDROP TABLE (Time Travel)
--
-- SOURCE SCHEMA (RETAIL_BANKING):
--   ✅ USAGE + SELECT (read-only reference)
--
-- WAREHOUSE (TU30_CORTEX_ANALYST_LAB_VWH):
--   ✅ USAGE (run queries)
--   ✅ OPERATE (suspend/resume for cache exercise)
--
-- MARKETPLACE DB (after subscription):
--   ✅ IMPORTED PRIVILEGES (query shared data)
--
-- ============================================================


-- ============================================================
-- TEARDOWN (run AFTER the lab to clean up)
-- ============================================================
/*
USE ROLE ACCOUNTADMIN;

BEGIN
    LET i INTEGER := 1;
    LET role_name VARCHAR;
    LET schema_name VARCHAR;
    
    FOR i IN 1 TO 30 DO
        role_name   := 'HOL_USER_' || LPAD(i::VARCHAR, 2, '0');
        schema_name := 'RETAIL_BANKING_' || LPAD(i::VARCHAR, 2, '0');
        
        -- Drop schema (CASCADE drops all objects inside)
        EXECUTE IMMEDIATE 'DROP SCHEMA IF EXISTS TU30_CORTEX_ANALYST_LAB.' || schema_name || ' CASCADE';
        
        -- Drop role
        EXECUTE IMMEDIATE 'DROP ROLE IF EXISTS ' || role_name;
    END FOR;
END;
*/
