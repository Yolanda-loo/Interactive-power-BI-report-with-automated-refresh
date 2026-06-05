## Key Benefits
- **Efficiency:** Manual reporting reduced by ~80%.
- **Accuracy:** KPIs always reflect the latest dataset.
- **Transparency:** Timestamp column shows last refresh time.
- **Scalability:** Pipeline can extend to SQL DB or Azure Data Factory.

## Business Impact
- Stakeholders access up-to-date insights without waiting for manual updates.
- Reporting cycle shortened from hours to minutes.
- Enables enterprise-scale automation with minimal overhead.

## Next Steps
- Integrate email notifications for refresh completion.
- Connect Power BI directly to SQL database for real-time dashboards.
- Expand automation to cloud pipelines for enterprise deployment.

what nned to be done when i am done with the code,

### 3. Azure Data Factory
- Create a pipeline with a Python activity.
- Upload `refresh_pipeline.py` to linked storage.
- Configure trigger: Weekly, Monday, 08:00 SAST.

## Verification
- Check `/data/business_kpi_refreshed.csv` for updated timestamp.
- Confirm Power BI visuals reflect new data.


