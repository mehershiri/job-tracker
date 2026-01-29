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

## Demo Screenshot

*(Optional: Add a screenshot of your dashboard here)*

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mehershiri/job-tracker.git
cd job-tracker

### 2. Create a virtual environment
python -m venv venv
# Activate the environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up MYSQL Server
This is essential to view and modify the database
1. Install MySQL Server
2. Create a database
CREATE DATABASE job_tracker;
3. Create Applications Table
CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(255),
    role VARCHAR(255),
    Application_Status VARCHAR(50),
    email_date DATETIME,
    email_uid VARCHAR(255) UNIQUE
);

### 5. Create a .env file
Please fill in with your credentials
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
DB_PASSWORD=your_mysql_password

### 6. Fetch Emails
python fetch_emails.py

### 7. Run the Dashboard
python fetch_emails.py
