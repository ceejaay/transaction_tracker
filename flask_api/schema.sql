DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transactions;

CREATE TABLE IF NOT EXISTS  merchants (
    merchant_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name text, description text);


CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name text, 
    last_name text, 
    dob text,
    merchant_user_id INTEGER NOT NULL, 
    FOREIGN KEY (merchant_user_id) REFERENCES merchants (merchant_id));

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    amount text, 
    description text,
    merchant_transaction_id INTEGER NOT NULL, 
    FOREIGN KEY (merchant_transaction_id) REFERENCES merchants);
