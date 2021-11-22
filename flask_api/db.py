# import sqlite3
# print("werking")

# def connect_to_db():
#     conn = sqlite3.connect('database.db')
#     return conn

# def create_db_table(con):
#     try:
#         con.execute('''
#             CREATE TABLE IF NOT EXISTS  merchants (
#                 merchant_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 name text,
#                 description text
#                 );
#                 '''
#                 )
#         con.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 first_name text, 
#                 last_name text, 
#                 dob text,
#                 merchant_user_id INTEGER NOT NULL, 
#                 FOREIGN KEY (merchant_user_id) REFERENCES merchants (merchant_id));
#                 '''
#                 )
#         con.execute('''
#             CREATE TABLE IF NOT EXISTS transactions (
#                 transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 amount text, 
#                 description text,
#                 merchant_transaction_id INTEGER NOT NULL, 
#                 user_transaction_id INTEGER NOT NULL, 
#                 FOREIGN KEY (merchant_transaction_id) REFERENCES merchants (merchant_id),
#                 FOREIGN KEY (user_transaction_id) REFERENCES users (users_id)
#                 );
#                 '''
#                 )
#         con.commit()
#         print("Merchants table created")
#     except:
#         print("failed")
#     finally:
#         con.close()

# # db = connect_to_db()
# # create_db_table(db)

# def insert_merchant(new_merchant):
#     inserted_user = {}
#     try:
#         conn = connect_to_db()
#         cur = conn.cursor()
#         cur.execute("INSERT INTO merchants (name, description) VALUES (?, ?)", 
#                 (new_merchant['name'], new_merchant['description'])
#                 )
#         conn.commit()
#         inserted_user = get_merchant_by_id(cur.lastrowid)
#     except:
#         conn.rollback()
#     finally:
#         conn.close()
#     return inserted_user

# def get_merchants():
#     merchants = []
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM merchants")
#         rows = cur.fetchall()
#         for i in rows:
#             merchant = {}
#             merchant['merchant_id'] = i['merchant_id']
#             merchant['name'] = i['name']
#             merchant['description'] = i['description']
#             merchants.append(merchant)
#     except:
#         merchants = []
#     return merchants

# def get_merchant_by_id(merch_id):
#     merchant = {}
#     try:
#         conn = connect_to_db()
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM merchants WHERE merchant_id = ?", (merch_id,))
#         row = cur.fetchone()

#         merchant['merchant_id'] = row['merchant_id']
#         merchant['name'] = row['name']
#         merchant['description'] = row['description']
#     except:
#         print("__ 2__ get one")
#         merchant = {}
#     return merchant

# def update_merchant(merchant):
#     updated_merchant = {}
#     try:
#         conn = connect_to_db()
#         cur = conn.cursor()
#         cur.execute("UPDATE merchants SET name = ?, description = ? WHERE merchant_id = ?", 
#                 (merchant['name'], merchant['description'],))
#         conn.commit()
#         updated_merchant = get_merchant_by_id(merchant['merchant_id'])
#     except:
#         conn.rollback()
#         update_merchant = {}
#     finally:
#         conn.closed()
#     return update_merchant

# def delete_merchant(merch_id):
#     message = {}
#     try:
#         conn = connect_to_db()
#         conn.execute("DELETE FROM merchants WHERE merchant_id = ?", (merch_id,))
#         conn.commit()
#         message['status'] = "User Deleted Succesfully"
#     except:
#         message['status'] = "Cannot Delete User"
#     finally:
#         conn.close()
#     return message
