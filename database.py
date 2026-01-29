import mysql.connector
import os
from dotenv import load_dotenv
import mysql

load_dotenv()
def insert_record(company,role,Application_Status,email_date,uid):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="job_tracker"
    )
    cursor=conn.cursor()
    query= """INSERT IGNORE INTO applications (company,role,Application_Status,email_date,email_uid)
    VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(query,(company,role,Application_Status,email_date,uid))
    conn.commit()
    conn.close()
    cursor.close()