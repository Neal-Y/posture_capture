from collections import deque

def weighted_side_detection(landmarks):
    weights = {
        "shoulder": 0.4,
        "hip": 0.3,
        "knee": 0.2,
        "ankle": 0.1
    }
    left_weight, right_weight = 0, 0
    left_count, right_count = 0, 0

    for point, coords in landmarks.items():
        body_part = point.split("_")[1]
        weight = weights.get(body_part, 0.1)

        if "left" in point:
            left_weight += coords["x"] * weight - coords.get("z", 0) * 0.1
            left_count += 1
        elif "right" in point:
            right_weight += coords["x"] * weight - coords.get("z", 0) * 0.1
            right_count += 1

    if left_count > right_count + 2:
        return "left"
    elif right_count > left_count + 2:
        return "right"

    return "left" if left_weight >= right_weight else "right"

def determine_side_from_multiple_frames(sides, prev_side="unknown", window_size=5):
    if not sides:
        return prev_side

    recent_sides = deque(sides[-min(len(sides), window_size):], maxlen=window_size)

    counts = {"left": 0, "right": 0, "unknown": 0}
    for side in recent_sides:
        counts[side] += 1

    total_valid = counts["left"] + counts["right"]
    
    if total_valid == 0:
        return prev_side

    left_ratio = counts["left"] / total_valid
    right_ratio = counts["right"] / total_valid

    if len(set(recent_sides)) == 1 and "unknown" not in recent_sides:
        return recent_sides[0]

    if left_ratio > 0.6: 
        return "left"
    elif right_ratio > 0.6:
        return "right"

    if counts["unknown"] > len(recent_sides) // 2:
        return prev_side if prev_side != "unknown" else "left"

    if abs(left_ratio - right_ratio) < 0.1:
        return prev_side

    return "left" if left_ratio > right_ratio else "right"

def filter_landmarks_by_side(landmarks, final_side):
    if not isinstance(landmarks, dict) or final_side == "unknown":
        return {}

    return {
        key.replace(f"{final_side}_", ""): value  
        for key, value in landmarks.items()
        if key.startswith(final_side)
    }
