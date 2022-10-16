# Guessing vowels

## Principle

Pillow is used to generate images from nltk's list of English words. The images are split into folders depending on their number of vowels.

Keras is then used to train a model that classifies the images into vowel counts.

When the training is done, you can give words to `infer.py` and see if it guesses the number of vowels correctly.

## Test

The following are the same words I use in `./tests/vowelize.py`. They should cover all cases of vowels.

```console
python infer.py save_at_25.h5 yoghurt turkey mostly unmyelinated myopic bicycle polymer lymph gym mr dude food overflow cat
```

```console
********************************
***  YOGHURT   has  2 vowels ***
==> Best guess is   2 PASS   <==
`-> % certain that 'yoghurt' has 2 vowels: 99.99%
`-> % certain that 'yoghurt' has 3 vowels:  0.01%
********************************
***   TURKEY   has  3 vowels ***
==> Best guess is   3 PASS   <==
`-> % certain that 'turkey' has 3 vowels: 100.00%
********************************
***   MOSTLY   has  2 vowels ***
==> Best guess is   2 PASS   <==
`-> % certain that 'mostly' has 2 vowels: 100.00%
**********************************
*** UNMYELINATED has  5 vowels ***
==> Best guess is   5 PASS   <==
`-> % certain that 'unmyelinated' has 5 vowels: 60.72%
`-> % certain that 'unmyelinated' has 6 vowels: 39.28%
********************************
***   MYOPIC   has  2 vowels ***
==> Best guess is   2 PASS   <==
`-> % certain that 'myopic' has 2 vowels: 99.95%
`-> % certain that 'myopic' has 3 vowels:  0.05%
********************************
***  BICYCLE   has  3 vowels ***
==> Best guess is   3 PASS   <==
`-> % certain that 'bicycle' has 3 vowels: 100.00%
********************************
***  POLYMER   has  3 vowels ***
==> Best guess is   3 PASS   <==
`-> % certain that 'polymer' has 3 vowels: 100.00%
********************************
***   LYMPH    has  1 vowels ***
==> Best guess is   1 PASS   <==
`-> % certain that 'lymph' has 1 vowels: 100.00%
********************************
***    GYM     has  1 vowels ***
==> Best guess is   1 PASS   <==
`-> % certain that 'gym' has 1 vowels: 100.00%
********************************
***     MR     has  0 vowels ***
==> Best guess is   0 PASS   <==
`-> % certain that 'mr' has 0 vowels: 100.00%
********************************
***    DUDE    has  2 vowels ***
==> Best guess is   2 PASS   <==
`-> % certain that 'dude' has 2 vowels: 99.98%
`-> % certain that 'dude' has 3 vowels:  0.02%
********************************
***    FOOD    has  2 vowels ***
==> Best guess is   2 PASS   <==
`-> % certain that 'food' has 2 vowels: 100.00%
********************************
***  OVERFLOW  has  3 vowels ***
==> Best guess is   3 PASS   <==
`-> % certain that 'overflow' has 3 vowels: 99.99%
`-> % certain that 'overflow' has 4 vowels:  0.01%
********************************
***    CAT     has  1 vowels ***
==> Best guess is   1 PASS   <==
`-> % certain that 'cat' has 1 vowels: 100.00%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% SCORE: 14/14 (100.00%) GOOD BOI! %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
