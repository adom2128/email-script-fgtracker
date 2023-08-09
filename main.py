import imaplib
import email
import re
import os
import requests
from dotenv import load_dotenv

load_dotenv()

imap_server = "imap.gmail.com"
email_address = os.environ("EMAIL_USER")
password = os.environ("EMAIL_PASSWORD")
path="http://127.0.0.1:5000/surveys"

mail = imaplib.IMAP4_SSL(imap_server)

mail.login(email_address, password)

mail.select("Inbox")

status, email_ids = mail.search(None, '(SUBJECT "updated prepaid card balance")')


if status == "OK":
    email_ids_list = email_ids[0].split()
    
    for email_id in email_ids_list:
        status, msg_data = mail.fetch(email_id, "(RFC822)")

        if status == "OK":
            msg = email.message_from_bytes(msg_data[0][1])
            
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8")

                    last_four_match = re.search(r'Card: \*(\d+)', body)
                    balance_match = re.search(r'\* Current balance: \* \$(\d+\.\d+)', body)

                    last_four = last_four_match.group(1)
                    payment_left = float(balance_match.group(1))

                    if last_four and payment_left:
                        response = requests.get(path)
                        surveys_list = response.json()

                        for survey in surveys_list:
                            if survey["last_four"] == last_four:
                                survey_id = survey["id"]

                                patch_path = f'{path}/{survey_id}'

                                response = requests.patch(patch_path, json={"payment_left": payment_left})