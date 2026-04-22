import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

def is_valid_name(name):
    return isinstance(name, str) and len(name) >= 2 and "<" not in name and ">" not in name and ";" not in name

def is_valid_username(username):
    return isinstance(username, str) and username != "" and " " not in username

def is_valid_password(password):
    return isinstance(password, str) and len(password) >= 6
 
 
def search_product_safe(name):
    if not is_valid_name(name):
        print("Invalid name")
        return None
    
    query = "SELECT * FROM products WHERE name LIKE ?"
    return conn.execute(query, (f"%{name}%",)).fetchall()

def login_safe(username, password):
    if not is_valid_username(username):
        print("Invalid username")
        return None
    
    if not is_valid_password(password):
        print("Invalid password")
        return None

    query = "SELECT * FROM users WHERE username=? AND password=?"
    return conn.execute(query, (username, password)).fetchone()

print("Test 1:", search_product_safe('cement'))
print("Test 2:", search_product_safe(''))
print("Test 3:", search_product_safe('<script>'))

print("Test 4:", login_safe('admin', 'admin123'))
print("Test 5:", login_safe('admin', 'ab'))
print("Test 6:", login_safe('ad min', 'pass123'))