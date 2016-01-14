class Email(object):
    """ Provide Emails Sending Service

    Example for config.py:
    "email": {
        "host": "smtp.gmail.com",
        "port": 587,
        "username": "james2015@gmail.com",
        "password": "88888888"
    }
    """
    available = False

    host = safe_get_config("email.host", "")
    port = safe_get_config("email.port", 587)
    username = safe_get_config("email.username", "")
    password = safe_get_config("email.password", "")
    postman = None
    error_message = ""

    def __init__(self):
        """check email-service parameters from config.py"""
        if self.host == "":
            self.error_message = "Email Error: host is empty"
        elif self.username == "":
            self.error_message = "Email Error: username is empty"
        elif self.password == "":
            self.error_message = "Email Error: password is empty"
        else:
            self.available = True
            # initial postman
            self.postman = Postman(
                host=self.host,
                port=self.port,
                middlewares=[
                    TLS(force=True),
                    Auth(username=self.username, password=self.password)
                ]
            )

    def send_emails(self, sender, receivers, subject, content, cc=[], bcc=[], attachments=[]):
        """Send emails
        notes: No all email-service providers support.
        if using Gmail, enable "Access for less secure apps" for the sender's account,

        Examples:
            xxx.send_emails("James jame2015@gmail.com",
                            ['receiver1@gmail.com', 'receiver2@gmail.com'],
                            'Subject: Hello',
                            '<b>Hi! Here is the content of email</b>',
                            ['cc1@gmail.com', 'cc2@gmail.com'],
                            ['bcc1@gmail.com', 'bcc2@gmail.com'],
                            ['C:/apache-maven-3.3.3-bin.zip'])

        :type sender: str|unicode
        :param sender: the nickname and email address of sender. Example:"James jame2015@gmail.com"

        :type receivers: list
        :param receivers: receivers' emails address. Example:['a@gmail.com', 'b@gmail.com']

        :type subject: str|unicode
        :param subject: subject of email's header. Example:'Hello'

        :type content: str|unicode
        :param content: content of the email. Example:'<b>Hi!</b>'

        :type cc: list
        :param cc: CarbonCopy. Example:['a@gmail.com', 'b@gmail.com']

        :type bcc: list
        :param bcc: BlindCarbonCopy. Example:['a@gmail.com', 'b@gmail.com']

        :type attachments: list
        :param attachments: Example:['C:/Users/Administrator/Downloads/apache-maven-3.3.3-bin.zip']

        :rtype boolean
        :return True if send emails successfully. False if fails to send.
        """
        if not self.available:
            log.error(self.error_message)
            return False

        e = email(sender=sender,
                  receivers=receivers,
                  cc=cc,
                  bcc=bcc,
                  subject=subject,
                  content=content)

        try:
            response = self.postman.send(e)
            if response.status_code == EMAIL_SMTP_STATUSCODE.SUCCESS:
                return True
            log.error("Send emails fail: " + response.message)
            return False
        except Exception as e:
            log.error(e)
            return False