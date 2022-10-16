import tensorflow as tf
from tensorflow import keras
import numpy as np
import argparse
from vowelize import vowelize
from make_image import make_image

parser = argparse.ArgumentParser(
    description="Guess the amount of vowels in a string (letter y is not well supported)")
parser.add_argument("model", type=str, help="Path of saved model")
parser.add_argument("words", type=str, nargs='+', help="Words to try to guess")

args = parser.parse_args()

model = keras.models.load_model(args.model)

data = []
for word in args.words:
    img_array = make_image(word, 0, as_array=True)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    data.append(img_array)

data = np.concatenate(data, axis=0)
predictions = model.predict(data)

for o, w in zip(range(predictions.shape[0]), args.words):
    obs = predictions[o,:]
    print(f"*** {w.upper():10} has {vowelize(w):2} vowels ***")
    guess = np.argmax(obs.flatten())
    print(f"--> Best guess is  {guess:2} {'PASS' if guess == vowelize(w) else 'FAIL'}   <--")
    for n, i in enumerate(obs.flatten()):
        if f"{i:.2%}" != "0.00%":
            print(f"\-> % certain that '{w.lower()}' has {n} vowels: {i:6.2%}")
