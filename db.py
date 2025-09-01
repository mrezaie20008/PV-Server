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
        self.db = connect(db)
        self.cur = self.db.cursor()
        self.table = table

    # Private Methods
    def _check_table(self, table: str):
        tables = self.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';")
        
        if not tables:
            return

        return tables


    # Properties
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        if table:
            try:
                data = self._check_table(table)
                
                if not data:
                    raise TableNotFoundError("The mentioned table not found!")
                
                self._table = table

            except OE as e:
                if findall("no such table", e.__str__()):
                    print("TABLE NOT FOUND!")
                
                elif findall("syntax error", e.__str__()):
                    print("SYNTAX ERROR")
                
                else:
                    print(e.__str__())
                
                exit()

        else:
            return
    
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

    def select_table(self, table: str, *columns: list):
        _columns = "*"

        if columns:
            _columns = ", ".join(columns)

        _query = f"SELECT {_columns} FROM {table}"
        
        data = self.execute(_query)

        return data

    def insert_table(self, **data):
        pass
    
    def __del__(self):
        self.db.close()

        

