class BenchPressAnalyzer:
    """
    臥推分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list, side):
        phases = {
            "Setup": [],
            "Lowering": [],
            "Pressing": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            if side == "unknown":
                print(f"Skipping frame {i}: Unable to determine side")
                continue  # 跳過無法判斷左右側的幀

            try:
                elbow = landmarks[f"{side}_elbow"]
                wrist = landmarks[f"{side}_wrist"]
                shoulder = landmarks[f"{side}_shoulder"]

                if self.is_setup_phase(wrist, shoulder):
                    phases["Setup"].append(landmarks)
                elif self.is_lowering_phase(elbow, wrist):
                    phases["Lowering"].append(landmarks)
                elif self.is_pressing_phase(elbow, wrist, shoulder):
                    phases["Pressing"].append(landmarks)
                elif self.is_lockout_phase(elbow, shoulder):
                    phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: Missing key {str(e)}")

        return phases

    def is_setup_phase(self, wrist, shoulder):
        """
        臥推的 Setup 階段判斷：
        - 手腕與肩膀接近相同水平
        """
        return abs(wrist["y"] - shoulder["y"]) < 0.1

    def is_lowering_phase(self, elbow, wrist):
        """
        臥推的 Lowering 階段判斷：
        - 手腕下降，接近胸部
        """
        return wrist["y"] > elbow["y"]

    def is_pressing_phase(self, elbow, wrist, shoulder):
        """
        臥推的 Pressing 階段判斷：
        - 手腕開始向上移動，遠離胸部
        """
        return wrist["y"] < elbow["y"] and wrist["y"] < shoulder["y"]

    def is_lockout_phase(self, elbow, shoulder):
        """
        臥推的 Lockout 階段判斷：
        - 手肘接近肩膀高度（完全伸展）
        """
        return abs(elbow["y"] - shoulder["y"]) < 0.05
