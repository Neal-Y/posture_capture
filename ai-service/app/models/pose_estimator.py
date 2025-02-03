import mediapipe as mp
from app.utils import image_utils

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        self.keypoints = {
            "left": ["left_shoulder", "left_hip", "left_knee", "left_ankle", "left_wrist", "left_ear"],
            "right": ["right_shoulder", "right_hip", "right_knee", "right_ankle", "right_wrist", "right_ear"],
        }

    def detect_pose(self, image):
        cv_image = image_utils.preprocess_image(image)
        results = self.pose.process(cv_image)
        if not results.pose_landmarks:
            return {"error": "Pose landmarks not detected"}

        landmarks = {}
        for side, points in self.keypoints.items():
            for point in points:
                try:
                    lm = results.pose_landmarks.landmark[
                        getattr(mp.solutions.pose.PoseLandmark, point.upper())
                    ]
                    landmarks[point] = {"x": lm.x, "y": lm.y, "z": lm.z}
                except AttributeError:
                    continue  # 如果有缺失的點
        return landmarks
