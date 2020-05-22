from smtplib import SMTP
import csv
gmail = 'example@example.com'
password = '*************'
message = open('message.txt',mode='r').read() 

with open ('ok - Sheet1.csv') as file:
    reader = csv.reader(file)
    next(reader)

    for Name, Email in reader:

            mailto = Email
            msg = ('Dear ' + Name +'\n'+ message).encode('utf-8')
            mailServer = SMTP('smtp.gmail.com', 587)
            mailServer.starttls()
            mailServer.login(gmail, password)
            print('sending email to'+mailto+'\n')
            mailServer.sendmail(gmail, mailto, msg)
            
            print('\n successfully sent to '+mailto)
            
            mailServer.quit()
file.close()
