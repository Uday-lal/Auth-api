from app import create_app
from app import socket_io


if __name__ == "__main__":
    app = create_app()
    socket_io.run(app=app, debug=True)
