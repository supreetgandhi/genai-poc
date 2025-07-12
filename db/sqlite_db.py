import sqlite3

class SQLiteDB:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE tickets (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                status TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE kb_articles (
                id INTEGER PRIMARY KEY,
                question TEXT,
                answer TEXT
            )
        """)
        self.conn.commit()

    def execute(self, query, params=(), fetch=False, fetchone=False):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        if fetch:
            return cursor.fetchall()
        if fetchone:
            return cursor.fetchone()

db = SQLiteDB()
