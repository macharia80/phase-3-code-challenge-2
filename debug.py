import sys
import os

# Add root folder to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.database import initialize

def main():
    try:
        initialize()
        print("✅ Database initialized.")

        # Create authors
        author1 = Author(name="Sam Macharia")
        author2 = Author(name="Rodgers Ogada")
        author3 = Author(name="Loyce Tsuma")

        author1.save()
        author2.save()
        author3.save()

        print(f"👤 Created author: {author1.name} (ID: {author1.id})")
        print(f"👤 Created author: {author2.name} (ID: {author2.id})")
        print(f"👤 Created author: {author3.name} (ID: {author3.id})")

        # Create magazine
        mag = Magazine(name="Science Today", category="Science")
        mag.save()
        print(f"📚 Created magazine: {mag.name} (ID: {mag.id}, Category: {mag.category})")

        # Add article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("Quantum Computing Breakthroughs", author1.id, mag.id))
        conn.commit()
        conn.close()

        print("✍️ Article added successfully.")

        # Print all articles by Sam Macharia
        print("\n📰 All articles by Sam Macharia:")
        for article in author1.articles():
            print(f" - {article['title']}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    main()