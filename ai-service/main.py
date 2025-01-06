from flask import Flask
from pose_api import pose_analysis

app = Flask(__name__)

app.register_blueprint(pose_analysis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
