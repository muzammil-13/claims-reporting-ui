import pandas as pd
import logging

logger = logging.getLogger(__name__)

def generate_summaries(df):
    """Generate overall, YTD, and segment-wise summaries."""
    logger.info("Aggregating metrics...")
    
    total_claims = len(df)
    total_aa = df['Is_AA'].sum()
    overall_aa_rate = (total_aa / total_claims * 100) if total_claims > 0 else 0
    
    # LOB / Segment summary
    lob_summary = df.groupby('SegmentCode').agg(
        Total_Claims=('ClaimID', 'count'),
        AA_Claims=('Is_AA', 'sum')
    ).reset_index()
    
    lob_summary['AA_Rate_%'] = (lob_summary['AA_Claims'] / lob_summary['Total_Claims'] * 100).round(2)
    
    # MTD Summary logic based on most recent date in data
    latest_month = df['YearMonth'].max()
    mtd_df = df[df['YearMonth'] == latest_month]
    
    return {
        'overall_aa_rate': overall_aa_rate,
        'lob_summary': lob_summary,
        'total_claims': total_claims
    }