class BenchPressAnalyzer:
    def analyze(self, landmarks_list):
        phases = {
            "Setup": [],
            "Descent": [],
            "Press": [],
            "Lockout": []
        }

        for i, landmarks in enumerate(landmarks_list):
            try:
                wrist = landmarks.get("wrist")
                elbow = landmarks.get("elbow")
                shoulder = landmarks.get("shoulder")
                chest = landmarks.get("nose")  # ✅ 改用 nose 作為胸部參考

                if None in (wrist, elbow, shoulder, chest):
                    raise KeyError("Missing key in landmarks")

                if self.is_setup_phase(wrist, chest, elbow):
                    phases["Setup"].append(landmarks)
                elif self.is_descent_phase(wrist, chest):
                    phases["Descent"].append(landmarks)
                elif self.is_press_phase(wrist, shoulder):
                    phases["Press"].append(landmarks)
                elif self.is_lockout_phase(wrist, shoulder):
                    phases["Lockout"].append(landmarks)
            except KeyError as e:
                print(f"Skipping frame {i}: {str(e)}")

        return phases

    def is_setup_phase(self, wrist, chest, elbow):
        """✅ 設置階段: 手腕高於胸部，肘部接近胸部"""
        return wrist["y"] < chest["y"] and abs(elbow["y"] - chest["y"]) < 0.1

    def is_descent_phase(self, wrist, chest):
        """✅ 下放階段: 手腕低於胸部"""
        return wrist["y"] > chest["y"]

    def is_press_phase(self, wrist, shoulder):
        """✅ 推起階段: 手腕上升但未超過肩膀"""
        return wrist["y"] < shoulder["y"] and wrist["y"] > shoulder["y"] - 0.2  # ✅ 確保手腕還沒鎖定

    def is_lockout_phase(self, wrist, shoulder):
        """✅ 鎖定階段: 手腕超過肩膀高度"""
        return wrist["y"] < shoulder["y"] - 0.1  # ✅ 需要比肩膀更高才算鎖定
