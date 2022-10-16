#import nltk
#nltk.download('words')
import os
from vowelize import vowelize
from make_image import make_image
from nltk.corpus import words

english_words = set(x.upper() for x in words.words())

if not os.path.exists("images"):
    os.makedirs("images")

for w in english_words:
    v = vowelize(w)
    make_image(w, v)
    
print(len(english_words))
