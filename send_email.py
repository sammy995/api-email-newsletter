import smtplib, ssl


def send_email(message):

    host = "127.0.0.1"
    port = 1025

    username = "noonebot13@proton.me"
    password = "1100##Pool"

    receiver = "shubham92895@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)