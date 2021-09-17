from app import app
from app import socket_io


if __name__ == "__main__":
    socket_io.run(app=app, debug=True)
