
import os
import smtplib
import imghdr
from email.message import EmailMessage
from getpass import getpass



def get_input(prompt=''):
    line = input(prompt)
    return line

def get_credentials():
    """Prompt for and return a username and password."""
    username = get_input('Username(Please input your AD credentials): ')
    password = getpass()
    return username, password

username, password = get_credentials()

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

'''send email to a group'''
contacts = ['hujie.331@gmail.com', 'jay.hu2@sony.com']

msg = EmailMessage()
msg['Subject'] = 'Test email sent from Python script'
msg['From'] = username
msg['To'] = contacts

msg.set_content('This is a test email sent from Python script to hujie.331@gmail.com')

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(username, password)
    smtp.send_message(msg)
