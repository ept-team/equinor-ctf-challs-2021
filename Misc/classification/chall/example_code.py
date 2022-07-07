import numpy as np 
from matplotlib import pyplot as plt


with open("data.npy", "rb") as f: 
    # Data to train on
    x_train = np.load(f)
    # Predict the correct class 
    x_test = np.load(f)
    # Training data (correct class)
    y_train = np.load(f)


# Example code to print the training data
plt.scatter(x_train[:, 0], x_train[:, 1], marker="o", c=y_train, s=25, edgecolor="k")
plt.show()

