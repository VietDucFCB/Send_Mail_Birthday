import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "kkagiuma1@gmail.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "Kkagiuma2004@")
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/friends.db")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "Happy Birthday!")
EMAIL_TEMPLATE_PATH = os.getenv("EMAIL_TEMPLATE_PATH", "templates/birthday_email.html")