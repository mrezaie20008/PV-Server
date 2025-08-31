from flask import (
    Flask,
    render_template
)
from pathlib import Path
from configs import *
from markupsafe import escape


# App Configurations
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("welcome/index.html", data="Mohammad")

@app.route("/vids")
def show_vids():
    return ", ".join(list_vids(VID_DIR))

@app.route("/vids/<vid>")
def get_vid(vid):
    return f"<h1> Are you looking for {escape(vid)} video?</h1>"

