# lib/models/author.py

import sqlite3
from lib.db.connection import get_connection


class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

    def save(self):
        """Save this author to the database."""
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            # Insert new author
            try:
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self.name,)
                )
                self.id = cursor.lastrowid
            except sqlite3.IntegrityError:
                conn.rollback()
                raise ValueError(f"Author with name '{self.name}' already exists.")
        else:
            # Update existing author
            cursor.execute(
                "UPDATE authors SET name = ? WHERE id = ?",
                (self.name, self.id)
            )
        conn.commit()

    @classmethod
    def create(cls, name):
        """Create and save a new author."""
        author = cls(name=name)
        author.save()
        return author

    @classmethod
    def find_by_id(cls, author_id):
        """Find an author by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        if row:
            return cls(id=row["id"], name=row["name"])
        return None

    @classmethod
    def find_by_name(cls, name):
        """Find an author by name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return cls(id=row["id"], name=row["name"])
        return None

    def articles(self):
        """Get all articles written by this author."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        return cursor.fetchall()

    def magazines(self):
        """Get all unique magazines this author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* 
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def add_article(self, magazine_id, title):
        """Add a new article for this author in a specific magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, (title, self.id, magazine_id))
        conn.commit()

    def topic_areas(self):
        """Get unique categories of magazines the author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        return [row["category"] for row in cursor.fetchall()]

    def delete(self):
        """Delete this author from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        conn.commit()