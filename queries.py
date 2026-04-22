import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# Query A
print("Query A:")
rows = cursor.execute("SELECT * FROM products").fetchall()
print(rows, "\n")

# Query B
print("Query B:")
rows = cursor.execute("SELECT name, price FROM products").fetchall()
print(rows, "\n")

# Query C
print("Query C:")
rows = cursor.execute("SELECT * FROM products WHERE id = 3").fetchall()
print(rows, "\n")

# Query D
print("Query D:")
rows = cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
print(rows, "\n")

# Query E
print("Query E:")
rows = cursor.execute("SELECT * FROM products ORDER BY price DESC").fetchall()
print(rows, "\n")

# Query F
print("Query F:")
rows = cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall()
print(rows, "\n")

# Query G (UPDATE)
print("Query G:")
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()

rows = cursor.execute("SELECT * FROM products").fetchall()
print(rows, "\n")