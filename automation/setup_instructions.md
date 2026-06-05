## Objective
Ensure the Power BI report refresh pipeline runs automatically every Monday at 08:00 SAST.

## Options

### 1. Windows Task Scheduler
- Open Task Scheduler → Create Basic Task.
- Name: "Power BI Refresh".
- Trigger: Weekly → Monday → 08:00.
- Action: Start a program → `python.exe`.
- Arguments: `scripts/refresh_pipeline.py`.
- Working directory: Project root.

### 2. Linux/Mac (cron job)
- Open terminal → `crontab -e`.
- Add entry:

