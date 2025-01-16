class ResultFormatter:
    """
    格式化動作分析的結果
    """
    def format_report(self, phases, movement_type):
        formatted_phases = []
        for phase_name, landmarks in phases.items():
            formatted_phases.append({
                "phase": phase_name,
                "landmarks": landmarks,
                "suggestions": self.generate_suggestions(phase_name, movement_type)
            })
        return {"movement_type": movement_type, "phases": formatted_phases}

    def generate_suggestions(self, phase_name, movement_type):
        if movement_type == "deadlift":
            if phase_name == "Setup":
                return ["Ensure back is straight", "Position hips properly"]
            elif phase_name == "Transition":
                return ["Keep bar path straight"]
            elif phase_name == "Lockout":
                return ["Good finish position"]
        return ["No suggestions available"]
