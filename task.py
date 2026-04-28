
import os
from dotenv import load_dotenv
import resend

import jinja2

load_dotenv()

template_loader = jinja2.FileSystemLoader(searchpath="templates/emails")
env = jinja2.Environment(loader=template_loader)

def render_template(template_name, **context):
    return env.get_template(template_name).render(context)

def send_simple_message(to,subject,text):
    
    resend.api_key=os.getenv("API_KEY")
    return  resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": to,
    "subject": subject,
    "html": f"<p>{text}</p>"
    })

def send_Registration_email(email,username):
    subject="Registration successful"
    text=render_template("action.html",username=username)
    send_simple_message(to=email,subject=subject,text=text)