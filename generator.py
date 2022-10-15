#from nltk.corpus import cmudict
#d = cmudict.dict()

#import nltk
#nltk.download('words')
import os
from PIL import Image, ImageDraw, ImageFont
from nltk.corpus import words

#english_words = set([x.upper() for x in words.words()][:10000])
english_words = set(x.upper() for x in words.words())

vowels = "AEIOU"

if not os.path.exists("images"):
    os.makedirs("images")

for w in english_words:
    v = sum(1 for x in w if x in vowels)
    if not os.path.exists(f"images/{v}"):
        os.makedirs(f"images/{v}")

for w in english_words:
    v = sum(1 for x in w if x in vowels)
    if v == 0 and "Y" in w:
        v = 1
    out = Image.new("L", (150, 16), 255)
    d = ImageDraw.Draw(out)
    d.text((75-2.75*len(w), 2), w.upper(), fill=0)
    out.save(f"./images/{v}/{w}.png")
    
print(len(english_words))
