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
            conn.commit()
        except sqlite3.IntegrityError:
            # Handle duplicate names
            conn.rollback()
            cursor.execute("SELECT id FROM authors WHERE name = ?", (self.name,))
            self.id = cursor.fetchone()[0]
        finally:
            conn.close()

    def add_article(self, magazine_id, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (title, self.id, magazine_id)
        )
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles
            WHERE author_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [{'title': row[0]} for row in results]