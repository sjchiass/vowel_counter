import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageDraw, ImageFont
import argparse
from make_image import make_image

parser = argparse.ArgumentParser(
    description="Guess the amount of vowels in a string (letter y is not well supported)")
parser.add_argument("model", type=str, help="Path of saved model")
parser.add_argument("word", type=str, help="A word to try to guess")

args = parser.parse_args()

model = keras.models.load_model(args.model)

img_array = make_image(args.word, 0, as_array=True)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
for n, i in enumerate(predictions.flatten()):
    print(f"{n} vowels: {i:5.2f}")
