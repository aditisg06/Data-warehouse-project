import pyodbc
from config import DB_CONFIG
from logger import get_logger

logger = get_logger("validator")

def get_connection():
    conn_str = (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

def check_row_count(cursor, table_name, expected_min=1):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    if count >= expected_min:
        logger.info(f"  ✓ {table_name}: {count} rows")
        return True
    else:
        logger.warning(f"  ✗ {table_name}: only {count} rows")
        return False

def check_nulls(cursor, table_name, column_name):
    cursor.execute(f"""
        SELECT COUNT(*) FROM {table_name}
        WHERE {column_name} IS NULL
    """)
    null_count = cursor.fetchone()[0]
    if null_count == 0:
        logger.info(f"  ✓ {table_name}.{column_name}: no nulls")
        return True
    else:
        logger.warning(f"  ✗ {table_name}.{column_name}: {null_count} nulls found")
        return False

def check_duplicates(cursor, table_name, key_column):
    cursor.execute(f"""
        SELECT COUNT(*) FROM (
            SELECT {key_column}, COUNT(*) as cnt
            FROM {table_name}
            GROUP BY {key_column}
            HAVING COUNT(*) > 1
        ) duplicates
    """)
    dup_count = cursor.fetchone()[0]
    if dup_count == 0:
        logger.info(f"  ✓ {table_name}.{key_column}: no duplicates")
        return True
    else:
        logger.warning(f"  ✗ {table_name}.{key_column}: {dup_count} duplicates found")
        return False

def validate_bronze(cursor):
    logger.info("--- Validating Bronze Layer ---")
    results = []
    # Replace with your actual Bronze table names
    results.append(check_row_count(cursor, "bronze.crm_cust_info"))
    results.append(check_row_count(cursor, "bronze.crm_prd_info"))
    results.append(check_row_count(cursor, "bronze.erp_cust_az12"))
    return all(results)

def validate_silver(cursor):
    logger.info("--- Validating Silver Layer ---")
    results = []
    # Replace with your actual Silver table names and key columns
    results.append(check_row_count(cursor, "silver.crm_cust_info"))
    results.append(check_nulls(cursor, "silver.crm_cust_info", "cst_id"))
    results.append(check_duplicates(cursor, "silver.crm_cust_info", "cst_id"))
    results.append(check_row_count(cursor, "silver.crm_prd_info"))
    results.append(check_nulls(cursor, "silver.crm_prd_info", "prd_id"))
    return all(results)

def validate_gold(cursor):
    logger.info("--- Validating Gold Layer ---")
    results = []
    # Replace with your actual Gold table names
    results.append(check_row_count(cursor, "gold.fact_sales"))
    results.append(check_nulls(cursor, "gold.fact_sales", "customer_key"))
    results.append(check_nulls(cursor, "gold.fact_sales", "product_key"))
    results.append(check_row_count(cursor, "gold.dim_customers"))
    results.append(check_row_count(cursor, "gold.dim_products"))
    return all(results)

def run_all_validations():
    logger.info("=" * 50)
    logger.info("Starting Data Quality Validation")
    logger.info("=" * 50)
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        bronze_ok = validate_bronze(cursor)
        silver_ok = validate_silver(cursor)
        gold_ok = validate_gold(cursor)
        
        logger.info("=" * 50)
        if bronze_ok and silver_ok and gold_ok:
            logger.info("ALL VALIDATIONS PASSED ✓")
        else:
            logger.warning("SOME VALIDATIONS FAILED — check logs above")
        logger.info("=" * 50)
        
    except Exception as e:
        logger.error(f"Validation error: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_all_validations()

