# lib/debug.py
from lib.models.author import Author
from lib.models.magazine import Magazine

def main():
    # Try creating a new author and article
    author = Author(name="Sam Macharia")
    author.save()

    mag = Magazine(name="Science Today", category="Science")
    mag.save()

    author.add_article(mag.id, "Quantum Computing Breakthroughs")

    print("All articles by Alice Johnson:")
    for article in author.articles():
        print(article['title'])

if __name__ == "__main__":
    main()