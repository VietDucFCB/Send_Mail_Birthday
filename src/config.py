import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SMTP_SERVER = os.getenv("SMTP_SERVER", "your_smtp_server_address")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587)) # Common default, non-sensitive
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your_email_username") # Generic placeholder
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_email_password") # Generic placeholder
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/friends.db") # This is usually fine as a default
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "Happy Birthday!")   # Fine as a default
EMAIL_TEMPLATE_PATH = os.getenv("EMAIL_TEMPLATE_PATH", "templates/birthday_email.html") # Fine as a default

# It's good practice to check if critical environment variables are set, especially for production.
# You could add checks here to ensure SMTP_USERNAME and SMTP_PASSWORD are not the placeholder values
# when the application starts in a production-like environment.
# For example:
# if SMTP_USERNAME == "your_email_username" or SMTP_PASSWORD == "your_email_password":
#     print("WARNING: SMTP credentials are not set or are using placeholder values. Email sending may fail.")
#     # Depending on the application, you might want to raise an error or exit here
#     # if not os.getenv("FLASK_DEBUG"): # e.g. only raise error if not in debug mode
#     #     raise ValueError("SMTP_USERNAME and SMTP_PASSWORD must be set in the environment.")