from PIL import Image, ImageDraw
import numpy as np

def make_image(text, n_vowels, as_array=False):
    out = Image.new("L", (150, 16), 255)
    d = ImageDraw.Draw(out)
    d.text((75-2.75*len(text), 2), text.upper(), fill=0)
    if as_array:
        return np.asarray(out)
    else:
        out.save(f"./images/{n_vowels}/{text}.png")
