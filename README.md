# Birthday Email Sender

This project is designed to send automated birthday wishes to friends via email. It utilizes a SQLite database to store friends' names, birth dates, and email addresses, and employs the SMTP protocol to send emails. The application is scheduled to run daily at midnight using GitHub Actions.

## Project Structure

```
birthday-email-sender
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── email_sender.py
│   ├── config.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   ├── test_database.py
│   └── test_email_sender.py
├── .github
│   └── workflows
│       └── daily_check.yml
├── data
│   └── friends.db
├── templates
│   └── birthday_email.html
├── .env.example
├── requirements.txt
├── setup.py
└── README.md
```

## Features

- **Database Management**: Store and manage friends' information using SQLite.
- **Email Sending**: Send personalized birthday emails using SMTP.
- **Automated Scheduling**: Use GitHub Actions to check for birthdays and send emails daily at midnight.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/birthday-email-sender.git
   cd birthday-email-sender
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy the `.env.example` to `.env` and fill in your SMTP credentials and database path.

4. **Database Initialization**:
   Run the application once to create the database and set up the initial data:
   ```bash
   python src/main.py
   ```

5. **Run the Application**:
   You can manually run the application to check for birthdays and send emails:
   ```bash
   python src/main.py
   ```

## Testing

To run the tests, use:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.