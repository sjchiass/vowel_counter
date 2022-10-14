# Guessing vowels

## Principle

Pillow is used to generate images from nltk's list of English words. The images are split into folders depending on their number of vowels.

Keras is then used to train a model that classifies the images.

When the training is done, you can generate another image from a word of your choice and see if it guesses the number of vowels correctly.

## Example

It can correctly guess that `lol` has one vowel.

```
python infer.py save_at_10.h5 lol
1/1 [==============================] - 0s 56ms/step
0 vowels:  0.00
1 vowels:  1.00
2 vowels:  0.00
3 vowels:  0.00
4 vowels:  0.00
5 vowels:  0.00
6 vowels:  0.00
7 vowels:  0.00
8 vowels:  0.00
9 vowels:  0.00
10 vowels:  0.00
11 vowels:  0.00
```
