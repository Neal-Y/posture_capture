class BenchPressAnalyzer:
    """
    分析臥推（Bench Press）
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Descent": [],
            "Press": []
        }

        for landmarks in landmarks_list:
            if landmarks["right_wrist"]["y"] > landmarks["right_shoulder"]["y"]:
                phases["Descent"].append(landmarks)
            elif landmarks["right_wrist"]["y"] < landmarks["right_shoulder"]["y"]:
                phases["Press"].append(landmarks)
            else:
                phases["Setup"].append(landmarks)

        return phases
