from flask import Flask
from pathlib import Path
from configs import HOME_DIR



app = Flask(__name__)

@app.route('/')
def hello_world():
    __html = open(Path(HOME_DIR).joinpath("templates", "welcome", "index.html"), "rb").read()

    return __html

