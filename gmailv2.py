import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ChemVentory@gmail.com"  # Enter your address
receiver_email = "baranauskasm@wit.edu","ChemVentory@gmail.com","haddadm2@wit.edu" # Enter receiver address
password = input("Type your password and press enter: ") #password for our project email is -> chem132for
message = """\
Subject: Python eating its tail  
Hey Buddy this is emailing you through python on the terminal. 
Spoiler Alert: Ned Stark is still alive

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
