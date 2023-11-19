import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from pathlib import Path

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train and test data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# data testing and displaying train characteristics
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: show few images from train set
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
plt.show()

# scaling the image to range [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# images have to be (28, 28, 1)
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)
print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")

# transform labels
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

# TODO: create a model using keras.Sequential(); show its structure using .summary()
model = keras.Sequential()
model.add(layers.Input(shape=(784, )))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(32, activation="relu"))
model.add(layers.Dense(10, activation="Softmax"))
model.summary()

# TODO: define characteristics of learning process using .compile()
model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["Accuracy", ])

# TODO: train the network
batch_size = 64
epochs = 5
history = model.fit(x_train_s,
                    y_train_s,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_split=0.1)

# TODO: show test accuracy and confusion matrix
score = model.evaluate(x_test_s, y_test_s, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
predicted_classes = np.argmax(model.predict(x_test_s), axis=-1)
conf_matrix = confusion_matrix(y_test, predicted_classes)
print(conf_matrix)

# TODO: save the model
model.save(Path("LV6/FCN/"))
