import mediapipe as mp
from app.utils import image_utils

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        
        # Unified landmark mapping
        self.landmark_map = {
            "left_shoulder": mp.solutions.pose.PoseLandmark.LEFT_SHOULDER,
            "right_shoulder": mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER,
            "left_hip": mp.solutions.pose.PoseLandmark.LEFT_HIP,
            "right_hip": mp.solutions.pose.PoseLandmark.RIGHT_HIP,
            "left_knee": mp.solutions.pose.PoseLandmark.LEFT_KNEE,
            "right_knee": mp.solutions.pose.PoseLandmark.RIGHT_KNEE,
            "left_ankle": mp.solutions.pose.PoseLandmark.LEFT_ANKLE,
            "right_ankle": mp.solutions.pose.PoseLandmark.RIGHT_ANKLE,
            "left_wrist": mp.solutions.pose.PoseLandmark.LEFT_WRIST,
            "right_wrist": mp.solutions.pose.PoseLandmark.RIGHT_WRIST,
            "left_ear": mp.solutions.pose.PoseLandmark.LEFT_EAR,
            "right_ear": mp.solutions.pose.PoseLandmark.RIGHT_EAR,
        }

    def detect_pose_return_landmarks(self, image):
        cv_image = image_utils.preprocess_image(image)
        results = self.pose.process(cv_image)
        if not results.pose_landmarks:
            return {"error": "Pose landmarks not detected"}

        landmarks = {}
        for key, landmark_enum in self.landmark_map.items():
            lm = results.pose_landmarks.landmark[landmark_enum]
            landmarks[key] = {"x": lm.x, "y": lm.y, "z": lm.z}
        return landmarks