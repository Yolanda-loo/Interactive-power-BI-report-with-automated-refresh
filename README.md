# 🔄 Automated Power BI Report Refresh

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Tool](https://img.shields.io/badge/Python-Power%20BI%20%7C%20Automation-blue)
![Focus](https://img.shields.io/badge/Domain-Reporting%20Efficiency-orange)

## 🚀 Objective
Create an **interactive Power BI report** connected to a dataset that automatically refreshes via a Python pipeline.  
This project demonstrates how automation can reduce manual reporting effort and ensure stakeholders always have access to the latest insights.

---

## 🛠️ Workflow
1. **Data Preparation**  
   - Raw dataset: `business_kpi_sample_data.csv`.  
   - Automated refresh script (`refresh_pipeline.py`) generates `business_kpi_refreshed.csv` with KPIs and a refresh timestamp.

2. **Power BI Report**  
   - Connects directly to the refreshed dataset.  
   - Visuals include:  
     - Revenue trends over time.  
     - Expenses by region.  
     - Product category contribution.  
   - Interactive filters for Region, Product, and Date.

3. **Automation**  
   - Python script scheduled via **cron job / Task Scheduler / Azure Data Factory**.  
   - Refresh occurs automatically (e.g., every Monday at 08:00 SAST).  
   - Timestamp column tracks last refresh for transparency.

---

## 📂 Deliverables
- `/data` → Raw and refreshed datasets.  
- `/scripts` → Python refresh pipeline (`refresh_pipeline.py`).  
- `/dashboard` → Power BI `.pbix` file + screenshots.  
- `/automation` → Documentation of scheduled refresh setup.  
- `/insights` → Markdown file summarizing efficiency gains.  
- `README.md` → Documentation (this file).  

---

## 🔍 Business Value
- **Efficiency** → Reduces manual reporting time by up to 80%.  
- **Accuracy** → Ensures KPIs are always up-to-date.  
- **Scalability** → Can be extended to cloud pipelines (Azure Data Factory, SQL Database).  

---

## 📸 Example Workflow
*(Insert screenshots of Power BI dashboard and refresh logs here)*

---

## 🧭 Next Steps
- Integrate with cloud services for enterprise-scale refresh.  
- Add email notifications when refresh completes.  
- Connect directly to SQL database for real-time reporting.
