class SendEmail(object):

    def __init__(self, email_from, email_to, email_message):
        self.email_from = email_from
        self.email_to = email_to
        self.email_message = email_message

    def send_email(self):
        return 'Enviar email'


class MyEmail(SendEmail):

    def send_email(self):
        SendEmail.send_email(self)
        return 'Alterado'


if __name__ == '__main__':
    e = SendEmail('from', 'to', 'message')
    e.email_from = 'teste'
    print('%s - %s - %s' % (e.email_from, e.email_to, e.email_message))
    print(e.send_email())
    e.send_email()

    m = MyEmail('from', 'to', 'message')
    print(m.send_email())
