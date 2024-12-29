import smtplib
sender_email="enteryourmailhere"
recipient=input("enter the recipient mail here")
#port 587 is chosen as the stam=ndard port blocks public requests
connection=smtplib.SMTP("smtp.gmail.com",587)
#with the command below, smtp  connection is made and  encryption is made
connection.starttls()
#look at readme to find out how to get  the one-time password so  u  dont have to login everytime with the password
connection.login(sender_email,"app_security_password")

message ='Subject:test\n\n\nhi theree'
#to sent mail
connection.sendmail(sender_email,recipient,message)
connection.close()
