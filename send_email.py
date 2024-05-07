import smtplib, ssl


def send_email(message):

    host = "127.0.0.1"
    port = 1025

    username = "SENDER_EMAIL"
    password = "SENDER_PASSWORD"

    receiver = "RECEIVER_EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
