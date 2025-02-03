from app.models.pose_estimator import PoseEstimator
from app.core.side_detector import weighted_side_detection, determine_side_from_multiple_frames
from app.core.phase_analyzer import PhaseAnalyzer

class PoseProcessor:
    def __init__(self):
        self.pose_estimator = PoseEstimator()
        self.phase_analyzer = PhaseAnalyzer()

    def process_sequence(self, frames, movement_type):
        side_results = []
        phase_results = []

        for frame in frames:
            landmarks = self.pose_estimator.detect_pose(frame)
            if "error" in landmarks:
                side_results.append("unknown")
                continue

            # 判斷左右側
            side = weighted_side_detection(landmarks)
            side_results.append(side)

            # 動作分階段
            phase = self.phase_analyzer.analyze_phases([landmarks], movement_type)
            phase_results.append({"landmarks": landmarks, "side": side, "phase": phase})

        # 多幀平滑結果
        final_side = determine_side_from_multiple_frames(side_results)
        return final_side, phase_results
