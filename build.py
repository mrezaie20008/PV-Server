from pathlib import Path
from pickle import dump


def build():
    HOME_DIR = Path(__file__).parent
    LOGS_DIR = HOME_DIR / "Logs"
    DB_DIR = HOME_DIR / "DBs"
    VID_DIR = HOME_DIR / "Videos"
    TEMP_DIR = HOME_DIR / ".temp"
    
    DB_FILE = DB_DIR / "main.db"
    TABLES = [
        "users",
        "history",
    ]
    
    # Making the folders
    for f in [fo for fn, fo in locals().items() if (fn.endswith("_DIR") and fn.upper()) and not fn.startswith("_")]:
        f.mkdir(exist_ok=True)

    _objs = {on:oo for on, oo in locals().items() if not on.startswith("_") and on.upper()}
    _file = open(HOME_DIR / ".bin", "wb")
    # Dumping the OBJECT
    dump(_objs, _file)

    print("\033[92m\033[01mBUILDING IS DONE!\033[00m")


if __name__ == "__main__":
    build()

