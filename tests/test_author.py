from lib.models.author import Author

def test_author_creation():
    author = Author(name="Test Author")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Test Author"
    def test_save_raises_on_duplicate_name_even_with_id_none():
        # Create an author, then manually create another with same name and id=None
        a1 = Author.create("Duplicate Name Test")
        a2 = Author(name="Duplicate Name Test")
        try:
            a2.save()
            assert False, "Expected ValueError for duplicate author name even if id is None"
        except ValueError as e:
            assert "already exists" in str(e)

    def test_update_to_existing_name_raises():
        # Create two authors, try to update one to other's name
        a1 = Author.create("First Name")
        a2 = Author.create("Second Name")
        a2.name = "First Name"
        try:
            a2.save()
            assert False, "Expected IntegrityError or ValueError when updating to duplicate name"
        except Exception as e:
            assert "already exists" in str(e) or "UNIQUE constraint failed" in str(e)

    def test_articles_returns_empty_for_new_author():
        author = Author.create("No Articles Author")
        articles = author.articles()
        assert isinstance(articles, list)
        assert len(articles) == 0

    def test_magazines_returns_empty_for_new_author():
        author = Author.create("No Magazines Author")
        magazines = author.magazines()
        assert isinstance(magazines, list)
        assert len(magazines) == 0

    def test_topic_areas_returns_empty_for_new_author():
        author = Author.create("No Topics Author")
        topics = author.topic_areas()
        assert isinstance(topics, list)
        assert len(topics) == 0

    def test_delete_removes_articles_but_not_magazines():
        # Create author, magazine, article
        author = Author.create("Cascade Author")
        conn = author.save.__self__.__globals__['get_connection']()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("CascadeMag", "CascadeCat"))
        mag_id = cursor.lastrowid
        conn.commit()
        author.add_article(mag_id, "Cascade Article")
        # Delete author
        author.delete()
        # Article should be gone, magazine should remain
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author.id,))
        assert cursor.fetchall() == []
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (mag_id,))
        assert cursor.fetchone() is not None

    def test_repr_with_none_id():
        author = Author(name="NoId Author")
        assert repr(author) == "<Author(id=None, name='NoId Author')>"

    # Additional tests

    def test_create_and_find_by_name():
        name = "FindByName Author"
        author = Author.create(name)
        found = Author.find_by_name(name)
        assert found is not None
        assert found.name == name

    def test_create_and_find_by_id():
        author = Author.create("FindById Author")
        found = Author.find_by_id(author.id)
        assert found is not None
        assert found.name == "FindById Author"

    def test_add_article_and_articles_method():
        author = Author.create("Article Author")
        conn = author.save.__self__.__globals__['get_connection']()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("TestMag", "Science"))
        magazine_id = cursor.lastrowid
        conn.commit()
        author.add_article(magazine_id, "Test Article")
        articles = author.articles()
        assert any(a["title"] == "Test Article" for a in articles)

    def test_magazines_returns_unique_magazines():
        author = Author.create("Magazine Author")
        conn = author.save.__self__.__globals__['get_connection']()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Mag1", "Tech"))
        mag1_id = cursor.lastrowid
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Mag2", "Health"))
        mag2_id = cursor.lastrowid
        conn.commit()
        author.add_article(mag1_id, "Art1")
        author.add_article(mag2_id, "Art2")
        mags = author.magazines()
        mag_names = [m["name"] for m in mags]
        assert "Mag1" in mag_names and "Mag2" in mag_names

    def test_topic_areas_returns_unique_categories():
        author = Author.create("Topic Author")
        conn = author.save.__self__.__globals__['get_connection']()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("MagA", "History"))
        magA_id = cursor.lastrowid
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("MagB", "Science"))
        magB_id = cursor.lastrowid
        conn.commit()
        author.add_article(magA_id, "Hist Article")
        author.add_article(magB_id, "Sci Article")
        categories = author.topic_areas()
        assert "History" in categories and "Science" in categories

    def test_delete_removes_author():
        author = Author.create("DeleteMe Author")
        author_id = author.id
        author.delete()
        assert Author.find_by_id(author_id) is None

    def test_find_by_id_returns_none_for_missing():
        assert Author.find_by_id(-9999) is None

    def test_find_by_name_returns_none_for_missing():
        assert Author.find_by_name("Nonexistent Author") is None

    def test_update_author_name():
        author = Author.create("Old Name")
        author.name = "New Name"
        author.save()
        updated = Author.find_by_id(author.id)
        assert updated.name == "New Name"
