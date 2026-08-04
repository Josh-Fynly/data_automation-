# Cloud Data Pipeline

> A modular backend automation project that processes structured data, generates analytics reports, and executes entirely in the cloud using GitHub Actions.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-success)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## Overview

Cloud Data Pipeline is a backend engineering project that demonstrates automated data processing using modern software engineering practices.

The application processes structured data through a modular pipeline, performs data cleaning and analysis, generates reports, and automates execution using GitHub Actions. By integrating CI/CD workflows, secure credential management, and reproducible cloud execution, the project demonstrates backend automation concepts commonly used in production environments.

---

## Why I Built This

I built this project to strengthen my backend engineering skills beyond traditional CRUD applications.

The goal was to design a modular system that demonstrates:

- Backend automation
- Cloud-based execution
- Reproducible workflows
- Secure configuration management
- Separation of concerns
- CI/CD integration

Rather than focusing solely on application features, this project emphasizes engineering practices that improve maintainability, reliability, and scalability.

---

# Features

- Automated data processing
- CSV data cleaning
- Data analysis
- Analytics report generation
- Modular backend architecture
- Secure email automation
- Cloud execution using GitHub Actions
- Downloadable workflow artifacts
- Secure credential management using environment variables
- Easily extensible for future REST API integration

---

# System Architecture

```text
                 GitHub Actions
                        │
                        ▼
              Generate Sample Data
                        │
                        ▼
                 main.py (Controller)
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Data Cleaning    Data Analysis    File Utilities
        │               │               │
        └───────────────┼───────────────┘
                        ▼
              Report Generation
                        │
                        ▼
                 report.json
                        │
                        ▼
               Upload Workflow Artifact
```

---

# Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── manual.yml
│
├── processor/
│   ├── Data cleaning
│   └── Data analysis
│
├── utils/
│   ├── File handling
│   └── Email service
│
├── output/
│   └── report.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Automation | GitHub Actions |
| Email | SMTP |
| Version Control | Git & GitHub |
| Execution Environment | Ubuntu (GitHub Runner) |

---

# CI/CD Pipeline

The project includes a fully automated cloud-based workflow using GitHub Actions.

## Trigger

Manual execution through GitHub Actions using:

```text
workflow_dispatch
```

## Workflow

1. Set up Python environment
2. Install project dependencies
3. Generate sample input data
4. Execute the processing pipeline (`main.py`)
5. Generate analytics report (`report.json`)
6. Upload the report as a downloadable workflow artifact

Each workflow executes inside a fresh Ubuntu runner, ensuring a clean and reproducible execution environment.

---

# Proof of Execution

The pipeline has been successfully executed in a cloud environment.

### Verification

- GitHub Actions completed successfully
- Processing pipeline executed without local dependencies
- `report.json` generated successfully
- Workflow artifact uploaded automatically

### Example Output

```text
Loading data...

Cleaning data...

Saving cleaned data...

Analyzing data...

Generating report...

Pipeline completed successfully.
```

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/Josh-Fynly/cloud-data-pipeline.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=recipient@example.com
```

When using GitHub Actions, configure these values as **GitHub Secrets** instead of storing credentials in the repository.

No sensitive information is hardcoded.

---

# Engineering Highlights

- Modular backend architecture
- Separation of concerns
- Stateless processing pipeline
- Automated CI/CD workflow
- Cloud-based execution
- Secure credential handling
- Report artifact generation
- Designed for future API integration

---

# Use Cases

- Business reporting automation
- Data preprocessing pipelines
- Backend analytics workflows
- Automated report generation
- Cloud-based data processing services

---

# Future Improvements

- Docker containerization
- REST API interface
- Scheduled workflow execution
- Database integration
- Dashboard for analytics
- Unit and integration testing
- Structured logging
- Monitoring and alerting

---

# Author

**Joshua Effiong Ekpenyong**

Backend Software Engineer

**GitHub**  
https://github.com/Josh-Fynly

**Portfolio**  
https://my-portfolio-zfnv.vercel.app

**LinkedIn**  
https://linkedin.com/in/joshua-ekpenyong-014014340

---

If you found this project helpful or interesting, feel free to star the repository.
