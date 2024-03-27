import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

# reading data from .env file
froom = os.getenv("from")
password = os.getenv("password")    # use google app password
from_name = "Team Dishank"

# read body message as html file
with open("body.html", "r") as hfile:
    html = hfile.read()

# html data as string
body = """\
{data}
"""

sent_list = list()  # to store the progress

# store the confirmation details in a file
def create_response():
    x = datetime.datetime.now()
    folder = x.strftime("%d-%m-%Y")
    name = x.strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"{folder}\\{name}.txt"
    try:
        os.mkdir(folder)
    except FileExistsError as f:
        pass
    with open(filename, "w") as f:
        for item in sent_list:
            for subitem in item:
                f.write(f"{subitem}, ")
            f.writelines("\n")

# send email
def send_email(subject):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(froom, password)
    with open("data.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for no, fn, ln, mail in reader:
            msg = EmailMessage()
            msg['subject'] = subject
            msg['to'] = mail
            msg['from'] = formataddr((from_name, froom))
            msg.add_alternative(body.format(data = html.format(FirstName = fn, LastName = ln)),subtype="html",)
            try:
                server.sendmail(froom, mail, msg.as_string())
                # print(no, fn, ln, mail)
                sent_list.append(list((no, fn, ln, mail, "Sent")))
            except Exception as e:
                # print(no, fn, ln, mail, f"Error: {e}")
                sent_list.append(list((no, fn, ln, mail, f"Error: {e}")))
    server.quit()
    # print(sent_list)
    create_response()

send_email("Demo Email")