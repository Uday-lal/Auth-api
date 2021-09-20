from flask import Flask
from flask_socketio import SocketIO



socket_io = SocketIO()

def create_app():
    from .views import views
    app = Flask(__name__)
    app.register_blueprint(views)
    socket_io.init_app(app)
    return app
