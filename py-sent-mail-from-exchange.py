
import os
import smtplib
import imghdr
from getpass import getpass
from email.message import EmailMessage
import exchangelib

# from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
# from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

from exchangelib import Account
from exchangelib import Credentials
from exchangelib import Configuration
from exchangelib import NTLM
from exchangelib import Message
from exchangelib import Mailbox


#BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

# cred = Credentials(r'sony.com\jhu1', 'HUjie@20211023')
#
# config = Configuration(server='https://outlook.office365.com/', credentials=cred, auth_type=NTLM)
# a = Account(primary_smtp_address='jay.hu2@sony.com', config=config, autodiscover=False, access_type=DELEGATE)

credentials = Credentials('sony.com\jhu1', 'HUjie@20211023')
account = Account(primary_smtp_address='(jay.hu2@sony.com)', credentials=credentials, autodiscover=True)



m = Message(
    account=account,
    folder=account.sent,
    subject=u'测试邮件',
    body= 'This is a test email',
    to_recipients=[Mailbox(email_address='jay.hu2@sony.com')]
)
m.send_and_save()
