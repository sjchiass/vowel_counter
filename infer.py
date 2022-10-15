import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser(
    description="Guess the amount of vowels in a string (letter y is not well supported)")
parser.add_argument("model", type=str, help="Path of saved model")
parser.add_argument("word", type=str, help="A word to try to guess")

args = parser.parse_args()

model = keras.models.load_model(args.model)

out = Image.new("L", (150, 16), 255)
d = ImageDraw.Draw(out)
d.text((75-2.75*len(args.word), 2), args.word.upper(), fill=0)
out.save("./test.png")

img = keras.preprocessing.image.load_img(
    "test.png", target_size=(16,150), color_mode="grayscale"
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
for n, i in enumerate(predictions.flatten()):
    print(f"{n} vowels: {i:5.2f}")
