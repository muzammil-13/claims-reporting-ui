# 🏥 Healthcare Claims Reporting Pipeline UI

**Automating Auto-Adjudication (AA) Reporting from Raw Claims Data to Shareable Insights via an Interactive UI**

---

## 🚀 Overview

This project transforms a **manual, error-prone healthcare claims reporting workflow** into a  **modular, reproducible data pipeline** .

It simulates an enterprise environment where claims data originates from mainframe systems and is processed into  **Auto-Adjudication (AA) metrics** , enabling faster and more reliable reporting.

> Designed and built during an IBM CIC internship to mirror real production workflows in claims processing systems.

---

## 🎯 Problem Statement

In traditional enterprise workflows:

* Claims data is generated via **mainframe batch jobs**
* Data is extracted manually via **TSO commands + Outlook attachments**
* Reports are created using **ad-hoc scripts and Excel workflows**
* Email reporting is **manual and inconsistent**

This leads to:

* ❌ Repetitive manual effort
* ❌ High risk of human error
* ❌ Lack of reproducibility
* ❌ No clear pipeline structure

---

## 💡 Solution

This project rebuilds the workflow as a  **structured data pipeline** :

```text
User Uploads File (Simulated Mainframe Extract) via Streamlit UI
        ↓
Data Ingestion
        ↓
Validation Layer
        ↓
Transformation (AA Logic)
        ↓
Aggregation (MTD / LOB / State)
        ↓
Report Generation
        ↓
Email Automation (Link-Based)
```

---

## ⚙️ Key Features

### 🖥️ Interactive UI (Streamlit)

* Drag-and-drop file uploading for simulated datasets
* Real-time pipeline execution and metrics visualization
* In-app HTML email preview

### Data Ingestion

* Simulates mainframe dataset extraction using structured input files
* Supports CSV/TXT formats

### ✅ Data Validation

* Ensures latest data (date checks)
* Schema validation for consistency

### 🔄 Transformation Engine

* Processes claims data using **pandas**
* Implements Auto-Adjudication (AA) logic

### 📊 Aggregation Layer

* Generates:
  * MTD (Month-to-Date) metrics
  * LOB-wise summaries

### 📤 Report Generation

* Outputs clean Excel reports
* Dashboard-ready tabular formats

### 📬 Email Automation (Simulated)

* Generates email-ready content
* Uses **link-based reporting** (aligned with SharePoint workflows)

---

## 🧱 Project Structure

```bash
healthcare-claims-reporting-pipeline/

├── data/
│   ├── input/              # Simulated mainframe input
│   ├── output/             # Generated reports
│
├── pipeline/
│   ├── ingest.py           # Data loading
│   ├── validate.py         # Data checks
│   ├── transform.py        # AA logic
│   ├── aggregate.py        # Metrics computation
│   ├── export.py           # Report generation
│
├── automation/
│   ├── email.py            # Email generation (link-based)
│
├── app.py                  # Streamlit UI Entry Point
├── config.yaml             # Configurations
├── progress_log.md         # Development tracking
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/muzammil-13/claims-reporting-ui.git
cd claims-reporting-ui
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Input Data

Place your sample dataset inside:

```bash
data/input/
```

---

### 4. Run the Pipeline

```bash
streamlit run app.py
```

---

## 📊 Sample Output

The pipeline generates:

* � `Report_<timestamp>.xlsx` (Daily/YTD report containing raw data and segment summaries)
* 📄 `westmarket.xlsx` (Updated historical dataset with daily metrics)
* 📊 Aggregated AA metrics (LOB)
* � Email-ready summary content

---

## 🧠 Design Decisions

### Why Modular Pipeline?

* Improves readability and maintainability
* Aligns with real-world data engineering systems

### Why Simulate Mainframe?

* Direct access is restricted
* Simulation enables reproducibility

### Why Link-Based Email?

* Enterprise systems use **SharePoint instead of attachments**
* Avoids versioning conflicts

---

## 🚧 Limitations

* Mainframe job triggering is simulated
* No real-time backend integration
* Email sending is mocked (no SMTP integration)

---

## 🔮 Future Enhancements

* 🔗 SharePoint API integration
* 📈 Streamlit dashboard for visualization
* ⏱️ Scheduling (cron / Airflow)
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
