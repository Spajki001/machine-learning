import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing import image_dataset_from_directory

# loading data from train directory
train_ds = image_dataset_from_directory(
 directory='Train',
 labels='inferred',
 label_mode='categorical',
 batch_size=32,
 image_size=(48, 48)
)

test_ds = image_dataset_from_directory(
 directory='Test',
 labels='inferred',
 label_mode='categorical',
 batch_size=32,
 image_size=(48, 48)
)

model = keras.Sequential()
model.add(layers.Input(shape=(48,48,3)))
model.add(layers.Conv2D(32,(3,3),padding='same',activation="relu"))
model.add(layers.Conv2D(32,(3,3),activation="relu"))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Dropout(0.2, input_shape=(23,23)))

model.add(layers.Input(shape=(48,48,3)))
model.add(layers.Conv2D(64,(3,3),padding='same',activation="relu"))
model.add(layers.Conv2D(64,(3,3),activation="relu"))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Dropout(0.2, input_shape=(23,23)))

model.add(layers.Input(shape=(48,48,3)))
model.add(layers.Conv2D(128,(3,3),padding='same',activation="relu"))
model.add(layers.Conv2D(128,(3,3),activation="relu"))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Dropout(0.2, input_shape=(23,23)))

model.add(layers.Flatten())

model.add(layers.Dense(512,activation="relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(43,activation='softmax'))
model.summary()

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["Accuracy", ])

# train the network
batch_size = 64
epochs = 5
history = model.fit(train_ds,
                    batch_size=batch_size,
                    epochs=epochs)

model.save('SN/')

# show test accuracy and confusion matrix
score = model.evaluate(test_ds, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
'''
predicted_classes = np.argmax(model.predict(train_ds), axis=-1)
conf_matrix = confusion_matrix(train_ds, predicted_classes)
print(conf_matrix)
'''