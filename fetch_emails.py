from imapclient import IMAPClient
import pyzmail
from parser import extract_details
from database import insert_record
import os   
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
HOST='imap.gmail.com'
USERNAME=os.getenv("EMAIL_USERNAME")
PASSWORD=os.getenv("EMAIL_PASSWORD")

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    server.select_folder('INBOX')
    messages = server.search(['SINCE','01-Jun-2025'])
    for uid in messages[-20:]:
        raw_message=server.fetch([uid],['BODY[]'])
        message= pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])
        subject= message.get_subject()
        from_email=message.get_addresses('from')[0][1]
        if message.text_part:
            body=message.text_part.get_payload().decode(message.text_part.charset,errors="ignore")
        else:
            body=""
        company,role,Application_Status=extract_details(subject, body, from_email)
        email_date=datetime.now()
        uid=uid
        insert_record(company,role,Application_Status,email_date,uid)
print("Email processed and store")  