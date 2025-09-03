from sqlite3 import (
    connect,
    OperationalError as OE,
)
from pathlib import Path
from exceptions import *
from re import (
    compile, 
    findall, 
    IGNORECASE as IC
)


class DB:
    def __init__(self, db: Path, table: str | None = None):
        self.db = connect(db, check_same_thread=False)
        self.cur = self.db.cursor()
        self.table = table


    # Methods
    def execute(self, query: str):
        try:
            self.cur.execute(query)

            return self.cur.fetchall()

        except OE as ie:
            ie = ie.__str__()

            if findall("no such table", ie, IC):
                raise TableNotFoundError("The mentioned table does not exist!")

            elif findall("syntax error", ie, IC):
                raise SyntaxError("Your SQLite3 query's syntax is incorrect!")

            else:
                raise Exception(ie)

    def find(self, column: str, value: str, *selected):
        __selected_columns = ", ".join(selected) if selected else "*"
        data = self.execute(f"SELECT {__selected_columns}  FROM {self.table} WHERE {column} = '{value}'")

        if data:
            return data

        else:
            return



    def select_all(self):
        _query = f"SELECT * FROM {self.table}"
        data = self.execute(_query)

        return data


    def insert_table(self, **data):
        pass


    def __del__(self):
        self.cur.close()
        self.db.close()

