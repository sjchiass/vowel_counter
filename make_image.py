import os
from PIL import Image, ImageDraw
import numpy as np


def make_image(text, n_vowels, as_array=False):
    # Use the L mode for smaller single-channel grayscale images
    out = Image.new("L", (150, 16), 255)
    d = ImageDraw.Draw(out)
    # In order to center the text, adjust its x origin according to the
    # number of characters in the word
    d.text((75-2.75*len(text), 2), text.upper(), fill=0)
    if as_array:
        # Return an array when inferring
        return np.asarray(out)
    else:
        # Otherwise save as a png
        if not os.path.exists(f"./images/{n_vowels}"):
            os.makedirs(f"./images/{n_vowels}")
        out.save(f"./images/{n_vowels}/{text}.png")

