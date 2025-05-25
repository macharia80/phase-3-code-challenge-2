from lib.models.author import Author
from lib.models.magazine import Magazine

def seed_data():
    # Create authors
    author1 = Author(name="Jane Smith")
    author1.save()

    author2 = Author(name="John Doe")
    author2.save()

    # Create magazines
    mag1 = Magazine(name="Tech Weekly", category="Technology")
    mag1.save()

    mag2 = Magazine(name="Fashion Monthly", category="Fashion")
    mag2.save()

    # Add articles
    author1.add_article(mag1.id, "The Rise of AI")
    author1.add_article(mag2.id, "Sustainable Fashion Trends")
    author2.add_article(mag1.id, "Why Python is Still Relevant")

    print("🌱 Sample data seeded.")

if __name__ == "__main__":
    seed_data()