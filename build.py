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
    SECRET_KEY = "TW9oYW1tYWQ6UmV6YWllOjIwMDg6TW9oYW1tYWRAOTk="
    
    DB_FILE = DB_DIR / "main.db"
    
    TABLES_NAMES = [
        "users",
        "history"
    ]
    TABLES_CONFIG = {
            TABLES_NAMES[0]: {
                "ID": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "username": "CHAR(128) NOT NULL",
                "password": "CHAR(255) NOT NULL",
                "Auth": "CHAR(255) NOT NULL"
                },
            TABLES_NAMES[1]: {
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
    build_db(TABLES_CONFIG, DB_FILE)
    
    print("\033[94m="*20)
    print("\033[92m\033[01mBUILDING IS DONE!\033[00m")
    print("\033[94m="*20, "\033[00m")


if __name__ == "__main__":
    build()

