from app.models.pose_estimator import PoseEstimator
from app.core.phase_analyzer import PhaseAnalyzer
from app.models.result_formatter import ResultFormatter

class PoseProcessor:
    """
    處理多幀數據並生成報告
    """
    def __init__(self):
        self.pose_estimator = PoseEstimator()
        self.phase_analyzer = PhaseAnalyzer()
        self.result_formatter = ResultFormatter()

    def process_sequence(self, frames, movement_type):
        """
        分析多幀並生成分階段報告
        """
        all_landmarks = [self.pose_estimator.detect_pose(frame) for frame in frames]
        phases = self.phase_analyzer.analyze_phases(all_landmarks, movement_type)
        return self.result_formatter.format_report(phases, movement_type)
