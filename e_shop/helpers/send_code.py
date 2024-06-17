import smtplib

def send_email(send_email, code):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('sobirjon0305@gmail.com', 'vtnmuwtbmmohwjzv')
        server.sendmail(from_addr='sobirjon0305@gmail.com', to_addrs=send_email, msg=code)
        print('Email sent!')

    except Exception as e:
        print(e)