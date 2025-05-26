import sqlite3
from lib.database import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self.id = cursor.lastrowid
        except sqlite3.IntegrityError:
            conn.rollback()
            cursor.execute("SELECT id FROM magazines WHERE name = ?", (self.name,))
            self.id = cursor.fetchone()[0]
        finally:
            conn.commit()
            conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [{'title': row[0]} for row in rows]