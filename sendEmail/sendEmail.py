#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib


__all__ = ["EmailClient"]
class EmailClient(object):
    def __init__(self, smtp_server, username, password):
        self.smtp_server = smtp_server
        self.username = username
        self.password = password

    def send_email(self, receiver, msg):
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)
        smtp.connect(self.smtp_server)
        smtp.login(self.username, password=self.password)
        smtp.sendmail(self.username, receiver, msg.as_string())
        smtp.quit()

