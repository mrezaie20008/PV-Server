from pathlib import Path
from pickle import load
from os import listdir


def setter():
    def getter():
        file = open(Path(__file__).parent / ".bin", "rb")
        
        return load(file)

    data = getter()

    for k, v in data.items():
        globals()[k] = v

setter()


# Functions
def get_html(addr: str | Path):
    __data = open(addr, "rb").read()

    return __data

def list_vids(vids_pth: Path = VID_DIR):
    __vids = [v for v in listdir(vids_pth) if v.split(".")[-1] == "mp4"]

    return __vids


