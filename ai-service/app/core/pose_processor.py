from app.models.pose_estimator import PoseEstimator
from app.core.side_detector import determine_side_from_multiple_frames

class PoseProcessor:
    """
    處理影片幀數，並提取骨架資訊
    """
    def __init__(self):
        self.pose_estimator = PoseEstimator()

    def process_sequence(self, frames):
        side_results = []
        all_landmarks = []

        for frame in frames:
            landmarks = self.pose_estimator.detect_pose(frame)
            if "error" in landmarks:
                side_results.append("unknown")
                continue

            all_landmarks.append(landmarks)
            side_results.append(self._detect_side(landmarks))

        if not all_landmarks:
            return "unknown", []

        final_side = determine_side_from_multiple_frames(side_results)
        return final_side, all_landmarks

    def _detect_side(self, landmarks):
        has_left = all(key in landmarks for key in ["left_hip", "left_knee", "left_shoulder", "left_ankle"])
        has_right = all(key in landmarks for key in ["right_hip", "right_knee", "right_shoulder", "right_ankle"])
        return "left" if has_left and not has_right else "right" if has_right and not has_left else "unknown"
