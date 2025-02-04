class DeadliftAnalyzer:
    """
    分析硬舉（Deadlift）
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Transition": [],
            "Lockout": []
        }

        for landmarks in landmarks_list:
            if landmarks["right_hip"]["y"] > landmarks["right_knee"]["y"]:
                phases["Setup"].append(landmarks)
            elif abs(landmarks["right_hip"]["y"] - landmarks["right_shoulder"]["y"]) < 0.1:
                phases["Lockout"].append(landmarks)
            else:
                phases["Transition"].append(landmarks)

        return phases
