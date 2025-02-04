import cv2

def extract_frames(video_file, fps=5):
    """
    提取影片的幀序列
    """
    video_path = "/tmp/uploaded_video.mp4"
    video_file.save(video_path)

    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, frame_rate // fps)  # 計算提取間隔

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frames.append(frame)
        frame_count += 1
    cap.release()
    return frames
