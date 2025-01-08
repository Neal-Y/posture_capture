class ResultFormatter:
    """
    格式化姿勢檢測的結果
    """
    def format_landmarks(self, landmarks):
        """
        將骨架數據封裝為結構化的結果
        """
        return {
            "message": "Analysis success",
            "landmarks": landmarks
        }
