# # import smtplib
# #
# #
# # def send_email(send_email, code):
# #     try:
# #         server = smtplib.SMTP('smtp.gmail.com', 587)
# #         server.starttls()
# #         server.login('re.fire761@gmail.com', 'onamotam./761')
# #         server.sendmail(from_addr='re.fire761@gmail.com', to_addrs=send_email, msg=code)
# #         print('Email sent!')
# #
# #     except Exception as e:
# #         print(e)
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# def send_email(to_email, code):
#     from_email = 're.fire761@gmail.com'
#     from_password = 'onamotam./761'
#
#     try:
#         # Create the email content
#         msg = MIMEMultipart()
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg['Subject'] = 'Your Confirmation Code'
#
#         body = f'Your confirmation code is: {code}'
#         msg.attach(MIMEText(body, 'plain'))
#
#         # Connect to the server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#
#         # Login to the email account
#         server.login(from_email, from_password)
#
#         # Send the email
#         server.sendmail(from_email, to_email, msg.as_string())
#         server.quit()
#         print('Email sent!')
#
#     except Exception as e:
#         print(f'Failed to send email: {e}')
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, code):
    from_email = 'sobirjon0305@gmail.com'
    from_password = 'vtnmuwtbmmohwjzv'

    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Your Confirmation Code'

        body = f'Your confirmation code is: {code}'
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the email account
        server.login(from_email, from_password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print('Email sent!')

    except Exception as e:
        print(f'Failed to send email: {e}')
