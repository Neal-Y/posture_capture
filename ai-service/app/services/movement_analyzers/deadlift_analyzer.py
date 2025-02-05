class DeadliftAnalyzer:
    """
    硬舉分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list, side):
        phases = {
            "Setup": [],
            "Transition": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            if side == "unknown":
                print(f"Skipping frame {i}: Unable to determine side")
                continue  # 跳過無法判斷左右側的幀

            try:
                # 只關注該側的關鍵點
                hip = landmarks[f"{side}_hip"]
                knee = landmarks[f"{side}_knee"]
                ankle = landmarks[f"{side}_ankle"]
                shoulder = landmarks[f"{side}_shoulder"]

                if self.is_setup_phase(hip, knee):
                    phases["Setup"].append(landmarks)
                elif self.is_lockout_phase(hip, shoulder):
                    phases["Lockout"].append(landmarks)
                else:
                    phases["Transition"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: Missing key {str(e)}")

        return phases

    def is_setup_phase(self, hip, knee):
        """
        硬舉的 Setup 階段判斷：
        - 髖部（hip）比膝蓋（knee）更高
        """
        return hip["y"] > knee["y"]

    def is_lockout_phase(self, hip, shoulder):
        """
        硬舉的 Lockout 階段判斷：
        - 髖部（hip）和肩膀（shoulder）大致呈現垂直對齊
        """
        return abs(hip["y"] - shoulder["y"]) < 0.1
