from app import create_app
from app import socket_io

app = create_app()
if __name__ == "__main__":
    socket_io.run(app=app, debug=True)
