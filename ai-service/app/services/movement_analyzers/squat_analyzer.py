class SquatAnalyzer:
    """
    深蹲分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list, side):
        phases = {
            "Setup": [],
            "Descent": [],
            "Ascent": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            if side == "unknown":
                print(f"Skipping frame {i}: Unable to determine side")
                continue  # 跳過無法判斷左右側的幀

            try:
                hip = landmarks[f"{side}_hip"]
                knee = landmarks[f"{side}_knee"]
                ankle = landmarks[f"{side}_ankle"]
                shoulder = landmarks[f"{side}_shoulder"]

                if self.is_setup_phase(hip, knee):
                    phases["Setup"].append(landmarks)
                elif self.is_descent_phase(hip, knee):
                    phases["Descent"].append(landmarks)
                elif self.is_ascent_phase(hip, knee, shoulder):
                    phases["Ascent"].append(landmarks)
                elif self.is_lockout_phase(hip, shoulder):
                    phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: Missing key {str(e)}")

        return phases

    def is_setup_phase(self, hip, knee):
        """
        深蹲的 Setup 階段判斷：
        - 髖部與膝蓋高度相當（準備下蹲）
        """
        return hip["y"] >= knee["y"] - 0.05

    def is_descent_phase(self, hip, knee):
        """
        深蹲的 Descent 階段判斷：
        - 髖部開始下降，低於膝蓋高度
        """
        return hip["y"] > knee["y"]

    def is_ascent_phase(self, hip, knee, shoulder):
        """
        深蹲的 Ascent 階段判斷：
        - 髖部開始上升，回到與膝蓋同高度
        - 肩膀和髖部同步移動
        """
        return hip["y"] < knee["y"] and abs(shoulder["y"] - hip["y"]) < 0.15

    def is_lockout_phase(self, hip, shoulder):
        """
        深蹲的 Lockout 階段判斷：
        - 髖部、肩膀接近直立
        """
        return abs(hip["y"] - shoulder["y"]) < 0.1
