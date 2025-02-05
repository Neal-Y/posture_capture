class BenchPressAnalyzer:
    """
    臥推分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Descent": [],
            "Press": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            try:
                # 直接取得單側的 landmarks，因為 process_sequence 已經過濾過了
                shoulder = landmarks.get("shoulder")
                elbow = landmarks.get("elbow")
                wrist = landmarks.get("wrist")

                if None in (shoulder, elbow, wrist):  # 確保關鍵點都存在
                    raise KeyError("Missing key in landmarks")

                if self.is_setup_phase(shoulder, elbow):
                    phases["Setup"].append(landmarks)
                elif self.is_descent_phase(shoulder, elbow, wrist):
                    phases["Descent"].append(landmarks)
                elif self.is_press_phase(shoulder, elbow, wrist):
                    phases["Press"].append(landmarks)
                elif self.is_lockout_phase(shoulder, elbow):
                    phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: {str(e)}")

        return phases

    def is_setup_phase(self, shoulder, elbow):
        return elbow["y"] > shoulder["y"] and abs(elbow["y"] - shoulder["y"]) > 0.1

    def is_descent_phase(self, shoulder, elbow, wrist):
        return elbow["y"] > wrist["y"] and abs(elbow["y"] - wrist["y"]) > 0.1

    def is_press_phase(self, shoulder, elbow, wrist):
        return elbow["y"] < wrist["y"] and abs(shoulder["y"] - elbow["y"]) > 0.1

    def is_lockout_phase(self, shoulder, elbow):
        return abs(shoulder["y"] - elbow["y"]) < 0.05
