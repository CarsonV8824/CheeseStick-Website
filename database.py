import sqlite3

class Database:

    def __init__(self, database="CheeseStick.sqlite"):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self._make_table()

    def _make_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS CheeseStick
    """)