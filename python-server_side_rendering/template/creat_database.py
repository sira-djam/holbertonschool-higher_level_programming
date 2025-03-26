import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT INTO Products (name, category, price)
        VALUES
        ('Laptop', 'Electronics', 799.99),
        ('Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
