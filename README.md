# Job Tracker

A **Python + MySQL project** that automatically fetches your job application emails, extracts company, role, and application status, stores them in a MySQL database, and visualizes them in a **Streamlit dashboard**.  

This project helps you **track job applications efficiently** and can be used as a portfolio project for **data-driven roles**.

---

## Features

- Fetch emails from Gmail (IMAP) using `imapclient` and `pyzmail36`  
- Parse company names, roles, and application status from email subject/body  
- Store application details in a **MySQL database**  
- View a **dashboard** with Streamlit:
  - Summary metrics: total applications, companies applied, applications by status  
  - Company-wise charts  
  - Filterable table of applications  
- Safe credentials management with `.env` file  

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mehershiri/job-tracker.git
cd job-tracker

---

### 2. Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


