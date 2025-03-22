import smtplib


def send_email(send_email, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user='xasannurmatovpython0710@gmail.com', password='rqrqgtgwoqfjcqhy')
        server.sendmail(from_addr='xasannurmatovpython0710@gmail.com', to_addrs=send_email, msg=message)
        print('Message sent!')

    except Exception as e:
        print(e)