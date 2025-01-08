import cv2
import numpy as np

def preprocess_image(image):
    """
    將圖像轉換為 OpenCV 格式
    """
    np_image = np.frombuffer(image.read(), np.uint8)
    cv_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    return cv_image