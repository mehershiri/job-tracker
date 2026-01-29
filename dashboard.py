# dashboard.py
import streamlit as st
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=DB_PASSWORD,
        database="job_tracker"
    )

# Fetch Data
@st.cache_data(ttl=300)  
def fetch_data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applications ORDER BY email_date DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return pd.DataFrame(rows)

st.set_page_config(page_title="Job Applications Dashboard", layout="wide")
st.title("Job Applications Tracker")

# Load data
df = fetch_data()

if df.empty:
    st.warning("No job applications found in the database!")
else:
    # Metrics
    st.subheader("Summary Metrics")
    total_applications = len(df)
    total_companies = df['company'].nunique()
    status_counts = df['Application_Status'].value_counts()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", total_applications)
    col2.metric("Companies Applied", total_companies)
    col3.metric("Applications by Status", "")

    st.write(status_counts.to_frame("Count"))

    # Company Wise
    st.subheader("Applications by Company")
    company_counts = df['company'].value_counts()
    st.bar_chart(company_counts)

    # Applications
    st.subheader("Detailed Applications")
    df['email_date'] = pd.to_datetime(df['email_date'])
    df_sorted = df.sort_values(by='email_date', ascending=False)
    st.dataframe(df_sorted)

    # Filter by Status
    st.subheader("Filter by Status")
    selected_status = st.multiselect(
        "Select Status",
        options=df['Application_Status'].unique(),
        default=df['Application_Status'].unique()
    )
    filtered_df = df[df['Application_Status'].isin(selected_status)]
    st.dataframe(filtered_df)
