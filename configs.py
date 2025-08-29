from pathlib import Path
from pickle import loads


def setter():
    def getter():
        file = open(Path(__file__).parent / ".bin", "rb")
        
        return loads(file)

    data = getter()

    for k, v in data.items():
        globals()[k] = v

setter()

