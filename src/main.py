from database import Database
from email_sender import EmailSender
import datetime
import schedule
import time
import os # Added for .env loading in main for scheduled job

def send_birthday_emails():
    """Check for birthdays today and send emails"""
    print(f"Running birthday check on {datetime.datetime.now()}")
    
    db = Database()
    email_sender = EmailSender()
    
    # Get friends with birthdays today
    birthday_friends = db.get_todays_birthdays()
    
    if not birthday_friends:
        print("No birthdays today!")
        return
    
    # Send emails to each birthday friend
    for friend in birthday_friends:
        name, email = friend
        print(f"Sending birthday email to {name} ({email})")
        email_sender.send_birthday_email(email, name)

def main_cli():
    """Command-line interface to send birthday emails immediately."""
    # This function can be called directly via the console script
    send_birthday_emails()

def main():
    """Schedules the birthday email check to run daily."""
    # Load .env file here if running as a scheduled service
    # This ensures env variables are loaded when the scheduler runs the job
    from dotenv import load_dotenv
    load_dotenv()

    print("Starting birthday email scheduler...")
    # Schedule the job to run every day at a specific time, e.g., 9:00 AM
    # You can adjust the time as needed.
    schedule.every().day.at("09:00").do(send_birthday_emails)

    print(f"Scheduled job: {schedule.get_jobs()}")

    while True:
        schedule.run_pending()
        time.sleep(60) # Check every minute

if __name__ == "__main__":
    # If you want to run the scheduler directly:
    # main()
    # If you want to run the task once immediately (e.g., for testing or via CLI):
    main_cli()