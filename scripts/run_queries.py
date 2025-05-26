import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now these imports should work
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.database import initialize

def main():
    try:
        initialize()  # Make sure tables exist

        # Create and save authors
        author1 = Author(name="Sam Macharia")
        author2 = Author(name="Rodgers Ogada")
        author3 = Author(name="Loyce Tsuma")

        author1.save()
        author2.save()
        author3.save()

        print("👤 All authors saved successfully.")

        # Create and save magazines
        mag1 = Magazine(name="Science Today", category="Science")
        mag2 = Magazine(name="Tech Weekly", category="Technology")
        mag3 = Magazine(name="Health Monthly", category="Health")
        mag4 = Magazine(name="Fashion Trends", category="Lifestyle")

        mag1.save()
        mag2.save()
        mag3.save()
        mag4.save()

        print("📚 All magazines saved successfully.")

    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    main()