from pathlib import Path
from pickle import dump
from sqlite3 import connect


def build_db(tables: dict[str:dict], db: str | Path):
    db = connect(db)
    cur = db.cursor()

    TEMPLATE = """
    CREATE TABLE IF NOT EXISTS {}({})
    """

    def order(feilds: dict):
        __string = ""
        

        for k, dt in feilds.items():
            if k == "E-FK":
                __string += f"{dt}"
                break

            elif k == list(feilds.keys())[-1]:
                __string += f"{k} {dt}"
                continue

            __string += f"{k} {dt}, "

        return __string


    for tn, cs in tables.items():
        cur.execute(TEMPLATE.format(tn, order(cs)))
        db.commit()

        print(f"\033[92m[BUILD] {tn} table created successfully!")


def build():
    HOME_DIR = Path(__file__).parent
    LOGS_DIR = HOME_DIR / "Logs"
    DB_DIR = HOME_DIR / "DBs"
    VID_DIR = HOME_DIR / "Videos"
    TEMP_DIR = HOME_DIR / ".temp"
    
    DB_FILE = DB_DIR / "main.db"
    TABLES = {
            "users": {
                "ID": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "username": "CHAR(128) NOT NULL",
                "password": "CHAR(255) NOT NULL",
                "Auth": "CHAR(255) NOT NULL"
                },
            "history": {
                "ID": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "Date": "CHAR(16) DEFAULT CURRENT_DATE",
                "Time": "CHAR(16) DEFAULT CURRENT_TIME",
                "User": "INTEGER NOT NULL",
                "E-FK": "FOREIGN KEY (User) REFERENCES users(ID)"
                },
    }
    
    # Making the folders
    for f in [fo for fn, fo in locals().items() if (fn.endswith("_DIR") and fn.upper()) and not fn.startswith("_")]:
        f.mkdir(exist_ok=True)

    _objs = {on:oo for on, oo in locals().items() if not on.startswith("_") and on.upper()}
    _file = open(HOME_DIR / ".bin", "wb")
    # Dumping the OBJECT
    dump(_objs, _file)

    # Building DataBase
    build_db(TABLES, DB_FILE)
    
    print("\033[94m="*20)
    print("\033[92m\033[01mBUILDING IS DONE!\033[00m")
    print("\033[94m="*20, "\033[00m")


if __name__ == "__main__":
    build()

