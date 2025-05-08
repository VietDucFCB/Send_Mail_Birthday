def format_date(date):
    return date.strftime("%B %d, %Y")

def generate_birthday_email(name):
    return f"Subject: Happy Birthday, {name}!\n\nDear {name},\n\nWishing you a wonderful birthday filled with joy and happiness!\n\nBest wishes,\nYour Birthday Reminder Bot"