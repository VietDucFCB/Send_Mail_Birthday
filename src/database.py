import sqlite3
import datetime

class Database:
    def __init__(self, db_file='data/friends.db'):
        self.db_file = db_file
        self._create_tables_if_not_exist()
        
    def _create_tables_if_not_exist(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS friends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
        ''')
        conn.commit()
        conn.close()
    
    def add_friend(self, name, email, birth_date):
        """Add a friend to the database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO friends (name, email, birth_date) VALUES (?, ?, ?)',
                      (name, email, birth_date))
        conn.commit()
        conn.close()
    
    def get_todays_birthdays(self):
        """Get all friends who have a birthday today"""
        today = datetime.datetime.now().strftime("%m-%d")
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Query for matching month and day, regardless of year
        cursor.execute('''
        SELECT name, email FROM friends 
        WHERE substr(birth_date, 6) = ?
        ''', (today,))
        
        birthday_friends = cursor.fetchall()
        conn.close()
        return birthday_friends