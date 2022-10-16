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

# Generate all images into memory as numpy arrays
data = []
for word in args.words:
    img_array = make_image(word, 0, as_array=True)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    data.append(img_array)

# Combine all images together
data = np.concatenate(data, axis=0)

# Make predictions
predictions = model.predict(data)

# Keep track of correct guesses
correct_guesses = 0
for o, w in zip(range(predictions.shape[0]), args.words):
    # Slice predictions array for one time along axis 0 (the observations)
    obs = predictions[o, :]
    # Make a pretty box for current word and include what should be the 
    # correct number of vowels
    reference = f"*** {w.upper():^10} has {vowelize(w):2} vowels ***"
    print(len(reference)*"*")
    print(reference)
    # Extract the model's guess from the predictions
    guess = np.argmax(obs.flatten())
    if guess == vowelize(w):
        correct_guesses += 1
        good_guess = True
    else:
        good_guess = False
    print(f"==> Best guess is  {guess:2} {'PASS' if good_guess  else 'FAIL'}   <==")
    # Print guess as long as they're greater than a hundreth of a percent
    for n, i in enumerate(obs.flatten()):
        if f"{i:.2%}" != "0.00%":
            print(f"`-> % certain that '{w.lower()}' has {n} vowels: {i:6.2%}")
# Count number of correct guesses, out of all words given
score = f"%%% SCORE: {correct_guesses:2}/{len(args.words):2} ({correct_guesses/len(args.words):.2%}) %%%"
if correct_guesses == len(args.words):
    score = score.replace(" %%%", " GOOD BOI! %%%")
print(len(score)*"%")
print(score)
print(len(score)*"%")
