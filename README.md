## ⚙️ Automation Pipeline (CI/CD)

This project includes a fully automated data processing pipeline using GitHub Actions.


### Trigger:
- Manual trigger via GitHub Actions UI (`workflow_dispatch`)

### Pipeline Steps:

1. Setup Python environment 
 
2. Install dependencies  

3. Generate sample input data  

4. Run processing pipeline (`main.py`)  

5. Upload report artifact (`report.json`)  

This ensures the system can run independently of local machines..


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

## 🔐 Environment Variables

This project uses environment variables for secure credential handling.

Create a `.env` file locally or configure GitHub Secrets:

EMAIL_USER=your_email@gmail.com  
EMAIL_PASS=your_app_password  
EMAIL_TO=recipient@example.com  

> Note: Never hardcode credentials in source code. This project follows secure practices using environment variables and GitHub Secrets.

 Workflow Capabilities:

- Runs in a cloud environment (Ubuntu runner)

- Automatically processes CSV data

- Generates cleaned data and analytics reports

- Uploads output as downloadable artifacts

- Supports secure email automation via secrets

📈 Use Cases

1. Business reporting automation

2. Data preprocessing pipelines

3. Automated analytics workflows

4. Backend data services

🔥 Key Highlight


