import sqlite3
from lib.database import get_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        except sqlite3.IntegrityError:
            # Handle duplicate names
            conn.rollback()
            cursor.execute("SELECT id FROM authors WHERE name = ?", (self.name,))
            self.id = cursor.fetchone()[0]
        finally:
            conn.commit()
            conn.close()