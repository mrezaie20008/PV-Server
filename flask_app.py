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

@app.errorhandler(403)
def not_allowed(error):
    return Response("NOT_ALLOWED", mimetype="text/plain"), 403


# Routes / Pages
@app.route('/', methods=["GET", "POST"])
def welcome():
    if request.method == "POST":

        if not "authToken" in request.cookies:
            abort(403)

        user = verify_token(request.cookies.get("authToken"))

        if not user:
            abort(403)

        __response = f"""HI, {user[0][1]}!\n/vids - For checking the stock of videos we have.\nThanks!"""

        return Response(__response, mimetype="text/plain"), 200

    else:
        abort(403)


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

