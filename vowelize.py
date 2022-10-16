def vowelize(word, vowels="AEIOU", handle_y=True):
    word = word.upper()
    v = sum(1 for x in word if x in vowels)
    if "Y" in word:
        # If there are no other vowels, then y is a vowel
        if v == 0:
            v = 1
        else:
            # If a `y` is preceded by a consonent, it is a vowel
            # NOTE: this doesn't apply to `y` at the end of a word
            for letter in range(1, len(word)-1):
                if word[letter] == "Y" and word[letter+1] not in vowels:
                    v += 1
            # If the word ends with `y`, then that `y` is always a vowel
            if word[-1] == "Y":
                v += 1
    return v

