class SquatAnalyzer:
    """
    分析深蹲（Squat）
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Bottom": [],
            "Standing": []
        }

        for landmarks in landmarks_list:
            if landmarks["right_hip"]["y"] > landmarks["right_knee"]["y"]:
                phases["Setup"].append(landmarks)
            elif abs(landmarks["right_knee"]["y"] - landmarks["right_ankle"]["y"]) < 0.1:
                phases["Bottom"].append(landmarks)
            else:
                phases["Standing"].append(landmarks)

        return phases
