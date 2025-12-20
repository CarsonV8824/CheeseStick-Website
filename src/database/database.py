import sqlite3
import json

#might use a different databse instead of sqlite later. This is a prototype of the database class

class Database:

    #constructor
    def __init__(self, database="CheeseStick.sqlite"):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self._make_table()

    #Can change data in table later if needed
    def _make_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS CheeseStick
        (id INTEGER PRIMARY KEY,
        name TEXT,
        quantity INTEGER)
    """)
        self.connection.commit()
    
    #adds data to the database
    def add_data(self,data):
        self.cursor.execute("INSERT INTO CheeseStick (name, quantity) VALUES (?, ?)", data)
        self.connection.commit()

    #retrieves data from the database
    def get_data(self):
        self.cursor.execute("SELECT * FROM CheeseStick")
        return self.cursor.fetchall()
    
    #the ? prevents SQL injection attacks
    def get_certain_data(self, data_id):
        self.cursor.execute("SELECT * FROM CheeseStick WHERE id=?", (data_id,))
        return self.cursor.fetchone()
    
    def close(self):
        self.connection.close()