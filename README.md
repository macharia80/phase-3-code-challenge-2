📰 Object Relations Code Challenge - Articles
This project models the relationship between Authors , Articles , and Magazines using SQLite and raw SQL queries in Python. It demonstrates how to manage many-to-many relationships through a relational database, while keeping object-oriented logic in Python.

🧩 Problem Statement
In this domain:

✅ An Author can write many Articles
✅ A Magazine can publish many Articles
✅ An Article belongs to one Author and one Magazine
✅ The Author-Magazine relationship is many-to-many
✅ Data is persisted in a SQL database (SQLite used here)
🛠️ Setup Instructions
Option 1: Using pipenv (Recommended)
pip install pipenv
pipenv install pytest sqlite3
pipenv shell
Option 2: Using venv
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install pytest
🗄️ Database Setup (SQLite)
The project uses SQLite for simplicity and ease of use
To Set Up the Database:
python scripts/setup_db.py
This creates a file called articles.db and sets up the schema with tables for authors, magazines, and articles.

To Seed Sample Data:
python lib/db/seed.py
 Running Queries
To see output from the model methods:
python scripts/run_queries.py
This script demonstrates querying:

All articles by an author
Magazines an author has contributed to
Authors who have written for a magazine
Article titles in a magazine
And more!
🧪 Testing with pytest
All core functionality is tested using pytest. You’ll find test files in the tests/ directory.
Run Tests:
pytest
Or with verbose output:
pytest -v
Tested features include:

CRUD operations for all models
Relationship queries
Complex SQL logic (e.g., filtering authors with multiple articles)
Transaction handling
📁 Folder Structure
articles_challenge/
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   └── debug.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
├── tests/
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
├── .gitignore
└── README.md
💡 Key Features Implemented
🧑‍💼 Author Methods
articles() – Get all articles written by the author
magazines() – Get all unique magazines the author has contributed to
add_article(magazine_id, title) – Add a new article to the database
topic_areas() – Get unique categories of magazines the author has written for
📚 Magazine Methods
articles() – Get all articles published in the magazine
contributors() – Get all authors who have written for the magazine
article_titles() – Get titles of all articles in the magazine
contributing_authors() – Get authors who have written at least two articles in the magazine
📰 Article Methods
save() – Save an article to the database
find_by_id() – Retrieve an article by its ID
🔄 Relationships
Many-to-many relationship between Author and Magazine via Article
Each Article links one Author to one Magazine
⚙️ Transactions
You can safely insert related records using transactions, such as adding an author and their articles together.

Example:
add_author_with_articles("Jane Smith", [
    {"title": "AI Trends", "magazine_id": 1},
    {"title": "Future Tech", "magazine_id": 2}
])
📝 Example Output
After running scripts/run_queries.py, you should see output like:
Articles by Jane Smith:
 - The Rise of AI
 - Sustainable Fashion Trends

Magazines Jane Smith contributed to:
 - Tech Weekly
 - Fashion Monthly

Authors who wrote for Tech Weekly:
 - Jane Smith
 - John Doe

Article titles in Tech Weekly:
 - The Rise of AI
 - Why Python is Still Relevant

Contributing authors in Tech Weekly:
 <empty unless someone has more than 2>
 🧪 Debugging
Use lib/debug.py for interactive debugging:
python lib/debug.py
This script allows you to create, save, and query objects interactively.

📦 Submission Requirements Met
✅ Raw SQL queries within Python classes
✅ Proper database schema design
✅ Efficient and correct SQL queries
✅ Transaction management
✅ OOP principles applied
✅ Protection against SQL injection
✅ Test coverage for all operations
✅ Git repository with incremental commits

🚀 Final Checklist
Install dependencies
pipenv install pytest sqlite3
or
pip install pytest
Activate environment
pipenv shell
or
source env/bin/activate
Setup DB
python scripts/setup_db.py
Seed test data
python lib/db/seed.py
Run queries
python scripts/run_queries.py
Run tests
pytest
🎉 You're Ready!

