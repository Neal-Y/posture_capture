from flask import Blueprint, request, jsonify
from app.core.pose_processor import PoseProcessor

# 創建 Blueprint
pose_api = Blueprint("pose_api", __name__)

# 初始化 PoseProcessor
pose_processor = PoseProcessor()

@pose_api.route("/analyze", methods=["POST"])
def analyze_pose():
    """
    接收上傳的圖像並進行姿勢分析
    """
    # 檢查是否有上傳圖像
    image = request.files.get("image")
    if not image:
        return jsonify({"error": "No image provided"}), 400

    # 調用核心邏輯處理圖像
    result = pose_processor.process_image(image)
    return jsonify(result), 200
