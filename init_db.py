import sqlite3

connection = sqlite3.connect("database/school.db")

with open("database/init_db.sql", "r", encoding="utf-8") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("Database initialized")