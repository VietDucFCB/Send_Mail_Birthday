import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file, if present
# GitHub Actions secrets will override these if names match
load_dotenv()

class EmailSender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        smtp_port_str = os.getenv("SMTP_PORT", "587")
        try:
            self.smtp_port = int(smtp_port_str)
        except ValueError:
            print(f"Error: Invalid SMTP_PORT value '{smtp_port_str}'. Using default 587.")
            self.smtp_port = 587

        # Try SENDER_EMAIL/PASSWORD first, then SMTP_USERNAME/PASSWORD as fallback
        self.sender_email = os.getenv("SENDER_EMAIL") or os.getenv("SMTP_USERNAME")
        self.sender_password = os.getenv("SENDER_PASSWORD") or os.getenv("SMTP_PASSWORD")

        if not all([self.smtp_server, self.sender_email, self.sender_password, self.smtp_port]):
            print("Error: Email sending not configured properly. Missing one or more of: SMTP_SERVER, SMTP_PORT, SENDER_EMAIL/SMTP_USERNAME, SENDER_PASSWORD/SMTP_PASSWORD.")
            # Consider raising an exception if you want to halt execution
            # raise ValueError("SMTP configuration is incomplete.")
            self.configured = False
        else:
            self.configured = True
            print("EmailSender initialized with:")
            print(f"  SMTP Server: {self.smtp_server}")
            print(f"  SMTP Port: {self.smtp_port}")
            print(f"  Sender Email: {self.sender_email}")
            # Avoid printing password, even if it's just '***'
            print(f"  Sender Password: {'Set' if self.sender_password else 'Not Set'}")


    def send_birthday_email(self, recipient_email, recipient_name):
        """Send a birthday email to a friend"""
        if not self.configured:
            print(f"Skipping email to {recipient_name} ({recipient_email}) due to incomplete EmailSender configuration.")
            return False

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Happy Birthday, {recipient_name}!"
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        
        # Create HTML version of the message
        # Ensure you have a templates/birthday_email.html or define HTML here
        # For simplicity, using a basic HTML string:
        html_template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'birthday_email.html')
        html_content = f"""
        <html>
            <body>
                <h1>Happy Birthday, {recipient_name}!</h1>
                <p>Wishing you a fantastic day filled with joy and happiness!</p>
                <p>Best wishes,</p>
                <p>Your Friend</p>
            </body>
        </html>
        """
        try:
            with open(html_template_path, 'r') as f:
                html_content = f.read().replace("{{name}}", recipient_name)
        except FileNotFoundError:
            print(f"Warning: Birthday email template not found at {html_template_path}. Using default HTML.")
            html_content = html_content.replace("{{name}}", recipient_name) # Basic replacement if needed

        
        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))
        
        try:
            # Create SMTP session with a timeout (e.g., 60 seconds)
            print(f"Attempting to send email to {recipient_name} via {self.smtp_server}:{self.smtp_port}")
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=60) as server:
                server.set_debuglevel(1) # Enable SMTP debug output
                print("Starting TLS...")
                server.starttls()
                print(f"Logging in as {self.sender_email}...")
                server.login(self.sender_email, self.sender_password)
                print("Sending message...")
                server.send_message(msg)
            print(f"Birthday email successfully sent to {recipient_name} at {recipient_email}")
            return True
        except smtplib.SMTPAuthenticationError as e:
            print(f"SMTP Authentication Error for {recipient_email}: {str(e)}.")
            print("Please check your sender email and password (or app password for services like Gmail).")
            return False
        except smtplib.SMTPConnectError as e:
            print(f"SMTP Connection Error for {recipient_email}: {str(e)}. Check SMTP server and port.")
            return False
        except smtplib.SMTPServerDisconnected as e:
            print(f"SMTP Server Disconnected for {recipient_email}: {str(e)}.")
            return False
        except TimeoutError as e: # socket.timeout is often aliased as TimeoutError
            print(f"SMTP Timeout for {recipient_email}: {str(e)}. Server might be slow or unreachable.")
            return False
        except Exception as e:
            print(f"Failed to send email to {recipient_email}. Error type: {type(e).__name__}, Message: {str(e)}")
            return False