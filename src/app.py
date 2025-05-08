from flask import Flask, request, redirect, url_for, render_template_string
import os
from database import Database # Assuming database.py is in the same directory or src is in PYTHONPATH

# Determine the absolute path to the project root to locate the database
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(project_root, 'data', 'friends.db')

app = Flask(__name__)
db = Database(db_file=db_path)

# HTML template for the form and displaying friends (optional)
# For simplicity, keeping it basic. You might want to move this to a separate HTML file in a 'templates' folder for larger apps.
HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Friend</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
        .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        form { margin-bottom: 20px; }
        label { display: block; margin-top: 10px; margin-bottom: 5px; }
        input[type='text'], input[type='email'], input[type='date'] {
            width: calc(100% - 22px);
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type='submit'] {
            background-color: #5cb85c;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type='submit']:hover { background-color: #4cae4c; }
        .message { padding: 10px; margin-bottom:15px; border-radius:4px; }
        .success { background-color: #dff0d8; color: #3c763d; border: 1px solid #d6e9c6; }
        .error { background-color: #f2dede; color: #a94442; border: 1px solid #ebccd1; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Add a New Friend</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="message {{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}
        <form method="POST" action="{{ url_for('add_friend_route') }}">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="birth_date">Birth Date (YYYY-MM-DD):</label>
            <input type="date" id="birth_date" name="birth_date" required pattern="\\d{4}-\\d{2}-\\d{2}">
            
            <input type="submit" value="Add Friend">
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/add', methods=['POST'])
def add_friend_route():
    try:
        name = request.form['name']
        email = request.form['email']
        birth_date_str = request.form['birth_date'] # Expected format YYYY-MM-DD

        # Validate date format if needed, though type="date" helps
        # For database compatibility, ensure it's stored as YYYY-MM-DD or MM-DD as per your DB schema
        # The current database schema stores it as TEXT, so YYYY-MM-DD is fine.
        # The get_todays_birthdays() method extracts MM-DD using substr(birth_date, 6)
        # So, the input format YYYY-MM-DD is compatible.

        db.add_friend(name, email, birth_date_str)
        # Flash a success message (optional, requires app.secret_key = 'some secret key')
        # from flask import flash
        # app.secret_key = 'your secret key' # Add this near app initialization
        # flash('Friend added successfully!', 'success')
    except Exception as e:
        print(f"Error adding friend: {e}") # Log error
        # flash(f'Error adding friend: {e}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Make sure to set FLASK_APP=src/app.py and run with `flask run`
    # or run `python src/app.py` for development.
    # For production, use a proper WSGI server like Gunicorn.
    app.run(debug=True, port=5001) # Running on a different port in case 5000 is in use
