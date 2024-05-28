import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Preprocess the big image and extract multiple faces (you can use face detection libraries like OpenCV or dlib)
big_image = cv2.imread('path_to_big_image.jpg')
# Face detection and extraction code here...

# Train a CNN model using extracted face images
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(height, width, channels)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Take new input image with a small crop face
new_image = cv2.imread('path_to_new_input_image.jpg')
# Face detection and extraction code here...

# Use the trained model to predict the face in the new input image
predicted_face = model.predict(new_face)

# Overlay colored mask on the detected face in the big image
colored_mask = np.zeros_like(big_image)
colored_mask[y:y+h, x:x+w] = [255, 0, 0]  # Color the detected face region (e.g., red)

output_image = cv2.addWeighted(big_image, 1, colored_mask, 0.5, 0)  # Overlay the colored mask on the big image

cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()