import mediapipe as mp
from app.utils import image_utils

class PoseEstimator:
    """
    封裝 Mediapipe 姿勢檢測邏輯
    """
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()

    def detect_pose(self, image):
        """
        檢測圖像中的姿勢
        """
        # 將圖像轉換為 OpenCV 格式
        cv_image = image_utils.preprocess_image(image)
        
        # 使用 Mediapipe 進行姿勢檢測
        results = self.pose.process(cv_image)
        if not results.pose_landmarks:
            return {"error": "No pose detected"}

        # 提取骨架數據
        return [
            {"x": lm.x, "y": lm.y, "z": lm.z}
            for lm in results.pose_landmarks.landmark
        ]
