

import os
import smtplib

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('GMAIL_PYTHON_PASWORD')

msg = message

with smtplib.SMTP('www.ge.com', 587) as smtp:
#with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login( EMAIL_USER, EMAIL_PASSWORD)

    subject = 'Just Testing'
    body = 'Sending emails using Python!!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_USER, 'stewart.cutler@ge.com', msg)

    smtp.quit()

    print('\n Sent')

