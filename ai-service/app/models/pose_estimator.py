import mediapipe as mp
from app.utils import image_utils

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        
        # Unified landmark mapping
        self.landmark_map = {
            "nose": mp.solutions.pose.PoseLandmark.NOSE,
            "left_eye_inner": mp.solutions.pose.PoseLandmark.LEFT_EYE_INNER,
            "left_eye": mp.solutions.pose.PoseLandmark.LEFT_EYE,
            "left_eye_outer": mp.solutions.pose.PoseLandmark.LEFT_EYE_OUTER,
            "right_eye_inner": mp.solutions.pose.PoseLandmark.RIGHT_EYE_INNER,
            "right_eye": mp.solutions.pose.PoseLandmark.RIGHT_EYE,
            "right_eye_outer": mp.solutions.pose.PoseLandmark.RIGHT_EYE_OUTER,
            "left_ear": mp.solutions.pose.PoseLandmark.LEFT_EAR,
            "right_ear": mp.solutions.pose.PoseLandmark.RIGHT_EAR,
            "mouth_left": mp.solutions.pose.PoseLandmark.MOUTH_LEFT,
            "mouth_right": mp.solutions.pose.PoseLandmark.MOUTH_RIGHT,
            "left_shoulder": mp.solutions.pose.PoseLandmark.LEFT_SHOULDER,
            "right_shoulder": mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER,
            "left_elbow": mp.solutions.pose.PoseLandmark.LEFT_ELBOW,
            "right_elbow": mp.solutions.pose.PoseLandmark.RIGHT_ELBOW,
            "left_wrist": mp.solutions.pose.PoseLandmark.LEFT_WRIST,
            "right_wrist": mp.solutions.pose.PoseLandmark.RIGHT_WRIST,
            "left_pinky": mp.solutions.pose.PoseLandmark.LEFT_PINKY,
            "right_pinky": mp.solutions.pose.PoseLandmark.RIGHT_PINKY,
            "left_index": mp.solutions.pose.PoseLandmark.LEFT_INDEX,
            "right_index": mp.solutions.pose.PoseLandmark.RIGHT_INDEX,
            "left_thumb": mp.solutions.pose.PoseLandmark.LEFT_THUMB,
            "right_thumb": mp.solutions.pose.PoseLandmark.RIGHT_THUMB,
            "left_hip": mp.solutions.pose.PoseLandmark.LEFT_HIP,
            "right_hip": mp.solutions.pose.PoseLandmark.RIGHT_HIP,
            "left_knee": mp.solutions.pose.PoseLandmark.LEFT_KNEE,
            "right_knee": mp.solutions.pose.PoseLandmark.RIGHT_KNEE,
            "left_ankle": mp.solutions.pose.PoseLandmark.LEFT_ANKLE,
            "right_ankle": mp.solutions.pose.PoseLandmark.RIGHT_ANKLE,
            "left_heel": mp.solutions.pose.PoseLandmark.LEFT_HEEL,
            "right_heel": mp.solutions.pose.PoseLandmark.RIGHT_HEEL,
            "left_foot": mp.solutions.pose.PoseLandmark.LEFT_FOOT_INDEX,
            "right_foot": mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX,
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