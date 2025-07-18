﻿# 📊 Smart Lead Validator & Prioritizer

This Streamlit-powered tool scores and prioritizes B2B leads based on seniority, contactability, and professional presence. It helps sales teams focus on high-quality prospects with minimal manual review.

## 🔧 Features

- ✅ Email format validation
- ✅ LinkedIn profile presence check
- ✅ Job title scoring (CEO/Founder > VP > Manager)
- ✅ Visual summary of lead quality (pie chart)
- ✅ Downloadable prioritized CSV
- ✅ Streamlit UI (no coding required)
- ✅ Mock "Send Email" interaction for top leads

## 📂 Sample Input

Upload a CSV file with the following columns:

| name | email | job_title | company | website | linkedin_url | location |
|------|-------|-----------|---------|---------|---------------|----------|

Use `sample_data.csv` for reference.
Here is your **final folder structure** for the project — clean, organized, and submission-ready:

---
## 📁 Folder Structure

```
smart-lead-prioritizer/
├── app.py                        # Streamlit UI
├── utils.py                      # Lead scoring logic
├── sample_data.csv               # Sample leads for testing/demo
├── requirements.txt              # All required Python packages
├── README.md                     # Project overview + instructions
├── lead_score_report.md          # One-page rationale report
├── demo.mp4                      # (Optional) Screen-recorded demo video
├── .gitignore                    # Ignore venv, __pycache__, etc.
└── venv/                         # (Optional) Virtual environment
```
---
## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
````

## 📦 Requirements

* Python 3.8+
* streamlit
* pandas
* plotly

Install all with:

```bash
pip install -r requirements.txt
```

## 🎥 Demo
https://smart-lead-validator-prioritizer.streamlit.app/

---

## 👨‍💼 Author

Lakshay Jain
🔗 [LinkedIn](https://www.linkedin.com/in/lakshay-jain-a48979289/) | 📫 \lakshayj539@gmail.com
