from flask import (
    Flask,
    render_template,
    jsonify,
    abort
)
from pathlib import Path
from configs import *
from markupsafe import escape


# App Configurations
app = Flask(__name__)


# Error Pages
@app.errorhandler(404)
def page_not_found(error):
    return "NOT_FOUND", 404


# Routes / Pages
@app.route('/')
def hello_world():
    pass


@app.route("/vids")
def show_vids():
    return ", ".join(list_vids())


@app.get("/vids/<vid>")
def get_vid(vid):
    if not vid in list_vids():
        abort(404)
    
    __res = {
        "message": "Video is available!",
    }

    return jsonify(__res)

