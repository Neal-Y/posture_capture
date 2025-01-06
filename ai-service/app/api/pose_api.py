from flask import Flask, request, jsonify
import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_pose():
    # Assume image data is sent as a base64 encoded string
    data = request.get_json()
    image_data = data.get('image')
    if not image_data:
        return jsonify({'error': 'No image data provided'}), 400

    # Decode the image
    nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the image
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Analyze pose landmarks
    if results.pose_landmarks:
        # Here you can calculate angles and provide feedback
        return jsonify({'message': 'Pose analyzed successfully'})
    else:
        return jsonify({'error': 'No pose landmarks detected'}), 400

if __name__ == '__main__':
    app.run(debug=True)
