# -*- coding: utf-8 -*-
"""Image Classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QpWTGT5xE5L1TgJNx-1PzNb_zo_MHIV_
"""

from sklearn.datasets import fetch_openml

# Load MNIST dataset
mnist = fetch_openml('mnist_784')

# Extract features (X) and labels (y)
X, y = mnist.data, mnist.target

print("Number of samples:", len(X))
print("Number of features:", X.shape[1])
print("Number of classes:", len(set(y)))

import matplotlib.pyplot as plt

# Display the first 10 images
fig, axes = plt.subplots(2, 5, figsize=(5, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(X.to_numpy()[i].reshape(28, 28), cmap='binary')
    ax.set_title(f"Label: {y[i]}")
    ax.axis('off')

plt.tight_layout()
plt.show()

from collections import Counter

# Count occurrences of each digit
digit_counts = Counter(y)

# Display the counts
for digit, count in digit_counts.items():
    print(f"Number of {digit}s:", count)

import matplotlib.pyplot as plt

# Count occurrences of each digit
digit_counts = Counter(y)

# Extract digits and counts
digits = list(digit_counts.keys())
counts = list(digit_counts.values())

# Plot the distribution
plt.figure(figsize=(8, 6))
plt.bar(digits, counts, color='skyblue')
plt.xlabel('Digits')
plt.ylabel('Count')
plt.title('Distribution of Digits in MNIST Dataset')
plt.xticks(range(10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the pixel values to be between 0 and 1
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert labels to one-hot encoded vectors
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Define the neural network architecture
model = Sequential([
    Dense(units=128, activation='relu', input_shape=(784,)),
    Dense(units=64, activation='relu'),
    Dense(units=10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", test_accuracy*100)

total_params = 0
for layer in model.layers:
    # Get weights and biases for the layer
    weights, biases = layer.get_weights()
    # Count parameters in the layer
    layer_params = weights.size + biases.size
    total_params += layer_params

print("Total number of parameters in the model:", total_params)