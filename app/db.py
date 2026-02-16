import sqlite3

def get_connection(path="db/sales.db"):
    return sqlite3.connect(path)


