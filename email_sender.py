from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'brianislevu@gmail.com'
email_password = 'virus13sting'

email_receiver = 'lehafi3503@cmeinbox.com'

subject = "Hello world"
body = """
this is a demo of email sending in python

"""

em = EmailMessage()
em['from'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


