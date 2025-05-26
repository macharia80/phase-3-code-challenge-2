import sys
import os

# Add current directory to Python path so it can find lib/
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.database import initialize

def main():
    initialize()  # ✅ Creates tables if they don't exist

    # Create and save an author
    author = Author(name="Sam Macharia")
    author.save()

    # Create and save a magazine
    mag = Magazine(name="Science Today", category="Science")
    mag.save()

    # Add article
    author.add_article(mag.id, "Quantum Computing Breakthroughs")

    # Print all articles by the author
    print("📰 All articles by Sam Macharia:")
    for article in author.articles():
        print(f" - {article['title']}")

if __name__ == "__main__":
    main()