import sqlite3
import logging


class SqliteAdapter:
    def __init__(self, 
                 path):
        self.path = path

        self.db_connection = None
        self.cursor = None

        self._connect_to_db()

    def _connect_to_db(self):
        self.db_connection = sqlite3.connect(self.path, check_same_thread=False)
        self.cursor = self.db_connection.cursor()
        logging.info("Connection to SQLite was established")
    
    def close_connection(self):
        self.db_connection.close()

    def start_db(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS students ('
            'name TEXT, '
            'age INTEGER, '
            'belt TEXT'
            ')'
        )
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS gyms ('
            'name TEXT, '
            'location TEXT, '
            'capacity TEXT'
            ')'
        )
        self.db_connection.commit()

    def insert_data(self,
                 table_name: str,
                 columns_values: dict):
        
        columns = ",".join(list(columns_values.keys()))
        values = tuple(columns_values.values())
        placeholders = ",".join(["?"] * len(columns_values))
        
        self.cursor.execute(
            f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})',
            values
        )
        self.db_connection.commit()