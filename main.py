import smtplib
from email.message import EmailMessage
try:
    #Replace these with your email and password 
    my_email = 'your email'
    password = 'your password'

    # Create the email message
    message = EmailMessage()
    message['From'] = my_email
    message['To'] = 'someone@example.com'
    message['Subject'] = 'Subject of email'
    message.set_content('This is the body of the email.')   


    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(message)

        
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate.Check your email and password.")

except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")