import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine

def main():
    # Example usage
    author = Author(name="Sam Macharia")
    author.save()

    mag = Magazine(name="Science Today", category="Science")
    mag.save()

    author.add_article(mag.id, "Quantum Computing Breakthroughs")
    author.add_article(mag.id, "Rise Of AI")
    author.add_article(mag.id, "Rise Of Humanoids")
    author.add_article(mag.id, "Downfall Of Network Engineering")
    author.add_article(mag.id, "The Future of Space Travel")
    author.add_article(mag.id, "Climate Change and Tech Solutions")
    author.add_article(mag.id, "Ethics in Artificial Intelligence")
    author.add_article(mag.id, "Renewable Energy Innovations")


    print("📰 All articles by Sam Macharia:")
    for article in author.articles():
        print(article['title'])

if __name__ == "__main__":
    main()