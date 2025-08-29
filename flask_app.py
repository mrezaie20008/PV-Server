from flask import Flask
from pathlib import Path
from configs import *


app = Flask(__name__)

@app.route('/')
def hello_world():
    __html = get_html(Path(HOME_DIR).joinpath("templates", "welcome", "index.html"))
    return __html

