from email.message import EmailMessage
import smtplib

EMAIL="ambikaagarwal83@yahoo.com"
PASSWORD='survikumari'

msg=EmailMessage()

msg['Subject']="Email using Python"
msg['From']=EMAIL
msg['To']=['venk2319@gmail.com']
#mailFrom=EMAIL
#mailTo='venk2319@gmail.com'
message = "this is sent by pycharm"
msg.set_content(message)

attachments=['C:\\Users\\DRAGON RIDER\\Desktop\\basic needs human.jpg']

for path in attachments:
    with open(path,'rb') as file:
        data=file.read()
        name=path.split("\\")[-1]


    msg.add_attachment(data,maintype='application',subtype = 'oclet-stream',filename=name)


with smtplib.SMTP_SSL(host='smtp.mail.yahoo.com',port=465) as smtp:
    smtp.login(EMAIL,PASSWORD)
    smtp.send_message(msg)
    smtp.quit()
    '''server = smtplib.SMTP_SSL(host='send.one.com', port=465)
    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(mailFrom, mailTo, text)
    server.quit()'''