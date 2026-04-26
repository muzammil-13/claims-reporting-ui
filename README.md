# 🏥 Claims Reporting UI

**Problem:** AA reporting is manual, slow, decision-heavy.

This repository showcases a Streamlit-based UI that turns a fragmented claims reporting process into a simpler, more intuitive workflow.

---

## Problem

The existing AA reporting process is:

* Manual
* Slow
* Dependent on Excel cleanup and human decisions

Teams are forced to move from JCL extracts into Excel, clean the data, email reports, and store results on SharePoint.

---

## Current Workflow

```text
JCL → Excel → cleanup → email → SharePoint
```

This flow creates friction because each step requires manual work, decision making, and file handoffs.

---

## Solution

This project delivers a UI-driven workflow that simplifies interpretation and reduces friction.

Key improvements:

* Centralized report upload and execution in a Streamlit app
* Automated data ingestion, validation, and AA transformation
* Clear metrics and summaries for faster review
* Email-ready output and SharePoint-friendly reporting

---

## Impact

* ✅ Faster decisions
* ✅ Less manual Excel work
* ✅ Reduced human error
* ✅ More consistent reporting

---

## Demo

Include screenshots or a GIF here to show the UI flow and output.

* Screenshot: input upload screen
![input upload screen](image/README/input_upload_screen-Healthcare-Claims-Pipeline.png)
* Screenshot: AA metric summary
![AA metric summary](image/README/AA_metric_summary-Healthcare-Claims-Pipeline.png)
* GIF: report preview and email-ready output
![1777176277842](image/README/1777176277842.gif)

> If you want, add real screenshots or a short animated GIF in this section.

---

## How to Run

```bash
git clone https://github.com/muzammil-13/claims-reporting-ui.git
cd claims-reporting-ui
pip install -r requirements.txt
streamlit run app.py
```

---

## What This Project Includes

* `app.py` — Streamlit UI entry point
* `pipeline/ingest.py` — data loading
* `pipeline/validate.py` — data checks and schema validation
* `pipeline/transform.py` — AA transformation logic
* `pipeline/aggregate.py` — metrics aggregation
* `pipeline/export.py` — report generation
* `automation/email.py` — email-ready report content

---

## If I Had More Time, I’d Add...

* SharePoint API integration for automated report publishing
* Interactive dashboard charts for AA trends
* Scheduler support (cron / Airflow)
* Real backend integration for authenticated data access
* Export to PDF or SharePoint link generation
* 🧪 Unit testing for pipeline stages
* 📦 Containerization (Docker)

---

## 📈 Impact

This project demonstrates:

* Transition from **manual operations → automated pipelines**
* Application of **data engineering principles in enterprise workflows**
* Ability to **reverse-engineer and systemize production processes**

---

## 🙌 Acknowledgements

* Built during internship at **IBM Consulting Client Innovation Center**
* Inspired by real-world claims processing workflows in healthcare systems

---

## 📬 Contact

If you’re working on similar automation or data pipeline problems, feel free to connect or discuss ideas.

---

⭐ If you found this useful, consider giving it a star!
