from flask import Blueprint, request, jsonify
from app.services.movement_service import MovementService
from app.utils.video_utils import extract_frames

pose_api = Blueprint("pose_api", __name__)
movement_service = MovementService()

@pose_api.route("/analyze/video", methods=["POST"])
def analyze_video():
    """
    影片分析 API，處理影片上傳並調用 MovementService 進行分析
    """
    try:
        video_file = request.files.get("video")
        if not video_file:
            return jsonify({"error": "No video file provided"}), 400

        movement_type = request.form.get("movement_type", "unknown")
        video_path = "/tmp/uploaded_video.mp4"
        video_file.save(video_path)

        # 提取幀數
        frames = extract_frames(video_path, fps=5)
        if not frames:
            return jsonify({"error": "No frames extracted from the video"}), 400

        # 調用 MovementService 進行分析
        response = movement_service.analyze_movement(frames, movement_type)

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
