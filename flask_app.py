from flask import (
    Flask,
    render_template
)
from pathlib import Path
from configs import *
from markupsafe import escape


# App Configurations
app = Flask(__name__)


# Error Pages
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Routes / Pages
@app.route('/')
def hello_world():
    return render_template("welcome/index.html", data="Mohammad")


@app.route("/vids")
def show_vids():
    return ", ".join(list_vids())


@app.get("/vids/<vid>")
def get_vid(vid):
    if not vid in list_vids():
        return f"<h1>Video Not Found</h1>"

    return f"<h1> Are you looking for {escape(vid)} video?</h1>"

