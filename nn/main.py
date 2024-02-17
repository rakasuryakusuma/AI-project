import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Load the mnist dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Build the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
# 10 is for our output from 10 neuron out of 1
model.add(tf.keras.layers.Dense(10, activation="softmax")) 

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# -Train the model
# epoch used to see how many times the models is gonna see the same data over and over again
model.fit(x_train, y_train, epochs=3)

# Save the model
model.save('handwritten.model')

# Load the model
model = tf.keras.models.load_model('handwritten.model')

# Test the model on digit images
image_number = 1
while os.path.isfile(f"nn/digits/digit{image_number}.png"):
    try:
        image = cv2.imread(f"/nn/digits/digit{image_number}.png", cv2.IMREAD_GRAYSCALE)
        # Invert and normalize the image
        image = np.invert(np.array([image]))
        image = tf.keras.utils.normalize(image, axis=1)

        # Predict the digit
        prediction = model.predict(image)
        predicted_digit = np.argmax(prediction)
        print(f"This digit is probably a {predicted_digit}")

        # Display the image
        plt.imshow(image[0], cmap=plt.cm.binary)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        image_number += 1