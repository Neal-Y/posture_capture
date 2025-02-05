from flask import Blueprint, request, jsonify
from app.services.movement_service import MovementService


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
        if movement_type not in ["deadlift", "squat", "bench_press"]:
            return jsonify({"error": "Invalid movement type"}), 400

        # 調用 MovementService 進行分析
        response = movement_service.analyze_movement(video_file, movement_type)

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
