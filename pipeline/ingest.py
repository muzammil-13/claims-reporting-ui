import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(file_path):
    """Load uploaded file into pandas DataFrame."""
    logger.info(f"Ingesting file: {file_path}")
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.txt'):
            return pd.read_csv(file_path, sep='|')
        else:
            raise ValueError("Unsupported file format. Must be .csv or .txt")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise