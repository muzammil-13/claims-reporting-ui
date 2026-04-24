import pandas as pd
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def export_reports(df, summaries, config):
    """Export reports to Excel files and update historical data."""
    logger.info("Exporting reports...")
    output_dir = config['paths']['output_dir']
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    paths = {}
    
    # 1. New Daily/YTD Report
    ytd_filename = f"YTD_{timestamp}.xlsx"
    ytd_path = os.path.join(output_dir, ytd_filename)
    
    with pd.ExcelWriter(ytd_path, engine='openpyxl') as writer:
        df.drop(columns=['YearMonth']).to_excel(writer, sheet_name='Raw_Data', index=False)
        summaries['lob_summary'].to_excel(writer, sheet_name='Segment_Summary', index=False)
        
    paths['Current Report'] = ytd_path
    
    # 2. Update Historical Dataset (Westmarket)
    historical_path = config['paths'].get('historical_data', os.path.join(output_dir, "westmarket.xlsx"))
    historical_sheet = 'westmarket'
    if 'ProcessDate' in df.columns:
        latest_date = pd.to_datetime(df['ProcessDate']).max()
        current_date = latest_date.strftime('%Y-%m-%d')
    else:
        current_date = datetime.now().strftime('%Y-%m-%d')
    new_row = pd.DataFrame([{
        'Date': current_date,
        'Total_Claims': summaries['total_claims'],
        'Overall_AA_Rate': summaries['overall_aa_rate']
    }])
    
    if os.path.exists(historical_path):
        try:
            existing_df = pd.read_excel(historical_path, sheet_name=historical_sheet)
        except ValueError:
            existing_df = pd.read_excel(historical_path)
        updated_df = pd.concat([existing_df, new_row], ignore_index=True)
    else:
        updated_df = new_row
        
    with pd.ExcelWriter(historical_path, engine='openpyxl') as writer:
        updated_df.to_excel(writer, sheet_name=historical_sheet, index=False)
    paths['Historical Data (westmarket.xlsx)'] = historical_path
    return paths