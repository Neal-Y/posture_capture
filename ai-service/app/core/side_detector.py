def weighted_side_detection(landmarks):
    weights = {
        "shoulder": 0.4,
        "hip": 0.3,
        "knee": 0.2,
        "ankle": 0.1
    }
    left_weight, right_weight = 0, 0

    for point, coords in landmarks.items():
        if "left" in point:
            left_weight += coords["x"] * weights.get(point.split("_")[1], 0.1)
        elif "right" in point:
            right_weight += coords["x"] * weights.get(point.split("_")[1], 0.1)

    if left_weight > right_weight:
        return "left"
    elif right_weight > left_weight:
        return "right"
    return "unknown"

def determine_side_from_multiple_frames(sides):
    counts = {"left": 0, "right": 0, "unknown": 0}
    for side in sides:
        counts[side] += 1
    return max(counts, key=counts.get)
