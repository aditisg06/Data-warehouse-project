import time
from load_bronze import load_bronze
from validate import run_all_validations
from logger import get_logger

logger = get_logger("pipeline")

def run_pipeline():
    logger.info("=" * 50)
    logger.info("PIPELINE STARTED")
    logger.info("=" * 50)
    
    pipeline_start = time.time()
    
    try:
        load_bronze()
        run_all_validations()
        
        total_time = round(time.time() - pipeline_start, 2)
        logger.info(f"PIPELINE COMPLETED in {total_time} seconds")
        
    except Exception as e:
        logger.error(f"PIPELINE FAILED: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()

