import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd
from datetime import datetime
import yaml

from pipeline.ingest import load_data
from pipeline.validate import validate_schema
from pipeline.transform import process_claims
from pipeline.aggregate import generate_summaries
from pipeline.export import export_reports
from automation.email import generate_email_preview, simulate_send_email

# Load Config
def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

config = load_config()

# Setup directories
os.makedirs(config['paths']['input_dir'], exist_ok=True)
os.makedirs(config['paths']['output_dir'], exist_ok=True)

st.set_page_config(page_title="Healthcare Claims Pipeline", layout="wide")
st.title("🏥 Healthcare Claims Reporting Pipeline")

st.markdown("Automating Auto-Adjudication (AA) Reporting from Raw Claims Data to Shareable Insights")

# 1. File Upload
uploaded_file = st.file_uploader("Upload Mainframe Dataset (CSV/TXT)", type=["csv", "txt"])

if uploaded_file is not None:
    # Save file temporarily
    file_path = os.path.join(config['paths']['input_dir'], uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    # Preview
    df_preview = load_data(file_path)
    st.subheader("Data Preview")
    st.dataframe(df_preview.head())
    
    # Run Pipeline Button
    if st.button("Run Pipeline"):
        with st.spinner("Processing pipeline..."):
            try:
                # Ingest
                df = load_data(file_path)
                st.write("✅ Data Ingested")
                
                # Validate
                is_valid, validation_msg = validate_schema(df)
                if not is_valid:
                    st.error(f"Validation Failed: {validation_msg}")
                    st.stop()
                st.write("✅ Data Validated")
                
                # Transform
                df_transformed = process_claims(df)
                st.write("✅ Data Transformed")
                
                # Aggregate
                summaries = generate_summaries(df_transformed)
                st.write("✅ Metrics Aggregated")
                
                # Export
                report_paths = export_reports(df_transformed, summaries, config)
                st.write("✅ Reports Generated")
                
                # Display Results
                st.header("📊 Pipeline Results")
                
                col1, col2 = st.columns(2)
                with col1:
                    overall_aa_rate = summaries['overall_aa_rate']
                    st.metric(label="Overall Auto-Adjudication Rate", value=f"{overall_aa_rate:.2f}%")
                
                st.subheader("Segment Summary")
                st.dataframe(summaries['lob_summary'])
                
                # Email Simulation
                st.header("📬 Email Automation")
                email_content = generate_email_preview(summaries, config)
                st.text_area("Email Preview", email_content, height=250)
                
                if st.button("Simulate Send Email"):
                # Render HTML email preview
                with st.expander("View HTML Email Preview", expanded=True):
                    components.html(email_content, height=450, scrolling=True)
                
                st.info("💡 Set environment variable `SEND_EMAIL=true` to send real emails via Outlook.")
                
                if st.button("Send Email (Simulated or Real)"):
                    send_msg = simulate_send_email(email_content, config)
                    st.success(send_msg)
                    
            except Exception as e:
                st.error(f"Pipeline Failed: {str(e)}")