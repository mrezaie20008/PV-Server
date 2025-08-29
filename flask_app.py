from flask import Flask
from pathlib import Path
from configs import HOME_DIR



app = Flask(__name__)

@app.route('/')
def hello_world():
    __html = f"<h1 style='color: blue;'>Working in {HOME_DIR}</h1>"

    return __html

