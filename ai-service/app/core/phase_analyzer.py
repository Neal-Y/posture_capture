class PhaseAnalyzer:
    """
    分析多幀數據並劃分動作階段
    """
    def detect_side(self, landmarks):
        """
        判斷輸入的 landmarks 是左側還是右側。
        """
        has_left = all(key in landmarks for key in ["left_hip", "left_knee", "left_shoulder", "left_ankle"])
        has_right = all(key in landmarks for key in ["right_hip", "right_knee", "right_shoulder", "right_ankle"])
        
        if has_left and not has_right:
            return "left"
        elif has_right and not has_left:
            return "right"
        elif has_left and has_right:
            # 如果左右側都有數據，可以根據應用場景選擇優先側，這裡假設優先檢測右側
            return "both"
        return "unknown"


    def analyze_phases(self, landmarks_list, movement_type):
        phases = {
            "Setup": ([], ["Ensure back is straight", "Engage core muscles"]),
            "Transition": ([], ["Keep bar path straight"]),
            "Lockout": ([], ["Good finish position"]),
        }

        for i, landmarks in enumerate(landmarks_list):
            side = self.detect_side(landmarks)
            if side == "unknown":
                print(f"Skipping frame {i}: Unable to determine side")
                continue

            try:
                if self.is_setup_phase(landmarks, side):
                    phases["Setup"][0].append(landmarks)
                elif self.is_lockout_phase(landmarks, side):
                    phases["Lockout"][0].append(landmarks)
                else:
                    phases["Transition"][0].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: Missing key {str(e)}")

        return phases


    def is_setup_phase(self, landmarks, side):
        """
        判斷是否為啟動階段
        """
        return landmarks[f"{side}_hip"]["y"] > landmarks[f"{side}_knee"]["y"]

    def is_lockout_phase(self, landmarks, side):
        """
        判斷是否為完成階段
        """
        return abs(landmarks[f"{side}_hip"]["y"] - landmarks[f"{side}_shoulder"]["y"]) < 0.1
