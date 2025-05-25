# scripts/run_queries.py

from lib.models.author import Author
from lib.models.magazine import Magazine

def main():
    # 🔍 Get an author by ID
    author = Author.find_by_id(1)
    if author:
        print(f"\nArticles by {author.name}:")
        for article in author.articles():
            print(" -", article['title'])

        print(f"\nMagazines {author.name} contributed to:")
        for mag in author.magazines():
            print(" -", mag['name'])

        print(f"\nTopic areas of {author.name}:")
        for topic in author.topic_areas():
            print(" -", topic)
    else:
        print("No author found with ID 1.")

    # 📰 Get a magazine by ID
    magazine = Magazine.find_by_id(1)
    if magazine:
        print(f"\nArticles in '{magazine.name}':")
        for article in magazine.articles():
            print(" -", article['title'])

        print(f"\nTitles of articles in '{magazine.name}':")
        for title in magazine.article_titles():
            print(" -", title)

        print(f"\nAuthors who wrote for '{magazine.name}':")
        for contributor in magazine.contributors():
            print(" -", contributor['name'])

        print(f"\nAuthors with >=2 articles in '{magazine.name}':")
        for row in magazine.contributing_authors():
            print(" -", row['name'])
    else:
        print("No magazine found with ID 1.")

if __name__ == "__main__":
    main()