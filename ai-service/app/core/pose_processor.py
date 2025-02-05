from app.models.pose_estimator import PoseEstimator
from app.core.side_detector import determine_side_from_multiple_frames, weighted_side_detection, filter_landmarks_by_side

class PoseProcessor:
    """
    處理影片幀數，並提取骨架資訊
    """
    def __init__(self):
        self.pose_estimator = PoseEstimator()

    def process_sequence(self, frames):
        """
        逐幀提取骨架資訊，並根據 `final_side` 過濾 landmarks
        """
        side_results = []
        all_landmarks = []

        for frame in frames:
            landmarks = self.pose_estimator.detect_pose_return_landmarks(frame)

            if not isinstance(landmarks, dict):  # 避免無效數據
                side_results.append("unknown")
                continue

            all_landmarks.append(landmarks)
            side_results.append(weighted_side_detection(landmarks))

        if not all_landmarks:
            return []  

        final_side = determine_side_from_multiple_frames(side_results)
        filtered_landmarks = [filter_landmarks_by_side(landmarks, final_side) for landmarks in all_landmarks]

        return filtered_landmarks