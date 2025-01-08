from flask import Flask
from app.api.pose_api import pose_api
from app.api.health_api import health_api

# 初始化 Flask 應用
app = Flask(__name__)
app.register_blueprint(pose_api)
app.register_blueprint(health_api)

if __name__ == "__main__":
    # 啟動服務
    app.run(host="0.0.0.0", port=8000)
