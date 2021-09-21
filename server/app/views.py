from . import socket_io
from flask import render_template, Blueprint
from flask_socketio import emit


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")


@socket_io.on("feed")
def send_feed(data):
    emit("feed-update", data, broadcast=True)
