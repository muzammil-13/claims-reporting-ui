from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def generate_email_preview(summaries, config):
    """Generate the email body and subject."""
    date_str = datetime.now().strftime('%Y-%m-%d')
    subject = config['email']['subject_template'].format(date=date_str)
    overall_rate = summaries['overall_aa_rate']
    
    table_str = summaries['lob_summary'].to_markdown(index=False)
    
    body = f"""Subject: {subject}

Hello Team,

The daily Healthcare Claims Auto-Adjudication Pipeline has completed successfully.

**Key Metrics:**
- Overall AA Rate: {overall_rate:.2f}%
- Total Claims Processed: {summaries['total_claims']}

**Segment Summary:**
{table_str}
"""
    return body.strip()

def simulate_send_email(email_content, config):
    """Simulate sending an email."""
    recipients = config['email']['recipients']
    return f"Email successfully sent to {', '.join(recipients)}! Check console/logs for details."