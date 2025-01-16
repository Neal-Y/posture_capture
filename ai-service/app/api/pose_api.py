from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.core.pose_processor import PoseProcessor
from app.utils.video_utils import extract_frames

pose_api = Blueprint("pose_api", __name__)
pose_processor = PoseProcessor()

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@pose_api.route("/analyze/video", methods=["POST"])
def analyze_video():
    """
    接收影片進行動作分析
    """
    if "video" not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    movement_type = request.form.get("movement_type")
    if not movement_type:
        return jsonify({"error": "Missing movement_type"}), 400

    # 儲存上傳的影片
    video_file = request.files["video"]
    filename = secure_filename(video_file.filename)
    video_path = os.path.join(UPLOAD_FOLDER, filename)
    video_file.save(video_path)

    # 提取幀序列
    frames = extract_frames(video_path, fps=5)  # 每秒提取 5 幀
    if not frames:
        return jsonify({"error": "Failed to process video"}), 500

    # 分析幀序列
    result = pose_processor.process_sequence(frames, movement_type)

    # 刪除臨時影片文件
    os.remove(video_path)

    return jsonify(result), 200
