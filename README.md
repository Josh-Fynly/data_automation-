# data_automation-

This project is a backend-driven data processing automation system designed to transform raw, messy CSV data into clean, structured outputs and actionable reports.
It simulates real-world business workflows where data must be cleaned, analyzed, and delivered automatically.

🎯 Features
Data cleaning pipeline (duplicates, missing values)
Automated data analysis (mean, sum, min, max)
Structured report generation (JSON output)
Email delivery of reports (SMTP integration)
Modular, scalable backend architecture

🧠 Architecture
processor/ → data cleaning & analysis
output/ → report generation
utils/ → file handling & email service
main.py → pipeline orchestration

⚙️ Tech Stack
Python
Pandas
NumPy
SMTP (Email automation)

▶️ How to Run
pip install -r requirements.txt
python main.py

🔐 Environment Variables
Create .env:
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com

📊 Example Workflow
Load raw CSV data
Clean and normalize dataset
Analyze numeric fields
Generate JSON report
Send report via email

📈 Use Cases
Business reporting automation
Data preprocessing pipelines
Automated analytics workflows
Backend data services

🔥 Key Highlight
Designed with backend engineering principles:
Separation of concerns
Modular architecture
Scalable processing pipeline

