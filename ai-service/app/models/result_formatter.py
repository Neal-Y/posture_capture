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
        suggestions_map = {
            "deadlift": {
                "Setup": ["Ensure back is straight", "Position hips properly"],
                "Transition": ["Keep bar path straight"],
                "Lockout": ["Good finish position"]
            },
            "squat": {
                "Setup": ["Brace core", "Keep chest up"],
                "Transition": ["Control descent"],
                "Lockout": ["Drive through heels"]
            },
            "bench_press": {
                "Setup": ["Grip the bar properly", "Position feet flat"],
                "Transition": ["Lower bar to chest"],
                "Lockout": ["Fully extend arms"]
            }
        }
        return suggestions_map.get(movement_type, {}).get(phase_name, ["No suggestions available"])
