import smtplib, ssl #both standard libraries for email sending vaghera affirs
import os
def send_email(message_to_send):
    Host="smtp.gmail.com" #constant value
    Port=465 #const

    username = "mahajanshubham54321@gmail.com"

    password = os.getenv("password_for_python_app")
    # this is app passowrd created in google acc
    # manage google acc< security< app password
    # the password was then stored in an environment variable in windows  for security purposes
    #after editing environment variables close pytcharm and open it again for it to update



    receiver ="mahajanshubham54321@gmail.com"
    Context=ssl.create_default_context()

    message=message_to_send

    with smtplib.SMTP_SSL(host=Host,port=Port,context=Context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)