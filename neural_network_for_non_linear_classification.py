# -*- coding: utf-8 -*-
"""Neural Network for Non-Linear Classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kQfAthsqQc32gJBJqqP9091ZhFhM-ghH

# Classification Problem on non-linearly separable data
"""

from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Generate nonlinear dataset
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
print("First 10 data points:")
print(X[:10])
print("Labels of the first 10 data points:")
print(y[:10])

# Plot the nonlinear dataset
plt.figure(figsize=(8, 6))
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Class 0')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='yellow', label='Class 1')
plt.title('Nonlinear Dataset (Moons)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.linear_model import LogisticRegression
import numpy as np

# Fit logistic regression model
log_reg = LogisticRegression(solver='lbfgs')
log_reg.fit(X, y)

# Plot decision boundary
plt.figure(figsize=(8, 6))
x1_min, x1_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
x2_min, x2_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01),
                       np.arange(x2_min, x2_max, 0.01))
Z = log_reg.predict(np.c_[xx1.ravel(), xx2.ravel()])
Z = Z.reshape(xx1.shape)
plt.contourf(xx1, xx2, Z, alpha=0.3)
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Class 0')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='yellow', label='Class 1')
plt.title('Decision Boundary (Logistic Regression)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.metrics import accuracy_score

# Predict the labels for the dataset
y_pred = log_reg.predict(X)

# Calculate the accuracy
accuracy = accuracy_score(y, y_pred)
print("Accuracy:", accuracy * 100)

"""**Useing Neural Network**"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

# Generate nonlinear dataset
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define neural network model
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(2,)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Function to plot decision boundary
def plot_decision_boundary(X, y, model, epoch):
    plt.figure()
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=20)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(f'Decision Boundary (Epoch {epoch})')
    plt.show()

# Train the model
for epoch in range(1, 51):
    history = model.fit(X_train, y_train, epochs=1, batch_size=32, validation_split=0.1, verbose=0)
    plot_decision_boundary(X_train, y_train, model, epoch)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

total_params = 0
for layer in model.layers:
    # Get weights and biases for the layer
    weights, biases = layer.get_weights()
    # Count parameters in the layer
    layer_params = weights.size + biases.size
    total_params += layer_params

print("Total number of parameters in the model:", total_params)