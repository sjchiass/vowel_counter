import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# The code is from these two guides:
# flow: https://keras.io/examples/vision/image_classification_from_scratch/
# model: https://keras.io/examples/vision/mnist_convnet/

image_size = (16, 150)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "./images",
    labels="inferred",
    label_mode="int",
    class_names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    validation_split=0.2,
    subset="training",
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size,
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "./images",
    labels="inferred",
    label_mode="int",
    class_names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    validation_split=0.2,
    subset="validation",
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size,
)

train_ds = train_ds.prefetch(buffer_size=32)
val_ds = val_ds.prefetch(buffer_size=32)


# An example NMIST digits model is sufficient for this task, even if this
# data is for words instead of single digits
def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    
    x = inputs
    x = layers.Rescaling(1.0 / 255)(x)
    x = layers.Conv2D(32, kernel_size=(3, 3), activation="relu")(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)
    x = layers.Conv2D(64, kernel_size=(3, 3), activation="relu")(x)

    x = layers.MaxPooling2D(pool_size=(2, 2))(x)
    x = layers.Flatten()(x)
    x = layers.Dropout(0.5)(x)
    
    outputs = layers.Dense(12, activation="softmax")(x)
    return keras.Model(inputs, outputs)


model = make_model(input_shape=image_size + (1,), num_classes=12)

# 25 epochs are good enough to get even the tougher words
epochs = 25

# Save the models to use with infer.py
callbacks = [
    keras.callbacks.ModelCheckpoint("save_at_{epoch}.h5"),
]

model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
model.fit(
    train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds,
)
