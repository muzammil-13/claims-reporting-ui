import pandas as pd
import logging

logger = logging.getLogger(__name__)

def process_claims(df):
    """Transform data and implement AA logic."""
    logger.info("Transforming data...")
    df = df.copy()
    
    # Clean and normalize
    df['ProcessDate'] = pd.to_datetime(df['ProcessDate'])
    df['Status'] = df['Status'].astype(str).str.upper()
    df['ProcessingType'] = df['ProcessingType'].astype(str).str.upper()
    
    # Auto-Adjudication Logic
    df['Is_AA'] = df['ProcessingType'] == 'AUTO'
    
    # Extract YearMonth for aggregations
    df['YearMonth'] = df['ProcessDate'].dt.to_period('M')
    return df