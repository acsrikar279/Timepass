
# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
sender_id = 'xxxxxx@gmail.com'
sender_password = 'xxxxxxxxx'
receiver_id = 'xxxxxx@xxxxxx.xxxx'

# Authentication
s.login(sender_id, sender_password)
 
# message to be sent
message = "Test message. This message is sent using Python Script"
 
# sending the mail
s.sendmail(sender_id, receiver_id, message)
 
# terminating the session
s.quit()
