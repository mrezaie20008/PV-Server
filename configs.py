from pathlib import Path
from pickle import load
from os import listdir
from flask import jsonify
from db import DB

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


def get_html(addr: str | Path):
    __data = open(addr, "rb").read()

    return __data

def list_vids(vids_pth: Path = VID_DIR):
    __vids = [v for v in listdir(vids_pth) if v.split(".")[-1] == "mp4"]

    return __vids


