from app.core.pose_processor import PoseProcessor
from app.models.result_formatter import ResultFormatter
from app.utils.video_utils import extract_frames
from app.services.movement_analyzers.deadlift_analyzer import DeadliftAnalyzer
from app.services.movement_analyzers.squat_analyzer import SquatAnalyzer
from app.services.movement_analyzers.bench_press_analyzer import BenchPressAnalyzer

class MovementService:
    """
    負責管理不同動作類型的分析
    """
    def __init__(self):
        self.pose_processor = PoseProcessor()
        self.result_formatter = ResultFormatter()

    def analyze_movement(self, video_file, movement_type):
        frames = extract_frames(video_file, fps=5)
        if not frames:
            return {"error": "No frames extracted from the video"}

        final_side, landmarks_list = self.pose_processor.process_sequence(frames)

        if movement_type == "deadlift":
            analyzer = DeadliftAnalyzer()
        elif movement_type == "squat":
            analyzer = SquatAnalyzer()
        elif movement_type == "bench_press":
            analyzer = BenchPressAnalyzer()
        else:
            return {"error": "Unknown movement type"}

        phases = analyzer.analyze(landmarks_list, final_side)
        return self.result_formatter.format_report(phases, movement_type)
