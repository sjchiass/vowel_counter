import os
from vowelize import vowelize
from make_image import make_image
from nltk.corpus import words

# Get all words from nltk
english_words = set(x.upper() for x in words.words())

# Make sure the ./images folder exists
if not os.path.exists("images"):
    os.makedirs("images")

# For each word, determine the number of vowels and then generate as an
# image in the appropriate sub-folder, e.g. ./images/1/CAT.png
for w in english_words:
    v = vowelize(w)
    make_image(w, v)

print(len(english_words))
