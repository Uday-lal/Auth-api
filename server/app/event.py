from . import socket_io
from flask_socketio import emit


@socket_io.on("feed")
def sendFeed(data):
    emit("feed_update", data, broadcast=True)
