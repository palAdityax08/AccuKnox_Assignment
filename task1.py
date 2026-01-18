import sqlite3
import json

# Note: Since no real URL was provided, I am mocking the API response data.
def fetch_books_data():
    # In a real project, I would use: response = requests.get('api_url').json()
    return [
        {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
        {"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
        {"title": "Artificial Intelligence", "author": "Russell & Norvig", "year": 2020}
    ]

def save_to_db(books):
    # Connect to SQLite (it creates the file 'books.db' automatically)
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    # Simple SQL to create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')
    
    # Loop through the list and insert each book
    print("Saving books to database...")
    for book in books:
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", 
                       (book["title"], book["author"], book["year"]))
    
    conn.commit()
    conn.close()

def display_data():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    print("\nReading from Database:")
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)
        
    conn.close()

if __name__ == "__main__":
    data = fetch_books_data()
    save_to_db(data)
    display_data()