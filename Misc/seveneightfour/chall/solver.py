import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

"""
Keras MNIST covnet: https://keras.io/examples/vision/mnist_convnet/
Creds dataset: https://www.kaggle.com/datamunge/sign-language-mnist 
"""

# Traning data
with open("testfolder/data/x.npy", "rb") as f:
    x_train = np.load(f)

# Label 
with open("testfolder/data/y.npy", "rb") as f:
    y_train = np.load(f)

# Some hidden message, can you figure it out?
with open("testfolder/data/pred.npy", "rb") as f:
    pred = np.load(f)

# Reshape flatted out images to 28,28,1
x_train = [x.reshape(28,28, 1) for x in x_train]
pred = [p.reshape(28,28,1) for p in pred]

# Number of classes
num_classes = 26
input_shape = (28, 28, 1)

# Convert to np.array
x_train = np.array(x_train)
pred = np.array(pred)

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
pred = pred.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
pred = np.expand_dims(pred, -1)

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)

# Creating the model
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fit the model
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

# Predictions
predictions = model.predict(pred)

numbers_to_char = {x:y for x,y in enumerate("abcdefghijklmnopqrstuvwxyz")}

flag = ""
# Convert the prediction (most likely number) and convert to a character
for prediction in predictions:
    flag += numbers_to_char[np.argmax(prediction)]

# Depending on initialization, k might be interperted as l in some cases. 
print(flag)

