#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.message import Message

from tools.mail import EmailClient
from tools.pm25 import getPM25


def run():
    """
    send email to users to tell them to take care the pm2.5
    """
    receiver = ['xuyaning98@163.com', '714178605@qq.com', '79509772@qq.com', '352511470@qq.com']

    message = Message()
    message['Subject'] = 'PM2.5'
    message['From'] = receiver[0]
    message['To'] = 'mybaby@521.com'
    message.set_payload(getPM25('beijing'))



    subject = 'PM2.5'
    username = 'xuyaning98@163.com'
    smtp_server = 'smtp.163.com'
    """
    msg = MIMEText('<a href="http://www.pm25.com/shanghai.html">See PM2.5!</a>','html','utf-8')#中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    """

    email_client = EmailClient(smtp_server, username, password= '1234567890')
    email_client.send_email(receiver[1], message)
    email_client.send_email(receiver[3], message)


if __name__ == '__main__':
    run()