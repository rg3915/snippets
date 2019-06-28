# -*- coding: utf-8 -*-
import email
import imaplib
import quopri

HOST = "imap.gmail.com"
USER = 'EMAIL'
PASSWORD = 'SENHA'
LABEL = "INBOX"

connection = imaplib.IMAP4_SSL(HOST, 993)
response, data = connection.login(USER, PASSWORD)
assert response == "OK"

response, count = connection.select(LABEL)
assert response == "OK"

response, (msg_nums,) = connection.search(None, "ALL")
assert response == "OK"

for msg_num in msg_nums.split():
    response, message_text = connection.fetch(msg_num, "(RFC822)")
    assert response == "OK"

    message = email.message_from_string(message_text[0][1])

    from_list = message.get_all("From") or []
    to_list = message.get_all("To") or []

    for body_message in message.walk():
        if body_message.get_content_maintype() == 'multipart':
            continue
        if body_message.get_content_subtype() != 'plain':
            continue
        boby_text = body_message.get_payload().decode('quopri').decode('utf-8')

    all_recipients_from = email.Utils.getaddresses(from_list)
    all_recipients_to = email.Utils.getaddresses(to_list)

    print ''
    print 'De: ' + "".join(addr.lower() for realname, addr in all_recipients_from)
    print 'Para: ' + "".join(addr.lower() for realname, addr in all_recipients_to)
    print 'Assunto: ' + message['Subject']
    print 'Corpo do Email:'
    print u'%s' % (boby_text.encode('ascii', 'ignore'))
    print 'Data de envio: ' + message['Date']
