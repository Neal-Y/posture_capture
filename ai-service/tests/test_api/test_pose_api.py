import unittest
from app import app
import os

class TestPoseAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_analyze_pose_no_image(self):
        """
        測試未提供圖像時的錯誤返回
        """
        response = self.client.post("/analyze")
        self.assertEqual(response.status_code, 400)
        self.assertIn("No image provided", response.get_json()["error"])

    
    def test_analyze_pose_success(self):
        """
        測試正確上傳圖像的情況
        """
        # 確保測試文件存在
        test_image_path = "tests/assets/test_image.jpg"
        self.assertTrue(os.path.exists(test_image_path), "Test image not found!")

        # 使用測試圖像進行測試
        with open(test_image_path, "rb") as image:
            response = self.client.post(
                "/analyze",
                data={"image": image},
                content_type="multipart/form-data"
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("landmarks", response.get_json())