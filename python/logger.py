import logging
from pathlib import Path #added

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"  #added
LOG_DIR.mkdir(exist_ok=True)                                #added
LOG_FILE = LOG_DIR / "pipeline.log"    #added

def get_logger(name):
    
    logger = logging.getLogger(name)

    if not logger.handlers: 
        logger.setLevel(logging.INFO)
    
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.propagate = False
    
    return logger
