from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
from sign_language_model import predict_sign  # Load your trained model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    np_arr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    detected_word = predict_sign(frame)  # Process frame and get word
    return jsonify({"word": detected_word})

if __name__ == '__main__':
    app.run(debug=True)
