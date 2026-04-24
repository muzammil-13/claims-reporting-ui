import logging

logger = logging.getLogger(__name__)

def validate_schema(df):
    """Validate schema and data integrity."""
    required_columns = ['ClaimID', 'ProcessDate', 'SegmentCode', 'Status', 'ProcessingType']
    
    # Check for required columns
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        logger.error(f"Missing columns: {missing_cols}")
        return False, f"Missing columns: {', '.join(missing_cols)}"
    
    # Check if empty
    if df.empty:
        logger.error("Dataset is empty")
        return False, "Dataset is empty"
        
    logger.info("Schema validation passed.")
    return True, "Success"