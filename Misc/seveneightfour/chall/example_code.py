import numpy as np 
import matplotlib.pyplot as plt


# Traning data
with open("x.npy", "rb") as f:
    x = np.load(f)

# Label 
with open("y.npy", "rb") as f:
    y = np.load(f)

# Some hidden message, can you figure it out?
with open("pred.npy", "rb") as f:
    pred = np.load(f)

# Show one of the images
plt.imshow(x[0].reshape(28,28), cmap='gray')
plt.show()
