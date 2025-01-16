class PhaseAnalyzer:
    """
    分析多幀數據並劃分動作階段
    """
    def analyze_phases(self, landmarks_list, movement_type):
        phases = {"Setup": [], "Transition": [], "Lockout": []}
        for i, landmarks in enumerate(landmarks_list):
            if "error" in landmarks:
                continue

            if self.is_setup_phase(landmarks, movement_type):
                phases["Setup"].append(landmarks)
            elif self.is_lockout_phase(landmarks, movement_type):
                phases["Lockout"].append(landmarks)
            else:
                phases["Transition"].append(landmarks)
        return phases

    def is_setup_phase(self, landmarks, movement_type):
        """
        判斷是否為啟動階段
        """
        if movement_type == "deadlift":
            return landmarks["right_hip"]["y"] > landmarks["right_knee"]["y"]
        # 針對其他動作的條件
        return False

    def is_lockout_phase(self, landmarks, movement_type):
        """
        判斷是否為完成階段
        """
        if movement_type == "deadlift":
            return abs(landmarks["right_hip"]["y"] - landmarks["right_shoulder"]["y"]) < 0.1
        # 針對其他動作的條件
        return False
