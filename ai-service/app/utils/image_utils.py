import cv2
import numpy as np

def preprocess_image(image):
    """
    Preprocess the image for pose detection.
    """
    if isinstance(image, np.ndarray):
        # If the image is already a numpy array, use it directly
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        # If the image is not a numpy array, read it as such
        np_image = np.frombuffer(image.read(), np.uint8)
        return cv2.imdecode(np_image, cv2.IMREAD_COLOR)