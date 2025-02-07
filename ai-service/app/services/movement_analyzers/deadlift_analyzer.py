class DeadliftAnalyzer:
    """
    硬舉分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Transition": [],
            "Lockout": []
        }

        current_phase = "Setup"  # 初始狀態必定為 Setup

        for i, landmarks in enumerate(landmarks_list):
            try:
                # 直接取得單側的 landmarks，因為 process_sequence 已經過濾過了
                hip = landmarks.get("hip")
                knee = landmarks.get("knee")
                shoulder = landmarks.get("shoulder")
                ankle = landmarks.get("ankle")

                if None in (hip, knee, shoulder, ankle):  # 確保關鍵點都存在
                    raise KeyError("Missing key in landmarks")

                if current_phase == "Setup":
                    if self.is_setup_phase(hip, knee, ankle, shoulder):
                        phases["Setup"].append(landmarks)
                    else:
                        current_phase = "Transition"

                if current_phase == "Transition":
                    if self.is_transition_phase(hip, knee, ankle, shoulder):
                        phases["Transition"].append(landmarks)
                    else:
                        current_phase = "Lockout"

                if current_phase == "Lockout":
                    if self.is_lockout_phase(hip, shoulder, knee, ankle):
                        phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: {str(e)}")

        return phases

    def is_setup_phase(self, hip, knee, ankle, shoulder):
        return knee["y"] > hip["y"] - 0.05 and hip["y"] < shoulder["y"] + 0.1 and abs(ankle["y"] - knee["y"]) > 0.02

    def is_transition_phase(self, hip, knee, ankle, shoulder):
        return hip["y"] > shoulder["y"] - 0.10 and knee["y"] > hip["y"] - 0.15

    def is_lockout_phase(self, hip, shoulder, knee, ankle):
        return (
            abs(hip["y"] - shoulder["y"]) < 0.20  # 放寬 hip & shoulder 直立條件
            and knee["y"] < hip["y"] + 0.10  # 放寬 knee 位置
            and abs(knee["x"] - shoulder["x"]) < 0.15  #  確保站直
            and abs(ankle["x"] - shoulder["x"]) < 0.15  #  確保站直
        )
