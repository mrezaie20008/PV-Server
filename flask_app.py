from flask import (
    Flask,
    jsonify,
    abort,
    request,
    Response,
)
from pathlib import Path
from configs import *


# App Configurations
app = Flask(__name__)


# Error Pages
@app.errorhandler(404)
def page_not_found(error):
    return Response("NOT_FOUND", mimetype="text/plain"), 404


# Routes / Pages
@app.route('/', methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        return Response("HI", mimetype="text/plain"), 200

    else:
        return Response(f"Hi There,\nThis is an API which we put videos on it for public use.", mimetype="text/plain"), 200


@app.route("/vids")
def show_vids():
    return jsonify(list_vids())


@app.get("/vids/<vid>")
def get_vid(vid):
    if not vid in list_vids():
        abort(404)
    
    __res = {
        "message": "Video is available!",
    }

    return jsonify(__res)

