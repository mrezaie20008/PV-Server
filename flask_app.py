from flask import Flask
from pathlib import Path


app = Flask(__name__)


@app.route('/')
def hello_world():
    __html = open(Path(__file__).parent.joinpath("templates", "welcome", "index.html"), "rb").read()
    return __html

