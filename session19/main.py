import sqlite3
# crud -> create table, create record, read table or only record,  update, delete
con = sqlite3.connect("data.db")
cur = con.cursor()
command = """
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT, 
        price REAL, 
        stock INTEGER
    )
"""
cur.execute(command)

command = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT, 
        phone TEXT
    )
"""


cur.execute(command)

command = """
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER, 
    product_id INTEGER, 
    amount INTEGER
)"""
cur.execute(command)



# command = """
#     INSERT INTO product (label, price, stock) VALUES
#         ('iphone', 100, 3),
#         ('laptop', 200, 6),
#         ('pc', 300, 7)
# """
# cur.execute(command)
# con.commit()




# read a record or list of table record
# command = """
#     SELECT * FROM product
# """
# result = cur.execute(command)

# print(result.fetchall())



# command = """
#     UPDATE product 
#     SET label = 'iPhone 15', 
#         price = 150, 
#         stock = 10 
#     WHERE id = 1
# """
# cur.execute(command)
# con.commit()


# command = "DELETE FROM product WHERE id = 2"
# cur.execute(command)
# con.commit()




