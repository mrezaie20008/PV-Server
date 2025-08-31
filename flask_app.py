from flask import Flask
from pathlib import Path
from configs import *

# App Configurations
app = Flask(__name__)

@app.route('/')
def hello_world():
    __html = get_html(Path(HOME_DIR).joinpath("templates", "welcome", "index.html"))

    return __html

@app.route("vids/<vid>")
def get_vid(vid):
    return f"<h1> Are you looking for {vid} video?</h1>"

