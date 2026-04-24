import logging
import pandas as pd

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

def check_nulls(df, critical_cols=None):
    """Warn about null values in critical columns."""
    if critical_cols is None:
        critical_cols = ['ClaimID', 'ProcessDate', 'SegmentCode', 'Status', 'ProcessingType']
    
    available_cols = [col for col in critical_cols if col in df.columns]
    if available_cols:
        nulls = df[available_cols].isnull().sum()
        if nulls.sum() > 0:
            logger.warning(f"Found nulls in columns:\n{nulls[nulls > 0]}")
    return df

def check_duplicates(df, subset=None):
    """Remove duplicate rows."""
    if subset is None:
        subset = ["ClaimID"] if "ClaimID" in df.columns else None
    
    before = len(df)
    if subset:
        df = df.drop_duplicates(subset=subset)
    after = len(df)
    
    if before > after:
        logger.info(f"Removed {before - after} duplicate rows")
    
    return df

def validate(df):
    """Run all validation checks and return the cleaned DataFrame."""
    is_valid, msg = validate_schema(df)
    if not is_valid:
        raise ValueError(msg)
    df = check_nulls(df)
    df = check_duplicates(df)
    return df