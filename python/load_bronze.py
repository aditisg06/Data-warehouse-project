import pyodbc
import time
from config import DB_CONFIG
from logger import get_logger

logger = get_logger("bronze_loader")

def get_connection():
    conn_str = (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

def load_bronze():
    logger.info("=" * 50)
    logger.info("Starting Bronze Layer Load")
    logger.info("=" * 50)
    
    start_time = time.time()
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        logger.info("Executing Bronze stored procedure...")
        cursor.execute("EXEC bronze.load_bronze")
        conn.commit()
        
        elapsed = round(time.time() - start_time, 2)
        logger.info(f"Bronze layer loaded in {elapsed} seconds")
        
    except Exception as e:
        logger.error(f"Bronze load failed: {str(e)}")
        raise
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    load_bronze()

