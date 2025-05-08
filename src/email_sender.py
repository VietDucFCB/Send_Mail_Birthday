import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

class EmailSender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
    
    def send_birthday_email(self, recipient_email, recipient_name):
        """Send a birthday email to a friend"""
        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Happy Birthday, {recipient_name}!"
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        
        # Create HTML version of the message
        html = f"""
        <html>
            <body>
                <h1>Happy Birthday, {recipient_name}!</h1>
                <p>Wishing you a fantastic day filled with joy and happiness!</p>
                <p>Best wishes,</p>
                <p>Your Friend</p>
            </body>
        </html>
        """
        
        # Attach HTML content
        msg.attach(MIMEText(html, 'html'))
        
        try:
            # Create SMTP session
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"Birthday email sent to {recipient_name} at {recipient_email}")
            return True
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {str(e)}")
            return False