from app.models.pose_estimator import PoseEstimator
from app.core.side_detector import determine_side_from_multiple_frames, weighted_side_detection, filter_landmarks_by_side

class PoseProcessor:
    def __init__(self):
        self.pose_estimator = PoseEstimator()
        self.prev_side = "unknown"
    
    def process_sequence(self, frames):
        if not frames:
            return []

        side_results = []
        all_landmarks = []

        for i, frame in enumerate(frames):
            landmarks = self.pose_estimator.detect_pose_return_landmarks(frame)

            if not isinstance(landmarks, dict) or "error" in landmarks or not landmarks:
                side_results.append("unknown")
                continue

            all_landmarks.append(landmarks)
            side_results.append(weighted_side_detection(landmarks))

        if not all_landmarks:
            return []  

        if self.prev_side == "unknown":
            first_valid_side = next((s for s in side_results if s != "unknown"), "unknown")
            self.prev_side = first_valid_side

        final_side = determine_side_from_multiple_frames(side_results, self.prev_side)
        self.prev_side = final_side  # 更新 prev_side

        filtered_landmarks = [
            filter_landmarks_by_side(landmarks, final_side) if filter_landmarks_by_side(landmarks, final_side) else "unknown"
            for landmarks in all_landmarks
        ]

        return filtered_landmarks

    # def process_single_frame(self, frame):
    #     """
    #     即時影像單幀處理：
    #     1. 偵測 `landmarks`
    #     2. 判斷側別 (`left` or `right`)
    #     3. 過濾 `landmarks` 只保留該側
    #     """
    #     landmarks = self.pose_estimator.detect_pose_return_landmarks(frame)
        
    #     if not isinstance(landmarks, dict) or "error" in landmarks:
    #         return {}, "unknown"

    #     side = weighted_side_detection(landmarks)

    #     if self.prev_side == "unknown":
    #         self.prev_side = side
        
    #     final_side = determine_side_from_multiple_frames([side, self.prev_side], self.prev_side, window_size=2)
    #     self.prev_side = final_side  # 更新 prev_side

    #     if final_side == "unknown" and self.prev_side != "unknown":
    #         final_side = self.prev_side  # 避免 `landmarks` 消失
        
    #     filtered_landmarks = filter_landmarks_by_side(landmarks, final_side)
        
    #     return filtered_landmarks, final_side