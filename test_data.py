import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# also pydot

image_size = (16, 160)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "./images",
	labels="inferred",
	label_mode="int",
	class_names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    validation_split=0.2,
    subset="training",
    seed=1,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size,
)

print(train_ds.take(1))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")

plt.show()
