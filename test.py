import os
import cv2
import numpy as np
import tensorflow as tf

# Step 1: Preprocess the Images
def preprocess_image(image_path):
    img = cv2.imread(image_path)  
    img = cv2.resize(img, (224, 224))  # Resize to a consistent size
    img = img / 255.0  # Normalize pixel values (assuming a model trained on [0, 1])

    return img

# Step 2: Load the Trained Model
model = tf.keras.models.load_model('BT_class')

# Step 3: Predict on Each Image
image_folder = 'path_to_image_folder'
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(image_folder, filename)
        preprocessed_image = preprocess_image(image_path)
        preprocessed_image = np.expand_dims(preprocessed_image, axis=0)  # Add batch dimension
        prediction = model.predict(preprocessed_image)

        # Step 4: Post-process Predictions (depends on your task)
        # For example, if you're doing classification, you might print the class label:
        predicted_class = np.argmax(prediction)
        print(f'Image: {filename}, Predicted Class: {predicted_class}')

        # For object detection, you would process bounding boxes and class probabilities here.

