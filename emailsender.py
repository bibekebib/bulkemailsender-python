from smtplib import SMTP
import csv
gmail = 'admin@example.com'
password = 'yourpassword'
message = open('message.txt', mode='r').read()
message1 = str(message)
with open('ok - Sheet1.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for Name, Email in reader:

        mailto = Email
        subject = 'This is testing mail.'
        msg1 = 'Dear ' + Name + '\n' + message1
        msg = 'subject: {}\n\n {}'.format(subject, msg1)
        mailServer = SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmail, password)
        print('sending email to'+mailto+'\n')
        mailServer.sendmail(gmail, mailto, msg.encode('utf-8'))

        print('\n successfully sent to '+mailto)

        mailServer.quit()
file.close()

