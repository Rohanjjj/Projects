import getpass
import smtplib

# SMTP server configuration
HOST = 'smtp.gmail.com'
PORT = 587

# Email details
FROM_EMAIL = "rohanjjogi@gmail.com"
PASSWORD = getpass.getpass("Enter your email password: ")
MESSAGE = """Subject: Mail from Python Script

Hello,
This is a test email sent using a Python script.
"""

try:
    # Connect to the SMTP server
    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.ehlo()
    print(f"Echoing the server: {status_code} {response.decode()}")

    # Start TLS encryption
    status_code, response = smtp.starttls()
    print(f"Starting TLS Connection: {status_code} {response.decode()}")

    # Log in to the SMTP server
    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"Login to server: {status_code} {response.decode()}")

    # Send the email
    with open("client.txt", "r") as file:
        for line in file:
            TO_EMAIL = line.strip()
            if TO_EMAIL:
                smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
                print("Email sent successfully!")

except smtplib.SMTPException as e:
    print(f"Failed to send email. Error: {e}")

finally:
    # Quit the SMTP server connection
    smtp.quit()
