from flask import Blueprint, request, jsonify
from app.core.pose_processor import PoseProcessor
from app.utils.video_utils import extract_frames

pose_api = Blueprint("pose_api", __name__)
pose_processor = PoseProcessor()

@pose_api.route("/analyze/video", methods=["POST"])
def analyze_video():
    try:
        # 接收並保存上傳的影片
        video_file = request.files.get("video")
        if not video_file:
            return {"error": "No video file provided"}, 400

        video_path = "/tmp/uploaded_video.mp4"  # 保存的臨時路徑
        video_file.save(video_path)


        # 提取幀
        frames = extract_frames(video_path, fps=5)
        if not frames:
            return {"error": "No frames extracted from the video"}, 400

        # 動作類型
        movement_type = request.form.get("movement_type", "unknown")

        # 分析幀序列
        final_side, results = pose_processor.process_sequence(frames, movement_type)

        # 返回結果
        response = {
            "side": final_side,
            "phases": results
        }
        return jsonify(response)
    except Exception as e:
        return {"error": str(e)}, 500