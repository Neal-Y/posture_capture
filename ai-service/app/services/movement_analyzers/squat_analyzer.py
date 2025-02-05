class SquatAnalyzer:
    """
    深蹲分析器，根據 `landmarks_list` 來劃分動作階段
    """
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Descent": [],
            "Ascent": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            try:
                # 直接取得單側的 landmarks，因為 process_sequence 已經過濾過了
                hip = landmarks.get("hip")
                knee = landmarks.get("knee")
                ankle = landmarks.get("ankle")
                shoulder = landmarks.get("shoulder")

                if None in (hip, knee, ankle, shoulder):  # 確保關鍵點都存在
                    raise KeyError("Missing key in landmarks")

                if self.is_setup_phase(hip, knee):
                    phases["Setup"].append(landmarks)
                elif self.is_descent_phase(hip, knee):
                    phases["Descent"].append(landmarks)
                elif self.is_ascent_phase(hip, knee, shoulder):
                    phases["Ascent"].append(landmarks)
                elif self.is_lockout_phase(hip, shoulder):
                    phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: {str(e)}")

        return phases

    def is_setup_phase(self, hip, knee):
        return hip["y"] >= knee["y"] - 0.05

    def is_descent_phase(self, hip, knee):
        return hip["y"] > knee["y"]

    def is_ascent_phase(self, hip, knee, shoulder):
        return hip["y"] < knee["y"] and abs(shoulder["y"] - hip["y"]) < 0.15

    def is_lockout_phase(self, hip, shoulder):
        return abs(hip["y"] - shoulder["y"]) < 0.1
