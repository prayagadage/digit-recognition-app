import io
import base64
import numpy as np
import cv2
from flask import Flask, render_template, request, jsonify
from PIL import Image
from tensorflow.keras.models import load_model

# Flask app
app = Flask(__name__)

# Load trained model
model = load_model("/Users/prayagadage/Desktop/Python_By_CJC/Prayag_py_projects/Handwriting_Recognition/mnist_cnn_model.h5")

# Preprocess function
def preprocess_image(image):
    # Convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Invert colors (MNIST expects white digit on black background)
    image = cv2.bitwise_not(image)
    # Resize to 28x28
    image = cv2.resize(image, (28, 28))
    # Normalize
    image = image.astype("float32") / 255.0
    # Expand dimensions -> (1, 28, 28, 1)
    image = np.expand_dims(image, axis=(0, -1))
    return image

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    img_data = data["image"]

    # Decode base64 → numpy array
    img_bytes = base64.b64decode(img_data.split(",")[1])
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = np.array(img)

    # Preprocess
    processed = preprocess_image(img)

    # Predict
    prediction = model.predict(processed)
    predicted_class = int(np.argmax(prediction, axis=1)[0])

    return jsonify({"prediction": predicted_class})

if __name__ == "__main__":
    app.run(debug=True)
