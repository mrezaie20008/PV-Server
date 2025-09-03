# TODO: Make the vids url the functional one, which brings up the real videos
from flask import (
    Flask,
    jsonify,
    abort,
    request,
    Response,
)
from pathlib import Path
from configs import *
from json import loads


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
        __data = loads(request.data.decode())

        if "password" not in __data.keys() or "username" not in __data.keys():
            abort(403)
        
        __hash = salted_hash(__data["username"], __data['password'])
        
        user = verify_token(__hash)

        if not user:
            abort(403)

        __response = __hash

        return Response(__response, mimetype="text/plain"), 200

    else:
        abort(403)


@app.route("/vids")
def show_vids():
    __auth = request.cookies.get("authToken")

    print(__auth)

    return jsonify(list_vids())


@app.get("/vids/<vid>/<int:sn>")
def get_vid(vid):
    if not vid in list_vids():
        abort(404)
    
    __res = {
        "message": "Video is available!",
    }

    return jsonify(__res)

