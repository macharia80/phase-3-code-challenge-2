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
            # Handle duplicate names
            conn.rollback()
            cursor.execute("SELECT id FROM magazines WHERE name = ?", (self.name,))
            result = cursor.fetchone()
            if result:
                self.id = result[0]
            else:
                raise Exception(f"Failed to save magazine: {self.name}")
        finally:
            conn.commit()
            conn.close()