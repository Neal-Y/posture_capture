from app.models.pose_estimator import PoseEstimator
from app.models.result_formatter import ResultFormatter

class PoseProcessor:
    """
    聚合姿勢檢測和結果格式化的邏輯
    """
    def __init__(self):
        self.pose_estimator = PoseEstimator()
        self.result_formatter = ResultFormatter()

    def process_image(self, image):
        """
        處理上傳的圖像並返回姿勢分析結果
        """
        # 使用 PoseEstimator 進行姿勢檢測
        landmarks = self.pose_estimator.detect_pose(image)
        if "error" in landmarks:
            return landmarks  # 返回檢測錯誤

        # 使用 ResultFormatter 格式化檢測結果
        return self.result_formatter.format_landmarks(landmarks)
