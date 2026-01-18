import csv
import sqlite3

def import_csv():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    
    # Open the CSV file and read it
    with open("users.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                           (row["name"], row["email"]))
    
    conn.commit()
    print("CSV data successfully imported into SQLite DB.")
    conn.close()

if __name__ == "__main__":
    import_csv()