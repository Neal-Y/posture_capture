from flask import Flask
from .api.pose_api import pose_api
from .api.health_api import health_api

app = Flask(__name__)
app.register_blueprint(pose_api)
app.register_blueprint(health_api)
