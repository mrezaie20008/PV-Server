from pathlib import Path
from pickle import load
from os import listdir
from db import DB
from hashlib import md5


# Configurations
def configure():
    def get_variables():
        file = open(Path(__file__).parent / ".bin", "rb")
        
        return load(file)

    # Settings Section
    data = get_variables()

    for k, v in data.items():
        globals()[k] = v
    
    globals()['db'] =  DB(DB_FILE)

configure()


# Functions
def verify_token(token: str):
    db.table = "users"
    user = db.find("Auth", token, "ID", "username")

    return user


def salted_hash(_hash: str, _salt: str):
    return md5((_hash+":"+_salt).encode()).hexdigest()


def list_vids():
    db.table = "videos"
    __vids = {vid[0]:list(vid[1:]) for vid in db.select_all()}

    return __vids


print(list_vids())

