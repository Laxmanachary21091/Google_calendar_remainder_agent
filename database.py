import sqlite3

def init_db():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        title TEXT,
                        time TEXT
                    )''')
    conn.commit()
    conn.close()

def save_event(date, title, time):
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (date, title, time) VALUES (?, ?, ?)", (date, title, time))
    conn.commit()
    conn.close()

def get_all_events():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return events
