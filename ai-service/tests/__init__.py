# 測試模組初始化
from flask import Flask

app = Flask(__name__)

# 可選：註冊其他模組（如路由）
from app.api.pose_api import pose_api
app.register_blueprint(pose_api)
