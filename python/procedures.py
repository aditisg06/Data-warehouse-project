import time

from db import get_connection
from logger import get_logger

logger = get_logger("procedure_runner")

def run_stored_procedure(proc_name, layer_name):

    logger.info("=" * 50)
    logger.info(f"Starting {layer_name} Layer Load")
    logger.info("=" * 50)

    start_time = time.time()

    try:

        with get_connection() as conn:

            cursor = conn.cursor()

            logger.info(f"Executing {proc_name}...")

            cursor.execute(f"EXEC {proc_name}")

            conn.commit()

        elapsed = round(time.time() - start_time, 2)

        logger.info(f"{layer_name} layer loaded in {elapsed} seconds")

    except Exception as e:

        logger.error(f"{layer_name} load failed: {str(e)}")

        raise