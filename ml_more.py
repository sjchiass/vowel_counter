import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# also pydot

# flow: https://keras.io/examples/vision/image_classification_from_scratch/
# model: https://keras.io/examples/vision/mnist_convnet/

image_size = (15, 125)
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

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "./images",
	labels="inferred",
	label_mode="int",
	class_names=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    validation_split=0.2,
    subset="validation",
    seed=1,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size,
)

train_ds = train_ds.prefetch(buffer_size=32)
val_ds = val_ds.prefetch(buffer_size=32)


def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    
    x = inputs
    # Entry block
    x = layers.Rescaling(1.0 / 255)(x)
    x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [128, 256]:#, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(256, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.5)(x)
    
    outputs = layers.Dense(12, activation="softmax")(x)
    return keras.Model(inputs, outputs)


model = make_model(input_shape=image_size + (1,), num_classes=12)
keras.utils.plot_model(model, show_shapes=True)

epochs = 10

callbacks = [
    keras.callbacks.ModelCheckpoint("more_save_at_{epoch}.h5"),
]
model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
model.fit(
    train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds,
)
