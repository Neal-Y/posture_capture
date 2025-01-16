import mediapipe as mp
from app.utils import image_utils

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        self.required_landmarks = ["shoulder", "hip", "knee", "ankle", "wrist"]

    def detect_pose(self, image):
        # 將圖像預處理為 OpenCV 格式
        cv_image = image_utils.preprocess_image(image)
        # 使用 Mediapipe 進行姿勢檢測
        results = self.pose.process(cv_image)
        if not results.pose_landmarks:
            return {"error": "Pose landmarks not detected"}

        # 確定哪一側有效，並僅保留該側的關鍵點
        landmarks = results.pose_landmarks.landmark
        side = self._determine_side(landmarks)

        # 過濾並提取需要的 landmarks
        filtered_landmarks = {}
        for lm in self.required_landmarks:
            lm_name = f"{side}_{lm}".upper()
            try:
                index = getattr(mp.solutions.pose.PoseLandmark, lm_name).value
                landmark = landmarks[index]
                filtered_landmarks[f"{side}_{lm}"] = {
                    "x": landmark.x,
                    "y": landmark.y,
                    "z": landmark.z,
                }
            except AttributeError:
                continue  # 忽略未找到的 landmarks
        return filtered_landmarks

    def _determine_side(self, landmarks):
        """
        確定應該使用哪一側（根據 landmarks 的 z 值）
        """
        left_z = sum(landmarks[getattr(mp.solutions.pose.PoseLandmark, f"LEFT_{lm.upper()}").value].visibility
                     for lm in self.required_landmarks if hasattr(mp.solutions.pose.PoseLandmark, f"LEFT_{lm.upper()}"))
        right_z = sum(landmarks[getattr(mp.solutions.pose.PoseLandmark, f"RIGHT_{lm.upper()}").value].visibility
                      for lm in self.required_landmarks if hasattr(mp.solutions.pose.PoseLandmark, f"RIGHT_{lm.upper()}"))

        # 判斷哪一側更明顯
        return "left" if left_z > right_z else "right"
