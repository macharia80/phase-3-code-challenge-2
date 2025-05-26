import sys
import os

# Add root folder to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.database import initialize, get_connection

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

        # Create magazines
        mag1 = Magazine(name="Science Today", category="Science")
        mag2 = Magazine(name="Tech Weekly", category="Technology")
        mag3 = Magazine(name="Health Monthly", category="Health")
        mag4 = Magazine(name="Fashion Trends", category="Lifestyle")
        mag5 = Magazine(name="Global Politics", category="Politics")

        mag1.save()
        mag2.save()
        mag3.save()
        mag4.save()
        mag5.save()

        print(f"📚 Created magazine: {mag1.name} (ID: {mag1.id}, Category: {mag1.category})")
        print(f"📚 Created magazine: {mag2.name} (ID: {mag2.id}, Category: {mag2.category})")
        print(f"📚 Created magazine: {mag3.name} (ID: {mag3.id}, Category: {mag3.category})")
        print(f"📚 Created magazine: {mag4.name} (ID: {mag4.id}, Category: {mag4.category})")
        print(f"📚 Created magazine: {mag5.name} (ID: {mag5.id}, Category: {mag5.category})")

        # Add articles
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("Quantum Computing Breakthroughs", author1.id, mag1.id))

        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("AI Ethics in Modern Tech", author2.id, mag2.id))

        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("Mental Health Awareness", author3.id, mag3.id))

        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("Sustainable Fashion Innovations", author1.id, mag4.id))

        cursor.execute("""
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        """, ("Rise of Populist Movements", author2.id, mag5.id))

        conn.commit()
        conn.close()

        print("✍️ Articles added successfully.")

        # Print all articles by Sam Macharia
        print("\n📰 All articles by Sam Macharia:")
        for article in author1.articles():
            print(f" - {article['title']}")

        # Print all articles by Rodgers Ogada
        print("\n📰 All articles by Rodgers Ogada:")
        for article in author2.articles():
            print(f" - {article['title']}")

        # Print all articles by Loyce Tsuma
        print("\n📰 All articles by Loyce Tsuma:")
        for article in author3.articles():
            print(f" - {article['title']}")

        # Print all articles in Science Today
        print("\n📚 Articles in Science Today:")
        for article in mag1.articles():
            print(f" - {article['title']}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    main()